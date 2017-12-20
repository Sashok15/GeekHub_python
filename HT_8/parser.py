from bs4 import BeautifulSoup
from config import *
import requests
import os
import csv

if not os.path.exists(PATH_REPORTS):
    os.makedirs(PATH_REPORTS)


def get_info_site(my_url):
    r = requests.get(url=my_url)
    # print(r.text)
    return r.text


def parse(html):
    soup = BeautifulSoup(html, 'lxml')

    for item in soup.find_all('div', class_='quote'):
        tags_n = []
        tags_u = []
        # print(item)
        text_data.append(item.contents[1].contents[0])
        author_name.append(item.contents[3].contents[1].contents[0])
        author_url.append(item.contents[3].contents[3].get('href'))
        for i in item.contents[5].find_all('a'):
            tags_n.append(i.text)
            tags_u.append(i.get('href'))
        tags_name.append(tags_n)
        tags_url.append(tags_u)

    for i in author_url:
        soup_for_author = BeautifulSoup(get_info_site(URL+i), 'lxml')
        for ele in soup_for_author.find_all('div', class_='author-details'):
            author_born_date.append(ele.contents[2].contents[2].contents[0])
            author_born_place.append(ele.contents[2].contents[4].contents[0])
            author_about.append(ele.find('div', class_='author-description').contents[0][:100])

    for urls in tags_url:
        tags_text_temp, tags_author_temp, tags_author_url_temp = [], [], []
        for url_tag in urls:
            soup_for_tags = BeautifulSoup(get_info_site(URL+url_tag), 'lxml')
            for ele in soup_for_tags.find_all('div', class_='quote'):
                tags_text_temp.append(ele.contents[1].contents[0])
                tags_author_temp.append(ele.contents[3].contents[1].contents[0])
                tags_author_url_temp.append(ele.contents[3].contents[3].get('href'))
            tags_text.append(tags_text_temp)
            tags_author.append(tags_author_temp)
            tags_author_url.append(tags_author_url_temp)

    result['info'] = {'text': text_data,
                      'author': {'author_name': author_name,
                                 'author_url': author_url,
                                 'author_born_date': author_born_date,
                                 'author_born_place': author_born_place,
                                 'author_about': author_about},
                      'tags': {'tags_name': tags_name,
                               'tags_url': tags_url,
                               'tags_text': tags_text,
                               'tags_author': tags_author,
                               'tags_author_url': tags_author_url}}
    print(result)
    return result


def write_to_csv():
    with open(CSV_PATH, "a", newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow('header')
        line_id = 1
        for item in result:
            # print(result['info']['text'])
            # add rows in our csv-file [line_id, item]
            list_col = [line_id, item]
            writer.writerow(list_col)
            line_id += 1

if __name__ == '__main__':
    parse(get_info_site(URL))
    # write_to_csv()