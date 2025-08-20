# String Slicing in python is defined as any string can be sliced to get the any part of that string

#string slicing

Alpha = 'abcdefghijklmnopqrzstuvwxy'
#index =[01234567890123456789012345]
#index =[-26: -0]
#index size start from 0 to upwards.

#straight slicing
Alpha1 = Alpha[3:9]
print(Alpha1)

#skip slicing
print(Alpha[:22])
print(Alpha[0:])

#negative slicing
Beta = 'Beta'
Beta1 = Beta[-4:-1]
Beta1 = Beta[1:3]
print(Beta1)