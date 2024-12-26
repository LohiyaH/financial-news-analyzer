from services.news_service import NewsService
from services.analysis_service import AnalysisService
from config import MAX_ARTICLES
from datetime import datetime

def format_analysis_report(article, analysis):
    """Format analysis results into a structured report"""
    report = [
        f"\n{'='*80}",
        f"FINANCIAL NEWS ANALYSIS REPORT",
        f"{'='*80}",
        f"\nArticle: {article.title}",
        f"Source: {article.source}",
        f"Published: {article.published_at.strftime('%Y-%m-%d %H:%M:%S')}",
        f"URL: {article.url}\n",
        
        f"\nSENTIMENT ANALYSIS",
        f"{'='*20}",
        f"Overall Sentiment: {analysis.sentiment_score:+.2f}",
        f"Confidence Level: {analysis.confidence:.1f}%",
        f"Market Impact: {analysis.market_impact.upper()}",
        
        f"\nKEY ENTITIES",
        f"{'='*20}",
        "Companies: " + (", ".join(analysis.key_companies) or "None detected"),
        "Sectors: " + (", ".join(analysis.key_sectors) or "None detected"),
        "Financial Instruments: " + (", ".join(analysis.financial_instruments) or "None detected"),
        
        f"\nFINANCIAL METRICS",
        f"{'='*20}"
    ]
    
    for metric in analysis.financial_metrics:
        report.append(f"• {metric.name.title()}: {metric.value}")
        report.append(f"  Context: \"{metric.context.strip()}\"")
    
    report.extend([
        f"\nCRITICAL QUOTES",
        f"{'='*20}"
    ])
    
    for quote in analysis.critical_quotes:
        report.append(f"• \"{quote}\"")
    
    report.extend([
        f"\nMARKET IMPLICATIONS",
        f"{'='*20}"
    ])
    
    for implication in analysis.market_implications:
        report.append(f"• {implication}")
    
    return "\n".join(report)

def main():
    news_service = NewsService()
    analysis_service = AnalysisService()
    
    print("Fetching latest financial news...")
    articles = news_service.get_financial_news()
    
    for article in articles[:MAX_ARTICLES]:
        try:
            analysis = analysis_service.analyze_article(
                article.title,
                article.content
            )
            report = format_analysis_report(article, analysis)
            print(report)
        except Exception as e:
            print(f"Error analyzing article: {article.title}")
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()