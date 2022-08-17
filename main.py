import config
import json
import webbrowser

from newsapi import NewsApiClient

newsapi = NewsApiClient(config.API_KEY)

def get_news():
  q = input('What do you want to get news about?\n')

  response = newsapi.get_everything(q, from_param='2022-08-17', to='2022-08-17', page=1, page_size=10, language='en',sort_by='relevancy')
  with open('api.json', 'w') as json_file:
    json.dump(response, json_file)
  
  select_article()

def select_article():
  with open('api.json', 'r') as json_file:
    data = json.load(json_file)
    for count, item in enumerate(data['articles']):
      print(count, item['title'], item['url'])
    choice = int(input("Which article you want to read? Enter a number from 0 to 9\n"))
    open_url(choice)

def open_url(num):
  urls = []
  with open('api.json', 'r') as json_file:
    data = json.load(json_file)
    for count, item in enumerate(data['articles']):
      urls.append(item['url'])
    webbrowser.open(urls[num])
      
get_news()