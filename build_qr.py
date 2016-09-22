#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals
from staticjinja import make_site

import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-i',
                    '--id',
                    help='Accepts id of the workshop attendee',
                    required=True)

args = vars(parser.parse_args())


def get_attendee_data():
    import csv
    with open('workshop.csv') as csvfile:
        pycon_india_worskhops = csv.reader(csvfile)
        attendee_id = int(args["id"])
        attendees = []
        for linenumber, row in enumerate(pycon_india_worskhops):
            if linenumber >= attendee_id:
                if linenumber > 16:
                    break
                attendee = {'name': str(row[0]).title(), 'id': linenumber}
                attendees.append(attendee)
        return attendees

if __name__ == "__main__":
    site = make_site(contexts=[
        ('index.html', {
            "attendees": get_attendee_data()
        })
    ])
    # enable automatic reloading
    site.render(use_reloader=True)
