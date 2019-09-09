from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target )
    req.encoding = "gbk"
    html = req.text

    bf = BeautifulSoup(html, "html5lib")
    texts = bf.find_all('div', class_='showtxt')
    print(texts[0].text)
