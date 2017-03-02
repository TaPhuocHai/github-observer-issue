#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib, urllib, urllib2, json, io, codecs, string, re, os, codecs, sys, requests
import unicodedata, re

def printLog (level,message, isPrintTerminal):
    try:
        m = str(int(level) * 4 * ' ') + message
        if isPrintTerminal:
            print m.encode('utf-8')

        logFile.write(m + '\n')
    except Exception as error:
        return None


def cleanLog (filename):
    logFilePath = os.path.join('tmp',filename)
    if os.path.isfile(logFilePath):
        os.remove (logFilePath)


def openLog (filename):
    global logFile
    logFilePath = os.path.join('tmp',filename)
    logFile = codecs.open(logFilePath, "a+", "utf-8")


def closeLog ():
    logFile.close()