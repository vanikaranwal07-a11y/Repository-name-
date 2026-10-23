# AI Customer Support Ticket Triage

An AI-powered application that classifies customer support tickets, predicts their priority, and routes them to the appropriate queue using Natural Language Processing (NLP) and Machine Learning.

## Features

- **Ticket classification:** Predicts billing, technical, account, or product categories.
- **Priority prediction:** Classifies tickets as low, medium, or high priority.
- **Confidence-based routing:** Routes tickets to a category queue or sends low-confidence predictions for human review.
- **Interactive web interface:** Built with Streamlit.
- **Model evaluation:** Uses precision, recall, F1-score, and confusion matrices.

## Tech Stack

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Joblib
- Matplotlib
- Streamlit

## Project Structure

```text
ticket-triage/
├── app.py
├── requirements.txt
├── data/
│   ├── tickets.csv
│   └── low_confidence_log.txt
├── models/
│   ├── category_model.pkl
│   └── priority_model.pkl
└── src/
    ├── __init__.py
    ├── make_data.py
    ├── explore.py
    ├── train.py
    └── predict.py
```

## Dataset

A synthetic dataset of 1,000 customer support tickets was generated for this baseline project.

- 250 billing tickets
- 250 technical tickets
- 250 account tickets
- 250 product tickets

Each ticket includes text, category, and priority labels.

## Model Performance

The models were evaluated using an 80/20 train-test split with `random_state=42`.

| Metric | Category Model | Priority Model |
|---|---:|---:|
| Accuracy | 100% | 70% |
| Macro F1-score | 1.00 | 0.72 |
| Weighted F1-score | 1.00 | 0.70 |

### Priority Classification F1-scores

| Class | F1-score |
|---|---:|
| High | 1.00 |
| Low | 0.62 |
| Medium | 0.53 |

**Note:** These are baseline results on synthetic data. The category score is unusually high because the generated messages contain clear category-specific patterns. Priority labels partly depend on randomness, limiting how well the model can learn them. Performance on real tickets may be substantially lower.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vanikaranwal07-a11y/Repository-name-.git
cd Repository-name-
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the dataset

```bash
python src/make_data.py
```

### 5. Train both models

```bash
python src/train.py
```

### 6. Run the prediction script

```bash
python src/predict.py
```

### 7. Launch the web application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Application Screenshot

Add a screenshot of the running Streamlit app at `screenshots/app.png`.

![Support Ticket Triage application screenshot](screenshots/app.png)

## Future Improvements

- Train and evaluate on a realistic, labelled customer support dataset.
- Improve priority prediction and validate confidence thresholds.
- Add ticket history and routing analytics.
- Improve the human-review workflow.
- Add automated tests and model monitoring.

## Disclaimer

This is an educational machine-learning prototype. Predictions and confidence scores should be validated before using the system for real customer support operations.
