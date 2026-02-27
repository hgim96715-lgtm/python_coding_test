def solution(n):
    arr=[[0]*n for _ in range(n)]
    # print(arr)
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    
    x,y,dir=0,0,0
    
    for num in range(1,n*n+1):
        arr[x][y]=num
        nx,ny=x+dx[dir],y+dy[dir]
        if nx<0 or nx>=n or ny<0 or ny>=n or arr[nx][ny]!=0:
            dir=(dir+1)%4
            nx,ny=x+dx[dir],y+dy[dir]
        x,y=nx,ny
    return arr