# wordcloud_generator.py

from wordcloud import WordCloud, STOPWORDS
import requests
import matplotlib.pyplot as plt

# URL zum Text von Alice im Wunderland
url = "https://www.gutenberg.org/files/11/11-0.txt"
response = requests.get(url)
text = response.text

# Stopwords zur Bereinigung des Texts
stopwords = set(STOPWORDS)
stopwords.update(["said", "Alice", "upon", "could", "would", "one", "know"])

# Wordcloud erstellen
wordcloud = WordCloud(width=800, height=400, 
                      background_color='white',
                      stopwords=stopwords, 
                      colormap='viridis', 
                      max_words=200).generate(text)

# Wordcloud anzeigen
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
