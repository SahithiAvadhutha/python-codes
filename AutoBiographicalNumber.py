from collections import Counter
def isauto(number,n):
    new_str = str(number)
    count = [0]*n
    for i in new_str:
        count[int(i)]+=1
        print(count)
    for i in range(n):
        if int(new_str[i]) != count[i]:
            return 0
    return 1

number =input('enter the number ')
n = len(str(number))
res  = isauto(number,n)
if res == 1 :
    new = str([*number])
    s = Counter(number).keys()
    print(len(s))
else:
    print('Not a autobiographical number!!')
