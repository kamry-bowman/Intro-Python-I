"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
from calendar import TextCalendar
from datetime import date

args = sys.argv
cal = TextCalendar()

if len(args) > 3:
    print('''Please provide one of the following:
    \n(a): no arguments, to get the current month
    \n(b): a single month argument, with jan = 1, to get that month of the current year
    \n(c): a month and a year argument, to get a calendar for that month year combination''')

else:
    try:
        if len(args) == 1:
            date = date.today()
            year = date.year
            month = date.month
        elif len(args) == 2:
            date = date.today()
            year = date.year
            month = int(args[1])
        elif len(args) == 3:
            month = int(args[1])
            year = int(args[2])

        print(cal.formatmonth(year, month))
    except:
        print('''An exception occured.
    \nPlease provide one of the following:
    \n(a): no arguments, to get the current month
    \n(b): a single month argument, with jan = 1, to get that month of the current year
    \n(c): a month and a year argument, to get a calendar for that month year combination''')
