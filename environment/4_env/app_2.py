import os 
from dotenv import load_dotenv 
env = os.getenv('ENVIRONMENT','development') 
load_dotenv(f'.env.{env}') 
print(f"Ambiente: {env}")
print(f"URL: {os.getenv('URL')}")