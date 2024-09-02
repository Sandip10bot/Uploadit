import os
import logging

# Set up logging
logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    # Read environment variables and set default values if not provided
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    try:
        API_ID = int(os.environ.get("API_ID", "0"))  # Default to "0" if not set
        if API_ID <= 0:
            raise ValueError("API_ID must be a positive integer.")
    except ValueError:
        raise ValueError("API_ID must be set and be a valid integer.")
    
    API_HASH = os.environ.get("API_HASH", "")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    try:
        CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", "128"))  # Default to "128" if not set
        if CHUNK_SIZE <= 0:
            raise ValueError("CHUNK_SIZE must be a positive integer.")
    except ValueError:
        raise ValueError("CHUNK_SIZE must be set and be a valid integer.")
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 0
    DEF_WATER_MARK_FILE = "LegendSources"
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "LegendSources")
    
    try:
        LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))  # Default to "0" if not set
        if LOG_CHANNEL <= 0:
            raise ValueError("LOG_CHANNEL must be a positive integer.")
    except ValueError:
        raise ValueError("LOG_CHANNEL must be set and be a valid integer.")
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    
    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", "0"))  # Default to "0" if not set
        if OWNER_ID <= 0:
            raise ValueError("OWNER_ID must be a positive integer.")
    except ValueError:
        raise ValueError("OWNER_ID must be set and be a valid integer.")
    
    TG_MIN_FILE_SIZE = 2097152000
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
