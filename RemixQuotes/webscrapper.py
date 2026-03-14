import requests
from bs4 import BeautifulSoup



class Quotes():
    
    def __init__(self):
        page = requests.get('http://www.quotationspage.com/random.php3')
        
        soup = BeautifulSoup(page.content, 'html.parser')
        soup.find_all('dt')
        soup.select("dd b a")
        
        self.quote = soup.find_all('dt')[3].get_text()
        self.author = soup.select("dd b a")[3].get_text()
    
    
    def randomquote(self):
        
        return self.quote
      
    def author(self):
        
        s = self.author
        
        return s

        

