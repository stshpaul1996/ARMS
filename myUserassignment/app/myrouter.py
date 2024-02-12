class Myrouter:
    def db_for_read(self,model,**hints):
        return "read_by" 
    def db_for_write(self,model,**hints):
        return "default"