import os
import httpx
from fastmcp import FastMCP
from starlette.responses import JSONResponse

# API key from environment
API_KEY = os.getenv("JULES_API_KEY")
if not API_KEY:
    raise ValueError("JULES_API_KEY environment variable is required")

BASE_URL = "https://jules.googleapis.com/v1alpha"

mcp = FastMCP(name="Jules API MCP Server")

@mcp.tool(tags={"jules", "api", "sources"})
def list_sources() -> str:
    """List all available sources connected to Jules."""
    response = httpx.get(f"{BASE_URL}/sources", headers={"X-Goog-Api-Key": API_KEY})
    response.raise_for_status()
    return response.text

@mcp.tool(tags={"jules", "api", "sessions", "create"})
def create_session(prompt: str, source: str, starting_branch: str = "main", title: str = None) -> str:
    """Create a new session with the given prompt and source."""
    if title is None:
        title = prompt[:50]  # Truncate if too long
    data = {
        "prompt": prompt,
        "sourceContext": {
            "source": source,
            "githubRepoContext": {
                "startingBranch": starting_branch
            }
        },
        "title": title
    }
    response = httpx.post(f"{BASE_URL}/sessions", headers={"Content-Type": "application/json", "X-Goog-Api-Key": API_KEY}, json=data)
    response.raise_for_status()
    return response.text

@mcp.tool(tags={"jules", "api", "sessions", "list"})
def list_sessions(page_size: int = 10) -> str:
    """List all sessions."""
    params = {"pageSize": page_size}
    response = httpx.get(f"{BASE_URL}/sessions", headers={"X-Goog-Api-Key": API_KEY}, params=params)
    response.raise_for_status()
    return response.text

@mcp.tool(tags={"jules", "api", "sessions", "approve"})
def approve_plan(session_id: str) -> str:
    """Approve the plan for the given session."""
    response = httpx.post(f"{BASE_URL}/sessions/{session_id}:approvePlan", headers={"Content-Type": "application/json", "X-Goog-Api-Key": API_KEY})
    response.raise_for_status()
    return response.text

@mcp.tool(tags={"jules", "api", "sessions", "activities"})
def list_activities(session_id: str, page_size: int = 30) -> str:
    """List activities in the given session."""
    params = {"pageSize": page_size}
    response = httpx.get(f"{BASE_URL}/sessions/{session_id}/activities", headers={"X-Goog-Api-Key": API_KEY}, params=params)
    response.raise_for_status()
    return response.text

@mcp.tool(tags={"jules", "api", "sessions", "message"})
def send_message(session_id: str, prompt: str) -> str:
    """Send a message to the given session."""
    data = {"prompt": prompt}
    response = httpx.post(f"{BASE_URL}/sessions/{session_id}:sendMessage", headers={"Content-Type": "application/json", "X-Goog-Api-Key": API_KEY}, json=data)
    response.raise_for_status()
    return response.text

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    """Health check endpoint."""
    return JSONResponse({"status": "healthy", "server": "Jules API MCP Server"})

# Create ASGI app with MCP at /mcp path
app = mcp.http_app(path='/mcp')