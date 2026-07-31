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
