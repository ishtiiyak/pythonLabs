balls=(3,3,3,3,3,8,3)
def check(balls):

    if balls[0]+balls[1]+balls[2]== balls[3]+balls[4]+balls[5]:
        return balls[6]
    elif balls[0]+balls[1]+balls[2]>balls[3]+balls[4]+balls[5]:
        if balls[0]==balls[1]:
            return balls[2] 
        elif balls[0]>balls[1]:
            return balls[0]
        else:
            return balls[1]
    elif balls[0]+balls[1]+balls[2]<balls[3]+balls[4]+balls[5]:
        if balls[3]==balls[4]:
            return balls[5] 
        elif balls[3]>balls[4]:
            return balls[3]
        else :
            return balls[4]
        

print(check(balls))