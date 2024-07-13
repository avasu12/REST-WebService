import re


# Validation variables

httpMethods = ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS", "TRACE", "CONNECT"]

# Ask for the HTTP Request
requestMessage = input("Enter Request: ")

print(requestMessage)

# Parse request
parsedRequestMessage = requestMessage.split(' ')
method = parsedRequestMessage[0]
URI = parsedRequestMessage[1]
version = parsedRequestMessage[2]

# Validate request

if method in httpMethods:
    print("HTTP/1.1 501 This API isn't fully developed yet - check in later!")
else:
    print("HTTP/1.1 400 Bad Request - your specified method isn't supported")
    

print("End of program")
