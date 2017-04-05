import falcon
import json
import os
import errno
import random
import ticket
import ticket_manager

#use HTTPie (command line HTTP client) to query

class TicketResource(object):
      
    #http GET localhost:8000/ticket?id=64d9caba-1428-4c6f-8f80-8a3b7253f5d0
    def on_get(self, req, resp):
        if req.get_param("id"):
            ticket_id = req.get_param("id")
            ticket_value = ticket_manager.get_ticket(ticket_id)        
            resp.body = ('Ticket ' + ticket_id + ':' + '\n\n' + str(ticket_value))
            resp.status = falcon.HTTP_200
        else:
            resp.body = resp.body = '{"message": "No ID provided"}'
            resp.status = falcon.HTTP_400

    #http POST localhost:8000/ticket?lines=6
    def on_post(self, req, resp):
        if req.get_param_as_int("lines"):
            num_of_lines = req.get_param_as_int("lines")
            if(num_of_lines <= 0):
                resp.body = '{"message": "number of lines should be at least 1"}'
                resp.status = falcon.HTTP_400
            else:
                new_ticket = ticket.Ticket(num_of_lines)
                resp.body = json.dumps("New ticket generated with " + str(num_of_lines) + " lines, ticket ID = " + str(new_ticket.id))
                resp.status = falcon.HTTP_200
        else:
            resp.body = json.dumps("Expects 1 parameter; 'lines")
            resp.status = falcon.HTTP_400

    #test 
    #when working with multiple parameters put url into quotes otherwise only recognises first argument
    #in the shell the ampersand is used for forking processes so does not behave as expected    
    #http PUT "localhost:8000/ticket?lines=3&id=10e477e2-1458-447c-8e83-80c37f024225"        
    def on_put(self, req, resp):
        if req.get_param("id") and req.get_param("lines"):
            ticket_id = req.get_param("id")
            num_of_lines = req.get_param_as_int("lines")
            ticket_manager.modify_ticket(ticket_id, num_of_lines)
            resp.body = json.dumps("Ticket " + ticket_id + " updated with " + str(num_of_lines) + " lines")
            resp.status = falcon.HTTP_200          
        else:
            resp.body = json.dumps("Expects 2 parameters; 'ID' and 'lines'")
            resp.status = falcon.HTTP_400

    #http DELETE localhost:8000/ticket?id=64d9caba-1428-4c6f-8f80-8a3b7253f5d0
    def on_delete(self, req, resp):
        if req.get_param("id"):
            ticket_id = req.get_param("id")
            ticket_manager.delete_ticket(ticket_id)
            resp.body = json.dumps("Ticket " + ticket_id + " deleted")
            resp.status = falcon.HTTP_200 
        else:
            resp.body = resp.body = '{"message": "No ID provided"}'
            resp.status = falcon.HTTP_400

           


        
       
        




    