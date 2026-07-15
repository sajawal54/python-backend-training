# # import math operation files this is called module when we use another file as a import in file it becomes module and modules can be reuse 
# import math_operations
# result = math_operations.add(5 , 9)
# print(result)

# # importing random library for doing some related functions
# import random
# result = random.randint(1 , 210)
# print(result)

# # we can import directly no need of math . and all
# from math import sqrt
# print(sqrt(25))


# # we can import every function of a library by using a steric
# from math import *

import math_operations as mo
import string_operations as so
print(mo.add(10,20))
print(mo.div(20 , 2))
print(so.to_upper("sajawal"))
print(so.to_lower("SAJAWAL"))
print(so.reverse_string("Sajawal jameel"))
print(so.count_characters("SAJAWAL"))

