# Systems Engineering: The BDL Revenue Recovery CRM & Calculator

This repository documents the architecture of a serverless lead acquisition system designed to recover lost revenue margins for businesses.

## 🚨 The Problem: High Cold-Outreach Friction & Poor Lead Conversion
Standard cold-email outreach has less than a 2% response rate because prospects receive generic pitches. Additionally, building calculators that run complex financial logic on the client-side exposes intellectual property, while directly connecting forms to databases creates database credentials leakage risks.

## 💡 The Solution: Secure, Server-Side Diagnostic Pipeline
I architected a serverless automation funnel:
* **Interactive Diagnostic Intake:** Prospects enter simple metrics on a React frontend.
* **API Proxy Masking:** Offloaded processing through a Cloudflare Workers proxy. This worker enforces strict CORS limits, blocks unauthorized scrapers, and hides the backend endpoint.
* **Server-Side Apps Script Engine:** Processes the financial calculations securely on the server-side, keeping logic private.
* **Automated Audit Delivery:** Instantly generates a customized, unredacted 6-page PDF audit report and schedules follow-up drip emails based on lead engagement.

## 📈 Business Impact
* **High Trust Value:** Cold prospects immediately receive a personalized PDF audit of their business leakage, increasing outreach conversions.
* **Zero Database Vulnerabilities:** By using API proxies and serverless backends, database credentials are never exposed to the client browser.
