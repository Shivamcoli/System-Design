class Payment:
    def make_payment(self,vehicle_type):
        if vehicle_type==1:
            print("Payment of $10 made for Small vehicle")
        elif vehicle_type==2:
            print("Payment of $20 made for Medium vehicle")
        elif vehicle_type==3:
            print("Payment of $30 made for Large vehicle")
            
        print("Payment successful. Thank you!")
