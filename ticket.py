import random
import uuid
import xml.etree.ElementTree as ET

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


    def add_ticket_to_xml(self):
        tree = ET.ElementTree(file = "tickets.xml")
        xmlRoot = tree.getroot()
        child = ET.SubElement(xmlRoot, "ticket")               
        child_id = ET.SubElement(child, 'ticket_id')
        child_id.text = str(self.id)  
        child_id.tail = '\n'           
        for line in self.ticket_lines:
            child_line = ET.SubElement(child, 'ticket_line')
            child_line.text = str(line)   
            child_line.tail = '\n'                
        ET.ElementTree(xmlRoot).write("tickets.xml")




        


