# -*- coding:utf-8 -*-
from meal import *
from Breakfast import *

def test():

    '''Test function'''

    print('Module meal test')

    #Generic no artuments
    print('Testing Meal class.')
    m = Meal()

    m.printIt("\t")

    m = Meal('green eggs and ham','tea')
    m.printIt("\t")

    # Test breakfast
    print('Testing Breakfast class.')
    b = Breakfast()
    b.printIt('\t')

    b.setName('breakfast of the fast')
    b.printIt('\t')

    # Test Dinner
    print('Testing Dinner class.')
    d = Dinner()
    d.printIt('\t')

    # Test lunch
    print('Testing Lunch class.')
    l = Lunch()
    l.printIt("\t")

    print('Calling Lunch.setFood().')
    try:
        l.setFood('hotdog')
    except AngryChefException:
        print ("\t",'The chef is angry .Pick an omelet.')

test()
