board = {
    'top-L': ' ', 'top-M' : ' ', 'top-R' : ' ',
    'mid-L': ' ', 'mid-M' : ' ', 'mid-R' : ' ',
    'low-L': ' ', 'low-M' : ' ', 'low-R' : ' ',
}

def printboard(board):
    print(board['top-L'] + ' |' + board['top-M'] + ' |' + board['top-R'])
    print('__+__+__')
    print(board['mid-L'] + ' |' + board['mid-M'] + ' |' + board['mid-R'])
    print('__+__+__')
    print(board['low-L'] + ' |' + board['low-M'] + ' |' + board['low-R'])

printboard(board)