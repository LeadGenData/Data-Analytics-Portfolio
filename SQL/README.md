# SQL & Database Querying: Data Staging & Extraction

This folder contains SQL scripts demonstrating relational database queries, table joins, and basic transactional staging structures.

## 🚨 The Problem: Trapped Data & Slow BI Dashboards
When preparing datasets for Power BI dashboards, raw transactional data is spread across multiple unjoined tables (like Customers, Orders, and Products). Querying these tables inefficiently or loading dirty data results in slow report rendering, duplicate records, and skewed business metrics.

## 💡 The Solution: Clean Staging Queries & Relational Joins
I write SQL queries to extract, clean, and structure data for business reporting:
* **Relational Joins:** Implemented INNER/LEFT joins to connect customer details against active order transactions.
* **Data Aggregation & Filters:** Used analytical functions, sorting, and groups (`GROUP BY`, `SUM`, `ORDER BY`) to extract KPIs like total customer spend.
* **Data Ingestion Staging:** Set up basic transactional updates (`INSERT`, `DELETE`) to stage test records in relational database structures.

## 🛠️ Code Breakdown & Skills
* **`transactional_order_processing.sql`** — Demonstrates SQL table querying, data filtering, and cascade deletes.
* **`hr_employee_procedures.sql`** — SQL stored procedures designed to stage transaction entries.
