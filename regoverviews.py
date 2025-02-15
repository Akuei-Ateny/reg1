#!/usr/bin/env python


"""Registrar application: show overviews of classes."""


import sys
import argparse
import textwrap
from database import get_class_overviews, DatabaseError




def parse_args():
   """Parse command line arguments.


   Returns:
       argparse.Namespace: Parsed command line arguments
   """
   parser = argparse.ArgumentParser(
       description='Registrar application: show overviews of classes.')
   parser.add_argument('-d', metavar='dept',
                       help='show only those classes whose department contains dept')
   parser.add_argument('-n', metavar='num',
                      help='show only those classes whose courses contain num')
   parser.add_argument('-a', metavar='area',
                       help='show only those classes whose area contains distribution area')
   parser.add_argument('-t', metavar='title',
                       help='show only those classes whose title contains title')
   args = parser.parse_args()
   return args


def format_output(rows):
   """Format the output as a table with wrapped text.


   Args:
       rows (list): List of tuples containing class data
   """


   if not rows:
       return


   print('ClsId Dept CrsNum Area Title')
   print('----- ---- ------ ---- -----')


   for row in rows:
       classid, dept, coursenum, area, title = row


       line = f'{classid:5} {dept:4} {coursenum:6} {area:4} {title}'
       wrapped = textwrap.wrap(line, width=72, subsequent_indent=' ' * 23)
       print('\n'.join(wrapped))


def main():
   """Main function to run the program."""
   args = parse_args()


   try:
       rows = get_class_overviews(args.d, args.n, args.a, args.t)
       format_output(rows)
       sys.exit(0)
   except DatabaseError as error:
       print(f"{sys.argv[0]}: {str(error)}", file=sys.stderr)
       sys.exit(1)


if __name__ == '__main__':
   main()
