# Student Health Risk Prediction — ML Deployment

Predicts student health risk category (at-risk / unhealthy / fit) from lifestyle and biometric data.
Built for the Kaggle Playground Series (July 2026), extended beyond the competition scope with a deployed inference API.

## Project structure
- Model training and experimentation: `notebook.ipynb` (Kaggle environment)
- Deployment: FastAPI service (`app/`) serving a trained LightGBM pipeline
- Model artifacts: `models/`

## Status
🚧 In progress — model trained (balanced accuracy ~0.95), deployment layer being built.

## Stack
- LightGBM, scikit-learn (modeling)
- FastAPI (serving)
- Streamlit (demo UI) — planned

## Run Locally
Primary Streamlit entry: `streamlit_app.py`

1. Create or activate your Python environment (example using Conda):

```powershell
conda activate health-api
pip install -r requirements.txt
```

2. Start the backend API:

```powershell
python -m uvicorn app.main:app --reload --port 8000
```

3. Start the Streamlit UI (in a separate shell):

```powershell
python -m streamlit run streamlit_app.py
```

Open `http://localhost:8501` in your browser. If the UI shows an error about predictions, ensure the backend is running at `http://127.0.0.1:8000`.

If you prefer the demo UI inside the `app/` folder, it has been removed to avoid duplication — use the root `streamlit_app.py` instead.

