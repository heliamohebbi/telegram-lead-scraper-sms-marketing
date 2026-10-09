# Telegram Lead Scraper for SMS Marketing & CRM

An asynchronous Python automation pipeline designed to extract verified audience contacts and lead metadata from niche Telegram communities for targeted **SMS Marketing campaigns**, **CRM enrichment**, and cold outreach workflows.

---

## 🎯 Marketing & Business Use Cases
- **SMS Campaign Targeting:** Generates clean CSV contact lists with phone numbers (where available) directly formatted for SMS bulk platforms.
- **Lead Enrichment:** Captures full name, Telegram usernames, and user IDs for multi-channel sales attribution.
- **Audience Research:** Scrapes active participants from industry-specific groups to build targeted ICP (Ideal Customer Profile) segments.

---

## ⚙️ Technical Highlights
- **High-throughput Async Retrieval:** Built with `Telethon` utilizing the MTProto API for fast, non-blocking pagination.
- **Security & Compliance:** Credential abstraction via `.env` files to prevent secret leakage in version control.
- **Data Export:** Clean tabular CSV output with standardized international phone prefix formatting.

---

## 🚀 Setup & Execution

### 1. Clone the repository
```bash
git clone https://github.com/heliamohebbi/telegram-lead-scraper-sms-marketing.git
cd telegram-lead-scraper-sms-marketing
