import os
import csv
import logging
from telethon.sync import TelegramClient
from dotenv import load_dotenv

# Configure structured logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)

# Load environment configuration
load_dotenv()
API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")
TARGET_COMMUNITY = os.getenv("TELEGRAM_TARGET_COMMUNITY")

if not API_ID or not API_HASH:
    raise ValueError("Missing API credentials. Please configure .env file.")

client = TelegramClient("lead_gen_session", int(API_ID), API_HASH)

async def extract_marketing_leads(output_file="marketing_leads.csv"):
    """
    Extracts group participants with contact metadata for SMS & cold outreach pipelines.
    """
    await client.start()
    logging.info("Connected to Telegram Client successfully.")

    try:
        entity = await client.get_entity(TARGET_COMMUNITY)
        community_name = getattr(entity, 'title', TARGET_COMMUNITY)
        logging.info(f"Target community found: {community_name}")
    except Exception as e:
        logging.error(f"Error resolving community target: {e}")
        return

    leads_data = []
    phone_lead_count = 0

    logging.info("Harvesting community profiles for SMS marketing pipeline...")

    async for user in client.iter_participants(entity):
        user_id = user.id
        first_name = user.first_name or ""
        last_name = user.last_name or ""
        username = user.username or "N/A"
        phone = getattr(user, "phone", None)

        if phone:
            phone_lead_count += 1
            phone_str = f"+{phone}" if not str(phone).startswith("+") else str(phone)
        else:
            phone_str = "N/A"

        leads_data.append([user_id, first_name, last_name, username, phone_str])

    # Export clean dataset to CSV ready for SMS / CRM platforms
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["User ID", "First Name", "Last Name", "Username", "Phone Number"])
        writer.writerows(leads_data)

    logging.info(f"Pipeline finished! Total records: {len(leads_data)} | Qualified phone leads: {phone_lead_count}")
    logging.info(f"Saved dataset to '{output_file}'.")

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(extract_marketing_leads())
