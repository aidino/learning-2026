from google.adk.agents.llm_agent import Agent
from .prompt import PROMPT

identify_new_info = Agent(
    model='gemini-2.5-flash',
    name='identify_new_info',
    description='A helpful assistant for identifying new information in meetings.',
    instruction=PROMPT,
    output_key='new_developments'
)
