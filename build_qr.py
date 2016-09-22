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
                if linenumber > attendee_id + 15:
                    break
                attendee = {'name': str(row[0]).title(), 'id': linenumber}
                # attendee = {'name': str(row[0]).title(), 'id': 1}
                attendees.append(attendee)
        print(len(attendees))
        return attendees[0:][::2], attendees[1:][::2]

if __name__ == "__main__":
    attendees_group_1, attendees_group_2 = get_attendee_data()
    site = make_site(contexts=[
        ('index.html', {
            "attendees_group_1": attendees_group_1,
            "attendees_group_2": attendees_group_2
        })
    ])
    # enable automatic reloading
    site.render(use_reloader=True)
