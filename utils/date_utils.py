"""Utility functions for date handling"""
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def parse_api_date(date_str: str) -> datetime:
    """Parse date string from API response into datetime object"""
    try:
        # Try common API date formats
        formats = [
            '%Y-%m-%d %H:%M:%S %z',  # Format: '2024-12-26 08:40:26 +0000'
            '%Y-%m-%dT%H:%M:%S%z',   # ISO format with timezone
            '%Y-%m-%dT%H:%M:%SZ'     # UTC format
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
                
        raise ValueError(f"Unsupported date format: {date_str}")
        
    except Exception as e:
        logger.error(f"Date parsing error: {e}")
        raise ValueError(f"Failed to parse date: {date_str}") from e