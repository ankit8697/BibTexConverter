import pandas as pd
import re
import requests
import os

FILE_NAME = ''

contents = ''
with open(f'{FILE_NAME}.txt', 'r') as f:
    contents = f.read()

articles = contents.split('Please Note: This link will expire in 7 days.')

rows = []
download_links = []
print('Creating spreadsheet...')
for article in articles[:-1]:
    lines = [string for string in article.split('\n') if string]
    title = lines[0]
    title = title[:title.rfind('[')]
    citation = article.split('Bluebook 21st ed.')[1].split('\n')[1]
    link = article.split('Permalink')[1].split('\n')[0][2:]
    download_link = article.split('Permalink')[1].split('\n')[2][15:]
    download_links.append({"title": title, "download_link": download_link})
    row = {"Title": title, "Link": link, "Citation": citation}
    rows.append(row)

df = pd.DataFrame(rows)
df.to_excel(f'{FILE_NAME}.xlsx',
            index=False, encoding='utf-8')

print('Spreadsheet complete!')

print('Downloading files...')

os.mkdir(f'{FILE_NAME}')

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "document",
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}

for download_link in download_links:
    response = requests.get(download_link['download_link'], stream=True, headers=headers)
    title = download_link['title']
    if response.status_code == 200:
        with open(f'{FILE_NAME}/{title}.pdf', 'wb') as f:
            f.write(response.content)
        print(f'Downloaded {title}')
    else:
        print(f'Error downloading file: {title}')

print('Finished downloading all files!')
