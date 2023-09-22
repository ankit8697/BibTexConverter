import bibtexparser
import pandas as pd
import requests
import os

print('starting conversion...')

FILE_NAME = ''

library = bibtexparser.parse_file(f"{FILE_NAME}.txt")

rows = []
download_links = []

class Placeholder:
    def __init__(self):
        self.value = ''


for entry in library.entries:
    title = entry.fields_dict['title'].value
    link = entry.fields_dict['URL'].value
    tag = link[link.rfind("/")+1:]
    download_link = f'https://www-jstor-org.opj.remotlog.com/stable/pdf/{tag}.pdf?refreqid=excelsior%3Af86b57e2b4834918775055f30af6d440&ab_segments=0%2Fbasic_search_gsv2%2Fcontrol&origin=&initiator=&acceptTC=1'
    download_links.append({'title': title, 'download_link': download_link})

    citation_sections = []
    citation_sections.append(
        entry.fields_dict.get('author', Placeholder()).value)
    citation_sections.append(title)
    citation_sections.append(
        entry.fields_dict.get('year', Placeholder()).value)
    citation_sections.append(
        entry.fields_dict.get('volume', Placeholder()).value)
    citation_sections.append(
        entry.fields_dict.get('number', Placeholder()).value)
    citation_sections.append(
        entry.fields_dict.get('journal', Placeholder()).value)
    citation_sections.append(
        entry.fields_dict.get('pages', Placeholder()).value)
    citation_sections = filter(lambda s: s != '', citation_sections)

    citation = ''
    for section in citation_sections:
        citation = citation + section + ', '
    citation = citation.rstrip(', ')

    abstract = entry.fields_dict.get('abstract', Placeholder()).value

    row = {"Title": title, "Link": link, "Citation": citation, "Direct Quote": abstract}
    rows.append(row)

df = pd.DataFrame(rows)
df.to_excel(f'{FILE_NAME}.xlsx', index=False, encoding='utf-8')

print(f"Done! See {FILE_NAME}.xlsx for results")

print(f"Downloading files for {FILE_NAME}")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Cookie": "ADD AUTH COOKIES HERE"
}

os.mkdir(FILE_NAME)

for download_link in download_links:
    title = download_link['title']
    response = requests.get(
        download_link['download_link'], headers=headers)
    if response.status_code == 200:
        with open(f'{FILE_NAME}/{title}.pdf', 'wb') as f:
            f.write(response.content)
            print(f'Downloaded {title}')
    else:
        print(f'Error downloading file: {response.status_code}')
        print(f'Could not get {title}')

