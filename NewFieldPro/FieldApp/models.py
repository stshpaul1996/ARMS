from django.db import models

# Create your models here.





class EncryptionField(models.Field):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)


    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        
        dic_num = {"f":"1", "e":"2", "v":"3", "r":"4", "o":"5", "l":"6", "q":"7", "p":"8", "m":"9", "z":"0" }
        dic_small = {"!":"a", "@":"b", "#":"c", "$":"d", "%":"e", "^":"f", "&":"g", "*":"h", "(":"i", ")":"j", "-":"k", "_":"l",
                     "+":"m", "=":"n", "|":"l", "?":"o", "/":"p", ">":"q", "<":"r", ".":"s", ",":"t", "{":"u", "}":"v", 
                     "[":"w", "]":"x", "~":"y", "`":"z"}
        res = ""
        for i in value:
            if i in dic_num:
                res += dic_num[i]
            else:
                res += dic_small[i]
        return res
        
    
    def  get_prep_value(self, value):
        if value is None:
            return value
        dic_num = {"1":"f", "2":"e", "3":"v", "4":"r", "5":"o", "6":"l", "7":"q", "8":"p", "9":"m", "0":"z" }
        dic_small = {"a":"!", "b":"@", "c":"#", "d":"$", "e":"%", "f":"^", "g":"&", "h":"*", "i":"(", "j":")", "k":"-", "l":"_",
                     "m":"+", "n":"=", "l":"|", "o":"?", "p":"/", "q":">", "r":"<", "s":".", "t":",", "u":"{", "v":"}", 
                     "w":"[", "x":"]", "y":"~", "z":"`"}
        res = ""
        for i in value:
            if i in dic_num :
                
                res += dic_num[i]
            else:
               
                res += dic_small[i]

        return res
    


class Customer(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=100)
    password = EncryptionField()
    email = models.EmailField(null=True)
