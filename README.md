# Stemming
Implement stemming in python using Porter stemming algorithm.

## Introduction
NLTK module provides a stemming function, and it is very convenient.    
However, it does not help for us to understand the principle of stemming.     
Thus, I did not use the module and implemented it based on the **porter stemming algorithm**.

I refer to the paper, which was released in 1980.    
<http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.848.7219&rep=rep1&type=pdf>

## What is stemming?
In linguistic, stemming is the process of reducing inflected words to their word stem.    
If the word is 'cats', remove 's' and make it as 'cat' which is a stem of the word.  
The stem need not to be identical to the morphological root of the word. e.g. irritant -> irrit