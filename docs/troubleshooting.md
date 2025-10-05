# Troubleshooting Guide

This guide provides solutions to common problems you may encounter while using the Jules API MCP Server.

## "JULES_API_KEY environment variable is required"

This error message indicates that the `JULES_API_KEY` environment variable is not set. The MCP server needs this key to authenticate with the Jules API.

**Solution:**

1.  **Obtain an API Key:** If you don't have one, generate a new API key from the Settings page in the Jules web app.
2.  **Set the Environment Variable:** Before running the server, set the environment variable in your terminal:
    ```bash
    export JULES_API_KEY="your_api_key_here"
    ```
    Replace `"your_api_key_here"` with your actual API key.

    If you are using Docker, make sure to pass the environment variable when running the container:
    ```bash
    docker run -e JULES_API_KEY="your_api_key_here" -p 8000:8000 jules-mcp
    ```

## "Connection refused" when sending a `curl` request

This error typically means that the MCP server is not running or is not accessible at the address you are trying to reach.

**Solution:**

1.  **Ensure the server is running:** Check your terminal to see if the `uvicorn` process is still active. If not, restart the server:
    ```bash
    uvicorn server:app --host 0.0.0.0 --port 8000
    ```
2.  **Verify the address and port:** By default, the server runs on `http://localhost:8000`. Make sure your `curl` commands are directed to the correct address and port.

## HTTP 401 Unauthorized

An `HTTP 401` status code means that your request was not authorized. This is likely due to an invalid or expired API key.

**Solution:**

1.  **Verify your API key:** Double-check that the `JULES_API_KEY` you have set is correct and has not been revoked.
2.  **Regenerate the key:** If you suspect your key has been compromised or is no longer valid, generate a new one from the Jules web app and update the `JULES_API_KEY` environment variable.

## "Not Found" or "Method Not Allowed"

If you receive a "Not Found" or "Method Not Allowed" error, it's likely that the URL or the HTTP method in your `curl` command is incorrect.

**Solution:**

1.  **Check the URL:** Ensure that the URL path is correct (e.g., `http://localhost:8000/mcp/list_sources`).
2.  **Check the HTTP Method:** Some endpoints require a `POST` request. Make sure you are using the correct method for the tool you are trying to use. Refer to the [MCP Server Documentation](mcp_server.md) for the correct `curl` examples.
3.  **Check the Content-Type header:** For `POST` requests, ensure you are sending the `Content-Type: application/json` header.

If you continue to experience issues, please open an issue on the GitHub repository.