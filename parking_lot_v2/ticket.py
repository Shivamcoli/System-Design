class Ticket:
    ticket_counter=1
    def __init__(self,spot_id):
        self.ticket_id=Ticket.ticket_counter
        Ticket.ticket_counter+=1
        self.spot_id=spot_id
        
    def get_ticket_id(self):
        return self.ticket_id
    
    def get_spot_id(self):
        return self.spot_id