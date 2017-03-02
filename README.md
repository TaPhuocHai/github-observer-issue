# Introdution

Using to handle app docbao

- slack.py : helper send message to slack
- ping.py  : ping server every 1 minute. If server is down, it's send a message to slack
- crawler.py : auto service run every 1 hour to get data from rss of papes

# Setup

1. Read [delpoy application with git](https://minhdanh.me/deploy-app-the-heroku-way-with-git-hooks/)
2. Make folder structer look like this

        docbao
           - webapp.git   : base git repo for webapp/app
           - service.git  : base git repo for webapp/service
           - webapp
               - app
               - service  : git repo
               - env
               - ...

3. `cd /home/docbao/service.git`
4. `git init --bare`
5. Copy content of file `post-receive.sh` to `service.git/hooks/post-receive`
6. `chmod 755 service.git/hooks/post-receive`
6. `cd /home/docbao/webapp/service`
7. `git init`
8. Create folder `service/tmp`

Now when push to repo service.git it will auto reload `ping` and `crawler` service

# Document

For debug in macbook

- [install memcached on mac](http://www.rahuljiresal.com/2014/03/installing-memcached-on-mac-with-homebrew-and-lunchy/)
