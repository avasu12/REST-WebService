import re


# Verify if the URI is formatted correctly
def checkURI(uri):
    print("Under construction")

# Validation variables

httpMethods = ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS", "TRACE", "CONNECT"]
URIs = ["api/v1.0/countries", "/"]

# Ask for the HTTP Request
requestMessage = input("Enter Request: ")



# Parse request
parsedRequestMessage = requestMessage.split(' ')
method = parsedRequestMessage[0]
URI = parsedRequestMessage[1]
version = parsedRequestMessage[2]

# Validate request

if method in httpMethods:
    if URI in URIs:
        print("HTTP/1.1 200 Success - here's your data.")
    else:
        print("HTTP/1.1 404 Resource not found")
else:
    print("HTTP/1.1 400 Bad Request - your specified method isn't supported")

print("Thank you for using my API :)")
