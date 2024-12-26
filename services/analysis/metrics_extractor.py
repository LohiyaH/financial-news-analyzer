"""Financial metrics extraction service"""
import re
from typing import List, Tuple
from models.article import FinancialMetric

class MetricsExtractor:
    def extract_metrics(self, text: str) -> List[FinancialMetric]:
        """Extract financial metrics from text"""
        metrics = []
        
        # Currency amounts
        currency_pattern = r'(?:Rs\.|USD|€|£|\$)\s*[\d,.]+(?:\s*(?:billion|million|trillion|B|M|T))?'
        matches = re.finditer(currency_pattern, text)
        for match in matches:
            context = self._get_context(text, match.start(), match.end())
            metrics.append(FinancialMetric(
                name='amount',
                value=match.group(),
                context=context
            ))
        
        # Percentages
        percentage_pattern = r'\d+(?:\.\d+)?%'
        matches = re.finditer(percentage_pattern, text)
        for match in matches:
            context = self._get_context(text, match.start(), match.end())
            metrics.append(FinancialMetric(
                name='percentage',
                value=match.group(),
                context=context
            ))
        
        return metrics
    
    def _get_context(self, text: str, start: int, end: int, context_window: int = 50) -> str:
        """Get surrounding context for a metric"""
        context_start = max(0, start - context_window)
        context_end = min(len(text), end + context_window)
        return text[context_start:context_end].strip()