import re
from datetime import datetime


current_datetime = datetime.utcnow()
http_date_string = current_datetime.strftime('%a, %d %b %Y %H:%M:%S GMT')

# Verify if the URI is formatted correctly
def check_request_uri(uri):
    no_resource = '*'
    absolute_uri_pattern = '^(http://|https://)'
    absolute_path = '^/([a-zA-Z0-9._~\-%]+)(/[a-zA-Z0-9._~\-%]+)*'

    test_string = "/My name is ..."
    response = re.match(absolute_path, test_string)

    print(response)

    if uri == no_resource:
        return true
    else:
        print("Under construction")

def check_http_version(version):
    print("Under construction")

def bad_request():
    print("HTTP/1.1 400 Bad Request\nDate: ", http_date_string, "\n\n There may be a problem with the request line.")
    # exit()

def OK_response():
    print("HTTP/1.1 200 OK\nDate: ", http_date_string ,"\n\nThank you for using my API :)")
    # exit()

def parse_request_line(request_line):
    parsed_request_line = request_line.split(' ')

    if len(parsed_request_line) == 3:
        method = parsed_request_line[0]
        uri = parsed_request_line[1]
        version = parsed_request_line[2]

        if method in http_methods:
            if check_request_uri(uri):
                if check_http_version(version):
                    print("Request Line looks good")
                    OK_response()
                else:
                    bad_request()
            else:
                bad_request()
        else:
            bad_request()
    else:
        bad_request()


   


# Validation variables

http_methods = ("GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS", "TRACE", "CONNECT")
uris = ["api/v1.0/countries", "/"]
allowed_versions = ["HTTP/0.9", "HTTP/1.0", "HTTP/1.1", "HTTP/1.2", "HTTP/2"]

# Ask for the HTTP Request
request_file = open('enter_request', 'r')
request_file.seek(0)
request_line = request_file.readline()



# Parse request line

parse_request_line(request_line)
