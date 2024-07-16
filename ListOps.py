# This module handles all transactions with the wordlist file to enable easy updates.
import gzip
import io
import secrets
import urllib.request
import os

words = []
ready = False
url = "https://cdn.jsdelivr.net/gh/rysto3/wordlist@main/wordlist.txt.gz"


def update_wordlist():
    with urllib.request.urlopen(url) as response:
        with gzip.GzipFile(fileobj=response) as compressed_file:
            with open('wordlist.txt', 'wb') as decompressed_file:
                decompressed_file.write(compressed_file.read())


def init():
    global ready, words
    if not ready:
        if not os.path.exists('wordlist.txt'):
            update_wordlist()
        lines = open('wordlist.txt').read().splitlines()
        words = secrets.SystemRandom().sample(lines, len(lines))
        ready = True
    return words


def fetch_word(num):
    return words[int(num)]

def get_count():
    return len(words)

init()