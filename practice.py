import random
a=0
for i in range(6):
    a = a*10 +random.randint(1, 9)
    
input = int(input())
if a== input:
    print("당첨 축하드립니다")

if a!= input:
    print("아쉽네요")
    print("당첨코드:%d" %(a))
