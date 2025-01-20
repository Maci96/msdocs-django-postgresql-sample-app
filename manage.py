#!/usr/bin/env python
"""Print SECRET_ENV environment variable."""
import os
import logging
from dotenv import load_dotenv

def main():
    """Log SECRET_ENV variable."""
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    # Load environment variables from the .env file
    load_dotenv('./.env')

    # Log the SECRET_ENV variable if it exists
    secret_env = os.getenv('SECRET_ENV')
    if secret_env:
        logging.info(f"SECRET_ENV: {secret_env}")
    else:
        logging.info("SECRET_ENV is not set")

if __name__ == '__main__':
    main()
