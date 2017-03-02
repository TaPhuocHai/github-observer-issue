#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import re
import sys
import urllib3
import socket

def post_slack(message, channel):
    url = "https://hooks.slack.com/services/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"
    payload = {'payload' : '{"text" : "' + message + '", "channel": "#' + channel + '"}'}
    requests.post(url, payload, timeout=30)

if len(sys.argv) == 3 and sys.argv[1] == '-m':
    post_slack(sys.argv[2], 'monitor')