import random

d = "abcdefghijklmnopqrstuvwxyz"
u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = "0123456789"
s = "!@#$%^&*()_+=-[{]}\|;:/?.><,*"

p = d + u + n + s
a = 16
password = "".join(random.sample(p,a))
print("you password:" +" "+ password) 