#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import requests
import re
import HTMLParser
from lxml import html
from lxml import etree
import json
from bs4 import BeautifulSoup
import schedule
import time
import Cookie
import html2text

from log import *
from slack import *

def job ():
  last_id = read_last_id()

  xpath = '//ul[@class="js-navigation-container js-active-navigation-container"]/li'
  page = requests.get("https://github.com/awesome-jobs/vietnam/issues", timeout=30)

  tree = html.fromstring(page.text)
  articles = tree.xpath(xpath)
  post_slack ('title', 'monitor')

  articles.reverse()
  for article in articles:
    title = article[0][4][0].text
    link  = "https://github.com" + article[0][4][0].attrib.get("href")
    article_id = int(article[0][4][0].attrib.get("href").split('/')[-1])

    if article_id > last_id:
      last_id = article_id
      process_job(title, link)

  write_last_id(last_id)


def process_job(title, link):
  if title.lower().find("ios") != -1:
    post_slack_job(title, link)
    return None

  if title.lower().find("mobile") != -1:
    post_slack_job(title, link)
    return None

  if title.lower().find("project manager") != -1:
    post_slack_job(title, link)
    return None

  if title.lower().find("team lead") != -1:
    post_slack_job(title, link)
    return None

  if title.lower().find("fullstack") != -1:
    post_slack_job(title, link)
    return None

  if title.lower().find("full stack") != -1:
    post_slack_job(title, link)
    return None

  if title.lower().find("full-stack") != -1:
    post_slack_job(title, link)
    return None


def post_slack_job(title, link):
  content = get_des_job(link)
  attachments = {'color' : '#36a64f', 'title' : title.strip(), 'title_link' : link, 'text' : content, 'mrkdwn_in': ["text"]}
  url = "https://hooks.slack.com/services/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"
  payload = {'payload' : '{"text" : "[awesome-jobs/vietnam]", "channel": "#monitor' + '", "attachments": [' + json.dumps(attachments) + ']}'}
  requests.post(url, payload, timeout=30)

def read_last_id():
  fp = open('id.txt')
  lines = fp.readline()
  fp.close()
  return int(lines)

def write_last_id(number):
  fp = open('id.txt', 'w')
  fp.write(str(number))
  fp.close()
  return None

def get_des_job(link):
  xpath = '//div[@class="edit-comment-hide"]'

  page = requests.get(link, timeout=30)
  tree = html.fromstring(page.text)
  article = tree.xpath(xpath)[0]
  raw_html = unicode(etree.tostring(article, pretty_print=True, encoding='UTF-8'),'UTF-8')
  return html2text.html2text(raw_html)

def schedule_job():
  post_slack ('start crawler', 'monitor')
  job()

  schedule.every(12).hour.do(job)
  while True:
    schedule.run_pending()
    time.sleep(10)

schedule_job()