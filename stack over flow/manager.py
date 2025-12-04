from question import Question
from answer import Answer

class Manager:
    def __init__(self):
        self.questions = []
        self.answers = {}
        self.q_id=1
        self.a_id=1    
    def add_question(self):
        question = Question(self.q_id)
        self.questions.append(question)
        self.answers[self.q_id]=[]
        self.q_id+=1
        return question
    
    def add_answer(self):
        while True:
            q_id = int(input("Enter the question id: "))
            for question in self.questions:
                if question.q_id == q_id:
                    answer = Answer(self.a_id,self.q_id)
                    self.answers[q_id].append(answer)
                    self.a_id+=1
                    return answer
            print("Invalid question id, please try again")
                

        
    
    def add_comment_to_question(self):
        while True:
            q_id = int(input("Enter the question id: "))
            for question in self.questions:
                if question.q_id == q_id:
                    question.add_comment()
                    return
            print("Invalid question id, please try again")
            
    def add_comment_to_answer(self):
        while True:
            q_id = int(input("Enter the question id: "))
            a_id = int(input("Enter the answer id: "))
            for q_id in self.answers:
                answer_list = self.answers[q_id]
                for answer in answer_list:
                    if answer.a_id == a_id:
                        answer.add_comment()
                        return
                print("Invalid answer id, please try again")
                continue
            print("Invalid question  please try again")
            
    def add_vote_to_question(self):
        while True:
            q_id = int(input("Enter the question id: "))
            for question in self.questions:
                if question.q_id == q_id:
                    question.add_vote()
                    return
            print("Invalid question id, please try again")
            
    def add_vote_to_answer(self):
        while True:
            q_id = int(input("Enter the question id: "))
            a_id = int(input("Enter the answer id: "))
            for q_id in self.answers:
                answer_list = self.answers[q_id]
                for answer in answer_list:
                    if answer.a_id == a_id:
                        answer.add_vote()
                        return
                print("Invalid answer id, please try again")
                continue
            print("Invalid question  please try again")
            
            
    def print_all_questions_answers_and_commnets(self):
        for question in self.questions:
            print("------------------------------------------------")
            print(f"Q-ID: {question.q_id}")
            print(f"Question: {question.question}")
            print(f"Comments: {question.comments}")
            print(f"Votes: {question.votes}")
            print("  --- Answers ---")
            
            # FIX 4: Retrieve only answers related to THIS question
            # .get(key, []) returns an empty list if no answers exist
            related_answers = self.answers.get(question.q_id, [])
            
            if not related_answers:
                print("  No answers yet.")
            
            for answer in related_answers:
                print(f"  [A-ID: {answer.a_id}] Answer: {answer.answer}")
                print(f"  Comments: {answer.comments}")
                print(f"  Votes: {answer.votes}")
                print("  ...............")
            print("------------------------------------------------")
            
if __name__ == "__main__":
    manager = Manager()
    while True:
        x=int(input("1.Add question 2.Add answer 3.Add comment to question 4.Add comment to answer 5.Add vote to question 6.Add vote to answer 7.Print all questions answers and comments 8.Exit\n"))
        if x ==1:
            manager.add_question()
        elif x==2:
            manager.add_answer()
        elif x==3:
            manager.add_comment_to_question()
        elif x==4:
            manager.add_comment_to_answer()
        elif x==5:
            manager.add_vote_to_question()
        elif x==6:
            manager.add_vote_to_answer()
        elif x==7:
            manager.print_all_questions_answers_and_commnets()
            
        elif x==8:
            break
        else:
            print("Invalid choice")