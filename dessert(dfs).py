import sys
input = sys.stdin.readline
#sys.setrecursionlimit(1000)

count = 0
con = True

def combine(val,ind, result,idx, change,b,con):
    global count
    value = -1
    if ind >n:
        value = val +b*change

    if value==0 and ind>n:
        
        count += 1
        if count <=20:
            
            for i in range(1,2*n):
                print(result[i], end = ' ')
            print()
            #print(result, val)
        return
    elif ind > n:
        return
    

    result[idx] = '+'
    
    combine(val+b*change,ind+1,result, idx+2, nums[ind],1,False)
    result[idx] = '-'
    
    combine(val+b*change, ind+1, result,idx+2, nums[ind],-1,False)
    result[idx] = '.'
    if con:
        change = str(change)+str(nums[ind])
        combine(val*10, ind+1,result, idx+2, int(change),b,True)
        
    else:
        change = str(change)+str(nums[ind])
        combine(val, ind+1,result, idx+2, int(change),b,False)
    return

'''
1,2,2,0,1
1,3,4,2,1


'''
n = int(input())
nums = [i for i in range(1, n+1)]
nums.insert(0,0)
#nums_arr = []
result = [0 for i in range(2*n)]
#print(nums)

q = 1
idx = 1
#print(result)

for i in range(1, 2*n, 2):
    result[i] = q
    q+= 1

count = 0 
combine(1,2,result, 2,0,1,True)
print(count)
