import requests
from bs4 import BeautifulSoup


class Quotes:
    
    def __init__(self):
        try:
            # Use HTTPS for security
            page = requests.get('https://www.quotationspage.com/random.php3', timeout=10)
            page.raise_for_status()
            
            soup = BeautifulSoup(page.content, 'html.parser')
            
            # Find all quotes and authors
            quotes = soup.find_all('dt')
            authors = soup.select("dd b a")
            
            # Use safer indexing with fallback
            if len(quotes) > 3 and len(authors) > 3:
                self.quote_text = quotes[3].get_text().strip()
                self.author_name = authors[3].get_text().strip()
            else:
                # Fallback to first available quote/author
                self.quote_text = quotes[0].get_text().strip() if quotes else "No quote found"
                self.author_name = authors[0].get_text().strip() if authors else "Unknown"
                
        except requests.RequestException as e:
            print(f"Error fetching quote: {e}")
            self.quote_text = "The only impossible journey is the one you never begin."
            self.author_name = "Tony Robbins"
        except Exception as e:
            print(f"Error parsing quote: {e}")
            self.quote_text = "The only impossible journey is the one you never begin."
            self.author_name = "Tony Robbins"
    
    def randomquote(self):
        return self.quote_text
      
    def get_author(self):
        return self.author_name

        

