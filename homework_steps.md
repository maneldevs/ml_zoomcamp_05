## Homework 5 - Steps

### Set up

- Install uv

```bash
pip install uv
uv version
```

- Install depencencies

```bash
uv sync --locked
```

- Test

```bash
uv run python smoke_test.py
sha256sum pipeline.bin
```

### Question 1. Environment check

```bash
uv --version
```
RESPONSE uv 0.12.24 (x86_64-unknown-linux-gnu)

### Question 2. Locked depencency

Open pyproject.toml and uv.lock. Which Scikit-Learn version is part of the 2026 reference environment?

RESPONSE: 1.7.2

### Question 3. Load the model

-  Create a new file called q3_test.py

```python
import pickle

LEAD = {
  "lead_source": "paid_ads",
  "industry": "technology",
  "employment_status": "employed",
  "location": "north_america",
  "number_of_courses_viewed": 2,
  "annual_income": 79276.0,
  "interaction_count": 4,
  "lead_score": 0.41
}

with open('pipeline.bin', 'rb') as model_file:
    pipeline = pickle.load(model_file)

y_pred = pipeline.predict_proba(LEAD)[0, 1]
print(f'Prediction: {round(y_pred, 3)}')
```

Run the test

```bash
uv run python q3_test.py
```

RESPONSE: Prediction: 0.533

### Question 4. Serve the model

```bash
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
```

Open a new terminal and run the following command:

```
curl http://localhost:9696/health
# {"status":"ok","model_sha256":"1646bbdcd38d4f044da6b630c5b332c93a314245a8c21929011c42de51f629f1","feature_defaults_sha256":"04c07631a4f95a7811bab977cc43ed9eb6f4c7490531630923581f2a0ae82dcf"}(mlzoomcamp-2026-deployment)
```

```bash
curl -X POST -H "Content-Type: application/json" -d '{"lead_source": "organic_search", "industry": "technology", "employment_status": "employed", "location": "europe", "number_of_courses_viewed": 4, "annual_income": 80304.0, "interaction_count": 7, "lead_score": 0.74}' http://localhost:9696/predict
```

{"conversion_probability":0.769799,"conversion":true}
RESPONSE: 0.770

### Question 5. Look at the container configuration

Exit from devcontainer and open folder in WSL2

Executes the following command to build and run the container:

```bash
docker build -t zoomcamp-model:2026-hw5 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw5
```

Open Dockerfile to see the image

RESPONSE: python:3.11.15-slim-bookworm


### Question 6. Run the container

- Open a new terminal and run the following command:
- python3 q6_test.py

{'conversion_probability': 0.769799, 'conversion': True}
RESPONSE: 0.770