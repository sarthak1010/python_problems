"""Filter used for only functions and iterables 

   filter only return true values and stores it in the variable

   filter is diffeent from all iterators

   """
amz=[1,2,3,4,5,6,7,0,8,9]
def filt(x):

       if x%2 ==0:
           return True

       else:
                return False

ev=filter(filt,amz)

for i in ev:
    print(i)