from dotenv import load_dotenv
import os

load_dotenv()

if __name__=="__main__":
    # Print the value of API_DYNAMIC_KEY from .env file
    print(os.getenv("API_DYNAMIC_KEY"))