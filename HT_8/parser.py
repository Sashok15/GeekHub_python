import requests
import xlsxwriter
import json
import re
import csv
import os
import logging

from bs4 import BeautifulSoup
from config import *

if not os.path.exists(PATH_REPORTS):
    os.makedirs(PATH_REPORTS)

logging.basicConfig(filename='reports/report.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def get_info_site(my_url):
    r = requests.get(url=my_url)
    return r.content


id_author = 0


def parse(html):
    # text
    text_data = []

    # authors
    author_name = []
    author_url = []
    author_born_date = []
    author_born_place = []
    author_about = []

    # tags
    tags_name = []
    tags_url = []
    tags_text = []
    tags_author = []
    tags_author_url = []
    soup = BeautifulSoup(html.decode('utf-8'), 'lxml')
    logging.info('parse start')
    for item in soup.find_all('div', class_='quote'):
        tags_n = []
        tags_u = []
        text_data.append(item.contents[1].contents[0])
        quote_for_search = item.contents[1].contents[0]

        author_name.append(item.contents[3].contents[1].contents[0])
        author_name_for_search = item.contents[3].contents[1].contents[0]

        author_url.append(item.contents[3].contents[3].get('href'))
        author_url_for_search = item.contents[3].contents[3].get('href')
        for i in item.contents[5].find_all('a'):
            tags_n.append(i.text)
            tags_u.append(i.get('href'))
        tags_name.append(tags_n)
        tags_name_for_search = tags_n

        tags_url.append(tags_u)
        tags_url_for_search = tags_u
        global id_author
        id_author += 1
        author_info_for_search.append({'text': quote_for_search,
                                       'author': {'author_name': author_name_for_search,
                                                  'author_url': author_url_for_search,
                                                  'id': id_author,
                                                  },
                                       'tags': {'tags_name': tags_name_for_search,
                                                'tags_url': tags_url_for_search}})
        logging.info('parse authors')
        for i in author_url:
            soup_for_author = BeautifulSoup(get_info_site(URL + i), 'lxml')
            for ele in soup_for_author.find_all('div', class_='author-details'):
                author_born_date.append(ele.contents[2].contents[2].contents[0])
                author_born_place.append(ele.contents[2].contents[4].contents[0])
                author_about.append(ele.find('div', class_='author-description').contents[0][:100])
    for urls in tags_url:
        tags_text_temp, tags_author_temp, tags_author_url_temp = [], [], []
        for url_tag in urls:
            soup_for_tags = BeautifulSoup(get_info_site(URL + url_tag), 'lxml')
            for ele in soup_for_tags.find_all('div', class_='quote'):
                tags_text_temp.append(ele.contents[1].contents[0])
                tags_author_temp.append(ele.contents[3].contents[1].contents[0])
                tags_author_url_temp.append(ele.contents[3].contents[3].get('href'))
            tags_text.append(tags_text_temp)
            tags_author.append(tags_author_temp)
            tags_author_url.append(tags_author_url_temp)

    logging.info('add info in full_info_list')
    full_info_list.append({'text': text_data,
                           'author': {'author_name': author_name,
                                      'author_url': author_url,
                                      'author_born_date': author_born_date,
                                      'author_born_place': author_born_place,
                                      'author_about': author_about},
                           'tags': {'tags_name': tags_name,
                                    'tags_url': tags_url,
                                    'tags_text': tags_text,
                                    'tags_author': tags_author,
                                    'tags_author_url': tags_author_url}})

    return full_info_list


def write_to_csv():
    with open(CSV_PATH, "a", newline='', encoding='utf8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(['information'])
        for item in full_info_list:
            writer.writerow(item['text'])
            writer.writerow(item['author']['author_name'])
            writer.writerow(item['author']['author_url'])
            writer.writerow(item['author']['author_born_date'])
            writer.writerow(item['author']['author_born_place'])
            writer.writerow(item['author']['author_about'])
            writer.writerow(item['tags']['tags_name'])
            writer.writerow(item['tags']['tags_url'])
            writer.writerow(item['tags']['tags_text'])
            writer.writerow(item['tags']['tags_author'])
            writer.writerow(item['tags']['tags_author_url'])

    logging.info('write data in csv file')


def write_to_txt():
    with open(TXT_PATH, "a", newline='', encoding='utf8') as f:
        for item in full_info_list:
            f.write(str(item['text']))
            f.write(str(item['author']['author_name']))
            f.write(str(item['author']['author_url']))
            f.write(str(item['author']['author_born_date']))
            f.write(str(item['author']['author_born_place']))
            f.write(str(item['author']['author_about']))
            f.write(str(item['tags']['tags_name']))
            f.write(str(item['tags']['tags_url']))
            f.write(str(item['tags']['tags_text']))
            f.write(str(item['tags']['tags_author']))
            f.write(str(item['tags']['tags_author_url']))

        logging.info('write data in txt file')


def write_to_xls():
    workbook = xlsxwriter.Workbook(XLS_PATH)
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    for item in full_info_list:
        worksheet.write(row, col, 'text')
        worksheet.write(row, col + 1, str(item['text']))
        row += 1
        worksheet.write(row, col, 'author_name')
        worksheet.write(row, col + 1, str(item['author']['author_name']))
        row += 1
        worksheet.write(row, col, 'author_url')
        worksheet.write(row, col + 1, str(item['author']['author_url']))
        row += 1
        worksheet.write(row, col, 'author_born_date')
        worksheet.write(row, col + 1, str(item['author']['author_born_date']))
        row += 1
        worksheet.write(row, col, 'author_born_place')
        worksheet.write(row, col + 1, str(item['author']['author_born_place']))
        row += 1
        worksheet.write(row, col, 'author_about')
        worksheet.write(row, col + 1, str(item['author']['author_about']))
        row += 1
        worksheet.write(row, col, 'tags_name')
        worksheet.write(row, col + 1, str(item['tags']['tags_name']))
        row += 1
        worksheet.write(row, col, 'tags_url')
        worksheet.write(row, col + 1, str(item['tags']['tags_url']))
        row += 1
        worksheet.write(row, col, 'tags_text')
        worksheet.write(row, col + 1, str(item['tags']['tags_text']))
        row += 1
        worksheet.write(row, col, 'tags_author')
        worksheet.write(row, col + 1, str(item['tags']['tags_author']))
        row += 1
        worksheet.write(row, col, 'tags_author_url')
        worksheet.write(row, col + 1, str(item['tags']['tags_author_url']))
        row += 1

    logging.info('write data in xls file')


def write_to_json():
    with open(JSON_PATH, 'a') as f:
        json.dump(full_info_list, f)


def write_to_json_search():
    with open('reports/for_search.json', 'a') as f:
        json.dump(author_info_for_search, f)

    logging.info('write data in json_search_file')


def read_json_search():
    with open('reports/for_search.json') as json_data:
        result = json.load(json_data)
    return result


def find_author(*id_authors):
    for id_ in id_authors:
        for item in read_json_search():
            id_found_author = re.findall('\'id\': (\d{1,2})', str(item))
            if str(id_) in id_found_author:
                print(id_)
                print(item)
                logging.info('found the author id - ' + str(id_))


if __name__ == '__main__':
    for i in range(1, 11):
        try:
            parse(get_info_site(URL + '/page/' + str(i) + '/'))
        except:
            parse(get_info_site(URL + '/page/' + str(i) + '/'))
    write_to_csv()
    write_to_txt()
    write_to_json()
    write_to_xls()
    write_to_json_search()
    find_author(1, 2, 5, 17)
