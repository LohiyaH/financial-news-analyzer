"""Main analysis service orchestrator"""
import logging
from typing import Dict, Any
from models.article import SentimentAnalysis
from services.analysis.sentiment_analyzer import SentimentAnalyzer
from services.analysis.entity_extractor import EntityExtractor
from services.analysis.metrics_extractor import MetricsExtractor

logger = logging.getLogger(__name__)

class AnalysisService:
    def __init__(self):
        self.sentiment_analyzer = SentimentAnalyzer()
        self.entity_extractor = EntityExtractor()
        self.metrics_extractor = MetricsExtractor()
    
    def analyze_article(self, title: str, content: str) -> SentimentAnalysis:
        """Analyze article content"""
        try:
            full_text = f"{title}. {content}"
            
            # Get sentiment analysis
            sentiment_data = self.sentiment_analyzer.analyze(full_text)
            
            # Extract entities and metrics
            entities = self.entity_extractor.extract_entities(full_text)
            metrics = self.metrics_extractor.extract_metrics(full_text)
            
            return SentimentAnalysis(
                sentiment_score=sentiment_data['sentiment_score'],
                confidence=sentiment_data['confidence'],
                market_impact=sentiment_data['market_impact'],
                key_companies=entities['companies'],
                key_sectors=entities['sectors'],
                financial_instruments=entities['instruments'],
                financial_metrics=metrics,
                critical_quotes=sentiment_data.get('critical_quotes', []),
                market_implications=sentiment_data.get('market_implications', [])
            )
        except Exception as e:
            logger.error(f"Analysis failed: {str(e)}")
            raise