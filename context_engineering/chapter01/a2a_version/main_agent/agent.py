from google.adk.agents import LoopAgent, LlmAgent, BaseAgent, SequentialAgent
from isolate_content.agent import isolate_content
from identify_new_info.agent import identify_new_info
from    summary_table.agent import summarize_agent
from draft_email.agent import draft_email_agent

main_agent = SequentialAgent(
    name="MettingNoteAgent",
    sub_agents=[isolate_content, identify_new_info, summarize_agent, draft_email_agent],
    description="The main agent that orchestrates the entire process.",
)

root_agent = main_agent