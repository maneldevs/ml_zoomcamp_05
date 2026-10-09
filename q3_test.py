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