import sys
class TicTacToe:
    
    def __init__(self):
        self.col = 3
        self.row = 3
        self.num = 0
        self.structure = []
        self.selected = []
        self.exchange = {
            7:[0,0],
            8:[0,1],
            9:[0,2],
            
            4:[1,0],
            5:[1,1],
            6:[1,2],
            
            1:[2,0],
            2:[2,1],
            3:[2,2],
        }
        
    def structureCreation(self):
        for i in range(0,self.col):
            self.structure.append([])
            for j in range(0,self.row):
                self.structure[i].append([])
        return self.structure
    
    def picker(self):
        A = True
        while A:
            X = True
            while X:
                if self.num <= 9:
                    
                    print('TURN: ',self.num)
                    print('Xs TURN')    
                    
                    self.mapMaker()
                    self.showSelected()
                    selection = int(input("ENTER THE NUMBER YOU WOULD LIKE: "))
                    while selection < 1 or selection > 9:
                        selection = int(input("ENTER THE NUMBER YOU WOULD LIKE: "))
                        print('\n')
                    
                    selection = self.exchange[selection]
                    self.structure[selection[0]][selection[1]].append('X')
                    self.num+=1
                    X = False

            O = True
            while O:
                
                if self.num >= 8:
                    A = False
                    X = False
                    O = False
                    self.winning()
                    print("SHOULD WE CONTINUE WITH A NEW GAME OR EXIT?\n[0] - NEW GAME\n[1] - EXIT\n---------------")
                    question = input('ANSWER HERE: ')
                    if question == '0':
                        self.clearBoard()
                        self.num = 0
                        self.picker()
                    if question == '1':
                        self.clearBoard()
                        self.num = 0
                        self.endGame()
                        self.picker()
                    O = False
                    A = False
                    X = False
                
                if self.num < 8: 
                    print('Turn: ',self.num)     
                    print('Os turn')
                        
                    self.mapMaker()
                    self.showSelected()
                    selection = int(input("ENTER THE NUMBER YOU WOULD LIKE: "))
                    while selection < 1 or selection > 9:
                        selection = int(input("ENTER THE NUMBER YOU WOULD LIKE: "))
                        print('\n')
                    
                    selection = self.exchange[selection]
                    self.structure[selection[0]][selection[1]].append('O')
                    self.num+=1
                    O = False
                    self.picker()
                   
    def checkWinHorizontal(self):
        #check horizontal
        a =''
        b=''
        c=''
        #for row one
        for i in self.structure[0]:
            for j in i:
                a = a + j
        if a == 'XXX':
            print('YOU WIN X')
            return True
        elif a =='OOO':
            print('YOU WIN O')
            return True
        ############
        #for row two
        for i in self.structure[1]:
            for j in i:
                b = b + j
        if b == 'XXX':
            print('YOU WIN X')
            return True
        elif b =='OOO':
            print('YOU WIN O')
            return True
        ############
        # for row three
        for i in self.structure[2]:
            for j in i:
                c = c + j
        if c == 'XXX':
            print('YOU WIN X')
            return True
        elif c =='OOO':
            print('YOU WIN O')
            return True
        else: 
            return False
        
    def checkWinVertically(self):
        a =''
        b=''
        c=''
        # for column one
        for i in self.structure:
            a = a + i[0][0]
        if a == 'XXX':
            print('YOU WIN X')
            return True
        elif a =='OOO':
            print('YOU WIN O')
            return True
        #for column two
        for i in self.structure:
            b = b + i[0][0]
        if b == 'XXX':
            print('YOU WIN X')
            return True
        elif b =='OOO':
            print('YOU WIN O')
            return True
        #for column 3
        for i in self.structure:
            c = c + i[0][0]
        if c == 'XXX':
            print('YOU WIN X')
        elif c =='OOO':
            print('YOU WIN O')
        else: 
            return False
                
    def checkWinDiagonally(self):
        #check Diagonalls
        if self.structure[0][0][0] + self.structure[1][1][0] + self.structure[2][2][0] == 'XXX':
            print('YOU WIN X')
            return True
        elif self.structure[0][2][0] + self.structure[1][1][0] + self.structure[2][0][0] == 'XXX':
            print('YOU WIN X')
            return True
        elif self.structure[0][0][0] + self.structure[1][1][0] + self.structure[2][2][0] == 'OOO':
            print('YOU WIN O')
            return True
        elif self.structure[0][2][0] + self.structure[1][1][0] + self.structure[2][0][0] == 'OOO':
            print('YOU WIN O')  
            return True
        else:
            return False
    
    def winning(self):
        self.showSelected()
        msg = ''
        if self.checkWinVertically() == True:
            msg += ' GAMEOVER THROUGH VERTICAL'
            
        elif self.checkWinHorizontal() == True:
            msg += ' GAMEOVER THROUGH HORIZONTAL'
                 
        elif self.checkWinDiagonally() == True:
            msg += ' GAME OVER THROUGH DIAGONOAL'
            
        elif (self.checkWinVertically() and self.checkWinHorizontal() and self.checkWinDiagonally()) == False:
            msg += " GAMEOVER THROUGH CAT'S GAME"
        
        print('Result: ', msg)
            
    def mapMaker(self):
        print('7 | 8 | 9')
        print('--|---|--')
        print('4 | 5 | 6')
        print('--|---|--')
        print('1 | 2 | 3\n')
        
    def showSelected(self):
        #self.structure[0][2][0] + self.structure[1][1][0] + self.structure[2][0][0]
        print(self.structure[0][0],'        |       ',self.structure[0][1],'        |       ',self.structure[0][2],'\n')
        print(self.structure[1][0],'        |       ',self.structure[1][1],'        |       ',self.structure[1][2],'\n')
        print(self.structure[2][0],'        |       ',self.structure[2][1],'        |       ',self.structure[2][2],'\n')
    
    def endGame(self):
        print('GOOD GAME THANKS FOR PLAYING')
        quit
        exit
        sys.exit()
    
    def clearBoard(self):
        for i in range(3):
            for j in range(3):
                self.structure[i][j].pop()

    def game(self):
        self.structureCreation()
        self.picker()
        
game1 = TicTacToe()
game1.game()