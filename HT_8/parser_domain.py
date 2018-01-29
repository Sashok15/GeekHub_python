import requests
import os
import csv
import xlsxwriter
import json
from bs4 import BeautifulSoup
from config_domain import *

if not os.path.exists(PATH_REPORTS):
    os.makedirs(PATH_REPORTS)


def parse_domains():
    next_page_url = '/deleted-info-domains/'
    while True:
        r = requests.get(URL_DOMAIN + next_page_url, timeout=10)
        soup = BeautifulSoup(r.content, 'lxml')
        links = soup.select('a.namelinks')

        for link in links:
            result_domains.append(link.text)

        write_to_csv(result_domains)
        # write_to_xls(result_domains)
        # write_to_txt(result_domains)
        # write_to_json(result_domains)
        try:
            next_page_url = soup.select('a.next')[-1].get('href')
        except IndexError:
            break


def write_to_csv(result):
    with open(CSV_PATH, 'a') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL, )
        for item in result:
            csv_writer.writerow([item])


def write_to_txt(result):
    with open(TXT_PATH, 'a') as f:
        for item in result:
            f.write(str(item) + '\n')


def write_to_xls(result):
    workbook = xlsxwriter.Workbook(XLS_PATH)
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    for i in result:
        worksheet.write(row, col, i)
        row += 1


def write_to_json(result):
    with open(JSON_PATH, 'a') as f:
        json.dump(result, f)


parse_domains()
