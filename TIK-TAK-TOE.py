class board:
    def __init__(self):
        self.board=[" " for i in range(1,10)]
    def wrap(self):
        for i in range(0,9,3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i<6:
                print("---------")
    def placeX(self):
        placex=0 
        while not (placex >0 and placex<=9):
            placex=int(input("gamer1: "))        
        return placex
    def placeO(self):
        placeo=0
        while not( placeo>0 and placeo<=9):
            placeo=int(input("gamer2: "))     
        return placeo
    def show(self):
      x=0
      self.wrap()
      
      for i in range(5) :
            px=self.placeX()
            while not (self.board[px-1]!="X" and self.board[px-1]!="O"):
                px=self.placeX()
            self.board[px-1]="X"
            self.wrap()
            if (self.board[0]=="X" and self.board[1]=="X" and self.board[2]=="X") or (self.board[3]=="X" and self.board[4]=="X" and self.board[5]=="X") or (self.board[6]=="X" and self.board[7]=="X" and self.board[8]=="X")or (self.board[0]=="X" and self.board[3]=="X" and self.board[6]=="X") or (self.board[1]=="X" and self.board[4]=="X" and self.board[7]=="X") or (self.board[2]=="X" and self.board[5]=="X" and self.board[8]=="X") or (self.board[0]=="X" and self.board[4]=="X" and self.board[8]=="X") or (self.board[2]=="X" and self.board[4]=="X" and self.board[6]=="X"):
                print("Gamer 1 you are win") 
                break
            x+=1
            if x==9:
                print("it's a draw")
                break
            po=self.placeO()
            while not (self.board[po-1]!="X" and self.board[po-1]!="O"):
              po=self.placeO()
            self.board[po-1]="O"
            self.wrap()
            if (self.board[0]=="O" and self.board[1]=="O" and self.board[2]=="O") or (self.board[3]=="O" and self.board[4]=="O" and self.board[5]=="O") or (self.board[6]=="O" and self.board[7]=="O" and self.board[8]=="O")or (self.board[0]=="O" and self.board[3]=="O" and self.board[6]=="O") or (self.board[1]=="O" and self.board[4]=="O" and self.board[7]=="O") or (self.board[2]=="O" and self.board[5]=="O" and self.board[8]=="O") or (self.board[0]=="O" and self.board[4]=="O" and self.board[8]=="O") or (self.board[2]=="O" and self.board[4]=="O" and self.board[6]=="O"):
                print("Gamer 2 you are win")
                break
            x+=1
            if x==9 :
                print("it's a Draw")
                break
                        
game=board()
game.show()