import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

paragraphs = soup.find_all('p')

with open("corpus.txt", "w", encoding="utf-8") as f:
    for p in paragraphs:
        text = p.get_text()
        if len(text) > 50:
            f.write(text + "\n")

print("Done! corpus.txt ban gaya")