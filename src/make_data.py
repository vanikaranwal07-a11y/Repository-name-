import random
import pandas as pd

random.seed(42)

templates = {
    "billing": [
        "I was charged twice for my {thing} this month",
        "Please refund my last payment, it was a mistake",
        "My invoice shows the wrong amount for {thing}",
        "Why was my card billed after I cancelled?",
        "I need a receipt for my {thing} payment",
    ],
    "technical": [
        "The app crashes whenever I open {thing}",
        "I get an error message when I try to upload a file",
        "The {thing} page is not loading at all",
        "Everything is very slow and keeps freezing",
        "I cannot connect, it says server timeout",
    ],
    "account": [
        "I forgot my password and cannot log in",
        "Please change the email address on my account",
        "My account is locked after too many attempts",
        "How do I delete my account and data?",
        "I did not receive the verification code for {thing}",
    ],
    "product": [
        "Does your {thing} plan include unlimited storage?",
        "Is there a way to export my data to Excel?",
        "I would like to request a dark mode feature",
        "What is the difference between the basic and pro {thing}?",
        "Can the {thing} integrate with other tools?",
    ],
}

things = ["subscription", "dashboard", "mobile app", "premium", "report", "settings"]
urgent_words = ["urgent", "asap", "immediately", "critical", "right now"]

rows = []
for category, tmpls in templates.items():
    for _ in range(250):
        text = random.choice(tmpls).format(thing=random.choice(things))
        if random.random() < 0.3:
            text += " " + random.choice(urgent_words) + "!"
            priority = "high"
        elif category in ("technical", "billing") and random.random() < 0.4:
            priority = "medium"
        else:
            priority = random.choice(["low", "low", "medium"])
        rows.append({"text": text, "category": category, "priority": priority})

df = pd.DataFrame(rows).sample(frac=1, random_state=42)
df.to_csv("data/tickets.csv", index=False)
print(df.head(), df.shape)