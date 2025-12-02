import requests
from bs4 import BeautifulSoup
from typing import List

class WikipediaPage:
    # Class attribute for the target word
    target_word = "effervescence"
    
    def __init__(self, keyword: str):
        """
        Initialize a WikipediaPage object.
        
        Args:
            keyword: The title of the Wikipedia page to fetch
            
        Raises:
            ValueError: If the Wikipedia page doesn't exist
            requests.RequestException: If there's an error fetching the page
        """
        self.keyword = keyword
        
        # Construct the URL (Wikipedia handles case insensitivity)
        url = f"https://en.wikipedia.org/wiki/{keyword}"
        
        # Set up headers with User-Agent as per Wikimedia policy
        headers = {
            'User-Agent': 'Educational Project CS2100 (your.email@northeastern.edu)'  # UPDATE THIS
        }
        
        # Request the page
        response = requests.get(url, headers=headers)
        
        # Check if the page exists
        if response.status_code == 404:
            raise ValueError(f"Wikipedia page for '{keyword}' does not exist")
        response.raise_for_status()  # Raise error for other bad status codes
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Store the text of the webpage
        # Get all text from the main content div
        content_div = soup.find('div', {'id': 'mw-content-text'})
        if content_div:
            # Remove unwanted elements (references, navigation boxes, etc.)
            for unwanted in content_div.find_all(['sup', 'div'], class_=['reference', 'navbox', 'reflist', 'infobox']):
                unwanted.decompose()
            self.text = content_div.get_text()
        else:
            self.text = soup.get_text()
        
        # Extract all Wikipedia links
        wiki_links = set()
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Check if it's a Wikipedia article link
            # Exclude special pages, files, categories, etc.
            if (href.startswith('/wiki/') and 
                ':' not in href and 
                not href.startswith('/wiki/Main_Page')):
                # Extract the article title (remove '/wiki/' prefix)
                article_title = href[6:]  # Remove '/wiki/'
                wiki_links.add(article_title)
        
        # Store as sorted list
        self.links = sorted(wiki_links)
        
        # Initialize children as empty list
        self.children: List['WikipediaPage'] = []
        
        # Calculate and cache the count of target_word
        self._target_word_count = self._count_target_word()
    
    def _count_target_word(self) -> int:
        """Count occurrences of target_word in the text (case-insensitive)."""
        return self.text.lower().count(self.target_word.lower())
    
    def __eq__(self, other) -> bool:
        """Two WikipediaPages are equal if they have the same keyword."""
        if not isinstance(other, WikipediaPage):
            return False
        return self.keyword == other.keyword
    
    def __hash__(self) -> int:
        """Hash based on the keyword."""
        return hash(self.keyword)
    
    def __repr__(self) -> str:
        """Return the keyword as the representation."""
        return self.keyword
    
    def __str__(self) -> str:
        """Return a message with keyword and target word count."""
        return f"WikipediaPage('{self.keyword}') contains '{self.target_word}' {self._target_word_count} times"
    
    # Comparison methods based on target_word count
    def __lt__(self, other) -> bool:
        """Less than: has fewer occurrences of target_word."""
        if not isinstance(other, WikipediaPage):
            return NotImplemented
        return self._target_word_count < other._target_word_count
    
    def __le__(self, other) -> bool:
        """Less than or equal to."""
        if not isinstance(other, WikipediaPage):
            return NotImplemented
        return self._target_word_count <= other._target_word_count
    
    def __gt__(self, other) -> bool:
        """Greater than: has more occurrences of target_word."""
        if not isinstance(other, WikipediaPage):
            return NotImplemented
        return self._target_word_count > other._target_word_count
    
    def __ge__(self, other) -> bool:
        """Greater than or equal to."""
        if not isinstance(other, WikipediaPage):
            return NotImplemented
        return self._target_word_count >= other._target_word_count