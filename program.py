#!/usr/bin/python3
# Program for calculating median of list of numbers

def median(numbers):
    n = len(numbers)
    if(n&1):
        return numbers[(n-1)/2]+numbers[(n+1)/2]
    return numbers[n/2]