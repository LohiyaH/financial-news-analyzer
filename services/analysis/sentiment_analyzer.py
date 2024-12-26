"""Sentiment analysis service with fallback mechanisms"""
import logging
from typing import Dict, Any
import openai
from config import OPENAI_API_KEY, OPENAI_MODEL

logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    def __init__(self):
        self.openai_api_key = OPENAI_API_KEY
        if self.openai_api_key:
            openai.api_key = self.openai_api_key

    def analyze(self, text: str) -> Dict[str, Any]:
        """Analyze text sentiment using available methods"""
        try:
            if self.openai_api_key:
                return self._analyze_with_openai(text)
            else:
                logger.warning("OpenAI API key not configured, using fallback analysis")
                return self._analyze_with_fallback(text)
        except Exception as e:
            logger.warning(f"OpenAI analysis failed: {str(e)}")
            return self._analyze_with_fallback(text)
    
    def _analyze_with_openai(self, text: str) -> Dict[str, Any]:
        """Analyze sentiment using OpenAI"""
        try:
            prompt = f"""Analyze the following financial news text and provide:
            1. Sentiment score (-1 to +1)
            2. Confidence (0-100)
            3. Market impact (bullish/bearish/neutral)
            4. Key quotes
            5. Market implications

            Text: {text}"""

            response = openai.ChatCompletion.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "You are a financial analyst expert."},
                    {"role": "user", "content": prompt}
                ]
            )

            analysis = response.choices[0].message.content
            
            # Extract sentiment score from analysis (basic implementation)
            sentiment_score = 0.0
            if "bearish" in analysis.lower():
                sentiment_score = -0.5
            elif "bullish" in analysis.lower():
                sentiment_score = 0.5
            
            return {
                'sentiment_score': sentiment_score,
                'confidence': 80.0,
                'market_impact': 'bullish' if sentiment_score > 0 else 'bearish' if sentiment_score < 0 else 'neutral',
                'critical_quotes': [],
                'market_implications': [analysis]
            }
        except Exception as e:
            logger.error(f"OpenAI analysis error: {str(e)}")
            raise

    def _analyze_with_fallback(self, text: str) -> Dict[str, Any]:
        """Simple rule-based sentiment analysis fallback"""
        positive_words = {
            'growth', 'profit', 'surge', 'rise', 'gain', 'positive', 'up', 'higher',
            'increase', 'improved', 'growing', 'strong', 'bullish', 'outperform'
        }
        negative_words = {
            'loss', 'decline', 'fall', 'negative', 'down', 'lower', 'decrease',
            'bearish', 'weak', 'poor', 'underperform', 'risk', 'volatile'
        }
        
        words = set(text.lower().split())
        pos_count = len(words.intersection(positive_words))
        neg_count = len(words.intersection(negative_words))
        
        total = pos_count + neg_count
        if total == 0:
            sentiment_score = 0
        else:
            sentiment_score = (pos_count - neg_count) / (pos_count + neg_count)
        
        return {
            'sentiment_score': sentiment_score,
            'confidence': 50.0,
            'market_impact': 'neutral' if abs(sentiment_score) < 0.2 else 'bullish' if sentiment_score > 0 else 'bearish',
            'critical_quotes': [],
            'market_implications': ['Market impact cannot be determined with high confidence']
        }