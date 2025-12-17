class Subscriber:
    def receive(self, topic_name, content):
        print(f"Received message from topic '{topic_name}': {content}")