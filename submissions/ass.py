#difference of 10 natural numbers

c=[]
d=[]

for i in range(1,11):
    d.append(i)
    c.append(i**2)

sum_square=sum(d)**2
square_sum=sum(c)
difference=sum_square-square_sum

print('sum_square:%d'%sum_square)
print('square_sum:%d'%square_sum)  
print('difference:%d'%difference)

#2)
#difference of 100 natural number

first=[]
second=[]

for num in range(1,101):
    first.append(num)
    second.append(num**2)
    
summ_of_square=sum(first)**2
square_of_summ=sum(second)
square_difference=summ_of_square-square_of_summ

print('square_of_summ:{}'.format(square_of_summ))
print('summ_of_square:{}'.format(summ_of_square))
print('square_difference:{}'.format(square_difference))
 
