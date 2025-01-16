# What are loops
# Python loop is a programming concept where
# code repeats itself under specific conditions.

# In python there are two versions of loops; for loop and while loop.

# For loops - this is a type of loop that will go through a list of any data you give it and depending on the data you give it might try to find something. / this is the type of loop that iterates over a collection of data and will run a specific set of instructions on data.

# While loops - A type of loop that will repeat a set of instructions so long as some conditions is true.

normalAttack = 2
specialAttack = 4
increasedHealth = 3
def battleFunction():
    hp = 100

    while hp > 0:
        if hp == 0:
            print('You Died')
        print('Do you want to attack')
        print(hp)
        hp -= normalAttack
        keepGoing = input('Do you want to keep going?')
        if keepGoing == 'y':
            print('Run function again')
        else:
            print('You Died')
        

battleFunction()

# x in this example, is an itorator. this x represents the numbers in this list
numbers = [1,2,3,4,5,6,7,8]



attackValues =[10,25,50, 90]
for x in numbers: 
    print(x)

for attacks in attackValues:
    print('attack index ' )
    print (attacks *2)


# Create a function where items over $50.00 give a 10% discount
def shoppingDiscountFunction():
    shoppingCart = []
    while shoppingCart > 0
    customerItem = input('How much does this item cost?')
    shoppingCart .append(customerItem)
    print("Here are the item prices in your cart:")
    print(shoppingCart)

shoppingDiscountFunction()