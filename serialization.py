import pickle
class employee:
    def __init__(self,e_no,fast_name, last_name,e_sal):
        self.No=e_no
        self.fastname=fast_name
        self.lastname = last_name
        self.Sal=e_sal
        self.mail=fast_name+last_name +'@gmail.com'


    def disply(self):
        return("E.NO :{}  NAME :{}.{} SALARY : {}  E-Mail: {} ".format(self.No,self.fastname,self.lastname,self.Sal,self.mail))

e1=employee(10,'Bhannu','Gaini',1000000)
e2=employee(11,'shrawan','Gaini',500000)
#print(e1.disply())
#print(e2.disply())

# SERIALIZATION

with open('abc.ser','wb') as f:
    pickle.dump(e1,f)
    print("completed")
    pickle.dump(e2, f)
    print("completed two aslo")

# deserializton
with open('abc.ser','rb') as f:
    new=pickle.load(f)
    new1 = pickle.load(f)
    print('deserialized complited')


print(new.disply())

print(new1.disply())
