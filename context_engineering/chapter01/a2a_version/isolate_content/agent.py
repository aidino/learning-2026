from google.adk.agents.llm_agent import Agent
from .prompt import PROMPT

isolate_content = Agent(
    model='gemini-2.5-flash',
    name='isolate_content',
    description='Bạn là một chuyên gia phân tích dữ liệu hội thoại.',
    instruction=PROMPT,
    output_key='substantive_content'
)

# root_agent = isolate_content
