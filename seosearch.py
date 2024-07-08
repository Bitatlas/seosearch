import os
import random
from bs4 import BeautifulSoup

# Function to parse a single HTML file
def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'lxml')
        
        title = soup.title.text if soup.title else 'No Title'
        text = ' '.join([p.text for p in soup.find_all('p')])
        
        return title, text

# Function to parse all HTML files in a directory
def parse_directory(directory):
    articles = {}
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            title, text = parse_html(file_path)
            articles[title] = text
    return articles

# Function to search articles for a keyword
def search_articles(articles, keyword):
    results = {}
    for title, text in articles.items():
        if keyword.lower() in text.lower():
            results[title] = text
    return results

# Directory containing HTML files
directory_path = r'C:\Users\henri\Downloads\medium-export\posts'  # Update your path

# Expanded list of emojis (fun and money-related)
emojis = ['😊', '🌟', '📚', '💡', '🚀', '🌈', '🎉', '🌿', '🌞', '🌙',
          '🎊', '🎯', '💰', '💸', '💵', '💴', '💶', '💷', '🤑', '🍾',
          '🏆', '👑', '🏅', '🥇', '🎁', '🎈', '🎠', '🎡', '🎢', '🎏',
          '🌺', '🍿', '🍦', '🍬', '🍭', '🍮', '🍩', '🍪', '🍰', '🧁']

# Parse all HTML files in the directory
articles = parse_directory(directory_path)
print("Parsed", len(articles), "articles.")

# Perform a keyword search
keyword = 'Warren Buffett'  # Replace 'example' with the keyword you're interested in
found_articles = search_articles(articles, keyword)

# Print the search results with numbering and random emoji
print(f"Found {len(found_articles)} articles containing the keyword '{keyword}'.")
for index, (title, content) in enumerate(found_articles.items(), start=1):
    if len(content) > 5000:  # Check if the article content is larger than 5 kb (5000 bytes)
        emoji = random.choice(emojis)  # Choose a random emoji from the expanded list
        print(f"{index}. {emoji} {title}")