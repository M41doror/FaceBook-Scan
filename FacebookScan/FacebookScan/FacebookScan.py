#!/usr/bin/python
import multiprocessing
import subprocess
from argparse import ArgumentParser
import sys

ACCESS_TOKEN= '' # provide a valid facebook graphs token for access
FB_GRAPH27 = "https://graph.facebook.com/v2.7/"

def retreive_id(url):
    '''Queries the Facebook API with a Facebook profile url to reteive an id'''
    params= {'id': USER_URL,'access_token': ACCESS_TOKEN}
    r = requests.get(FB_GRAPH27, params=params)
    return r.json().get('id')

def print_id(url):
    '''Queries the Facebook API for the specific group ID, and populates the
        results dictionary with the Group ID, User Name, and User ID'''


def print_logo():
    print(".-. .-. .-. .-. .-. .-. .-. . .   .-. .-. .-. . .")
    print("|-  |-| |   |-  |(  | | | | |<    `-. |   |-| |\|")
    print("'   ` ' `-' `-' `-' `-' `-' ' `   `-' `-' ` ' ' `")

def main():
    
    parser = ArgumentParser()
    parser.add_argument("-url", dest="url", help="Provide a url for a facebook profile to scan.")
    parser.add_argument("-id", dest="id", help="Provide an id for a facebook profile to scan.")
    parser.add_argument("--printid", dest="printid",  action="store_true", help="Retreive and print the id of a provided facebook url.")
    parser.add_argument("--printurl", dest="printurl",  action="store_true", help="Retreive and print the url of a provided facebook id.")
    parser.add_argument("--quiet", dest="quiet",  action="store_true", help="Supress banner and headers to limit to comma dilimeted results only.")

    arguments = parser.parse_args()

    if len(sys.argv) == 1:
        parser.error("No arguments given.  Please specify a profile (url or id) as well as the type of queries to generate.")
        sys.exit()

    if arguments.quiet is not True:
        print_logo()

    if arguments.id is None and arguments.url is None:
        parser.error("No facebook id or url specified, please supply a url or id to continue.")
        sys.exit()

    if arguments.id is not None and arguments.quiet is not True:
        print("Provided id: {}".format(arguments.id))

    if arguments.url is not None and arguments.quiet is not True:
        print("Provided url: {}".format(arguments.url))

    if arguments.printid is True:
        print("Facebook profile id is:")

    if arguments.printurl is True:
        print("Facebook url is:")

if __name__ == "__main__":
    main()