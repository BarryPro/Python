# -*- coding:utf-8 -*-

from meal import *

class Breakfast(Meal):
    '''Holds the food and drink for breakfast.'''

    def __init__(self):
        '''Initialize with an omelet and coffee.'''
        Meal.__init__(self,'omelet','coffess')
        self.setName('breakfast')

class Lunch(Meal):
    '''Holds the food and drink for lunch.'''

    def __init__(self):
        '''Initialize with an omelet and coffee.'''
        Meal.__init__(self,'sandwich','gin and tonic')
        self.setName('midday meal')

    # Override setFood().
    def setFood(self,food='sandwich'):
        if food != 'sandwich' and food != 'omelet':
            raise AngryChefException
            Meal.setFood(self,food)

class Dinner(Meal):
    '''Holds the food and drink for dinner.'''

    def __init__(self):
        '''Initialize with an omelet and coffee.'''
        Meal.__init__(self,'steak','merlot')
        self.setName('dinner')

    def piritIt(self,prefix=''):
        '''Print even more nicely.'''
        print(prefix,'A gourmet',self.name,'with',self.food,'and',self.drink)
