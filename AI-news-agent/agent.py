from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
import os

from langchain_google_genai import ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(model='gemini-1.5-flash', verbose=True, temperature=0.5, google_api_key=os.getenv("GOOGLE_API_KEY"))
news_researcher=Agent(role="Senior Researcher", goal='Uncover ground breaking technologies in {topic}',
verbose=True,
memory=True,
backstory=("Driven by curiosity, you're at the forefront of"
"innvoation, eager to explore and share knowledge that could change"
"the world"),
tools=[],
llm=llm,
allow_delegation=True)

news_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "with a flair for simplifying complex topics, you craft engaging narratives that captivate and educate"
        "bringing new discoveries to light in an accessible manner"
    ),
    tools=[tool_search],
    llm=llm,
    allow_delegation=False
)