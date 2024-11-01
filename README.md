# YouTube Video Summarization App with Flask and Hugging Face Transformers

This Flask web application takes a YouTube video URL, retrieves the video's transcript, and generates a concise summary using Hugging Face’s Transformer summarization pipeline. This app is ideal for creating quick, digestible summaries of long-form video content.

### Key Features
- YouTube Transcript Retrieval: Extracts transcripts directly from YouTube videos via YouTubeTranscriptApi.
- Automatic Summarization: Uses Hugging Face’s summarization pipeline to break down large transcripts.
- Scalability: Processes long transcripts by dividing them into chunks for smooth summarization.
- User-Friendly Interface: Simple web UI for URL input and summary output.

### How It Works
- Extract Video ID: Parses the YouTube URL to obtain the video ID.
- Retrieve Transcript: Uses the video ID to fetch the transcript.
- Chunking & Summarization: Breaks down the transcript into 1000-token chunks, summarizes each chunk, and appends the results.
- Display Summary: Combines and displays the summarized content on the results page.

### Installation
1. Clone the repository
   ```sh
   git clone https://github.com/letsdoitbycode/YouTube-Video-Summarization-App.git
   cd YouTube-Video-Summarization-App
   ```

3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install requirements.txt
   ```
   
4. Run the Flask app:
    ```sh
    python app.py
    ```

### Project Structure
```plaintext
YouTube-Video-Summarization-App/
│
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # Main HTML file
│   └── result.html         # Result file
├── static/
│   ├── style.css           # CSS styles
├── requirements.txt        # requirements for the project
└── README.md               # This README file
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.
