"""Web scraper for random quotes from quotationspage.com."""

import requests
from bs4 import BeautifulSoup


class Quotes:
    """Fetches a random quote and its author from quotationspage.com."""

    def __init__(self):
        self._quote = ""
        self._author = ""
        self._fetch_quote()

    def _fetch_quote(self):
        """Fetch a random quote from the web."""
        try:
            page = requests.get(
                "https://www.quotationspage.com/random.php3", timeout=10
            )
            page.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching quote: {e}")
            self._quote = "Could not fetch a quote at this time."
            self._author = "Unknown"
            return

        soup = BeautifulSoup(page.content, "html.parser")

        quotes = soup.find_all("dt")
        authors = soup.select("dd b a")

        if len(quotes) > 3 and len(authors) > 3:
            self._quote = quotes[3].get_text()
            self._author = authors[3].get_text()
        elif quotes and authors:
            self._quote = quotes[0].get_text()
            self._author = authors[0].get_text()
        else:
            self._quote = "No quote found."
            self._author = "Unknown"

    def randomquote(self):
        """Return the fetched random quote."""
        return self._quote

    def get_author(self):
        """Return the author of the fetched quote."""
        return self._author


if __name__ == "__main__":
    q = Quotes()
    print(f'"{q.randomquote()}"')
    print(f" — {q.get_author()}")
