import falcon
import json
import os
import errno
import random
import ticket

class TicketResource(object):
    
    def __init__(self):
        ticket_store = '/Users/$UNAME/Desktop/lottery/tickets/'
        #create folder if not already exists
        try:
            os.makedirs('tickets')
        #ignore error related to folder already existing
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        
        
    def on_get(self, req, resp):
        if req.get_param("id"):
            resp.body = resp.body = '{"message": "ID provided"}'
            resp.status = falcon.HTTP_200
        else:
            resp.body = resp.body = '{"message": "No ID provided"}'
            resp.status = falcon.HTTP_400

    
    def on_post(self, req, resp):
        #generates ticket
        #todo: create on_put to modify existing ticket
        if req.get_param("lines"):
            num_of_lines = int(req.get_param("lines"))
            #number of lines should be between 1 and 3
            if(num_of_lines <= 0 or num_of_lines > 3):
                resp.body = '{"message": "number of lines should be between 1 and 3"}'
                resp.status = falcon.HTTP_400
            else:
                new_ticket = ticket.Ticket(num_of_lines)
                #test
                print new_ticket.ticket_lines
                resp.body = '{"message": ticket}'
                resp.status = falcon.HTTP_200
        else:
            resp.body = '{"message": "number of lines not provided"}'
            resp.status = falcon.HTTP_400
        
       
        




    