

def create_mcp_message(sender, content, metadata=None):
    """Creates a standardized MCP message."""
    return {
        "protocol_version": "1.0",
        "sender": sender,
        "content": content,
        "metadata": metadata or {}
    }