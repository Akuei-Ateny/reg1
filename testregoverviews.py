#!/usr/bin/env python


#-----------------------------------------------------------------------
# testregoverviews.py
# Author: Bob Dondero
#-----------------------------------------------------------------------


import os
import sys


#-----------------------------------------------------------------------


MAX_LINE_LENGTH = 72
UNDERLINE = '-' * MAX_LINE_LENGTH


#-----------------------------------------------------------------------


def print_flush(message):
   print(message)
   sys.stdout.flush()


#-----------------------------------------------------------------------


def exec_command(program, args):


   print_flush(UNDERLINE)
   command = 'python ' + program + ' ' + args
   print_flush(command)
   exit_status = os.system(command)
   if os.name == 'nt':  # Running on MS Windows?
       print_flush('Exit status = ' + str(exit_status))
   else:
       print_flush('Exit status = ' + str(os.WEXITSTATUS(exit_status)))


#-----------------------------------------------------------------------


def main():
   if len(sys.argv) != 2:
       print('usage: ' + sys.argv[0] + ' regprogram', file=sys.stderr)
       sys.exit(1)


   program = sys.argv[1]


   # Basic functionality tests
   exec_command(program, '')  # Test with no arguments
   exec_command(program, '-d COS')  # Test department filter
   exec_command(program, '-n 333')  # Test course number filter
   exec_command(program, '-n b')    # Test partial course number
   exec_command(program, '-a Qr')   # Test area filter
   exec_command(program, '-t intro') # Test title filter
   exec_command(program, '-t science') # Test another title filter


   # Multiple parameter tests
   exec_command(program, '-d cos -n 3')  # Test department and number
   exec_command(program, '-d cos -a qr -n 2 -t intro')  # Test all parameters


   # Special character tests
   exec_command(program, '-t C_S')  # Test underscore in title
   exec_command(program, '-t c%S')  # Test percent in title
   exec_command(program, '-t "Independent Study"')  # Test spaces in title
   exec_command(program, '-t "Independent Study "')  # Test trailing space
   exec_command(program, '-t " Independent Study"')  # Test leading space
   exec_command(program, '-t "  Independent Study"')  # Test multiple spaces
   exec_command(program, '-t=-c')  # Test special characters


   # Error handling tests
   exec_command(program, 'a qr')  # Test invalid arguments
   exec_command(program, '-A qr')  # Test invalid flag
   exec_command(program, '"-a " qr')  # Test space in flag
   exec_command(program, '-a qr st')  # Test extra argument
   exec_command(program, '-a')  # Test missing argument value
   exec_command(program, '-a qr -d')  # Test missing value after flag
   exec_command(program, '-a -d cos')  # Test missing value between flags
   exec_command(program, '-x')  # Test unknown flag
#-----------------------------------------------------------------------


if __name__ == '__main__':
   main()
