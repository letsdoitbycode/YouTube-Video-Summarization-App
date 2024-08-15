from flask import Flask, request, render_template
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline('summarization', framework='pt')

def extract_video_id(url):
    """Extract the video ID from the YouTube URL."""
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    elif parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        query = parse_qs(parsed_url.query)
        return query.get('v', [None])[0]
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_video():
    try:
        # Get the video link from the form
        youtube_video = request.form['video_url']
        video_id = extract_video_id(youtube_video)

        if video_id is None:
            return render_template('result.html', summary="Invalid YouTube URL")

        # Retrieve the transcript from YouTube
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Combine all transcript text
        result = ""
        for i in transcript:
            result += ' ' + i['text']

        # Summarize the text
        num_iters = len(result) // 1000
        summarized_text = []
        for i in range(0, num_iters + 1):
            start = i * 1000
            end = (i + 1) * 1000
            chunk = result[start:end]
            out = summarizer(chunk)
            summarized_text.append(out[0]['summary_text'])

        # Join the summarized text
        final_summary = ' '.join(summarized_text)

        # Render the result page with the summary
        return render_template('result.html', summary=final_summary)

    except Exception as e:
        return render_template('result.html', summary=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
