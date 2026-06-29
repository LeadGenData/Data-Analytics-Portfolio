# BDL Revenue Leakage Calculator & CRM

Documentation for the serverless revenue leakage recovery suite designed for business diagnostics and lead acquisition management.

## ⚙️ Architecture & Components
* **Intake Form:** Client-side form directing diagnostic metrics to the backend.
* **API Proxy Gateway:** Enforces CORS limits and masks endpoints via Cloudflare Workers.
* **Backend Database:** Google Sheets CRM running database integrity self-healing routines.
* **Document Auto-Generation:** Automated triggers building custom 6-page PDF audit reports and scheduling follow-up email campaigns.
