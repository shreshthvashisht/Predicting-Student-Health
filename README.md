# Student Health Risk Prediction — ML Deployment

Predicts student health risk category (at-risk / unhealthy / fit) from lifestyle and biometric data.
Built for the Kaggle Playground Series (July 2026), extended beyond the competition scope into a fully deployed, containerized inference service.

**Live demo**: [add your Render URL once live]

## Architecture
- **Model training**: LightGBM classifier in a scikit-learn `Pipeline` (imputation, scaling, one-hot encoding), tuned via `GridSearchCV`, trained in a Kaggle notebook (`predicting_stduent_health.ipynb`)
- **Serving**: FastAPI backend (`app/`) loading the trained pipeline, exposing a validated `/predict` endpoint via Pydantic schemas
- **Frontend**: Streamlit UI (`streamlit_app.py`) calling the FastAPI backend over HTTP
- **Containerization**: single Docker image running both services together (`Dockerfile`, `start.sh`)
- **Deployment**: hosted on Render (free tier), built directly from the Dockerfile

## Project structure
app/
├── schema.py # Pydantic request/response models
├── model.py # Model loading + inference logic
└── main.py # FastAPI app and routes
models/ # Trained pipeline + label encoder (.pkl)
streamlit_app.py
Dockerfile
start.sh
requirements.txt


## Status
✅ Model trained (balanced accuracy ~0.95)
✅ FastAPI + Streamlit working end-to-end, locally and containerized
✅ Deployed live on Render

## Notes on missing data
The trained pipeline includes imputers (median for numeric fields, a distinct category for missing categorical fields), so the API and UI both accept partial/blank input rather than requiring every field. Predictions on heavily incomplete input are less reliable than on complete records.

## Run locally

1. Create or activate your Python environment (example using Conda):
```powershell
conda activate health-api
pip install -r requirements.txt
```

2. Start the backend API:
```powershell
python -m uvicorn app.main:app --reload --port 8000
```

3. Start the Streamlit UI, in a separate terminal:
```powershell
python -m streamlit run streamlit_app.py
```

Open `http://localhost:8501` in your browser. If the UI shows a prediction error, confirm the backend is running at `http://127.0.0.1:8000`.

## Run with Docker

```bash
docker build -t health-app .
docker run -p 7860:7860 health-app
```
Open `http://localhost:7860`.

## Stack
- LightGBM, scikit-learn (modeling)
- FastAPI, Pydantic (serving)
- Streamlit (demo UI)
- Docker (containerization)
- Render (hosting)