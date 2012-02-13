import requests 
import os
import re
import json 
import sys
from urlparse import urljoin
from subprocess import call

base_github_api_url = "https://api.github.com/repos"
python_urls = re.compile(r'href=[",\']?([\w\d\/:\.]*\.py)[",\']+')


def scrape_github():

	uw_python_github_url = 'https://api.github.com/repos/jon-jacky/uw_python/git/blobs/5407f36f9a88dcb8c1bf5cea60e89da48eb6b96f'

	url = 'http://jon-jacky.github.com/uw_python/winter_2012/'

	r = requests.get(uw_python_github_url,headers={'Accept':'application/vnd.github-blob.raw'})

	if r.status_code != 200:
		print "Bad request, please try again"
		sys.exit(r.status_code)

	results = [urljoin(url,x) for x in re.findall(python_urls, r.content)]

	print results

	for x in results:
		call(['wget','--progress=dot','--timeout=5','--tries=3',x])

	print "List of files downloaded:"
	pprint([x.split("/")[-1] for x in results])

if __name__ == "__main__":
	
	print "Commence scouring uw_python winter_2012 .py files...."
		
	scrape_github()

	print "Github scrape for python files finished."