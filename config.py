from tortoise.backends.base.config_generator import expand_db_url
from os import environ as env
import logging

# Get DATABASE_URL from environment
database_url = env.get("DATABASE_URL")

if not database_url:
    # Railway should provide this automatically if you add a PostgreSQL service
    logging.error("DATABASE_URL environment variable is not set!")
    logging.error("Make sure you've added a PostgreSQL database service in Railway")
    raise ValueError("DATABASE_URL environment variable is not set!")

# Railway PostgreSQL URLs sometimes need SSL mode adjustment
if database_url.startswith("postgresql://") and "sslmode" not in database_url:
    # Add SSL mode for Railway PostgreSQL
    database_url += "?sslmode=require"

logging.info(f"Connecting to database: {database_url.split('@')[0]}@[HIDDEN]")

tortoise = {
    "connections": {
        "default": expand_db_url(database_url)
    },
    "apps": {
        "default": {
            "models": [
                "models"
            ]
        }
    }
}

del expand_db_url

# Jishaku Flags
flags = [
    "no underscore",
    "hide", 
    "retain",
    "force paginator",
    "no dm_traceback",
]

for flag in flags: 
    env[("jishaku_"+flag).upper().replace(" ","_")] = "t"
del flags