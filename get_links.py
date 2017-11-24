from __future__ import print_function
import os, sys


DOCS_DIR = 'docs/'

SWAGGER_UI_URL = 'https://generator.swagger.io/?url='
HOST = 'https://raw.githubusercontent.com/'
USER = 'bdmbdsm/'
REPO_NAME = 'openprocurement-swagger-docs/'
BRANCH = 'master/'

PATH = 'docs/'


def get_link_for_filename(filename):
    return ''.join((
        SWAGGER_UI_URL, HOST, USER, REPO_NAME, BRANCH, PATH, filename
    ))


def generate_links():
    files = [f for f in os.listdir(DOCS_DIR) if os.path.isfile(os.path.join(DOCS_DIR, f))]
    links = ''

    for filename in files:
        links +=\
            ''.join((
                '[', filename, '](', get_link_for_filename(filename), ')\n\n'
            ))

    return links


if __name__ == '__main__':
    sys.exit(print(generate_links()))

