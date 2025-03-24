from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file,get_file
import google.generativeai as genai
import time
from pathlib import Path

import tempfile

from dotenv import load_dotenv
load_dotenv()

import os

API_KEY=os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)

multimodal_Agent = Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True,
    )



video_file = ""
user_query = input()
processed_video = upload_file(video_file)
print(processed_video.state.name)
while processed_video.state.name == "PROCESSING":
                        time.sleep(1)
                        processed_video = get_file(processed_video.name)

# Prompt generation for analysis
analysis_prompt = (
    f"""
    Analyze the uploaded video for content and context.
    Respond to the following query using video insights and supplementary web research:
    {user_query}

    Provide a detailed, user-friendly, and actionable response.
    """
)

response = multimodal_Agent.run(analysis_prompt,videos=[processed_video])

print(response.content)