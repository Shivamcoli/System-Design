from topic import Topic
from subscriber import Subscriber
from message import Message

class Manager:
    def __init__(self):
        self.topics = {}
        
    def create_topic(self, topic_name):
        if topic_name not in self.topics:
            self.topics[topic_name] = Topic(topic_name)
            
    def subscribe(self, topic_name, subscriber):
        if topic_name in self.topics:
            self.topics[topic_name].add_subscriber(subscriber)
            
    def unsubscribe(self, topic_name, subscriber):
        if topic_name in self.topics:
            self.topics[topic_name].remove_subscriber(subscriber)
            
    def publish(self, topic_name, content):
        if topic_name in self.topics:
            topic = self.topics[topic_name]
            for subscriber in topic.list_of_subscribers:
                subscriber.receive(topic_name, content)
        else:
            print(f"Topic '{topic_name}' does not exist.")
                
                
if __name__ == "__main__":
    manager = Manager()
    
    # Create Topics
    manager.create_topic("Sports")
    manager.create_topic("Technology")
    
    # Create Subscribers
    subscriber1 = Subscriber()
    subscriber2 = Subscriber()
    
    # Subscribe to Topics
    manager.subscribe("Sports", subscriber1)
    manager.subscribe("Technology", subscriber2)
    
    # Publish Messages
    message1 = Message()
    manager.publish(message1.topic_name, message1.content)
    
    message2 = Message()
    manager.publish(message2.topic_name, message2.content)