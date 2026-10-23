
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

df = pd.read_csv("data/tickets.csv").dropna(
    subset=["text", "category", "priority"]
)
df["text"] = df["text"].str.lower().str.strip()

Path("models").mkdir(exist_ok=True)

def train(target, filename):
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"],
        df[target],
        test_size=0.2,
        stratify=df[target],
        random_state=42
    )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2)),
        ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ])

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"\n=== {target} ===")
    print(classification_report(y_test, y_pred))

    ConfusionMatrixDisplay.from_predictions(
        y_test, y_pred, xticks_rotation=45, cmap="Blues"
    )
    plt.title(f"Confusion Matrix - {target}")
    plt.tight_layout()
    plt.show()

    mistakes = pd.DataFrame({
        "text": X_test,
        "actual": y_test,
        "predicted": y_pred
    })
    mistakes = mistakes[mistakes["actual"] != mistakes["predicted"]]

    print("\n=== Misclassified Tickets ===")
    if mistakes.empty:
        print("No misclassified tickets!")
    else:
        print(mistakes.head(10).to_string(index=False))

    joblib.dump(model, filename)
    print(f"Saved model: {filename}")

train("category", "models/category_model.pkl")
train("priority", "models/priority_model.pkl")
