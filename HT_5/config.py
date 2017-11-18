# path
folder_path = "C:/Users/sashok/GeekHub/GeekHub_python/HT_5/reports"
logging_path = "reports/hn_parser.log"
csv_path = "reports/report.csv"

# parameters
choices = ['askstories', 'showstories', 'newstories', 'jobstories']
default_parameter = 'newstories'

# filsters
from_date = 1510852024
score = 10

# url for requests
url_for_new = 'https://hacker-news.firebaseio.com/v0/' \
              'newstories.json?print=pretty'
url_for_ask = 'https://hacker-news.firebaseio.com/v0/' \
              'askstories.json?print=pretty'
url_for_show = 'https://hacker-news.firebaseio.com/v0/' \
               'showstories.json?print=pretty'
url_for_job = 'https://hacker-news.firebaseio.com/v0/' \
              'jobstories.json?print=pretty'
