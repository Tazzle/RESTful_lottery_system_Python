import xml.etree.ElementTree as ET
import random

def get_ticket(id):
    ticket_lines = []
    tree = ET.ElementTree(file="tickets.xml")
    tickets = tree.getroot()
    for ticket in tickets:
        if ticket.find("ticket_id").text == id:
            ticket_lines = [line.text for line in ticket.iter("ticket_line")]
            return ticket_lines
            break

def modify_ticket(id, num_of_lines):
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

def generate_lines(num_of_lines):
    addendum = []
    for x in range(0,num_of_lines):
        #generate three lines with three random numbers between 1-3
        line = [random.randrange(1,4) for x in range(0,3)]
        addendum.append(line)
    return addendum 

def delete_ticket(id):
    tree = ET.ElementTree(file="tickets.xml")
    tickets = tree.getroot()
    for ticket in list(tickets):
        if ticket.find("ticket_id").text == id:
            tickets.remove(ticket)
            ET.ElementTree(tickets).write("tickets.xml")
            break

    