# MCP Server API Reference

This document provides a detailed reference for the tools available through the Jules API MCP Server.

## `list_sources`

List all available sources connected to Jules.

**Returns:** A JSON string containing a list of sources.

**Example:**
```json
{
  "sources": [
    {
      "name": "sources/github/example-user/example-repo",
      "id": "github/example-user/example-repo",
      "githubRepo": {
        "owner": "example-user",
        "repo": "example-repo"
      }
    }
  ]
}
```

## `create_session`

Create a new session with a given prompt and source.

**Arguments:**

*   `prompt` (str): The initial prompt for the session.
*   `source` (str): The name of the source to use for the session (e.g., "sources/github/example-user/example-repo").
*   `starting_branch` (str, optional): The starting branch for the session. Defaults to "main".
*   `title` (str, optional): The title of the session. Defaults to the first 50 characters of the prompt.

**Returns:** A JSON string representing the newly created session.

**Example:**
```json
{
  "name": "sessions/1234567890",
  "id": "1234567890",
  "title": "My New Session",
  "sourceContext": {
    "source": "sources/github/example-user/example-repo",
    "githubRepoContext": {
      "startingBranch": "main"
    }
  },
  "prompt": "My new session prompt."
}
```

## `list_sessions`

List all sessions.

**Arguments:**

*   `page_size` (int, optional): The number of sessions to return per page. Defaults to 10.

**Returns:** A JSON string containing a list of sessions.

## `approve_plan`

Approve the plan for a given session.

**Arguments:**

*   `session_id` (str): The ID of the session.

**Returns:** An empty JSON response on success.

## `list_activities`

List activities in a given session.

**Arguments:**

*   `session_id` (str): The ID of the session.
*   `page_size` (int, optional): The number of activities to return per page. Defaults to 30.

**Returns:** A JSON string containing a list of activities.

## `send_message`

Send a message to a given session.

**Arguments:**

*   `session_id` (str): The ID of the session.
*   `prompt` (str): The message to send.

**Returns:** An empty JSON response on success.