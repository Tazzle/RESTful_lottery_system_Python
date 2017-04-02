import falcon
import ticket_service

api = application = falcon.API()

ticket = ticket_service.TicketResource()

api.add_route('/ticket', ticket)