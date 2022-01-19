import random
import time

num, num2, i, j, k = 0, 0, 0, 0, 0
a, b, c = 0, 0, 0
num3, num4 = 0, 0


while True:
    num = random.randrange(1, 249)
    num2 = random.randrange(1, 249)
    num3 = random.randrange(1, 249)
    num4 = (num + num2)//num3

    
    if num4 <= 10:
        print("CODE_RUNNUNG_TIME (%d%d : %d%d : %d%d)\n" % (k//10, k%10, j//10, j%10, i//10, i%10, ))

    if num4 > 5:
        print("TIME %d%d : %d%d : %d%d\n" % (k//10, k%10, j//10, j%10, i//10, i%10, ))
        print("ERROR_CODE: %d" %num4)
        print("usr/bin/lists/lock//home/ganrabbit34/catkin_ws/src/mavros/mavros_extras/ PORT::%d%d\n\n" % (num4//2, num4%2))

    i = i+1

    if i==60 and j==59 and k==23:
        print("\nTIME OUT\n")
        time.sleep(2)
        print("\nRESET_TIME\n")
        time.sleep(2)

        for i in range(1, 4):
            j = 4-i
            print("%d second before resetting the time...." %j)
            time.sleep(2)

        print("\n")
        i=j=k=0

    if i == 60:
        j = j+1
        i = 0

        if j == 60:
            k = k+1
            j = 0

    time.sleep(1)