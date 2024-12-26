"""Entity extraction service"""
import logging
from typing import Dict, List, Any
import re

logger = logging.getLogger(__name__)

class EntityExtractor:
    def __init__(self):
        self.company_indicators = {'Ltd', 'Limited', 'Corp', 'Inc', 'AG', 'NV', 'SA'}
        self.sector_keywords = {
            'technology': {'tech', 'software', 'digital', 'IT'},
            'finance': {'bank', 'insurance', 'financial', 'investment'},
            'healthcare': {'pharma', 'health', 'medical', 'biotech'},
            'energy': {'oil', 'gas', 'renewable', 'power'}
        }
        self.financial_instruments = {
            'stocks', 'shares', 'bonds', 'futures', 'options', 
            'etf', 'mutual fund', 'derivatives', 'forex'
        }
    
    def extract_entities(self, text: str) -> Dict[str, Any]:
        """Extract relevant entities from text"""
        return {
            'companies': self._extract_companies(text),
            'sectors': self._extract_sectors(text),
            'instruments': self._extract_instruments(text),
            'metrics': self._extract_metrics(text)
        }
    
    def _extract_companies(self, text: str) -> List[str]:
        """Extract company names using indicators and patterns"""
        companies = []
        words = text.split()
        for i, word in enumerate(words):
            if word in self.company_indicators and i > 0:
                companies.append(words[i-1] + ' ' + word)
        return companies
    
    def _extract_sectors(self, text: str) -> List[str]:
        """Extract sector mentions"""
        text_lower = text.lower()
        sectors = []
        for sector, keywords in self.sector_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                sectors.append(sector)
        return sectors

    def _extract_instruments(self, text: str) -> List[str]:
        """Extract financial instruments mentions"""
        text_lower = text.lower()
        instruments = []
        for instrument in self.financial_instruments:
            if instrument in text_lower:
                instruments.append(instrument)
        return instruments

    def _extract_metrics(self, text: str) -> List[str]:
        """Extract financial metrics"""
        metrics = []
        # Add metric extraction logic here if needed
        return metrics