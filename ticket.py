import uuid
import xml.etree.ElementTree as ET
import ticket_manager

class Ticket():

    def __init__(self, lines):
        self.ticket_lines = ticket_manager.generate_lines(lines)
        self.id = uuid.uuid4()
        self.add_ticket()


    def add_ticket(self):
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


   

    
        




        


