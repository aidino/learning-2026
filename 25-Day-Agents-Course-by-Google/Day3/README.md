# Gemini 3 + ADK

## Links

- Build an AI Agent with Gemini 3 (Video): youtube.com/watch?v=9EGtawwvlNs&list=PLOU2XLYxmsIJCVXV1bLV7qnT5hilN3YJ7&index=4&t=1s
- Gemini 3 Agent Demo (GitHub): https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/ai-ml/agent-labs/gemini-3-pro-agent-demo
- ADK Google Search Tool Docs: https://google.github.io/adk-docs/tools/#google-search
- Gemini 3 Announcement: https://blog.google/products/gemini/gemini-3/#gemini-3

## Code

One liner with Agent Starter Pack

```
uvx agent-starter-pack create -y --api-key YOUR_GEMINI_API_KEY
```

Using ADK CLI

```bash
uv init
uv add google-adk
uv add google-genai
export GOOGLE_API_KEY="YOUR_API_KEY"
source .venv/bin/activate
adk create my_agent
```
