import falcon
import json
import os
import errno
import random
import ticket

class TicketResource(object):
    
    def __init__(self):
        self.ticket_store = '/Users/$UNAME/GitHub_Repos/lottery/tickets/'
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
                #generate new ticket
                new_ticket = ticket.Ticket(num_of_lines)
                #add new ticket to 'tickets' folder
                filename = str(new_ticket.id) + '.html'
                with open(os.path.join(self.ticket_store, filename), 'wb') as temp_file:
                    for line in new_ticket.ticket_lines:
                        temp_file.write("<body>" + str(line) + "</body>")
                #return new ticket ID with response
                resp.body = json.dumps("New ticket generated with " + str(num_of_lines) + " lines, ticket ID = " + str(new_ticket.id))
                resp.status = falcon.HTTP_200
        else:
            resp.body = '{"message": "number of lines not provided"}'
            resp.status = falcon.HTTP_400

        
       
        




    