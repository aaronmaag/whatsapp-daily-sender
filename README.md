Python service that sends a daily WhatsApp message to phone numbers in a database.
Uses a temporary stubbed WhatsApp API. Demonstrate's core scheduling and data-handling logic before proper integration.

Overview:
    Reads active phone numbers from the database

    Ensures each user receives at most one message per day (via database constraints)

    Logs all message attempts (sent, skipped, or failed)

    Supports dry-run mode for testing

    Can be triggered manually, via cron, or by GCP Cloud Scheduler calling a Cloud Run endpoint