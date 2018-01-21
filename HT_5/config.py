# path
PATH_REPORTS = "/reports"
PATH_LOGS = "reports/hn_parser.log"
PATH_CSV = "reports/report.csv"

# parameters
CATEGORIES = ['askstories', 'showstories', 'newstories', 'jobstories']

# filsters
FROM_DATE = 1510852024
SCORE = 10

# url for requests
URL_FOR_NEW = 'https://hacker-news.firebaseio.com/v0/' \
              'newstories.json?print=pretty'
URL_FOR_ASK = 'https://hacker-news.firebaseio.com/v0/' \
              'askstories.json?print=pretty'
URL_FOR_SHOW = 'https://hacker-news.firebaseio.com/v0/' \
               'showstories.json?print=pretty'
URL_FOR_JOB = 'https://hacker-news.firebaseio.com/v0/' \
              'jobstories.json?print=pretty'
