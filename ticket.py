import random
import uuid

def generate_lines(num_of_lines):
    addendum = []
    for x in range(0,num_of_lines):
        #generate three lines with three random numbers between 1-3
        line = [random.randrange(1,4) for x in range(0,3)]
        addendum.append(line)
    return addendum

class Ticket():


    def __init__(self, lines):
        self.ticket_lines = []
        self.id = uuid.uuid4()
        for x in range(0,lines):
            #generate three lines with three random numbers between 1-3
            line = [random.randrange(1,4) for x in range(0,3)]
            self.ticket_lines.append(line)



        


