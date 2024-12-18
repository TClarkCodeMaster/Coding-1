def discountFunction (membership, itemPrice):
    if membership == 'superShopper':
        print('You are getting 10 percent off!')
        discount= itemPrice * .1
        total= itemPrice -discount
        print(discount)
    elif membership== 'megashopper':
        print('You are getting 15 percent off!')
    elif membership== 'ultraShopper':
        print('You are getting 20 percent off!')
    else:
        print('Error: sorry that membership type doesnt exist')

discountFunction('ultraShopper', 200)

