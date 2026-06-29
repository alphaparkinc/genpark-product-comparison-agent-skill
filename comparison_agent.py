import os
from typing import List, Dict, Any, Optional

class ProductComparisonClient:
    """
    Production-grade comparison engine that computes weighted recommendation scores
    and outputs auto-formatted markdown feature grids.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("COMPARISON_API_KEY")

    def compare(self, products: List[Dict[str, Any]], priorities: Dict[str, Any]) -> Dict[str, Any]:
        """
        Runs mathematical comparison scoring and constructs a markdown matrix table.
        """
        if len(products) < 2:
            return {
                "comparison_table_markdown": "Minimum of 2 products required to compare.",
                "ranked_skus": []
            }

        price_weight = priorities.get("price_importance", 3)
        feature_weight = priorities.get("feature_richness", 3)

        # 1. Math scoring
        scored = []
        prices = [p["price"] for p in products]
        min_price = min(prices) if prices else 1.0

        for prod in products:
            sku = prod["sku"]
            name = prod["name"]
            price = float(prod["price"])
            rating = float(prod["rating"])
            features = prod.get("features", {})
            feature_count = len(features)

            # Price Score: cheaper is better (relative to min price)
            price_score = (min_price / price) * 10.0 if price > 0 else 10.0
            
            # Feature Richness Score
            feature_score = min(10.0, feature_count * 2.0)

            # Weighted sum
            total_score = round(
                ((price_score * price_weight) + (feature_score * feature_weight)) / (price_weight + feature_weight), 
                2
            )

            verdict = "Excellent choice" if total_score >= 8.0 else "Decent value" if total_score >= 6.0 else "Consider alternatives"
            scored.append({
                "sku": sku,
                "name": name,
                "score": total_score,
                "verdict": verdict,
                "price": price,
                "rating": rating,
                "feature_count": feature_count
            })

        # Sort ranked products by score descending
        scored.sort(key=lambda x: x["score"], reverse=True)

        # 2. Markdown comparison table generation
        header = "| Spec / Attribute | " + " | ".join([p["name"] for p in scored]) + " |\n"
        separator = "| --- | " + " | ".join(["---" for _ in scored]) + " |\n"
        
        row_price = "| **Price** | " + " | ".join([f"${p['price']:.2f}" for p in scored]) + " |\n"
        row_rating = "| **Rating** | " + " | ".join([f"{p['rating']:.1f}/5.0" for p in scored]) + " |\n"
        row_score = "| **GenPark Score** | " + " | ".join([f"**{p['score']:.2f}/10.0**" for p in scored]) + " |\n"
        row_verdict = "| **Verdict** | " + " | ".join([p["verdict"] for p in scored]) + " |\n"

        markdown_table = header + separator + row_price + row_rating + row_score + row_verdict

        return {
            "comparison_table_markdown": markdown_table,
            "ranked_skus": [
                {"sku": p["sku"], "score": p["score"], "verdict": p["verdict"]} for p in scored
            ]
        }
