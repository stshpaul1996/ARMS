from time import sleep
import threading
def fun(x,y):
    res=x+y
    print("result=",res)
    return res
t1 = threading.Thread(target=fun, args=(100,200))
t1.start()

    
