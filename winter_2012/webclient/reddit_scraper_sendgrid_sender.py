"""
This little script will scrape the subreddit /r/awww and then sort
the posts into the top scoring and then send the contents via SendGrid email smtp
to my girlfriend.

Created as a gift on Valentine's Day :) 

"""
import feedparser
import random
import smtplib
import requests
import sys
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from operator import itemgetter
from credentials import username, password, recipient, pictures_feed, recipient_name


def send_email(content, image_url):
	# Your From email address
	fromEmail = "dalan.miller@gmail.com"
	# Recipient
	toEmail = recipient
	 
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "%s!, Your Awwwwwww Moment of the Day" % (recipient_name)
 	msg['From'] = fromEmail
	msg['To'] = toEmail
	 
	# Create the body of the message (a plain-text and an HTML version).
	# text is your plain-text email
	# html is your html version of the email
	# if the reciever is able to view html emails then only the html
	# email will be displayed
	text = "If you see this, I <3 you"
	html = u"""
	<html>
	  <head>

	  </head>
	  <body>
	    <h2>Haiii %s! (My Boo)</h2>
	    <p>I (Dan) would like you to share with you some the top ten /r/awww posts at this moment!</p>
	    <p>I wrote this is a Valentine's day present for you, and they might be randomly coming into your mailbox in the future to brighten your day :).</p> 

	    <div style="margin-top:25px;margin-bottom:25px;">
	    	
	    	%s

	    </div>

	    <div style="margin-top:15px;margin-bottom:15px;">
	    <h2> Oh yeah, here's a randomly selected picture of us :) </h2>
		
		<img src="%s"/>

	    </div>

	    <div style="margin-top:10px;">
	    	<h3><3,</h3>

	    	<h4>Dan</h4>
	    </div>
	  </body>
	</html>
	""" % (recipient_name, content, image_url)
	# Login credentials


	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')
	 
	# Attach parts into message container.
	msg.attach(part1)
	msg.attach(part2)
	 
	# Open a connection to the SendGrid mail server
	s = smtplib.SMTP('smtp.sendgrid.net', 587)
	 
	# Authenticate
	s.login(username, password)
	 
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.sendmail(fromEmail, toEmail, msg.as_string())
	 
	print html
	s.quit()


if __name__ == '__main__':
	r = requests.get('http://www.reddit.com/r/aww.json')

	r = json.loads(r.content)['data']['children']

	top_ten_posts = [x['data'] for x in r]

	sorted_top = sorted(top_ten_posts, key=itemgetter('score'), reverse=True)[:10]

	trs = ""
	for x in sorted_top:
		trs += "<tr>"
		trs += '<td><a href="%s">%s</a></td>' % (''.join(['http://reddit.com',x['permalink']]),x['title'][:65])
		trs += '<td><a href="%s">%s</a></td>' % (x['url'], x['url'][:30])
		trs += '<td>%s</td>' % (x['score'])
		trs += "</tr>"

	html = """<table class="table">
	<thead>
		<tr>
		<th>Post Title</th>
		<th>Link</th>
		<th>Score</th>
		</tr>
	</thead>
	<tbody>
	%s
	</tbody>
	</table>""" % (trs)

	feed = feedparser.parse(pictures_feed)

	image_url = random.choice([x['media_content'][0]['url'] for x in feed['entries']])

	send_email(html, image_url)