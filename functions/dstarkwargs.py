def d_kwargs(**kwargs): #keyword arguments
   print(kwargs)

d_kwargs(name="Keerthi", age=22, city="Davanagere")

def kwargs2(**bank_details):
    print(bank_details)

kwargs2(acc_holder="Keerthi", joint_holder="Kavya")

def kwargs3(**st_details):
    print(st_details)

kwargs3(name="Keerthi", uni="ubdt", locality="Davanagere")
kwargs3(pass_year=2024)

def kwargs4(**food):
    print(food)

kwargs4(name="Dosa", cost=55, rest="Madhura")

def kwargs5(**places):
    print(places)

kwargs5(name="Banglore", area="Malleshwaram")