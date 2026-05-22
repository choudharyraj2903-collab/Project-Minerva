import requests
from bs4 import BeautifulSoup
import nltk
# nltk.download('punkt')
# nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer

url = "https://www.bbc.com/future/article/20260515-the-1950s-blunder-which-causes-mass-hay-fever-in-japan"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify()) 

title = soup.find("h1").text

paragraphs = soup.find_all("p")

article_text = ""

for p in paragraphs:
    article_text += p.text + "\n"

title_tokens=word_tokenize(title)
article_tokens=word_tokenize(article_text)

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

title_embedding=model.encode(title_tokens)
article_embedding=model.encode(article_tokens)
print(title_embedding.shape)
print(article_embedding.shape)

print(title_tokens)
print(title_embedding)

print(article_tokens)
print(article_embedding)

# print(word_tokenize(title))

# print("TITLE: ")
# print(title)

# print("\nARTICLE: ")
# print(article_text)

# with open("article.txt", "w", encoding="utf-8") as f:
#     f.write(title + "\n\n")
#     f.write(article_text)
