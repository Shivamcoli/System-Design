class Board:
    def __init__ (self,size,snake,ladder,board):
        self.size = size
        self.board = board
        self.snake=snake
        self.ladder=ladder
        
    def is_snake_head(self,position):
        if position in self.snake:
            return self.snake[position]
        else:
            return -1
        
    def is_ladder_base(self,position):
        if position in self.ladder:
            return self.ladder[position]
        else:
            return -1