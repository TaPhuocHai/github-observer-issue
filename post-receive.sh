#!/bin/bash
unset GIT_DIR
APP_REPO="/home/webapp/service.git"
PING_PID_FILE="/home/webapp/service/tmp/ping.pid"
CRAWLER_PID_FILE="/home/webapp/service/tmp/crawler.pid"

while read oldrev newrev ref
do
    branch=`echo $ref | cut -d/ -f3`
    if [ "$branch" == "master" ] ; then
      cd /home/webapp/service/
      echo "--------> Getting latest code..."
      git pull $APP_REPO master
      echo "--------> Restarting ping server..."
      kill -KILL $(cat $PING_PID_FILE)
      rm -f $PING_PID_FILE
      /home/webapp/env/bin/python ping.py & echo $! > $PING_PID_FILE
      echo "--------> Restarting crawler server..."
      kill -KILL $(cat $CRAWLER_PID_FILE)
      rm -f $CRAWLER_PID_FILE
      /home/webapp/env/bin/python crawler.py & echo $! > $CRAWLER_PID_FILE
    fi
done