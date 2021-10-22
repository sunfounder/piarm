import json
import time
import sys
import tty
import termios
import random
import os 
from types import DynamicClassAttribute

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

manual = '''
Press keys on keyboard to record value!
    Q: record
    W: reproduce
    E: clear
    ESC: Quit
'''

path = '/home/pi/piarm/tests/test.json'
data = []
buff = []
name = 'two'
index = 0

def init():
    global data,index
    if not os.path.exists(path):
        print('Steps record file does not exist.Create now...')
        try:
            os.system('sudo mkdir -p '+path.rsplit('/',1)[0])
            os.system('sudo touch '+path)
            os.system('sudo chmod a+rw '+path)

            data.append({'name':'none','values':None})
            data.append({'name':'one','values':None})
            data.append({'name':'two','values':None})
            data.append({'name':'three','values':None})
            with open(path,'w')as f:
                json.dump(data,f)
                time.sleep(0.1)
                f.close()

        except Exception as e:
            print(e)  

    clear() 

    try:
        with open(path,'r')as f:
            data = json.load(f)
            time.sleep(0.1)
            f.close()
    except Exception as e:
        print(e)

    print(type(data))
    print(len(data)) 

    if name == 'none':
        index = 0
    if name == 'one':
        index = 1
    if name == 'two':
        index = 2
    if name == 'three':
        index = 3

def record():
    global data,index
    buff.append([random.randint(0,100) for _ in range(3)])
    buff.append(random.randint(0,100))

    msg = {
        'name':name,
        'values':buff,
    }
    data[index] = msg

    try:
        with open(path,'w')as f:
            json.dump(data,f)
            time.sleep(0.1)
            f.close()
    except Exception as e:
        print(e)     


def reproduce():
    global index
    # read data
    try:
        with open(path,'r')as f:
            _data = json.load(f)
            time.sleep(0.1)
            f.close()
    except Exception as e:
        print(e)

    print(_data[index]['name'])
    print(_data[index]['values'])


def clear():
    buff.clear()


if __name__ == "__main__":
    init()
    print(manual)
    while True:
        key = readchar()
        print(key)
        if 'q' == key:
            record()
        if 'w' == key:
            reproduce()
        if 'e' == key:
            clear()
        if chr(27) == key:
            break
        time.sleep(0.01)