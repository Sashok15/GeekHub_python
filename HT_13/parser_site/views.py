from django.http import HttpResponse
from django.shortcuts import render
from parser_site.config import *
import requests
import os
import logging
from parser_site.models import *

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
            category_info.append(info)
        except Exception as e:
            logging.exception("Error in my func add_items", e)
    return category_info


def save_in_db(category_name, category_data):
    for item in category_data:
        # print(item)
        try:
            if category_name == 'askstories':
                c = Category.objects.get(id=1)
                c.articles_set.create(
                    id_article=item[0], title=item[1], time=item[2],
                    descendants=item[3], by=item[4], kids=item[5],
                    type=item[6], score=item[7], text=item[8], url=item[9]
                )

            elif category_name == 'showstories':
                c = Category.objects.get(id=2)
                c.articles_set.create(
                    id_article=item[0], title=item[1], time=item[2],
                    descendants=item[3], by=item[4], kids=item[5],
                    type=item[6], score=item[7], text=item[8], url=item[9]
                )
            elif category_name == 'newstories':
                c = Category.objects.get(id=3)
                c.articles_set.create(
                    id_article=item[0], title=item[1], time=item[2],
                    descendants=item[3], by=item[4], kids=item[5],
                    type=item[6], score=item[7], text=item[8], url=item[9]
                )
            elif category_name == 'jobstories':
                c = Category.objects.get(id=4)
                c.articles_set.create(
                    id_article=item[0], title=item[1], time=item[2],
                    descendants=item[3], by=item[4], kids=item[5],
                    type=item[6], score=item[7], text=item[8], url=item[9]
                )
            else:
                logging.info('False category in func /////save_in_db/////')
        except Exception as e:
            logging.exception('error', e)


def main_func(request):
    logging.info("Start func main_func")
    for item in CATEGORIES:
        data_list = add_items_in_category_list(parse_category(URL_FOR_ALL.format(item)))
        logging.info("finish parse" + item)
        save_in_db(item, data_list)
        logging.info("save in db" + item)

    html = '<h1>Write in db - done<h1>'
    return HttpResponse(html)


def index(request):
    context = {
        'categories': Category.objects.all(),
        'askstories': Articles.objects.filter(category_id=1),
        'showstories': Articles.objects.filter(category_id=2),
        'newstories': Articles.objects.filter(category_id=3),
        'jobstories': Articles.objects.filter(category_id=4),
    }
    return render(request, 'parser_site/index.html', context)
