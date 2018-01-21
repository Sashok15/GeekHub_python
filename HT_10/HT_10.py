import argparse
import os
import requests
import time
import logging
import psycopg2
from psycopg2 import sql

from config import *


class Parser(object):

    def __init__(self, options):
        self.options = options

    def get_for_one_category(self):
        data = []
        category_info = []
        # select url under the category
        logging.info("Check category in url")
        try:
            # choices['askstories', 'showstories', 'newstories', 'jobstories']
            if self.options.category == CHOICES[0]:
                response = requests.get(URL_FOR_ASK, timeout=10)
                data = response.json()

            elif self.options.category == CHOICES[1]:
                response = requests.get(URL_FOR_SHOW, timeout=10)
                data = response.json()

            elif self.options.category == CHOICES[2]:
                response = requests.get(URL_FOR_NEW, timeout=10)
                data = response.json()

            elif self.options.category == CHOICES[3]:
                response = requests.get(URL_FOR_JOB, timeout=10)
                data = response.json()
            else:
                raise Exception("Error! not correct the parameters")
        except UnicodeEncodeError:
            logging.error('This is an error message. Unicode encode trouble. '
                          'Check data in request!!!')
        except Exception:
            logging.exception("error in func get_one_category")

        # get the records in category
        for item in data:
            info = []
            try:
                url = 'https://hacker-news.firebaseio.com/' \
                      'v0/item/' + str(item) + '.json?print=pretty'
                response = requests.get(url, timeout=10)
                item_info = response.json()
                if item_info['score'] >= SCORE and item_info['time'] >= FROM_DATE:
                    id = item_info['id']
                    title = item_info['title']
                    time = item_info['time']
                    type = item_info['type']
                    score = item_info['score']
                    by = item_info['by']
                    try:
                        descendants = item_info['descendants']
                    except KeyError:
                        descendants = 'descendants'
                    try:
                        kids = item_info['kids']
                    except KeyError:
                        kids = 'kids'
                    try:
                        text = item_info['text']
                    except KeyError:
                        text = 'text'
                    try:
                        url = item_info['url']
                    except KeyError:
                        url = 'url'
                    info.extend([id, title, time, descendants, by, kids, type, score, text, url])
                    category_info.append(info)
            except UnicodeEncodeError:
                logging.ERROR('This is an error message. Unicode encode trouble. '
                              'Check data in request!!!')
            except Exception:
                logging.exception('error in category`s {} data'.format(self.options.category))
        return category_info

    @staticmethod
    def get_id_from_db(category):
        id_in_db = []
        cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier(category)))
        rows = cursor.fetchall()
        for i in rows:
            id_in_db.append(i[0])
        return id_in_db

    @staticmethod
    def get_data_from_db(category):
        data = []
        cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier(category)))
        rows = cursor.fetchall()
        for item in rows:
            data.append('<tr><td>' + str(item) + '</td></tr>')
        return data

    @staticmethod
    def write_data_in_db(my_list, category):
        id_from_db = Parser.get_id_from_db(category)
        for temp_list in my_list:
            if temp_list[0] in id_from_db:
                cursor.execute(sql.SQL("""UPDATE {} SET title = %S, TIME = %S, descendants = %S, BY = %S, kids = %S, 
                                          TYPE = %S, score = %S, TEXT = %S, url = %S WHERE id = %S;"""
                                       ).format(sql.Identifier(category)),
                               (temp_list[1], temp_list[2], temp_list[3],
                                temp_list[4], str(temp_list[5]), temp_list[6], temp_list[7],
                                temp_list[8], temp_list[9], temp_list[0]))
            else:
                print('insert')
                cursor.execute(sql.SQL("""INSERT INTO {} (id, title, TIME, descendants, BY, kids, TYPE, score, TEXT, url)
                                              VALUES (%S, %S, %S, %S, %S, %S, %S, %S, %S, %S);"""
                                       ).format(sql.Identifier(category)),
                               (temp_list[0], temp_list[1], temp_list[2], temp_list[3],
                                temp_list[4], str(temp_list[5]), temp_list[6], temp_list[7],
                                temp_list[8], temp_list[9]))
                # row = cursor.fetchone()
                conn.commit()

    @staticmethod
    def write_all_data_to_html(category):
        data_show = Parser.get_data_from_db('showstories')
        data_new = Parser.get_data_from_db('newstories')
        data_ask = Parser.get_data_from_db('askstories')
        data_job = Parser.get_data_from_db('jobstories')
        html = get_html().format(data_ask, data_show, data_new, data_job)
        time_now = time.strftime("%Y%m%d-%H%M%S")
        with open('reports/' + time_now + '.html', 'a') as f:
            f.write(html)


if __name__ == '__main__':
    conn = psycopg2.connect(database='HT_10', user='postgres',
                            password='root', host='localhost', port=5432)
    cursor = conn.cursor()

    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
        logging.info("Create folder 'reports'")

    logging.basicConfig(filename=LOGGING_PATH, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    logging.info("Program started")

    arg_parser = argparse.ArgumentParser(
        description='Great Description To Be Here')

    arg_parser.add_argument("--category", "-c", type=str, default="askstories",
                            help="select all categories - 'all' or one category with this list: "
                                 "'askstories', 'showstories',"
                                 "'newstories', 'jobstories'")
    options = arg_parser.parse_args()
    pars = Parser(options)

    if options.category in CHOICES:
        print(options)
        logging.info("User selected true-category: " + options.category)
        # pars.write_data_in_db(pars.get_for_one_category(), options.category)
        Parser.write_all_data_to_html(options.category)
    elif options.category is None:
        logging.info("User did`t select nothing. Appointed default category")
    else:
        logging.error('User selected non-correct category: ' + options.category)
        raise Exception("Error! not correct the parameters" + options.category)
