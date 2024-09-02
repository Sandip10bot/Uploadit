import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    # Default to 0 if environment variable is missing or invalid
    API_ID = int(os.environ.get("API_ID", "0"))
    if API_ID == 0:
        raise ValueError("API_ID must be set and be a valid integer.")
    
    API_HASH = os.environ.get("API_HASH", "")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Default value for chunk size
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", "128"))
    
    # Ensure CHUNK_SIZE is positive
    if CHUNK_SIZE <= 0:
        raise ValueError("CHUNK_SIZE must be a positive integer.")
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 0
    DEF_WATER_MARK_FILE = "LegendSources"
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "LegendSources")
    
    # Default to 0 if environment variable is missing or invalid
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))
    if LOG_CHANNEL == 0:
        raise ValueError("LOG_CHANNEL must be set and be a valid integer.")
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    
    # Default to 0 if environment variable is missing or invalid
    OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
    if OWNER_ID == 0:
        raise ValueError("OWNER_ID must be set and be a valid integer.")
    
    TG_MIN_FILE_SIZE = 2097152000
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
