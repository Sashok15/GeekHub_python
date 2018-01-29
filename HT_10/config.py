# path
FOLDER_PATH = "reports"
LOGGING_PATH = "reports/hn_parser.log"
CSV_PATH = "reports/report.csv"

# parameters
CHOICES = ['askstories', 'showstories', 'newstories', 'jobstories']
DEFAULT_PARAMETER = 'newstories'

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

category_info_ask = []
category_info_show = []
category_info_new = []
category_info_job = []

def get_html():
    html = """<!doctype html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css"
                                          integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy" crossorigin="anonymous">
                                    <meta name="viewport"
                                          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
                                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                    <title>Homework - 10</title>
                                </head>
                                <body>
                                <h2>Homework - 9</h2>
                                <div role="tablist">
                                    <div class="card">
                                        <div class="card-header" role="tab" id="headingOne">
                                            <h5 class="mb-0">
                                                <a data-toggle="collapse" href="#collapseOne" role="button" aria-expanded="false"
                                                   aria-controls="collapseOne">
                                                    askstories
                                                </a>
                                            </h5>
                                        </div>

                                        <div id="collapseOne" class="collapse show" role="tabpanel" aria-labelledby="headingOne">
                                            <div class="card-body">
                                                <table class="table">
                                                    <thead>
                                                    <tr>
                                                        <th scope="col">askstories_info</th>
                                                    </tr>
                                                    </thead>
                                                    <tbody>
                                                        {}
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="card">
                                        <div class="card-header" role="tab" id="headingTwo">
                                            <h5 class="mb-0">
                                                <a class="collapsed" data-toggle="collapse" href="#collapseTwo" role="button" aria-expanded="false"
                                                   aria-controls="collapseTwo">
                                                    showstories
                                                </a>
                                            </h5>
                                        </div>
                                        <div id="collapseTwo" class="collapse" role="tabpanel" aria-labelledby="headingTwo" data-parent="#accordion">
                                            <div class="card-body">
                                                <table class="table">
                                                    <thead>
                                                    <tr>
                                                        <th scope="col">showstories_info</th>
                                                    </tr>
                                                    </thead>
                                                    <tbody>
                                                        {}
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="card">
                                        <div class="card-header" role="tab" id="headingThree">
                                            <h5 class="mb-0">
                                                <a class="collapsed" data-toggle="collapse" href="#collapseThree" role="button" aria-expanded="false"
                                                   aria-controls="collapseThree">
                                                    newstories
                                                </a>
                                            </h5>
                                        </div>
                                        <div id="collapseThree" class="collapse" role="tabpanel" aria-labelledby="headingThree">
                                            <div class="card-body">
                                                <table class="table">
                                                    <thead>
                                                    <tr>
                                                        <th scope="col">newstories_info</th>
                                                    </tr>
                                                    </thead>
                                                    <tbody>
                                                        {}
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="card">
                                        <div class="card-header" role="tab" id="headingFour">
                                            <h5 class="mb-0">
                                                <a class="collapsed" data-toggle="collapse" href="#collapseFour" role="button" aria-expanded="false"
                                                   aria-controls="collapseFour">
                                                    jobstories
                                                </a>
                                            </h5>
                                        </div>
                                        <div id="collapseFour" class="collapse" role="tabpanel" aria-labelledby="headingFour">
                                            <div class="card-body">
                                                <table class="table">
                                                    <thead>
                                                    <tr>
                                                        <th scope="col">jobstories_info</th>
                                                    </tr>
                                                    </thead>
                                                    <tbody>
                                                        {}
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                </body>
                                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
                                        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
                                        crossorigin="anonymous"></script>
                                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
                                        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
                                        crossorigin="anonymous"></script>
                                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js"
                                        integrity="sha384-a5N7Y/aK3qNeh15eJKGWxsqtnX/wWdSZSKp+81YjTmS15nvnvxKHuzaWwXHDli+4"
                                        crossorigin="anonymous"></script>
                                </html>"""
    return html
