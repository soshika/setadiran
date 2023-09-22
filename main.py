import os
from dotenv import load_dotenv


def get_personal_info():
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    username = os.getenv("PERSONAL_USERNAME")
    password = os.getenv("PERSONAL_PASSWORD")

    return username, password


