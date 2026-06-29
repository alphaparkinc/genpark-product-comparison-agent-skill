# GenPark Product Comparison Agent Skill

This repository contains the **GenPark Product Comparison Agent Skill** — an agent configuration skill config (`skill.json`), a production-ready Python SDK client (`comparison_agent.py`), and executable verification tests. It is designed to compare multiple retail/product SKUs, apply dynamic weights to user pricing vs. features priorities, and generate structured markdown tables.

---

## 🚀 Capabilities

* **Weighted Priority Scoring:** Calculates relative values based on custom importance factors.
* **Auto-Markdown Generation:** Automatically constructs side-by-side spec comparison matrices.
* **Verdict Synthesis:** Resolves standard action guidelines for product recommendations.

---

## 🛠️ Setup & Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 SDK Usage Reference

```python
from comparison_agent import ProductComparisonClient

# Initialize client
client = ProductComparisonClient()

# Execute comparison
result = client.compare(
    products=[
        {"sku": "SKU-A", "name": "Item A", "price": 100, "rating": 4.5, "features": {"f1": "yes"}},
        {"sku": "SKU-B", "name": "Item B", "price": 80, "rating": 4.0, "features": {}}
    ],
    priorities={"price_importance": 4, "feature_richness": 1}
)

print(result["comparison_table_markdown"])
```

---

## 📜 License
This project is licensed under the MIT License.
