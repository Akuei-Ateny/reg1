#!/usr/bin/env python


"""Registrar application: show details about a class."""


import sys
import argparse
import textwrap
from database import get_class_details, DatabaseError




def parse_args():
   """Parse command line arguments.


   Returns:
       argparse.Namespace: Parsed command line arguments
   """
   parser = argparse.ArgumentParser(
       description='Registrar application: show details about a class')
   parser.add_argument('classid',
                       help='the id of the class whose details should be shown')
   return parser.parse_args()




def format_details(details):
   """Format the class details for display.


   Args:
       details (tuple): Tuple containing class details, crosslistings, and professors
   """
   if not details:
       return False


   basic_info, crosslistings, professors = details
   (classid, courseid, days, starttime, endtime, bldg, roomnum,
    area, title, descrip, prereqs) = basic_info


   # Print class details
   print('Class Details')
   print('-------------')
   print('Class Id:', classid)
   print('Course Id:', courseid)
   print('Days:', days if days else '')
   print('Start time:', starttime if starttime else '')
   print('End time:', endtime if endtime else '')
   print('Building:', bldg if bldg else '')
   print('Room:', roomnum if roomnum else '')
   print('--------------')


   # Print cross-listings
   print('Course Details')
   print('--------------')
   for dept, coursenum in crosslistings:
       print('Dept and Number: ' + f'{dept} {coursenum}')
   # Print area and title
   print('Area:', area if area else '')
   print('Title:', title)


   # Print description
   if descrip:
       wrapped_desc = textwrap.wrap(descrip, width=72)
       print('Description: ' + '\n'.join(wrapped_desc))


   # Print prerequisites
   if prereqs:
       wrapped_prereqs = textwrap.wrap(prereqs, width=72)
       print('Prerequisites: ' + '\n'.join(wrapped_prereqs))


   # Print professors
   for (profname,) in professors:
       print('Professor: ' + profname)


   return True




def main():
   """Main function to run the program."""
   args = parse_args()


   try:
       details = get_class_details(args.classid)
       if not format_details(details):
           print(f"{sys.argv[0]}: no class with classid {args.classid} exists",
                 file=sys.stderr)
           sys.exit(1)
       sys.exit(0)
   except DatabaseError as error:
       print(f"{sys.argv[0]}: {str(error)}", file=sys.stderr)
       sys.exit(1)




if __name__ == '__main__':
   main()
