rows = 6
columns = 6
b=[]
for i in range(rows):
    a=list(map(int,input().split()))
    b.append(a)
#print(b)
rs = []
for i in range(1,rows-1):
    for j in range(1,columns-1):
        hg = b[i-1][j-1] + b[i-1][j] + b[i-1][j+1] + b[i][j] + b[i+1][j-1] + b[i+1][j] + b[i+1][j+1]
        rs.append(hg)
print(max(rs))
