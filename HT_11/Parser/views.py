from django.http import HttpResponse
from django.shortcuts import render
from .config import *
import requests
import os
import logging
from Parser.models import *

if not os.path.exists(PATH_FOLDER):
    os.makedirs(PATH_FOLDER)

logging.basicConfig(filename=PATH_LOGGING, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def parse_category(url_category):
    data = {}
    try:
        response = requests.get(url_category, timeout=10)
        data = response.json()
        return data
    except UnicodeEncodeError:
        logging.error('This is an error message. Unicode encode trouble. '
                      'Check data in request!!!')
    except Exception:
        logging.exception("Error in func  parse_category" + str(data), exc_info=True)


def add_items_in_category_list(for_category):
    category_info = []
    for item in for_category:
        try:
            url = 'https://hacker-news.firebaseio.com/' \
                  'v0/item/' + str(item) + '.json?print=pretty'
            response = requests.get(url, timeout=10)
            item_info = response.json()
            # if item_info['score'] >= SCORE and item_info['time'] >= FROM_DATE:
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
            info = [id, title, time, descendants, by, kids, type, score, text, url]
            # logging.DEBUG()
            category_info.append(info)
            # with open('reports/log_list.txt', 'a') as f:
            #     f.write(str(category_info)+'\n')
        except Exception:
            logging.exception("Error in my func add_items")
    return category_info


def save_in_db(category_name, category_data):
    for item in category_data:
        print(item)
        try:
            if category_name == 'askstories':
                ask = Askstories(id=item[0], title=item[1], time=item[2],
                                 descendants=item[3], by=item[4], kids=item[5],
                                 type=item[6], score=item[7], text=item[8], url=item[9])
                ask.save()
            elif category_name == 'showstories':
                show = Showstories(id=item[0], title=item[1], time=item[2],
                                   descendants=item[3], by=item[4], kids=item[5],
                                   type=item[6], score=item[7], text=item[8], url=item[9])
                show.save()
            elif category_name == 'newstories':
                new = Newstories(id=item[0], title=item[1], time=item[2],
                                 descendants=item[3], by=item[4], kids=item[5],
                                 type=item[6], score=item[7], text=item[8], url=item[9])
                new.save()
            elif category_name == 'jobstories':
                job = Jobstories(id=item[0], title=item[1], time=item[2],
                                 descendants=item[3], by=item[4], kids=item[5],
                                 type=item[6], score=item[7], text=item[8], url=item[9])
                job.save()
            else:
                logging.info('False category in func /////save_in_db/////')
        except Exception as e:
            logging.exception('error', e)


def main_func(request):
    logging.info("Start func parse_category")

    for_ask = parse_category(URL_FOR_ASK)
    category_list = add_items_in_category_list(for_ask)
    logging.info("finish parse askstories")
    save_in_db('askstories', category_list)
    logging.info("save in db askstories")

    for_show = parse_category(URL_FOR_SHOW)
    category_list = add_items_in_category_list(for_show)
    logging.info("finish parse showstories")
    save_in_db('showstories', category_list)
    logging.info("save in db showstories")

    for_new = parse_category(URL_FOR_NEW)
    category_list = add_items_in_category_list(for_new)
    logging.info("finish parse newstories")
    save_in_db('newstories', category_list)
    logging.info("save in db newstories")

    for_job = parse_category(URL_FOR_JOB)
    category_list = add_items_in_category_list(for_job)
    logging.info("finish parse jobstories")
    save_in_db('jobstories', category_list)
    logging.info("save in db jobstories")

    html = '<h1>Write in db - done<h1>'
    return HttpResponse(html)


def index(request):
    context = {
        'askstories': Askstories.objects.all(),
        'showstories': Showstories.objects.all(),
        'newstories': Newstories.objects.all(),
        'jobstories': Jobstories.objects.all()

    }
    return render(request, 'Parser/index.html', context)
