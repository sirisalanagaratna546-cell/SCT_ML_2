from flask import Flask, jsonify, send_from_directory
from pathlib import Path
import random

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent

segment_profiles = [
    {"name": "Budget Conscious", "color": "#f59e0b", "baseIncome": 18, "baseSpend": 20, "spread": 7},
    {"name": "Value Seekers", "color": "#38bdf8", "baseIncome": 28, "baseSpend": 35, "spread": 6},
    {"name": "Premium Buyers", "color": "#34d399", "baseIncome": 45, "baseSpend": 60, "spread": 8},
    {"name": "Occasional Shoppers", "color": "#fb7185", "baseIncome": 32, "baseSpend": 15, "spread": 6},
    {"name": "Loyal High Spenders", "color": "#a78bfa", "baseIncome": 60, "baseSpend": 78, "spread": 5},
]


def generate_customers():
    customers = []
    for idx, profile in enumerate(segment_profiles):
        count = [55, 45, 35, 35, 30][idx]
        for _ in range(count):
            income = round(max(8, profile["baseIncome"] + (random.random() - 0.5) * profile["spread"] * 2 + len(customers) * 0.08), 1)
            spend = round(max(5, profile["baseSpend"] + (random.random() - 0.5) * profile["spread"] * 2 - len(customers) * 0.03), 1)
            age = int(max(18, min(70, profile["baseIncome"] + 16 + random.random() * 25 - len(customers) * 0.1)))
            customers.append({
                "CustomerID": len(customers) + 1,
                "Gender": "Female" if random.random() > 0.5 else "Male",
                "Age": age,
                "AnnualIncome": income,
                "SpendingScore": spend,
                "Segment": profile["name"],
                "Cluster": idx + 1,
                "color": profile["color"],
            })
    return customers


@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "customer_dashboard.html")


@app.route("/api/customers")
def customers_api():
    return jsonify(generate_customers())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
