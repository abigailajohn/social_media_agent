# Social Media Content Generator

This Python application automatically generates social media content from YouTube video transcripts. It uses the YouTube Transcript API to fetch video transcripts and OpenAI's GPT model to generate engaging social media posts.

## Features

- YouTube video transcript fetching
- Multi-platform content generation (LinkedIn, Twitter, Facebook)
- OpenAI GPT integration for content generation


## Prerequisites

- Python 3.7+
- OpenAI API key
- Internet connection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/social-media-agent.git
cd social-media-agent
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run the script:
```bash
# For normal execution
python social_media_agent.py

# For execution with OpenAI API tracing
# Windows PowerShell
$env:OPENAI_TRACE=1; python social_media_agent.py

# Windows Command Prompt
set OPENAI_TRACE=1 && python social_media_agent.py

# Linux/Mac
OPENAI_TRACE=1 python social_media_agent.py
```

2. The script will:
   - Check internet connectivity
   - Fetch the transcript from the specified YouTube video
   - Generate social media content for different platforms
   - Display the generated content

## Configuration

You can modify the following in `social_media_agent.py`:
- Video ID: Change the `video_id` variable in the `main()` function
- Social media platforms: Modify the `platforms` list in the `main()` function
- OpenAI model: Change the `model` parameter in `generate_social_media_content()`

## Error Handling

The script includes comprehensive error handling for:
- Internet connectivity issues
- YouTube transcript fetching errors
- OpenAI API errors
- General exceptions

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [OpenAI Python SDK](https://github.com/openai/openai-python) 