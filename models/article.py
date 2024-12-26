from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class FinancialMetric:
    name: str
    value: str
    context: str

@dataclass
class NewsArticle:
    title: str
    content: str
    source: str
    url: str
    published_at: datetime
    
@dataclass
class SentimentAnalysis:
    sentiment_score: float  # -1 to +1
    confidence: float  # 0 to 100
    market_impact: str  # bullish/bearish/neutral
    key_companies: List[str]
    key_sectors: List[str]
    financial_instruments: List[str]
    financial_metrics: List[FinancialMetric]
    critical_quotes: List[str]
    market_implications: List[str]
    analyzed_at: datetime = datetime.now()