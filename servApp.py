#!/usr/bin/python
#-*- coding:utf-8 -*-


import webapp
import sys
import random


class aleat(webapp.webApp):
    
    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        nextPage = str (random.randint (0,10000))
        nextUrl = "http://" + "localhost" + ":" + "1234" +'/aleat/' + nextPage
        htmlBody = '<p>Quieres mas?: <a href="' \
            + nextUrl + '">'+ nextPage + "</a></p>"
        return ("302\r\n\r\n","<html><body><h1>" + htmlBody +"</h1></body></html>")
			
        

   

if __name__ == "__main__":
	testAleat = aleat("localhost", 1234)
