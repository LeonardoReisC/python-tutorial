import os
from dotenv import load_dotenv

print(os.environ)  # return all loaded env variables

load_dotenv()  # load all declared env variables from .env

print(os.getenv("BD_USER"))

# GOOD PRACTICE: create a .env-example file to show developers to change .env
# env variables values