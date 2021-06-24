# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:34:50 2021

@author: mateu
"""
# Binary Search
import math

def binary_search(element, list_elements):
    list_elements = sorted(list_elements)
    left = 0
    right = len(list_elements)
    itarations = 1
    while True:
        middle = math.floor((left+right)/2)
        if element == list_elements[middle]:
            return {'iterations': itarations, 'position_element': middle}
        elif element > list_elements[middle]:
            left = middle
        elif element < list_elements[middle]:
            right = middle
            
        if right == left:
            return {'iterations': itarations, 'position_element': middle}
        
        itarations+=1