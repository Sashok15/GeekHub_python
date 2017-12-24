import requests
import xlsxwriter
import json
import csv
import os

from bs4 import BeautifulSoup
from config import *

if not os.path.exists(PATH_REPORTS):
    os.makedirs(PATH_REPORTS)


def get_info_site(my_url):
    r = requests.get(url=my_url)
    return r.content


id_author = 0


def parse(html):
    soup = BeautifulSoup(html.decode('utf-8'), 'lxml')
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
        global id_author
        id_author += 1
        author_info_for_search.append({'text': text_data,
                                       'author': {'author_name': author_name,
                                                  'author_url': author_url,
                                                  'id': id_author,
                                                  },
                                       'tags': {'tags_name': tags_name,
                                                'tags_url': tags_url}})

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
    print(author_info_for_search)

    return full_info_list


def clear_data():
    # text
    text_data.clear()
    # authors
    author_name.clear()
    author_url.clear()
    author_born_date.clear()
    author_born_place.clear()
    author_about.clear()
    # tags
    tags_name.clear()
    tags_url.clear()
    tags_text.clear()
    tags_author.clear()
    tags_author_url.clear()

    full_info_list.clear()


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


def write_to_json():
    with open(JSON_PATH, 'a') as f:
        json.dump(full_info_list, f)


def write_to_txt_search():
    with open(TXT_PATH_FOR_SEARCH, 'a', encoding='utf8') as f:
        for item in author_info_for_search:
            f.write(str(item['text']))
            f.write(str(item['author']['author_name']))
            f.write(str(item['author']['author_url']))
            f.write(str(item['author']['id']))
            f.write(str(item['tags']['tags_name']))
            f.write(str(item['tags']['tags_url']))


def read_from_txt():
    with open(TXT_PATH_FOR_SEARCH, 'r') as f:
        return f.readline()


def find_authors(*author_id):
    pass


if __name__ == '__main__':
    for i in range(1, 10):
        parse(get_info_site(URL + '/page/' + str(i) + '/'))
    # parse(get_info_site(URL))
        write_to_csv()
        write_to_txt()
        write_to_json()
        write_to_xls()
        clear_data()
    # write_to_txt_search()
    # print(read_from_txt())
    # print(find_authors(1, 2))
