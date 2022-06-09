################################ BIG'O' ##############################################
''' def print_nums(n):
    for i in range(n):
        for j in range(n):
            
               print(i,j)
    for K in range(n):
        print(K)           
print_nums(10) ''' 

################################ Classes #############################################
''' class toy:
    def __init__(self, color) : #constructor#
        self.color = color
    def get_color(self):   #method#
       return self.color
    def set_color(self,color): #method#
        self.color = color   

toy1= toy("green")
toy2 = toy('blue')



print('color of toy1 is :',toy1.get_color())
print('the color of toy2 is:',toy2.get_color())

toy2.set_color('red')

print('color of toy1 is :',toy1.get_color())
print('the color of toy2 is:',toy2.get_color()) '''

############################### Pointers #############################################

''' num1 = 11
num2 = num1

print('the value of num 1',num1) #values#
print('the value of num 2',num2)

print('the value of num 1',id(num1)) #address#
print('the value of num 2',id(num2))

num2 = 22
#after updating num2#
print('the value of num 1',num1) #values#   #INTEGERS ARE IMMUTABLE#
print('the value of num 2',num2)

print('the value of num 1',id(num1)) #address#
print('the value of num 2',id(num2))
 '''

''' dict1 = {'value':11}
dict2=dict1

print('dict1=',dict1)
print('dict2=',dict2)

print('the value of num 1',id(dict1)) #address#
print('the value of num 2',id(dict2))


dict2['value']=22

print('dict1=',dict1)   #value gets updated for both the dicts#
print('dict2=',dict2)   #DICTS ARE MUTABLE#

print('the value of num 1',id(dict1)) #address#
print('the value of num 2',id(dict2)) '''
############################## END ###################################################