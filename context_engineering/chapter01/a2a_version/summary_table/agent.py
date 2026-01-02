from google.adk.agents.llm_agent import Agent
from .prompt import PROMPT

summarize_agent = Agent(
    model='gemini-2.5-flash',
    name='summarize_agent',
    description='Summarize the content of the document.',
    instruction=PROMPT,
    output_key='final_summary_table'
)
