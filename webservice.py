import re


# Verify if the URI is formatted correctly
def checkURI(uri):
    print("Under construction")

# Validation variables

httpMethods = ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS", "TRACE", "CONNECT"]
URIs = ["api/v1.0/countries", "/"]
allowedVersions = ["HTTP/0.9", "HTTP/1.0", "HTTP/1.1", "HTTP/1.2", "HTTP/2"]

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
        if version in allowedVersions:
            print("HTTP/1.1 200 Success - here's your data.")
        else:
            print("HTTP/1.1 400 Bad request - your protocol & version might be incorrect")
    else:
        print("HTTP/1.1 404 Resource not found")
else:
    print("HTTP/1.1 405 Method not allowed - your specified method isn't supported")

print("Thank you for using my API :)")
