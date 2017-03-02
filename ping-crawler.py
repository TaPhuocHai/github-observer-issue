#!/usr/bin/env python
# -*- coding: utf-8 -*-

import schedule
import os
import time
from subprocess import call

from slack import *

jobIsDoing = False

def restart_cralwer():
    post_slack('AUTO RESTART CRAWLER', 'monitor')
    call ('/home/webapp/env/bin/python crawler.py & echo $! > /home/webapp/service/tmp/crawler.pid', shell=True)


def job():
    global jobIsDoing
    if jobIsDoing == True:
        print 'wating ...'
        return

    # Kiểm tra pid của crawler có tồn tại
    try:
        pid = 0
        with open('tmp/crawler.pid', 'r') as f:
            pid = int(f.read())
        f.closed

        if pid != 0:
            os.getpgid(pid)
        else:
            post_slack('Không tìm thấy thông tin pid crawler. Vui lòng kiểm tra lại', 'monitor')
    except OSError as e:
        restart_cralwer()

    jobIsDoing = False

# DO JOB
job ()
schedule.every(4).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(4)
