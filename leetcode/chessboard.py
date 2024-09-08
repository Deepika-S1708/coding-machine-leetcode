class Solution:
    def chessboard(self, inputNum:int):
        board=[]
        for i in range(inputNum):
            row=[]
            for j in range(inputNum):
                if (i+j)%2==0:
                    row.append("W")
                else:
                    row.append("B")
            print(row)
            board.append(" ".join(row))
        return board

if __name__=="__main__":
    s=Solution()
    inputNum=5
    res= s.chessboard(inputNum)
    # print(res)
    for i in res:
        print(i)

         



