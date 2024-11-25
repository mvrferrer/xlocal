import feedparser
from transformers import pipeline
from jinja2 import Environment, FileSystemLoader
import os

# Configure RSS Feed URLs
RSS_FEED_URLS = ["https://brutalist.report/"]

# Initialize Hugging Face Summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Summarize content using Hugging Face
def summarize_content(content):
    try:
        summary = summarizer(content, max_length=50, min_length=10, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error generating summary: {e}")
        return "Summary unavailable."

# Parse RSS Feeds and Generate Summaries
def fetch_and_summarize_feeds():
    articles = []
    for url in RSS_FEED_URLS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            description = entry.description if "description" in entry else "No description available."
            summary = summarize_content(description)
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": summary,
                "date": entry.published if "published" in entry else "No date available."
            })
    return articles

# Generate Static HTML
def generate_static_site(articles):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html")
    output_from_parsed_template = template.render(articles=articles)

    # Save the rendered HTML to a static file
    with open("output/index.html", "w", encoding="utf-8") as f:
        f.write(output_from_parsed_template)

if __name__ == "__main__":
    print("Fetching and summarizing RSS feeds...")
    articles = fetch_and_summarize_feeds()

    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    print("Generating static site...")
    generate_static_site(articles)

    print("Website generated in 'output/index.html'")
