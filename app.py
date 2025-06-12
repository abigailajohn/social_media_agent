import streamlit as st
import os
from dotenv import load_dotenv
from social_media_agent import get_transcript, generate_social_media_content

load_dotenv()

st.set_page_config(
    page_title="Social Media Content Writer",
    page_icon="✍️",
    layout="wide"
)

if 'results' not in st.session_state:
    st.session_state.results = None

st.title("✍️ Social Media Content Writer")
st.markdown("""
This app helps you generate social media content from YouTube videos. 
Enter a video ID and your query to get started!
""")

col1, col2 = st.columns(2)

with col1:
    video_id = st.text_input(
        "YouTube Video ID",
        placeholder="Enter the video ID (e.g., dQw4w9WgXcQ)",
        help="The ID is the part after 'v=' in a YouTube URL"
    )

with col2:
    platform = st.selectbox(
        "Platform",
        ["LinkedIn", "Twitter", "Instagram"],
        help="Select the social media platform for content generation"
    )

if st.button("Generate Content", type="primary"):
    if not video_id:
        st.error("Please provide a video ID!")
    else:
        try:
            with st.spinner("Generating content... This may take a few minutes."):
                transcript = get_transcript(video_id)
                
                result = generate_social_media_content(transcript, platform)
                
                st.session_state.results = result
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if st.session_state.results:
    st.markdown("---")
    st.subheader("Generated Content")
    st.markdown(st.session_state.results)

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and OpenAI") 