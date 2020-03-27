import requests
from bs4 import BeautifulSoup
import pprint

response= requests.get("https://www.biospace.com/news/")
soup = BeautifulSoup(response.text, 'html.parser')

link= soup.select(".lister__header")
#print(link)

def list_articles(link):
	articles=[]
	for index, item in enumerate(link):
		title= link[index].getText()
		atab= link[index].a
		href= atab.get('href') 
		url= 'https://www.biospace.com'+href
		articles.append({'title':title, 'link':url})
	return articles

pprint.pprint(list_articles(link))

with open('Current_BioSpace_Articles.txt', mode='w') as file:
	text_file=(list_articles(link)) 
	for element in text_file:
		file.write(f"{element}\n")
		




