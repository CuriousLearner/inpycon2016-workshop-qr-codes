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


def get_attendee_name():
    import csv
    with open('workshop.csv') as csvfile:
        pycon_india_worskhops = csv.reader(csvfile)
        attendee_id = int(args["id"])
        for linenumber, row in enumerate(pycon_india_worskhops):
            if linenumber == attendee_id:
                print row[0]
                return row[0]


if __name__ == "__main__":
    site = make_site(contexts=[
        ('index.html', {
            "id": args["id"],
            "name": get_attendee_name()
        })
    ])
    # enable automatic reloading
    site.render(use_reloader=True)
