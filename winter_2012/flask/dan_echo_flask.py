"""

Simple echo app which presents a form to submit a message, on the 
next page all messages are listed.

Requires ZODB to store messages and will create the DB if it 
doesn't already exist. 

"""

from flask import Flask, request
from flaskext.zodb import ZODB, Dict, List, Object

# no need for template here - just a constant string
form_page = """<head>
<title>Echo request</title>
</head>
<body>
<form method="POST" action="/">
Message: <input type="text" name="message" size="40">
<input type="submit" value="Submit">
</form>
</body>
</html>
"""

app = Flask(__name__)

app.config['ZODB_STORAGE'] = 'file://app.fs'

db = ZODB(app) 

app.debug = True # development only - remove on production machines

@app.before_request
def set_db_defaults():
    if 'entries' not in db:
        db['entries'] = List()

@app.route('/', methods=['POST', 'GET'])
def form():
	if request.method == 'POST':
		db['entries'].append(request.form['message'])

		return u"""<H1>Hello!</h1> 

		<p>Previous Messages:</p>
		
		%s
		
		<p>Add another message?</p>

		<form method="POST" action="/">
Message: <input type="text" name="message" size="40">
<input type="submit" value="Submit">
</form>


		""" % ('<br>'.join([x for x in db['entries']]))
	
	else:
		return form_page


if __name__ == '__main__':
    app.run()

