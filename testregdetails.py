#!/usr/bin/env python


#-----------------------------------------------------------------------
# testregdetails.py
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
       print('Usage: ' + sys.argv[0] + ' regdetailsprogram',
             file=sys.stderr)
       sys.exit(1)


   program = sys.argv[1]


   # Valid class ID tests
   exec_command(program, '8321')  # Basic class lookup
   exec_command(program, '9032')  # Another class
   exec_command(program, '8293')  # Test different class
   exec_command(program, '9977')  # Test class with different structure
   exec_command(program, '9012')  # Test another format
   exec_command(program, '10188')  # Test larger class ID


   # Test classes with special cases
   exec_command(program, '8745')  # Class with multiple professors
   exec_command(program, '9156')  # Class with no professors
   exec_command(program, '8901')  # Class with multiple crosslistings
   exec_command(program, '9234')  # Class with long description
   exec_command(program, '9567')  # Class with special characters in title


   # Error handling tests
   exec_command(program, '')  # Missing classid
   exec_command(program, '8321 9032')  # Too many arguments
   exec_command(program, 'abc123')  # Invalid classid format
   exec_command(program, '9034')  # Non-existent classid
   exec_command(program, '-h')  # Help message
   exec_command(program, '--help')  # Long form help
   exec_command(program, '-8321')  # Negative number
   exec_command(program, '8321.5')  # Decimal number


   # Test boundary cases
   exec_command(program, '0')  # Test with zero
   exec_command(program, '99999')  # Test with very large number
   exec_command(program, ' 8321')  # Leading space
   exec_command(program, '8321 ')  # Trailing space


if __name__ == '__main__':
   main()
