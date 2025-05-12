def Constboard(board):
  print("CURRENT STATE OF BOARD: \n\n");
  for i in range(0,9):
     if((i>0) and (i%3==0)):
      print("\n");
     if(board[i]==0):
      print("_ ", end=" ");
     if(board[i]==-1):
      print("X ", end=" ");
     if(board[i]==1):
      print("O ", end=" ");
  print("\n\n");

def User1turn(board):
  pos=int(input("ENTER THE POSITION YOU WANT TO PLACE X (1, 2, 3, 4, 5, 6, 7, 8, 9): "));
  if(board[pos-1]!=0):
    print("WRONG MOVE ");
    exit(0);
  board[pos-1]=-1;

def User2turn(board):
  pos=int(input("ENTER THE POSITION YOU WANT TO PLACE O (1, 2, 3, 4, 5, 6, 7, 8, 9): "));
  if(board[pos-1]!=0):
    print("WRONG MOVE ");
    exit(0);
  board[pos-1]=1;

def minmax(board,player):
  x = analyzeboard(board);
  if(x!=0):
    return(x*player);
  pos=-1;
  value=-2;
  for i in range(0,9):
    if(board[i]==0):
      board[i]=player;
      score=-minmax(board,player*-1)
      board[i]=0;
      if(score>value):
        value=score;
        pos=i;
    if(pos==-1):
      return 0;
    return value;

def CompTurn(board):
  pos=-1;
  value=-2;
  for i in range(0,9):
    if(board[i]==0):
      board[i]=1;
      score=-minmax(board,-1)
      board[i]=0;
      if(score>value):
        value=score;
        pos=i;
  board[pos]=1;

def analyzeboard(board):
  cb= [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  for i in range(0,8):
    if(board[cb[i][0]!=0] and
       board[cb[i][0]]==board[cb[i][1]] and
       board[cb[i][0]]==board[cb[i][2]]):
      return board[cb[i][0]];

  return 0;


def main():
  choice= int(input("ENTER 1 FOR SINGLE PLAYER OR 2 FOR 2 PLAYER: "));
  board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  if(choice==1):
    print("COMPUTER: O  V/S  YOU: X");
    player= int(input("ENTER TO PLAY 1ST OR 2ND(1 OR 2):  "));
    for i in range(0,9):
      if(analyzeboard(board)!=0):
        break;
      if((i+player)%2==0):
        CompTurn(board);
      else:
        Constboard(board);
        User1turn(board);
  else:
    for i in range(0,9):
      if(analyzeboard(board)!=0):
        break;
      if(i%2==0):
        Constboard(board);
        User1turn(board);
      else:
        Constboard(board);
        User2turn(board);

  x = analyzeboard(board);
  if(x==0):
    Constboard(board);
    print("DRAW!!");
  if(x==-1):
    Constboard(board);
    print("PLAYER X WON!!! PLAYER O LOST!!!");
  if(x==1):
    Constboard(board);
    print("PLAYER O WON!!! PLAYER X LOST!!!");

if __name__ == "__main__":
    main()