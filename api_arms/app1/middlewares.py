import time
class TimeOut:
    def __init__(self, view):
        self.view=view
    def __call__(self, request):
        print("*"*20)
        print("middleware called")
        resp = self.view(request)  # 4secs
        # t1 = Thread(target=self.view, args=(request,))
        # t1.start()
        # star_time = time.time()
        # while t1.isactive():
        #     if time.time()-star_time==2:
        #         raise TimoutException("")
            

        return resp