import re
import nltk
from typing import Dict, List, Tuple

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def clean_text(text: str) -> str:
    """Clean and normalize text for analysis"""
    # Remove special characters except quotes
    text = re.sub(r'[^\w\s"\'$%.-]', '', text)
    # Normalize whitespace
    text = ' '.join(text.split())
    return text

def extract_entities(text: str) -> Dict[str, List]:
    """Extract relevant entities from text"""
    # Tokenize and tag text
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    
    # Initialize results
    results = {
        'companies': [],
        'sectors': [],
        'instruments': [],
        'metrics': []
    }
    
    # Extract companies (Named Entities)
    for entity in entities:
        if hasattr(entity, 'label'):
            if entity.label() == 'ORGANIZATION':
                results['companies'].append(' '.join([e[0] for e in entity]))
    
    # Extract financial metrics
    metric_patterns = [
        (r'\$[\d,.]+[BMK]?', 'amount'),
        (r'\d+\.?\d*\s*%', 'percentage'),
        (r'(?i)(revenue|profit|loss|growth|decline)', 'metric')
    ]
    
    for pattern, metric_type in metric_patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            # Get context (20 chars before and after)
            start = max(0, match.start() - 20)
            end = min(len(text), match.end() + 20)
            context = text[start:end]
            results['metrics'].append((
                metric_type,
                match.group(),
                context
            ))
    
    # Extract sectors and instruments from predefined lists
    sectors = ['technology', 'healthcare', 'finance', 'energy']
    instruments = ['stocks', 'bonds', 'futures', 'options']
    
    text_lower = text.lower()
    results['sectors'] = [s for s in sectors if s in text_lower]
    results['instruments'] = [i for i in instruments if i in text_lower]
    
    return results