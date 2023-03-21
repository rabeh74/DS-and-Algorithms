"""
Write a program that takes two arrays representing integers, and retums an integer represent- ing their product. For example, since 193707721.x -761838257287 = -147573952589676412927, if the inputs are (1,9,3,7,0,7,7,2, 1) and <-7,6,L,8,3,8,2,5,7,2,8,7>,
 your function should return (-1, 4,7, 5,7,3, 9, 5, 2, 5,8,9, 6,7, 6, 4, 1., 2,9,2,7>.
"""

def multiply( num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    res=[0] *(len(num1)+len(num2))
    num1[0],num2[0]=abs(num1[0]),abs(num2[0])
    m =len(num1)
    n =len(num2)

    for i in reversed(range(m)):
        for j in reversed(range(n)):
            res[i+j+1] += num1[i] * num2[j]
            res[i+j] += res[i+j+1] //10
            res[i+j+1] %=10
    
    # remove leading zero
    for i in range(len(res)):
        if res[i]!=0:
            break
    res[i] *=sign

    return res[i:]

if __name__ == "__main__":
    num1=[1,9,3,7,0,7,7,2,1]
    num2=[-7,6,1,8,3,8,2,5,7,2,8,7]
    res=multiply(num1,num2)
    print(res)
    #[-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7]
    num1=[1,5]
    num2=[2,6]
    res=multiply(num1,num2)
    print(res)
    #[3, 9, 0]