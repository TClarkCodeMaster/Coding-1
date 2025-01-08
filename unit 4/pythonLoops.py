def gradeToTitle():
    year = int(input('What year are you in'))
    if year == 1:
        print('You are a freshman in undergrad.')
    elif year == 2:
        print('You are a sophmore in undergrad.')
    elif year == 3:
           print('You are a junior in undergrad.')
    elif year == 4:
        print('You are a senior in undergrad')
    elif year == 5 and year == 6:
        print('You are in a masters program and in grad school')
    elif year >= 7 and year <=10:
        print ('you are in a doctors program.')
    else: 
        print('something went wrong. Please check your input.')
gradeToTitle()