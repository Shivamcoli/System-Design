class Topic:
    
    def __init__(self, name):
        self.name = name
        self.list_of_subscribers = []
        
    def add_subscriber(self, subscriber):
        self.list_of_subscribers.append(subscriber)
        
    def remove_subscriber(self, subscriber):
        self.list_of_subscribers.remove(subscriber)