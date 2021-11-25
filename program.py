#!/usr/bin/python3
# Program for calculating median of list of numbers

def median(numbers):
    n = len(numbers)
    if(n&1):
        return numbers[n>>1]
    return (numbers[(n-1)>>1]+numbers[(n+1)>>1])/2.0
