# Data dictionary
| Table | Grain | Key columns |
|---|---|---|
| DimDate | one row per day (2023-01-01 → 2025-12-31) | DateKey, Date, Year, Quarter, MonthNo, MonthName, Weekday, IsWeekend |
| DimStore | one row per store | StoreID, StoreName, City, StoreType (Premium/Standard/Economy) |
| DimProduct | one row per product | ProductID, ProductName, Category, Segment, BasePrice |
| DimCustomer | one row per customer | CustomerID, CustomerName, Segment (Low/Medium/High Spender), RegistrationYear |
| FactSales | one row per order line | OrderID, DateKey, StoreID, CustomerID, ProductID, OrderHour, Quantity, UnitPrice, DiscountPct, UnitCost |
| FactInventory | monthly stock snapshot per store/product | InventoryDate, StoreID, ProductID, StockQty |
| FactOperations | hourly per store (2025 only) | Date, StoreID, Hour, CustomersServed, StaffCount, AvgQueueMinutes |

Revenue = Quantity × UnitPrice × (1 − DiscountPct/100); Profit = Revenue − Quantity × UnitCost.
