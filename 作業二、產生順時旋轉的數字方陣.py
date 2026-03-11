n = int(input("input ur n:"))
x,y,count,turn,xcount,layer = 0,0,0,"U",0,n
matrix=[[0]*n for i in range(0,n)]
if n%2==1:
    y,x,turn = n-1,0,"L"
else:
    y,x,turn=0,n-1,"R"
while(n**2-count>0):
    matrix[x][y] = n**2-count
    if x==layer-1 and y==layer-1:
        x,turn=x-1,"U"
    elif turn=="D":
        if n%2==1 and y==n-layer and x>=layer-1:
            y,turn = y+1,"R"
        elif n%2==0 and x==layer-2:
            y,turn,layer = y+1,"R",layer-1#轉向右
        else:
            x+=1#向下
    elif y == n-layer and x == n-layer and x+1!=n:
        x,turn = x+1,"D" #轉向下
    elif x>=n-layer and turn=="U":
        if n%2==0 and x==n-layer:
            y,turn = y-1,"L"#轉向左
        elif n%2==1 and x-1==n-layer:
            turn,layer,y ="L",layer-1,y-1#轉向左
        else:
            x-=1 #向上
    elif turn == "U":
        x-=1 
        if x-1==n-layer and y==layer-1 and n%2==1:
            y,turn,layer = y-1,"L",layer-1#機層數減少 轉向左
    elif turn == "L":
        y-=1 #向左
    elif turn == "R":
        if y+1<layer:
            y+=1#向右
        elif y+1==layer:
            x,turn = x-1,"U"#轉向上 
    count += 1
for row in matrix:
    for num in row:
        print(f"{num:3}", end=" ")
    print()