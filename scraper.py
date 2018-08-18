from bs4 import BeautifulSoup
from csv import writer
import requests

response = requests.get('https://android-developers.googleblog.com/')
soup = BeautifulSoup(response.text, features="html5lib")
posts = soup.find_all(class_='post')

with open('posts.csv', 'w', newline='') as csv_file:
    csv_writer = writer(csv_file)
    headers = ["Title", "Date", "Link"]
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find(class_='title').get_text().replace('\n', '')
        date = post.find(class_='published').get_text().replace('\n', '')
        link = post.find('a')['href'].replace('\n','')
        csv_writer.writerow([title, date, link])
