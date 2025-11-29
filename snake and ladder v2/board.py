class Board:
    board=[]
    snake={}
    ladder={}
    def __init__(self):
        size=int(input("Enter the size of the board: "))
        for i in range(size):
            for j in range(size):
                self.board.append(i*size+j+1)
                
        snake_number=int(input("Enter number of snakes: "))
        for i in range(snake_number):
            head=int(input(f"Enter head of snake {i+1}: "))
            tail=int(input(f"Enter tail of snake {i+1}: "))
            self.snake[head]=tail
        ladder_number=int(input("Enter number of ladders: "))
        for i in range(ladder_number):
            start=int(input(f"Enter start of ladder {i+1}: "))
            end=int(input(f"Enter end of ladder {i+1}: "))
            self.ladder[start]=end
                
    