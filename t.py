import datetime
import random
import os
import time

end = datetime.datetime.now()
start = end - datetime.timedelta(days=200)

def do(dt):
    if not random.randint(0, 2):
        for i in range(random.randint(0, 3)):
            with open('commit.log', 'a+') as f:
                f.write(str(dt) +'\n')
            os.system('git add .')
            print(f"{str(dt)[:-9]}{random.randint(0,59)}", i)
            os.system(f'GIT_AUTHOR_DATE="{str(dt)[:-9]}{random.randint(10,59)}" GIT_COMMITTER_DATE="{str(dt)[:-9]}{random.randint(10,59)}" git commit -a -m "update"')



while start < end - datetime.timedelta(days=3):
    start = start + datetime.timedelta(days=random.randint(1, 3))
    do(start)


