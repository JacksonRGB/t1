import datetime
import random
import os
import time

end = datetime.datetime.now()
start = end - datetime.timedelta(days=194)

def do(dt):
    if not random.randint(0, 7):
        for i in range(random.randint(0,4)):
            with open('commit.log', 'a+') as f:
                f.write(str(dt) +'\n')
            os.system('git add .')
            print(f"{str(dt)[:-9]}{random.randint(0,59)}", i)
            os.system(f'git commit -a -m "update" --date="{str(dt)[:-9]}{random.randint(10,59)}"')



while start < end - datetime.timedelta(days=91):
    start = start + datetime.timedelta(days=1)
    do(start)


