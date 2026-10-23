import joblib

cat_model = joblib.load("models/category_model.pkl")
pri_model = joblib.load("models/priority_model.pkl")
THRESHOLD = 0.6

def triage(text):
    text = text.lower().strip()
    cat_probs = cat_model.predict_proba([text])[0]
    pri_probs = pri_model.predict_proba([text])[0]
    category = cat_model.classes_[cat_probs.argmax()]
    priority = pri_model.classes_[pri_probs.argmax()]
    confidence = float(min(cat_probs.max(), pri_probs.max()))

    queue = f"{category}_queue" if confidence >= THRESHOLD else "human_review"
    if queue == "human_review":
        with open("data/low_confidence_log.txt", "a") as f:
            f.write(f"{text}\n")
    return {"category": category, "priority": priority,
            "confidence": round(confidence, 2), "queue": queue}

if __name__ == "__main__":
    print(triage("I was charged twice and need this fixed asap"))