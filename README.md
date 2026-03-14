# RemixFBQuotes

A Python web scraper that fetches random inspirational quotes and automatically posts them to Facebook.

## What it does

This tool scrapes random quotes from quotationspage.com and posts them to your Facebook timeline using the Facebook Graph API. Perfect for sharing daily inspiration with your friends and followers.

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python 3 | Core language |
| 🌐 requests | HTTP requests |
| 🍲 BeautifulSoup4 | HTML parsing |
| 📘 facepy | Facebook Graph API |

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/stabgan/RemixFBQuotes.git
   cd RemixFBQuotes
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get Facebook Access Token:**
   - Visit [Facebook Graph API Explorer](https://developers.facebook.com/tools/explorer)
   - Generate an access token with `publish_to_groups` permission
   - Set it as environment variable:
     ```bash
     export FB_ACCESS_TOKEN="your_token_here"
     ```

4. **Run the script:**
   ```bash
   cd RemixQuotes
   python FacebookPost.py
   ```

## Features

- ✅ Secure HTTPS connections
- ✅ Error handling and fallback quotes
- ✅ Environment variable support for tokens
- ✅ Robust quote parsing with multiple fallbacks
- ✅ Clean, readable output formatting

## ⚠️ Known Issues

- The quotationspage.com website structure may change, affecting quote extraction
- Facebook API tokens expire and need periodic renewal
- Rate limiting may apply for frequent posts

## License

Check the [LICENSE](LICENSE) file for details.

---

*Last updated: 2024 - Modernized with security improvements and error handling*
