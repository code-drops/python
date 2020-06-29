# Represents the 3*3 grid of the game
board = {'topleft':' ','topmid':' ','topright':' ',
         'midleft':' ','mid':' ','midright':' ',
         'bottomleft':' ','bottommid':' ','bottomright':' '}
         
# check for the win situation 
def checkforwin(board,turn):
    if board['topleft']==board['topmid']==board['topright']==turn:
        return True
    elif board['midleft']==board['mid']==board['midright']==turn:
        return True
    elif board['bottomleft']==board['bottommid']==board['bottomright']==turn:
        return True
    elif board['topleft']==board['midleft']==board['bottomleft']==turn:
        return True
    elif board['topmid']==board['mid']==board['bottommid']==turn:
        return True
    elif board['topright']==board['midright']==board['bottomright']==turn:
        return True
    elif board['topleft']==board['mid']==board['bottomright']==turn:
        return True
    elif board['topright']==board['mid']==board['bottomleft']==turn:
        return True
    return False

# print the board instance at every iteration
def printboard(board):
    print(board['topleft']+'|'+board['topmid']+'|'+board['topright'])
    print('-+-+-')
    print(board['midleft'] + '|' + board['mid'] + '|' + board['midright'])
    print('-+-+-')
    print(board['bottomleft'] + '|' + board['bottommid'] + '|' + board['bottomright'])

if __name__=='__main__':
    turn = 'X'
    count=1
    while count<=9:
        print()
        printboard(board)
        move = input(str(count)+") "+ turn+" turn : ")
        
        # for overwriting value
        if board[move]!=' ':
            print("Invalid value")
            continue
        board[move] = turn
        if checkforwin(board,turn):
            print('#######'+turn +' wins ########')
            break
        count = count + 1
        
        # change the turn
        if turn=='X':
            turn = '0'
        elif turn=='0':
            turn='X'
    if count>=9:
        print("####### It's a Draw #######")
    printboard(board)
