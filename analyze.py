#!/usr/bin/env python

from textblob import TextBlob

string = TextBlob("This is my birthday!")
print(TextBlob.tokenize(string))
print(string.parse())
