# Supermarket Sales Analysis — Power BI

An end-to-end Power BI project analysing sales, customers, inventory and store operations of a **simulated** supermarket chain (8 stores, 15 products, 2,500 customers, 2023–2025, ~97K orders).

> **Note:** the dataset is synthetic and created for portfolio purposes. Store and customer names are fictional; any resemblance to real companies is coincidental. Findings describe this dataset only.

## Report pages
| Page | What it answers |
|---|---|
| Executive Summary | Sales vs target, average basket, growth, sales by city and category |
| Product Analysis | Sales, profit, margin and inventory turnover by category / segment / product |
| Customer & Campaign Analysis | Customer segments, repeat rate, impact of discounts on sales and profit |
| Inventory & Operations | Stock levels and value, queue time and staffing by hour and store |

*(add screenshots to `images/` and link them here)*

## Key findings
- Revenue grew every year (1.56M → 2.72M → 4.54M), but profit fell in 2025 (351K → 226K).
- Discounts of 25%+ account for ~18% of revenue and produce a net loss (~156K).
- Two stores run at a slightly negative margin (≈ −2%); the rest earn ≈ 12–13%.
- Premium products drive most revenue but earn ≈ 7% margin vs ≈ 26% for Standard.
- Checkout queues average ~35 min between 6–8 PM vs ~6 min otherwise.

## Data model
Star schema: `FactSales`, `FactInventory`, `FactOperations` connected to `DimDate`, `DimStore`, `DimProduct`, `DimCustomer`. See [DATA_DICTIONARY.md](DATA_DICTIONARY.md).

## Data cleaning
Documented in the `Change_Log` sheet and `scripts/`:
- 706 exact duplicate sales rows removed
- 15 quantity outliers (8–45 vs. normal 1–7) removed
- 980 customers had a registration year later than their first purchase → corrected
- Customer name inconsistencies fixed; all text translated to English

## How to open
1. Open `report/Supermarket_Sales_Dashboard.pbix` in Power BI Desktop.
2. If data is missing: *Transform data → Data source settings* and point to `data/Supermarket_Sales_Analysis_clean.xlsx`, then **Refresh**.

## Tools
Power BI, DAX, Power Query, Excel, Python (pandas).
