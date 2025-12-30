# Source-Based Deployment

## Links

- [Source-Based Deployment Tutorial (Video)](youtube.com/watch?v=8RjzMG3BKA0&feature=youtu.be)
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)

## Code

Create new project with Agent Starter Pack

```bash
uvx agent-starter-pack create my-agent -a adk_base -d agent_engine
cd my-agent && make deploy
```

Enhance existing ADK agent

```bash
uvx agent-starter-pack enhance --d agent_engine
```