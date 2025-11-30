class PaymentProcessor:
    def pay(self,vehicle_type):
        if vehicle_type == 1:
            amount = 10  # Small vehicle parking fee
        elif vehicle_type == 2:
            amount = 20  # Medium vehicle parking fee
        elif vehicle_type == 3:
            amount = 30  # Large vehicle parking fee
        else:
            raise ValueError("Invalid vehicle type")

        print(f"Processing payment of ${amount} for vehicle type {vehicle_type}.")
        # Here you would integrate with a real payment gateway
        print("Payment successful!")