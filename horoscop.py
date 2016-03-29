# -*- coding: utf-8 -*-
import urllib2
print ('Welcome to the text game horoscop')
name = raw_input('Enter your name: ')
while len(name) == 0 or not name.isalpha():
    print ("You don't fool me")
    name = raw_input('Enter your name: ')
else:
    if len(name) > 0 and name.isalpha():
        print ("Hello", name)
    else:
        quit(1)
year = input('How old arr you? ')
if year >= 8:
    if year >= 99:
        print ("You too old for this game")
        quit(1)
elif year <= 18:
    print ("You too yang for this game")
    quit()
elif year.isalpha():
    print ("Something wrong with your age ")
    year = input('How old arr you? ')
else:
    print ("Somsing wrong with you age ")
    year = input('How old arr you? ')
print("Ok")
znak = []
month_birthday = raw_input('In what month you were born : ')
birthday = input('And day of you\'r birthday :')
z = []
print z
if month_birthday in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                      'September', 'October', 'November', 'December'] and birthday in range(1, 31):
    if month_birthday == 'March' and birthday in range(21, 31):
        znak = 'Aries'
    elif month_birthday == 'April' and birthday in range(1, 20):
        znak = 'Aries'
    elif month_birthday == 'April' and birthday in range(20, 31):
        znak = 'Taurus'
    elif month_birthday == 'May' and birthday in range(1, 21):
        znak = 'Taurus'
    elif month_birthday == 'May' and birthday in range(21, 31):
        znak = 'Gemini'
    elif month_birthday == 'June' and birthday in range(1, 22):
        znak = 'Gemini'
    elif month_birthday == 'June' and birthday in range(22, 31):
        znak = 'Cancer'
    elif month_birthday == 'July' and birthday in range(1, 23):
        znak = 'Cancer'
    elif month_birthday == 'July' and birthday in range(23, 31):
        znak = 'Leo'
    elif month_birthday == 'August' and birthday in range(1, 23):
        znak = 'Leo'
    elif month_birthday == 'August' and birthday in range(23, 31):
        znak = 'Virgo'
    elif month_birthday == 'September' and birthday in range(1, 23):
        znak = 'Virgo'
    elif month_birthday == 'September' and birthday in range(23, 31):
        znak = 'Libra'
    elif month_birthday == 'October' and birthday in range(1, 23):
        znak = 'Libra'
    elif month_birthday == 'October' and birthday in range(23, 31):
        znak = 'Scorpio'
    elif month_birthday == 'November' and birthday in range(1, 22):
        znak = 'Scorpio'
    elif month_birthday == 'November' and birthday in range(22, 31):
        znak = 'Sagittarius'
    elif month_birthday == 'December' and birthday in range(1, 22):
        znak = 'Sagittarius'
    elif month_birthday == 'December' and birthday in range(22, 31):
        znak = 'Capricorn'
    elif month_birthday == 'January' and birthday in range(1, 20):
        znak = 'Capricorn'
    elif month_birthday == 'January' and birthday in range(20, 31):
        znak = 'Aquarius'
    elif month_birthday == 'February' and birthday in range(1, 19):
        znak = 'Aquarius'
    elif month_birthday == 'February' and birthday in range(19, 31):
        znak = 'Pisces'
    elif month_birthday == 'March' and birthday in range(1, 21):
        znak = 'Pisces'
else:
    print ("Somsing wrong with you month or day of born ")
    month_birthday = raw_input('In what month you were born : ')
    birthday = input('And day of you\'r birthday :')

print(month_birthday, birthday)
print ('You ar ', znak)
print('An you horoskop for today')

if znak == 'Pisces':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/pisces.html')
    contents = c.read()
    print contents[1915:2065]
elif znak == 'Aquarius':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/aquarius.html')
    contents = c.read()
    print contents[1920:2095]
elif znak == 'Sagittarius':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/sagittarius.html')
    contents = c.read()
    print contents[1927:2095]
elif znak == 'Capricorn':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/capricorn.html')
    contents = c.read()
    print contents[1915:2075]
elif znak == 'Leo':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/Leo.html')
    contents = c.read()
    print contents[1915:2075]
elif znak == 'Virgo':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/Virgo.html')
    contents = c.read()
    print contents[1920:2095]
elif znak == 'Libra':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/Libra.html')
    contents = c.read()
    print contents[1927:2095]
elif znak == 'Scorpio':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/Scorpio.html')
    contents = c.read()
    print contents[1915:2075]
elif znak == 'Cancer':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/pisces.html')
    contents = c.read()
    print contents[1915:2075]
elif znak == 'Gemini':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/aquarius.html')
    contents = c.read()
    print contents[1920:2085]
elif znak == 'Taurus':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/sagittarius.html')
    contents = c.read()
    print contents[1927:2095]
elif znak == 'Aries':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/capricorn.html')
    contents = c.read()
    print contents[1915:2075]
elif znak == 'Leo':
    c = urllib2.urlopen('http://www.astrology.com/horoscope/daily/Leo.html')
    contents = c.read()
    print contents[1915:2075]
else:
    quit
print('Thank\'s for you chois', name)
