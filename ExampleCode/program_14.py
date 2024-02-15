# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 06:28:48 2022

@author: EDUARDO

Description: Some basic exercises about regular expressions

The first thing to recognize when usign regular expressions is that everything
is essentially a character, and we are writing patterns to match a specific
sequence of characters
"""



import re

s = 'interesting links to woodchucks and lemurs, Woodchucks'
l = re.findall('woodchucks', s) # RE pattern, strig
l = re.findall('Woodchucks', s) # RE pattern are case sensitive
l = re.findall('[wW]oodchucks', s) # Captures either w o W (grouping options)

s = 'In uomini, in soldati'
l = re.findall('[abc]', s) # Captures either a, b or c

s = 'plenty of 7  to 5'
l = re.findall('[0123456789]', s) # Capture any digit

s = "we should call it 'Drenched Blossoms'"
l = re.findall('[A-Z]', s) # Captures any capital letter (Ranges)
l = re.search('[A-G]', s).group() #Return only the first ocurrence of the pattern

s = "WE SHOULD CALL IT 'DREnchED BLOSSOMS'"
l = re.findall('[a-h]', s) # Capture letters in range a-h

s = "Chapter 1: Down the Rabbit Hole"
l = re.findall('[0-9]', s) # Capture any digit

s = "Oyfn pripetchik"
l = re.findall('[^A-Z]', s) # Capture all chars except capital letters
l = re.findall('[^a-g]', s) # Capture all chers except the ones in the range

s = "Look up ^ now"
l = re.findall('[n^]', s) # Capture n or ^ chars

s = "interesting links to woodchuck and lemus, Woodchuks"
l = re.findall('[wW]oodchucks?', s) # The ? indicates the previus char is optional

s = "color among colours"
l = re.findall('colou?rs?', s) 

s = "begin, beg'n, begun"
l = re.findall('beg.n', s) # The wildcard . indicates any char

s = "baa! baaa! baaaa! baaaaa!"
l = re.findall('ba*!', s) # The * means zero or more occurrences of the
                          # previous character (or regular expression)
                          
                          
s = "b! ba! baa! baaa! baaaa! baaaaa!"
l = re.findall('ba*!', s) # 
l = re.findall('baa*!', s) # Forces to have one a before a sequence of a's

s = 'abcd adbcd ardg ababbaba'
l = re.findall('[ab][ab]*', s) # Captures string starting whit a or b and followed by zero or more ocurrences a or b

s = 'b! ba! baa! baaa! baaaa! baaaaa! baaaa'
l = re.findall('ba+!', s) # The means one or more ocurrences of the previus character (or regular expression)

s = "The sun and the moon "
l = re.findall('^[Tt]he', s) # The anchor ^ captures the start of a line, the pattern is only captured at the end of a line

s = "The dog and the cat that follow the cat\n"
l = re.findall('cat$', s) # The anchor $ captures the end of line, the pattern is only captured at the end of a line 

s = "It costs \n $999.00 \t \r _" #

l = re.findall('\d', s) # Captures all digit chars [0-9] 
l = re.findall('\D', s) # Captures all non-digit chars [0-9]
l = re.findall('\w', s) # Captures all alphanumeric chars [a-zA-Z0-9]
l = re.findall('\W', s) # Captures all non-alphanumeric chars [a-zA-Z0-9]
l = re.findall('\s', s) # Captures all whiespace chars (space, tab, newline, return)
l = re.findall('\S', s) # Captures all non-whiespace chars (space, tab, newline, return)

s = 'b! ba! baa! baaa! baaaa! baaaaa! baaaaaa!'
l = re.findall('ba{2}!', s) # Captures 2 occurrences of previus char
l = re.findall('ba{4,5}!', s) # Captures between 4 and 5 occurrences of previous 
l = re.findall('ba{2,}!', s) # Captures at least n ocurrences  of previous char
l = re.findall('ba{,3}!', s) # Captures up to m ocurrences {,m} of previous char

s = "it\'s raining cats and dogs, cat dog"
l = re.findall('cats?|dog?', s) #Captures either cat or dog 

s = "I like guppies, my pet is a guppy"
l = re.findall('gupp(?:ies|y)', s) # Captures gupp followed either by ies or y, indicates the parentheses are not for groups

