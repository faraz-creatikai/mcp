import os
import json
import urllib.request
from mcp.server.mcpserver import MCPServer

# 1. Initialize using the new v2 class name
mcp = MCPServer("MyFirstMCP")

# 2. Expose the tool
@mcp.tool()
def send_lead_to_n8n(name: str, email: str) -> str:
    """Sends a user's name and email to the n8n automation webhook."""
    webhook_url = "https://automation.ibigdata.in/webhook/35f9e9b4-ca60-4f2a-8f1e-395af53368d1"
    
    payload = json.dumps({"name": name, "email": email}).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(webhook_url, data=payload, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req) as response:
            return f"Successfully sent {name}'s data to n8n! Response: {response.read().decode('utf-8')}"
    except Exception as e:
        return f"Failed to send data to n8n. Error: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)