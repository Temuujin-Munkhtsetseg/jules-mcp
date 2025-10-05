FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

# The API key should be provided at runtime via environment variable
# ENV JULES_API_KEY=your_api_key_here

EXPOSE 8000

# Use uvicorn to run the ASGI app
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]