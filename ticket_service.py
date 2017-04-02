import falcon
import json
import os
import random

class TicketResource(object):
    
    def __init__(self):
        os.makedirs('tickets')
        #ticket_store = '/Users/$UNAME/Desktop/lottery/tickets'
        

    def on_get(self, req, resp):
        if req.get_param("id"):
            resp.body = resp.body = '{"message": "ID provided"}'
            resp.status = falcon.HTTP_200
        else:
            resp.body = resp.body = '{"message": "No ID provided"}'
            resp.status = falcon.HTTP_400

    
    def on_post(self, req, resp):
        if req.get_param("lines"):
            resp.body = '{"message": "No. of lines provided"}'
            resp.status = falcon.HTTP_200
        else:
            resp.body = '{"message": "number of lines not provided"}'
            resp.status = falcon.HTTP_400
        
       
        




    