import sys
sys.stdin = open("input.txt", "r")

# import sys
# input = sys.stdin.readline

# 10158 개미, 원큐에 도착해야 한다.
# 가로와 세로를 나누어서 생각한다.
# 자신의 축의 두 배에 해당하는 값이 넣어지면 제자리로 돌아온다. (좌우로 왔다갔다 했다는 것이다.)

def move(x, y, z): # 현재 위치, 이동, 축의 범위
    if x + y <= z:
        return x + y
    else:
        temp = 2*z - x - y
        if  temp > 0:
            return temp
        else:
            return - temp

w, h = map(int, input().split()) # 가로 세로
p, q = map(int, input().split()) # 축의 값
t = int(input())
t1 = t % (2 * w)
t2 = t % (2 * h)
    
res1 = move(p, t1, w)
res2 = move(q, t2, h)

print(res1, res2)