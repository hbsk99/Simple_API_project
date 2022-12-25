# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def funct1():
    import requests as req
    response = req.get('https://official-joke-api.appspot.com/random_joke')
    joke = response.json()
    print(joke['setup'],joke['punchline'])


