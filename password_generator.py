"""
Password Generator Script

This script generates secure, random passwords based on user preferences.
Users can specify the length of the password and choose to include letters which
consists of uppercase and lowercase letters, numbers, and special characters.

Author: Cedrick
Date: December 10, 2024
"""
import random

# Creating separate lists for letters, numbers, and special characters
upper_lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
           'm', 'n', 'o', 'p', 'r', 's', 't', 'u' 'v', 'w', 'x', 'y', 
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-',
            '?', ':', ';', ',', '.', '[', ']', '{', '}', '|', '_', '>', '<']
