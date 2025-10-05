# MCP Server Documentation

This document provides detailed information on setting up and using the MCP server to interact with the Jules API.

## Getting Started

Follow these steps to get the MCP server up and running.

### Prerequisites

- Python 3.7+
- An API key for the Jules API. You can generate one from the Jules web app.

### Installation & Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/example/jules-mcp-server.git
    cd jules-mcp-server
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set the API key:**

    ```bash
    export JULES_API_KEY="your_api_key_here"
    ```

4.  **Run the server:**

    ```bash
    uvicorn server:app --host 0.0.0.0 --port 8000
    ```

The MCP server will be accessible at `http://localhost:8000/mcp`, and the health check is available at `http://localhost:8000/health`.

### Docker Setup

Alternatively, you can use Docker to run the server.

1.  **Build the image:**

    ```bash
    docker build -t jules-mcp .
    ```

2.  **Run the container:**

    ```bash
    docker run -e JULES_API_KEY="your_api_key_here" -p 8000:8000 jules-mcp
    ```

## Examples

Here are some examples of how to use the MCP server with `curl`.

### List Sources

List all available sources connected to Jules.

```bash
curl http://localhost:8000/mcp/list_sources
```

### Create a Session

Create a new session with a prompt and a source.

```bash
curl http://localhost:8000/mcp/create_session \
    -H "Content-Type: application/json" \
    -d '{
        "prompt": "Create a boba app!",
        "source": "sources/github/bobalover/boba"
    }'
```

### List Sessions

List all of your active sessions.

```bash
curl http://localhost:8000/mcp/list_sessions
```

### Approve a Plan

Approve the plan for a given session.

```bash
curl http://localhost:8000/mcp/approve_plan \
    -H "Content-Type: application/json" \
    -d '{"session_id": "YOUR_SESSION_ID"}'
```

### List Activities

List the activities within a given session.

```bash
curl http://localhost:8000/mcp/list_activities \
    -H "Content-Type: application/json" \
    -d '{"session_id": "YOUR_SESSION_ID"}'
```

### Send a Message

Send a message to a specific session.

```bash
curl http://localhost:8000/mcp/send_message \
    -H "Content-Type: application/json" \
    -d '{
        "session_id": "YOUR_SESSION_ID",
        "prompt": "Can you make the app corgi themed?"
    }'
```