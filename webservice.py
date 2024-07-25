import re
from datetime import datetime


# Verify if the URI is formatted correctly
def checkURI(uri):
    print("Under construction")

# Validation variables

http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS", "TRACE", "CONNECT"]
uris = ["api/v1.0/countries", "/"]
allowed_versions = ["HTTP/0.9", "HTTP/1.0", "HTTP/1.1", "HTTP/1.2", "HTTP/2"]

# Ask for the HTTP Request
request_file = open('enter_request', 'r')
request_message = request_file.read()
print(request_message)

'''

# Parse request
parsed_request_message = request_message.split(' ')
method = parsed_request_message[0]
uri = parsed_request_message[1]
version = parsed_request_message[2]

# Validate request

if method in http_methods:
    if uri in uris:
        if version in allowed_versions:
            print("HTTP/1.1 200 Success - here's your data.")
        else:
            print("HTTP/1.1 400 Bad request - your protocol & version might be incorrect")
    else:
        print("HTTP/1.1 404 Resource not found")
else:
    print("HTTP/1.1 405 Method not allowed - your specified method isn't supported")


text = open('api/v1.0/countries', 'r')

print(text.read())
'''

pattern = '...$'

test_string = "My name is ..."
response = re.match(pattern, test_string)

print(response)


current_datetime = datetime.utcnow()
http_date_string = current_datetime.strftime('%a, %d %b %Y %H:%M:%S GMT')

print("HTTP/1.1 200 OK\nDate: ", http_date_string ,"\n\nThank you for using my API :)")
