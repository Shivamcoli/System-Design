class Answer:
    def __init__(self,a_id,q_id):
        self.a_id=a_id
        self.q_id=q_id
        self.comments=[]
        self.votes=0
        self.answer=input("Enter the answer you want to give: ")
        
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