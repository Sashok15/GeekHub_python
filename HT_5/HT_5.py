import argparse
import os
import requests
import csv
import logging
import re

from config import *

if not os.path.exists(FOLDER_PATH):
    os.makedirs(FOLDER_PATH)
    logging.info("Create folder 'reports'")


logging.basicConfig(filename=LOGGING_PATH, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

arg_parser = argparse.ArgumentParser(
    description='Great Description To Be Here')

arg_parser.add_argument("--category", "-c", type=str, default="newstories",
                        help="select one category with this list: "
                             "'askstories', 'showstories', "
                             "'newstories', 'jobstories'")
options = arg_parser.parse_args()

logging.info("Program started")

if options.category in CHOICES:
    print(options)
    logging.info("User selected true-category: "+options.category)
elif options.category is None:
    logging.info("User did`t select nothing. Appointed default category")
else:
    logging.error('User selected non-correct category: '+options.category)
    raise Exception("Error! not correct the parameters"+options.category)

data = []
# select url under the category
logging.info("Check category in url")
try:
    # choices['askstories', 'showstories', 'newstories', 'jobstories']
    if options.category == CHOICES[0]:
        response = requests.get(URL_FOR_ASK, timeout=5)
        data = response.json()

    elif options.category == CHOICES[1]:
        response = requests.get(URL_FOR_SHOW, timeout=5)
        data = response.json()

    elif options.category == CHOICES[2]:
        response = requests.get(URL_FOR_NEW, timeout=5)
        data = response.json()

    elif options.category == CHOICES[3]:
        response = requests.get(URL_FOR_JOB, timeout=5)
        data = response.json()
    else:
        raise Exception("Error! not correct the parameters")
except UnicodeEncodeError:
    logging.error('This is an error message. Unicode encode trouble. '
                  'Check data in request!!!')

category_info = []

# get the records in category

for item in data:
    try:
        url = 'https://hacker-news.firebaseio.com/' \
              'v0/item/'+str(item)+'.json?print=pretty'
        response = requests.get(url, timeout=5)
        item_info = response.json()
        if item_info['score'] >= SCORE and item_info['time'] >= FROM_DATE:
            info = re.sub('<.+>', '', str(item_info))
            category_info.append(info)
    except UnicodeEncodeError:
        logging.ERROR('This is an error message. Unicode encode trouble. '
                      'Check data in request!!!')
        continue
logging.info('found all files by filter')
title = ['number', options.category]
with open(CSV_PATH, "a", newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(title)
    line_id = 1
    for item in category_info:
        # add rows in our csv-file [line_id, item]
        list_col = [line_id, item]
        writer.writerow(list_col)
        line_id += 1
    logging.info('writed records in file by filter')
