from bs4 import BeautifulSoup
import requests

url = "https://www.baidu.com/"
r = requests.get(url)
r.raise_for_status()
print(r.text)

bs = BeautifulSoup(r.text,"html.parser")
print(bs.title)