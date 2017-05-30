

# Web application file

def application(environ, start_response):
	# For testing
	data = environ['QUERY_STRING']
	data = '\n'.join(data.split('&'))
	
	response_headers = [
		('Content-type', 'text/plain'),
		('Content-Lenghth', str(len(data)))
	]
	
	status = '200 OK'
	
	start_response(status, response_headers)
	return iter([data])