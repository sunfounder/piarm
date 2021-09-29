import json
import time
path = '/home/pi/piarm/tests/test.json'

def fuc(): 
    dict1 = {'name':'one','type':1,'value':1001}
    dict2 = {'name':'two','type':2,'value':1002}
    dict3 = {'name':'three','type':3,'value':1003}
    dict4 = {'name':'four','type':4,'value':1004}
    data_in = []
    data_in.append(dict1)
    data_in.append(dict2)
    data_in.append(dict3)
    data_in.append(dict4)
    # w   
    try:
        with open(path,'w')as f:
            json.dump(data_in,f)
            time.sleep(0.1)
            f.close()
    except Exception as e:
        print(e)    

    # r
    # data_out = []
    try:
        with open(path,'r')as f:
            data_out = json.load(f)
            time.sleep(0.1)
            f.close()
    except Exception as e:
        print(e)

    print(type(data_out))
    for d in data_out:
        if d['name'] == 'three':
            print(d['type'])
            print(d['value'])

def fuc2():
    dict5 = {'name':'four','type':404,'value':1004}
    # r 
    try:
        with open(path,'r')as f:
            data_out = json.load(f)
            time.sleep(0.1)
            f.close()
    except Exception as e:
        print(e)
    # w
    for index,d in enumerate(data_out):
        if d['name'] == 'four':
            data_out[index] = dict5
            break
    else:
        data_out.append(dict5)
    print(data_out)
    try:
        with open(path,'w')as f:
            json.dump(data_out,f)
            time.sleep(0.1)
            f.close()
    except Exception as e:
        print(e)    


if __name__ == "__main__":
    fuc2()