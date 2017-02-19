#!/usr/bin/python
import multiprocessing
import subprocess
from argparse import ArgumentParser
import sys
import json
import urllib2
import re

def print_id(url):
    '''Queries the Facebook API for the specific group ID, and populates the
        results dictionary with the Group ID, User Name, and User ID'''


def print_logo():
    print(".-. .-. .-. .-. .-. .-. .-. . .   .-. .-. .-. . .")
    print("|-  |-| |   |-  |(  | | | | |<    `-. |   |-| |\|")
    print("'   ` ' `-' `-' `-' `-' `-' ' `   `-' `-' ` ' ' `")

def main():
    print_logo()
    
    parser = ArgumentParser()
    parser.add_argument("-url", dest="url", help="Provide a url for a facebook profile to scan.")
    parser.add_argument("-id", dest="id", help="Provide an id for a facebook profile to scan.")
    parser.add_argument("--printid", dest="printid",  action="store_true", help="Retreive and print the id of a provided facebook url")

    arguments = parser.parse_args()

    if len(sys.argv) == 1:
        parser.error("No arguments given.  Please specify a profile (url or id) as well as the type of queries to generate.")
        sys.exit()

    if arguments.id is None and arguments.url is None:
        print("No facebook id or url specified, please supply a url")

    if arguments.url is not None:
        print("Profile url is: {}".format(arguments.url))

    if arguments.id is True:
        print("Facebook profile id is:")

if __name__ == "__main__":
    main()