#!/usr/bin/python

import requests
import sys 
import json

class VtmTrigger(object):

    def __init__(self, trigger=None):
        super(VtmTrigger, self).__init__()

def main():
    trigger = VtmTrigger()

    event = sys.argv[1][len("--eventtype="):]
    details = sys.argv[2].split("\t", 3)

    level = details[0]
    config = details[1] if len(details) >= 2 else ""
    trigger = details[2] if len(details) >= 3 else ""
    message = details[3] if len(details) >= 4 else ""

    payload = { "event": event, "level": level, "config": config } 

    if "/" in trigger:
        payload["additional"] = trigger
        trigger, message = message.split("\t", 1)

    payload["trigger"] = trigger
    payload["message"] = message

    print payload

if __name__ == "__main__":
    main()

