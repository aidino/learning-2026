from google.adk.agents.llm_agent import Agent
from .prompt import PROMPT

draft_email_agent = Agent(
    model='gemini-2.5-flash',
    name='draft_email_agent',
    description='Draft a follow-up email based on the summary table.',
    instruction=PROMPT,
    output_key='draft_email'
)
