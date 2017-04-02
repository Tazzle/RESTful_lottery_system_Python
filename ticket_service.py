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
            ticket_value = ""
            ticket_id = req.get_param("id")
            filename = str(ticket_id) + '.html'
            with open(os.path.join(self.ticket_store, filename), 'r') as ticket:
                for line in ticket:
                    ticket_value += line.replace("<p>", "").replace("</p>","\n")   
            #json.dumps() not using \n           
            resp.body = ('Ticket ' + ticket_id + ':' + '\n\n' + ticket_value)
            resp.status = falcon.HTTP_200
        else:
            resp.body = resp.body = '{"message": "No ID provided"}'
            resp.status = falcon.HTTP_400

    
    def on_post(self, req, resp):
        #generates new ticket ticket
        if req.get_param_as_int("lines"):
            num_of_lines = req.get_param("lines")
            #number of lines should be between 1 and 3
            if(num_of_lines <= 0):
                resp.body = '{"message": "number of lines should be at least 1"}'
                resp.status = falcon.HTTP_400
            else:
                #generate new ticket
                new_ticket = ticket.Ticket(num_of_lines)
                #add new ticket to 'tickets' folder
                filename = str(new_ticket.id) + '.html'
                with open(os.path.join(self.ticket_store, filename), 'wb') as temp_file:
                    for line in new_ticket.ticket_lines:
                        temp_file.write("<p>" + str(line) + "</p>")
                #return new ticket ID with response
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
            num_of_lines = req.get_param("lines")
            f = open(os.path.join(self.ticket_store, ticket_id + ".html"), 'a')
            if(f):
                new_lines = ticket.generate_lines(num_of_lines)
                for line in new_lines:
                   f.write("<p>" + str(line) + "</p>")
                resp.body = json.dumps("Ticket " + ticket_id + " updated with " + num_of_lines + " lines")
                resp.status = falcon.HTTP_200
                f.close()
            else:
                resp.body = json.dumps("File not found")
                resp.status = falcon.HTTP_404            
        else:
            resp.body = json.dumps("Expects 2 parameters; 'ID' and 'lines'")
            resp.status = falcon.HTTP_400
           


        
       
        




    