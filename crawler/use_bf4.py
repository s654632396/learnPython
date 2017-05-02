# coding=utf-8 
from bs4 import BeautifulSoup


# build BeautifulSoup Object by HTML string

html_doc = """
<!DOCTYPE html>
<html>
<head>
    <title>    laraCafe
</title>
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"/>
    <link rel="stylesheet" href="http://localhost/carefreeWizard/laravel5.2/public/index.php/src/css/main.css">
    <style>

        html, body {
            height: 100%;
        }
        .container {
            text-align: center;
            display: table-cell;
            vertical-align: middle;
        }
    </style>
</head>
<body>
<header>
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                        data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">LaraCafe</a>
                <ul class="nav navbar-nav navbar-left">
                <li><a href="http://localhost/carefreeWizard/laravel5.2/public/index.php/dashboard">Dashboard</a></li>
                </ul>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->

    </nav>
</header><div class="container">
        <div class="row">
        <div class="col-md-6">
            <form action="http://localhost/carefreeWizard/laravel5.2/public/index.php/signup" method="post">
                <h3>Sign Up</h3>
                <div class="form-group ">
                    <label for="email">your email:</label>
                    <input class="form-control" type="text" placeholder="take an email here" name="email" id="email" value="">
                </div>
                <div class="form-group ">
                    <label for="username">your username:</label>
                    <input class="form-control" type="text" name="username" placeholder="take your name here" id="username" value="">
                </div>
                <div class="form-group ">
                    <label for="password">your password:</label>
                    <input class="form-control" type="password" name="password" id="password">
                </div>
                <input type="hidden" name="_token" value="XBRCQC3ZQ4bUF8r5QZTVbaGghr4w8DJYolQNOa7A">
                <button type="submit" class="btn btn-primary">submit</button>
            </form>
        </div>
        <div class="col-md-6">
            <form action="http://localhost/carefreeWizard/laravel5.2/public/index.php/signin" method="post">
                <h3>Sign In</h3>
                <div class="form-group ">
                    <label for="email">your email:</label>
                    <input class="form-control" type="text" name="email" id="email" value="">
                </div>
                <div class="form-group ">
                    <label for="password">your password:</label>
                    <input class="form-control" type="password" name="password" id="password" value="">
                </div>
                <input type="hidden" name="_token" value="XBRCQC3ZQ4bUF8r5QZTVbaGghr4w8DJYolQNOa7A">
                <button type="submit" class="btn btn-primary">submit</button>
            </form>
        </div>
    </div>

<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
    <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.js"></script>
    <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <script src="http://localhost/carefreeWizard/laravel5.2/public/index.php/src/js/app.js"></script>
</div>
</body>
</html>
"""

soup = BeautifulSoup(
    html_doc,
    'html.parser',
    from_encoding='utf8',
)

print 'capture all links----'
links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()

print 'capture one input where id=username'
input = soup.find('input', id='username')
print input
print input.name , input['class'], input['type']

print 'capture with regular expression'
import re
ele = soup.find_all('script', src=re.compile(r'laravel'))
print ele

divs = soup.find_all('div', {'class':'form-group'})
label_s = []

for div in divs:
    labels = soup.find_all('label', text=re.compile(r'email:'))
    if labels is not False:
        for label in labels:
            label_s.append(label)

print len(label_s)