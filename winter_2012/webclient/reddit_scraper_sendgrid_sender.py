"""
This little script will scrape the subreddit /r/awww and then sort
the posts into the top scoring and then send the contents via SendGrid email smtp
to my girlfriend.

Created as a gift on Valentine's Day :) 

"""


import smtplib
import requests
import sys
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from operator import itemgetter

def send_email(content):
	# Your From email address
	fromEmail = "dalan.miller@gmail.com.com"
	# Recipient
	toEmail = "dalan.miller@gmail.com"
	 
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Awwwwwww Moment of the Day"
	msg['From'] = fromEmail
	msg['To'] = toEmail
	 
	# Create the body of the message (a plain-text and an HTML version).
	# text is your plain-text email
	# html is your html version of the email
	# if the reciever is able to view html emails then only the html
	# email will be displayed
	text = "If you see this, I <3 you"
	html = """\
	<html>
	  <head></head>
	  <body>
	    <p>Haiii Karthika!</p>
	    <p>I (Dan) would like you to see these top ten /r/awww posts today! 

	    <div style="margin-top:25px;>
	    	
	    	%s

	    </div>

	    <div style="margin-top:10px;">
	    	<p><3,</p>

	    	<p>Dan</p>
	    </div>
	  </body>
	</html>
	""" % (content)
	# Login credentials
	from credentials import username, password


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
	 
	s.quit()


if __name__ == '__main__':
	r = requests.get('http://www.reddit.com/r/aww.json')

	r = json.loads(r.content)['data']['children']

	top_ten_posts = [x['data'] for x in r]

	sorted_top = sorted(top_ten_posts, key=itemgetter('score'), reverse=True)[:10]

	trs = ""
	for x in sorted_top:
		trs += "<tr>"
		trs += '<td><a href="%s">%s</a></td>' % (''.join(['http://reddit.com',x['permalink']]),x['title'][:50])
		trs += '<td><a href="%s">%s</a></td>' % (x['url'], x['url'])
		trs += '<td>%s</td>' % (x['score'])
		trs += "</tr>"

	html = """<table>
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


	print html

	#send_email(html)