class Question:
    
    def __init__(self,q_id):
        self.q_id=q_id
        self.comments=[]
        self.votes=0
        self.question=input("Enter the question you want to ask: ")
        
        
    def add_comment(self):
        self.comment=input("Enter your comment: ")
        self.comments.append(self.comment)
        
    def add_vote(self):
        while True:
            self.vote=int(input("Enter your vote (1 or -1): "))
            if self.vote==1:
                self.votes+=1
                break
            elif self.vote==-1:
                self.votes-=1
                break
            else:
                print("Invalid vote")