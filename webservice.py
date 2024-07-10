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
    print("The user would like to ", method, " ", URI, " using ", version, ".")
else:
    print("Method not supported or recognized")
    

print("Success!")
