from math import sqrt
class quadratic():
    def solve(a,b,c):#-b plus or minus squareroot of b squared - 4ac over 2a
        bneg = b * -1##_
        print(bneg)
        ans1 = b**2#                                  ________
        print(ans1)
        ac = a*c#                                                 __ac only
        ans2 = 4 * ac#                                           ___all
        print(ans2)
        ans12 = ans1 - ans2#                         _______________
        print(ans12)
        ans4 = sqrt(ans12)#             ____________________________
        print(ans4)
        ansplus = bneg + ans4#______________________________________everytging up to 2a
        print(ansplus)
        print(a)
        print(c)
        under  =2 *a#                                                     __
        ansallplus = ansplus / under#all plus
        ansmin = bneg - ans4
        print(ansmin)
        ansallminus = ansmin / under
        print('____________________________ANSWER______________________________________')
        print('      _________')
        print('-b +-√ b² - 4ac')
        print('----------------')
        print('       2a       ')
        print(ansallplus)
        print(ansallminus)
        print('__________________________END___________________________________________')
while True:
    print('Leo Foster on github.com/leofoster made it - Quadradrrict equation solver DoeS not do imaginary numbers')
    print('if you get a ValueError double check your equation specifically a math domain error')
    a1 = int(input('a'))
    b1 = int(input('b'))
    c1 = int(input('c'))
    quadratic.solve(a1,b1,c1)
    
    
