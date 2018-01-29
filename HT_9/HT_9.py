import argparse
import os
import requests
import time
import pickle
import logging
import re

from config import *


class Parser(object):

    def __init__(self, options):
        self.options = options

    def get_for_one_category(self):
        data = []
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
            try:
                url = 'https://hacker-news.firebaseio.com/' \
                      'v0/item/' + str(item) + '.json?print=pretty'
                response = requests.get(url, timeout=5)
                item_info = response.json()

                if item_info['score'] >= SCORE and item_info['time'] >= FROM_DATE:
                    info = re.sub('<.+>', '', str(item_info))
                    list_id.append(item_info['id'])
                    category_info.append('<tr><td>' + info + '</td></tr>')
            except UnicodeEncodeError:
                logging.ERROR('This is an error message. Unicode encode trouble. '
                              'Check data in request!!!')
                continue

    @staticmethod
    def get_for_all_categories():
        try:
            response = requests.get(URL_FOR_ASK, timeout=10)
            data_for_ask = response.json()
            for item in data_for_ask:
                try:
                    url = 'https://hacker-news.firebaseio.com/' \
                          'v0/item/' + str(item) + '.json?print=pretty'
                    response = requests.get(url, timeout=10)
                    item_info = response.json()
                    if item_info['id'] not in Parser.upload_with_pickle() or Parser.upload_with_pickle() is None:
                        if item_info['score'] >= SCORE and item_info['time'] >= FROM_DATE:
                            info = re.sub('<.+>', '', str(item_info))
                            list_id.append(item_info['id'])
                            category_info_ask.append('<tr><td>' + info + '</td></tr>')
                except UnicodeEncodeError:
                    logging.ERROR('This is an error message. Unicode encode trouble. '
                                  'Check data in request!!!')
                    continue
                except Exception:
                    logging.exception("Error in my loop for ask")
                    continue

            response = requests.get(URL_FOR_SHOW, timeout=10)
            data_for_show = response.json()

            for item in data_for_show:
                try:
                    url = 'https://hacker-news.firebaseio.com/' \
                          'v0/item/' + str(item) + '.json?print=pretty'
                    response = requests.get(url, timeout=10)
                    item_info = response.json()
                    if item_info['id'] not in Parser.upload_with_pickle():
                        if item_info['score'] >= SCORE and item_info['time'] >= FROM_DATE:
                            info = re.sub('<.+>', '', str(item_info))
                            list_id.append(item_info['id'])
                            category_info_show.append(('<tr><td>' + info + '</td></tr>'))
                except UnicodeEncodeError:
                    logging.ERROR('This is an error message. Unicode encode trouble. '
                                  'Check data in request!!!')
                    continue
                except Exception:
                    logging.exception("Error in my loop for show")
                    continue

            response = requests.get(URL_FOR_NEW, timeout=10)
            data_for_new = response.json()

            for item in data_for_new:
                try:
                    url = 'https://hacker-news.firebaseio.com/' \
                          'v0/item/' + str(item) + '.json?print=pretty'
                    response = requests.get(url, timeout=10)
                    item_info = response.json()
                    if item_info['id'] not in Parser.upload_with_pickle():
                        if item_info['score'] >= SCORE and item_info['time'] >= FROM_DATE:
                            info = re.sub('<.+>', '', str(item_info))
                            list_id.append(item_info['id'])
                            category_info_new.append(('<tr><td>' + info + '</td></tr>'))
                except UnicodeEncodeError:
                    logging.ERROR('This is an error message. Unicode encode trouble. '
                                  'Check data in request!!!')
                    continue
                except Exception:
                    logging.exception("Error in my loop for news")
                    continue

            response = requests.get(URL_FOR_JOB, timeout=10)
            data_for_job = response.json()

            for item in data_for_job:
                try:
                    url = 'https://hacker-news.firebaseio.com/' \
                          'v0/item/' + str(item) + '.json?print=pretty'
                    response = requests.get(url, timeout=10)
                    item_info = response.json()
                    if item_info['id'] not in Parser.upload_with_pickle():
                        if item_info['score'] >= SCORE and item_info['time'] >= FROM_DATE:
                            info = re.sub('<.+>', '', str(item_info))
                            list_id.append(item_info['id'])
                            category_info_job.append(('<tr><td>' + info + '</td></tr>'))
                except UnicodeEncodeError:
                    logging.ERROR('This is an error message. Unicode encode trouble. '
                                  'Check data in request!!!')
                    continue
                except Exception:
                    logging.exception("Error in my loop for job")
                    continue
        except UnicodeEncodeError:
            logging.error('This is an error message. Unicode encode trouble. '
                          'Check data in request!!!')
        except Exception:
            logging.exception("Error in func get all categories", exc_info=True)

    @staticmethod
    def write_to_html(html):
        time_now = time.strftime("%Y%m%d-%H%M%S")
        with open('reports/' + time_now + '.html', 'a') as f:
            f.write(html)

    @staticmethod
    def write_to_pickle(category):
        with open('reports/pickle_id', 'ab') as file:
            pickle.dump(category, file)

    @staticmethod
    def upload_with_pickle():
        with open('reports/pickle_id', 'rb') as file:
            data_in_pickle = pickle.load(file)
        return data_in_pickle


if __name__ == '__main__':
    logging.basicConfig(filename=LOGGING_PATH, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    logging.info("Program started")

    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
        logging.info("Create folder 'reports'")

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
        Parser.write_to_pickle(list_id)
        # print(Parser.upload_with_pickle())
        # Parser.write_to_html(HTML_FILE_FOR_ALL)
    elif options.category == 'all':
        pars.get_for_all_categories()
        html = get_html().format(category_info_ask, category_info_show, category_info_new,
                                 category_info_job)

        Parser.write_to_html(html)
    elif options.category is None:
        logging.info("User did`t select nothing. Appointed default category")
    else:
        logging.error('User selected non-correct category: ' + options.category)
        raise Exception("Error! not correct the parameters" + options.category)
