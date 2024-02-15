# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 04:11:54 2021

@author: oscar

@Description: Ramdom numbers
"""
import random as rn

#Ramdom numbers
rn.ramdom()             #Return the next ramdom floating point number in
                        #the range[0.0, 1.0]
rn.uniform(2.5, 7.8)    #Return a ramdom floating point number N
                        #between a and b
rn.seed(90.89)          #Initialize internal state of the random number
                        #generator
rn.getrandbits(9)       #Return a python int with k random bits
rn.randrange(100,200)   #Return a randomly selected element from
                        #range(start, stop)
rn.randrange(100, 200, 2)  #Return a randomly selected element from 
                            #range(star, stop, step)
rn.randint(100, 200)    #Return a random integer N such that a <= N <= b.

x = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c']
rn.choice(x)            #Return one element at random from iterable
rn.shuffle(x)           #Shuffle the sequence in place
rn.sample(x, 3)         #Return a k lenght list of unique elements chosen
                        #from sequence
