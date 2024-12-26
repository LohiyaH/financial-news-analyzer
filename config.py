from dotenv import load_dotenv
import os

load_dotenv('D:\python projects\Financial_news_analyzer\project-bolt-secret-python-gpwmrzxw\project\.env')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# API Configuration
NEWS_API_BASE_URL = "https://api.currentsapi.services/v1"  # Updated to Currents API endpoint
OPENAI_MODEL = "gpt-3.5-turbo"

# Analysis Configuration
MAX_ARTICLES = 5
SENTIMENT_THRESHOLD = {
    'VERY_POSITIVE': 0.6,
    'POSITIVE': 0.2,
    'NEUTRAL': -0.2,
    'NEGATIVE': -0.6,
    'VERY_NEGATIVE': -1.0
}