#!/bin/bash
set -e

# Start the FastAPI backend in the background, on an internal-only port.
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Give it a moment to finish loading the pickled model before Streamlit
# starts sending it requests.
sleep 3

# Start Streamlit in the foreground, on the port Hugging Face Spaces expects.
# --server.address 0.0.0.0 makes it reachable from outside the container.
streamlit run streamlit_app.py --server.port 7860 --server.address 0.0.0.0