# Falcon 9 Web Scraper Project

This project extracts, analyzes, and compares launch data for Falcon 9 rockets from Wikipedia.

We implemented two pipelines:
- Traditional scraping with BeautifulSoup
- AI-powered scraping using ScrapeGraphAI + Ollama

## Folder Structure

```
falcon9-scraper-project/
├── ai/
│   ├── ai_b1only.py
│   ├── ai_b4only.py
│   ├── ai_b5only.py
│   ├── ai_f9only.py
│   ├── ai_fhonly.py
│   ├── ai_fhpairs.py
│   ├── ai_fastestTurnaround.py
│   ├── ai_longestTurnaround.py
│   └── ai_mostLaunches.py
├── beautifulsoup/
│   ├── b1only.py
│   ├── b4only.py
│   ├── b5only.py
│   ├── f9only.py
│   ├── fhonly.py
│   ├── fhpairs.py
│   ├── fastestTurnaround.py
│   ├── longestTurnaround.py
│   └── mostLaunches.py
├── README.md
```

## BeautifulSoup Scripts

Located in the 'beautifulsoup/' folder.

Each script uses `requests` and `BeautifulSoup` to parse the Falcon 9 booster table and extract key information.

Examples:
- b1only.py — Filter Block 1 boosters
- fhpairs.py — Retrieve Falcon Heavy core pairings
- fastestTurnaround.py — Compute fastest turnaround
- mostLaunches.py — Find most reused booster

Setup:
```bash
pip install requests beautifulsoup4
```

## AI-Powered Scripts

Located in the 'ai/' folder.

These scripts use ScrapeGraphAI with the Ollama Mistral model to scrape the same data using natural language prompts.

Sample prompt:
Extract all Falcon 9 booster launches that are NOT Block 1, 1.1, 4, or 5. For each, include: booster ID, launch date, flight number.

Setup:
1. Install Ollama and run the model:
```bash
brew install ollama
ollama run mistral
```

2. Install Python dependencies:
```bash
pip install scrapegraphai playwright
playwright install
```

## Comparison

| Feature                   | BeautifulSoup | ScrapeGraphAI |
|--------------------------|----------------|----------------|
| HTML parsing             | Yes            | No             |
| Natural language prompts | No             | Yes            |
| Setup complexity         | Low            | Moderate       |
| Extensibility            | Yes            | Yes            |

## Author

- Jasmine Czemerinski  
- CIS 4340A – Homework 3  
- Spring 2025

## License

MIT License
