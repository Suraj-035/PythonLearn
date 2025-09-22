'''
Real-World Example : Multithreading for I/O bounds tasks
scenario: Web scrapping
Web scrapping often involves making numerous network requests to fetch webpages. These tasks are I/O bound
becoz they spend a lot of time waiting for responses from servers. Multithreading can significantly improve the perfomance by allowing
multiple webpages to be fetched concurrently
'''

import threading
import requests #This module helps you download web pages using HTTP.
from bs4 import BeautifulSoup ##for parsing HTML (turning that messy webpage into readable text) -->It’s like having a cleaner that says: “Ye sab <div> <span> chhod, mujhe sirf asli text chahiye.”

urls=['https://python.langchain.com/v0.2/docs/introduction/',
      'https://python.langchain.com/v0.2/docs/concepts/',
      'https://python.langchain.com/v0.2/docs/tutorials/']

def fetch_content(url):
    response=requests.get(url) ##This sends an HTTP GET request to the URL.
    soup=BeautifulSoup(response.content,'html.parser') #This line takes the HTML from the webpage and cleans it. soup now contains the whole page — but in a nicely searchable format
    print(f'Fetch {len(soup.text)} characters from{url}') #soup.text extracts just the visible text (not HTML tags).

threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,)) #threading.Thread(..)-->Makes a worker
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    
print("All webpages fetched")
