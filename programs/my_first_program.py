# Getting the sum of variable of linear Equation
from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    a = SecretInteger(Input(name="my_int1", party=party1))
    b = SecretInteger(Input(name="my_int2", party=party1))
    c = SecretInteger(Input(name="my_int3", party=party1))
    d = SecretInteger(Input(name="my_int4", party=party1))
    e = SecretInteger(Input(name="my_int5", party=party1))
    f = SecretInteger(Input(name="my_int6", party=party1))

  # Getting the X value 
    result_x = e*d
    result_y = result_x - b
    result_z = result_y * f

  #Getting the Y value
    result_p = a * f
    result_q = result_p - e
    result_r = result_q * c

  # Adding the X value and Y value of Linear Equation
    result = result_z + result_r
    # make sure you change the output below to be your new output

    return [Output(result, "my_output", party1)
    ]