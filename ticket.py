import random
import uuid

class Ticket():

    ticket_lines = []
    id = 0

    def __init__(self, lines):
        ticket_lines = self.ticket_lines
        self.id = uuid.uuid4()
        for x in range(0,lines):
            #generate three lines with three random numbers between 1-3
            line = [random.randrange(1,4) for x in range(0,3)]
            ticket_lines.append(line)



        


