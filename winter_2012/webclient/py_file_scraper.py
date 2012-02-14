"""
This script allows the user to specify a website in which they would like
scrape to find all the links which contain .py at the end and then download
each python file to the current directory via wget.
"""

import requests
import re
import os
from sys import argv
from urlparse import urljoin
from subprocess import call
from pprint import pprint


def scrape(url): 

	python_urls = re.compile(r'href=[",\']?([\w\d\/:\.]*\.py)[",\']+')

	r = requests.get(url)

	results = re.findall(python_urls, r.content)

	results = [urljoin(url,x) for x in results]

	for x in results:
		call(['wget','--progress=dot','-v','--timeout=5','--tries=3',x])

	print "List of files downloaded:"
	pprint([x.split("/")[-1] for x in results])

if __name__ == "__main__":
	if not argv[1]: 
		print "Please determine the website you'd like to download all the .py files from"
	else:
		scrape(argv[1])
