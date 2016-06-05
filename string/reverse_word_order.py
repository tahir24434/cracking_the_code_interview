import sys


def reverse(sentence):
    sentence = 'This is a string to try'
    answer = ''
    temp = ''
    for char in sentence:
        if char != ' ':
            temp += char
        else:
            answer = temp + ' ' + answer
            temp = ''
    answer = temp + ' ' + answer
    print (answer)

reverse("This is a string to try")