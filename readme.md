# Financial News Analyzer

A Python-based financial news analysis tool that fetches real-time financial news and provides sentiment analysis, market impact assessment, and key insights extraction.

## Features

- **Real-time Financial News**: Fetches latest financial news using the Currents API
- **Smart Filtering**: Automatically identifies and filters finance-related news
- **Sentiment Analysis**: Dual-mode sentiment analysis using:
  - OpenAI GPT-3.5 for advanced analysis
  - Rule-based fallback system for reliability
- **Entity Extraction**: Identifies key financial entities including:
  - Companies
  - Sectors
  - Financial instruments
- **Metrics Analysis**: Extracts and analyzes financial metrics from news content
- **Comprehensive Reporting**: Generates detailed analysis reports including:
  - Overall sentiment score
  - Market impact assessment
  - Confidence levels
  - Critical quotes
  - Market implications

## Prerequisites

- Python 3.8+
- Currents API key
- OpenAI API key (optional, falls back to rule-based analysis if not provided)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/financial-news-analyzer.git
cd financial-news-analyzer
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```env
NEWS_API_KEY=your_currents_api_key
OPENAI_API_KEY=your_openai_api_key  # Optional
```

## Usage

Run the analyzer:
```bash
python main.py
```

The program will:
1. Fetch the latest financial news
2. Filter for finance-related articles
3. Perform sentiment analysis
4. Generate detailed reports for each article

## Project Structure

```
financial-news-analyzer/
├── config.py                 # Configuration settings
├── main.py                  # Main application entry point
├── models/
│   └── article.py          # Data models
├── services/
│   ├── news_service.py     # News fetching service
│   └── analysis/
│       ├── entity_extractor.py    # Entity extraction
│       ├── metrics_extractor.py   # Financial metrics extraction
│       └── sentiment_analyzer.py  # Sentiment analysis
└── utils/
    ├── date_utils.py       # Date handling utilities
    └── text_processor.py   # Text processing utilities
```

## Configuration

Key configuration options in `config.py`:
- `MAX_ARTICLES`: Maximum number of articles to analyze
- `SENTIMENT_THRESHOLD`: Threshold values for sentiment classification
- `OPENAI_MODEL`: OpenAI model selection
- API configuration settings

## Error Handling

The system includes robust error handling:
- Graceful fallback to rule-based analysis if OpenAI is unavailable
- Comprehensive logging for debugging
- Input validation and error reporting

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Currents API](https://currentsapi.services/en) for financial news data
- [OpenAI](https://openai.com/) for advanced text analysis capabilities