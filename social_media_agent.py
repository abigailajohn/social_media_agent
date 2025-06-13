import os
import asyncio
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Optional
import traceback

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
def get_transcript(video_id: str, languages: list = None) -> str:
    if languages is None:
        languages = ["en"]

    try:
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id, languages=languages)

        transcript_text = " ".join(snippet.text for snippet in fetched_transcript)

        return transcript_text

    except Exception as e:
        from youtube_transcript_api._errors import (
            CouldNotRetrieveTranscript, 
            VideoUnavailable,
            InvalidVideoId, 
            NoTranscriptFound,
            TranscriptsDisabled
        )

        if isinstance(e, NoTranscriptFound):
            error_msg = f"No transcript found for video {video_id} in languages: {languages}"
        elif isinstance(e, VideoUnavailable):
            error_msg = f"Video {video_id} is unavailable"
        elif isinstance(e, InvalidVideoId):
            error_msg = f"Invalid video ID: {video_id}"
        elif isinstance(e, TranscriptsDisabled):
            error_msg = f"Transcripts are disabled for video {video_id}"
        elif isinstance(e, CouldNotRetrieveTranscript):
            error_msg = f"Could not retrieve transcript: {str(e)}"
        else:
            error_msg = f"An unexpected error occurred: {str(e)}"

        print(f"Error: {error_msg}")
        raise Exception(error_msg) from e


def generate_social_media_content(transcript: str, platform: str = "LinkedIn") -> str:
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

        prompt = f"""Generate an engaging {platform} post based on the following video transcript.
        The post should be informative, engaging, and appropriate for {platform}'s audience.
        Include relevant hashtags and a call to action.

        Transcript:
        {transcript}

        Please format the post appropriately for {platform}."""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "You are a professional social media content creator."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2500,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Error generating content: {str(e)}")
        raise

async def main():
    try:        
        video_id = "kKvK2foOTJM" 
        
        print(f"Fetching transcript for video: {video_id}")
        try:
            transcript = get_transcript(video_id)
            print("Transcript fetched successfully!")

            platforms = ["LinkedIn", "Twitter", "Facebook"]
            
            for platform in platforms:
                print(f"\nGenerating content for {platform}...")
                content = generate_social_media_content(transcript, platform)
                print(f"\n{platform} Post:")
                print("-" * 50)
                print(content)
                print("-" * 50)
                
        except Exception as e:
            print(f"\nDetailed error information:")
            print(f"Error type: {type(e).__name__}")
            print(f"Error message: {str(e)}")
            print("\nFull traceback:")
            traceback.print_exc()
            raise
            
    except Exception as e:
        print(f"Error in main: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())


