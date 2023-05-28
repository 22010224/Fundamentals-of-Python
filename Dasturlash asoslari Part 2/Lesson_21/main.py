import requests

from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlip.pyplot as plt

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title")
matn = ""
for n in news:
    matn += n.text

    #important words
    stopwords = ["Salom!","Qalesan",'Samandar',"Fayzulloh","Muqumjon","Sobir"]
    #creating a cloud
    wordcloud = WordCloud(width = 1000, height = 1000,
                          background_color = 'green',
                          stopwords = stopwords,
                          min_font_size = 20).generate(matn)
    plt.figure(figsize = (8,8), facecolor = 'black')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()