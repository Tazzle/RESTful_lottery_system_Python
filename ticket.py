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

def get_ticket_from_xml(id):
    ticket_lines = []
    tree = ET.ElementTree(file="tickets.xml")
    tickets = tree.getroot()
    for ticket in tickets:
        if ticket.find("ticket_id").text == id:
            ticket_lines = [line.text for line in ticket.iter("ticket_line")]
            return ticket_lines
            break

def modify_ticket_in_xml(id, num_of_lines):
    new_lines = generate_lines(num_of_lines)
    tree = ET.ElementTree(file="tickets.xml")
    tickets = tree.getroot()
    for ticket in tickets:
        if ticket.find("ticket_id").text == id:
            for line in new_lines:             
                child_line = ET.SubElement(ticket, 'ticket_line')
                child_line.text = str(line)   
                child_line.tail = '\n'    
            ET.ElementTree(tickets).write("tickets.xml") 
            break     

def delete_ticket_in_xml(id):
    tree = ET.ElementTree(file="tickets.xml")
    tickets = tree.getroot()
    for ticket in list(tickets):
        if ticket.find("ticket_id").text == id:
            tickets.remove(ticket)
            ET.ElementTree(tickets).write("tickets.xml")
            break
        

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

    
        




        


