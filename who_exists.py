#! /usr/bin/python

"""
parse /etc/passwd to print a list of all usernames

TODO debug: doesnt show users jon and jonr1 on my macbook air
(I think the cause is that mac uses some auth system that circumvents /etc/passwd)
"""


import sys # sys.argv
import optparse # optparse.OptionParser class
import os # os.system
import subprocess # .call and .check_output
import tempfile # tempfile.NamedTemporaryFile class


# Console LOG
def clog(*myargs):
    # print myargs
    pass


with open('/etc/passwd', 'r') as f:
    for line in f.readlines():
        clog (line)
        clog (line.find(':'))
        clog ("HAD")

        loc_first_comment = line.find('#')
        loc_first_colon = line.find(':')

        loc_second_token = None
        #
        if loc_first_comment != -1:
            loc_second_token = loc_first_comment
            clog ("KUNG", loc_second_token)
        #
        if loc_first_colon != -1:
            if loc_second_token is None or loc_first_colon < loc_second_token:
                loc_second_token = loc_first_colon
                clog ("FU", loc_second_token)

        clog ("NINJA", loc_second_token)

        if loc_second_token > 0:
            first_token = line[0:loc_second_token]
            username = first_token
            #
            print username

# end with

