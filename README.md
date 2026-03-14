# RemixFBQuotes

A Python script that scrapes a random quote from the web and posts it as your Facebook status using the Graph API.

## How It Works

1. Scrapes a random quote and its author from [quotationspage.com](https://www.quotationspage.com/random.php3)
2. Formats the quote with attribution
3. Posts it to your Facebook timeline via the Graph API

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python 3 | Core language |
| 🍜 BeautifulSoup4 | HTML parsing and web scraping |
| 🌐 Requests | HTTP client |
| 📘 Facepy | Facebook Graph API wrapper |

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/stabgan/RemixFBQuotes.git
   cd RemixFBQuotes
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get a Facebook access token from [Facebook Graph API Explorer](https://developers.facebook.com/tools/explorer)

4. Paste your token into `RemixQuotes/FacebookPost.py`:
   ```python
   ACCESS_TOKEN = "your_token_here"
   ```

5. Run:
   ```bash
   cd RemixQuotes
   python FacebookPost.py
   ```

You can also test the scraper standalone:
```bash
python RemixQuotes/webscrapper.py
```

## ⚠️ Known Issues

- Facebook Graph API user tokens expire quickly; you need to regenerate them for each session
- The `facepy` library is no longer actively maintained — consider migrating to the official `facebook-sdk` or raw HTTP requests
- The quote scraper depends on the HTML structure of quotationspage.com, which may change without notice

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.
