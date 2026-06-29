import sys
import json
from comparison_agent import ProductComparisonClient

def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        
    print("=== GenPark Multi-Product Comparison Agent Verification ===")
    client = ProductComparisonClient()

    # Product Options to compare
    products = [
        {
            "sku": "SKU-ZENITH-A1",
            "name": "Zenith Hub Pro",
            "price": 199.00,
            "rating": 4.8,
            "features": {"wireless": "Yes", "smart_assistant": "GenPark", "warranty": "2 years", "battery": "12 hours"}
        },
        {
            "sku": "SKU-BUDGET-B1",
            "name": "EcoHub Standard",
            "price": 99.00,
            "rating": 4.1,
            "features": {"wireless": "Yes", "smart_assistant": "Fallback", "warranty": "1 year"}
        }
    ]

    # Weighted Priorities: User values Price more than feature count
    priorities = {
        "price_importance": 5,
        "feature_richness": 2
    }

    result = client.compare(products, priorities)
    
    print("\n--- Ranked Results ---")
    print(json.dumps(result["ranked_skus"], indent=2))
    
    print("\n--- Generated Markdown Comparison Matrix ---")
    print(result["comparison_table_markdown"])

if __name__ == "__main__":
    main()
