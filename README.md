# Jules API MCP Server

This is a Model Context Protocol (MCP) server that provides tools to interact with the Jules API.

## Setup

### Local Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set the API key:

   ```bash
   export JULES_API_KEY=your_api_key_here
   ```

3. Run the server:

   ```bash
   uvicorn server:app --host 0.0.0.0 --port 8000
   ```

The MCP server will be accessible at `http://localhost:8000/mcp` and the health check at `http://localhost:8000/health`.

### Docker Setup

1. Build the image:

   ```bash
   docker build -t jules-mcp .
   ```

2. Run the container:

   ```bash
   docker run -e JULES_API_KEY=your_api_key_here -p 8000:8000 jules-mcp
   ```

The server will be accessible at `http://localhost:8000/mcp` and health check at `http://localhost:8000/health`.

## Tools

- `list_sources`: List all available sources connected to Jules.
- `create_session`: Create a new session with a prompt and source.
- `list_sessions`: List all sessions.
- `approve_plan`: Approve the plan for a given session.
- `list_activities`: List activities in a given session.
- `send_message`: Send a message to a given session.

## API Reference

See `docs/api.md` for the Jules API documentation.
