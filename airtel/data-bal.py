#!/usr/bin/env python
import requests
from BeautifulSoup import BeautifulSoup
from mailer import mail

# Message
message = "Error"

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:

    # An authorised request.
    smartBytesPage = s.get('http://122.160.230.125:8080/planupdate/')

    # Use BeautifulSoup to parse the HTML
    parsedHtml = BeautifulSoup(smartBytesPage.text)

    # Extract the part that has the data balance info that we need
    detailsNode = parsedHtml.findAll("div", {"class": "detail"})

    message = detailsNode[0].text

# Print/Mail the percentage
print (message)
