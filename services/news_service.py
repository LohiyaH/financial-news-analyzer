import requests
import json
import logging
from datetime import datetime
from typing import List
from models.article import NewsArticle
from config import NEWS_API_KEY, NEWS_API_BASE_URL
from utils.date_utils import parse_api_date

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class NewsService:
    def __init__(self):
        self.api_key = NEWS_API_KEY
        self.base_url = NEWS_API_BASE_URL
        self.finance_keywords = {
            'market', 'stock', 'shares', 'trading', 'investor', 'investment',
            'financial', 'economy', 'economic', 'bank', 'finance', 'profit',
            'revenue', 'earnings', 'IPO', 'merger', 'acquisition', 'dividend',
            'nasdaq', 'dow', 'nifty', 'sensex', 'treasury', 'forex', 'bond'
        }
        
        if not self.api_key:
            logger.error("Currents API key is not configured")
            raise ValueError("Currents API key is required")

    def is_finance_related(self, article: dict) -> bool:
        """Check if the article is finance-related based on content and keywords"""
        text = f"{article.get('title', '')} {article.get('description', '')}".lower()
        return any(keyword in text for keyword in self.finance_keywords)

    def get_financial_news(self, query: str = None) -> List[NewsArticle]:
        """Fetch financial news articles from Currents API"""
        params = {
            'apiKey': self.api_key,
            'category': 'business',
            'language': 'en',
            'page_size': 20  # Increased to ensure we get enough finance-related articles
        }
        if query:
            params['keywords'] = query

        url = f"{self.base_url}/latest-news"
        
        safe_params = params.copy()
        safe_params['apiKey'] = '***'
        logger.debug(f"Making request to: {url}")
        logger.debug(f"With parameters: {safe_params}")

        try:
            response = requests.get(url, params=params)
            logger.debug(f"Response status code: {response.status_code}")
            response.raise_for_status()
            
            data = response.json()
            articles = data.get('news', [])
            
            # Filter for finance-related articles
            finance_articles = [
                self._create_article(article)
                for article in articles 
                if article.get('description') and self.is_finance_related(article)
            ][:5]  # Limit to 5 articles
            
            logger.info(f"Successfully fetched {len(finance_articles)} finance-related articles")
            return finance_articles
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            if hasattr(e, 'response'):
                logger.error(f"Error response: {e.response.text}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise

    def _create_article(self, article_data: dict) -> NewsArticle:
        """Create NewsArticle object from API response data"""
        try:
            return NewsArticle(
                title=article_data['title'],
                content=article_data.get('description', ''),
                source=article_data.get('author', 'Unknown'),
                url=article_data['url'],
                published_at=parse_api_date(article_data['published'])
            )
        except KeyError as e:
            logger.error(f"Missing required field in article: {e}")
            logger.error(f"Article data: {json.dumps(article_data, indent=2)}")
            raise
        except ValueError as e:
            logger.error(f"Invalid date format in article: {e}")
            raise