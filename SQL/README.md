# SQL & Database Engineering: Relational Integrity & Performance

This repository showcases how I solve database structure and performance problems, ensuring relational integrity and transaction safety.

## 🚨 The Problem: Transactional Cascade Faults
In production systems, deleting or modifying a parent record (like a Customer) without cleanly handling related transactional records (like Order Items or Active Shipments) causes orphaned rows, database bloat, and application crashes. In addition, slow query latency during high-traffic order placements leads to lost sales.

## 💡 The Solution: Safe Transaction Staging & Automated Procedures
I designed database constraints and PL/SQL procedures to secure transactions:
* **Cascading Safety:** Implemented staged multi-table deletes (Order Items -> Orders -> Customers) to guarantee that zero orphaned records remain in the system.
* **Auto-Sequence ID Ingestion:** Designed stored procedures to safely auto-increment IDs during bulk entries, preventing sequence clashes.
* **Transaction Safe-Guards (`COMMIT`/`ROLLBACK`):** Wrapped procedures in secure transaction blocks to roll back changes automatically if a step fails during runtime, keeping the database corruption-free.

## 🛠️ Code Breakdown & Skills
* **`transactional_order_processing.sql`** — Staged cascading deletions, foreign key management, and sequence tracking.
* **`hr_employee_procedures.sql`** — PL/SQL stored procedures implementing identity column auto-generations and rollback transaction logic.
