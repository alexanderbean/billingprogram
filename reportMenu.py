# ------------------------------------------------------------------
# Author: Alexander Bean & Raj Khanderia
# Program:
#
# Description:
# This is the menu module that ties all modules together. Includes
# main calls to write billing info and to build the ad hoc report.
# ------------------------------------------------------------------

import reportWrite as repWrite, reportAdHoc as repAdHoc, reportFunctions as repFunc

def main():
    loopControl = True
    while loopControl:
        try:
            print('\nBilling System Menu:\n')
            print('\t0 - End')
            print('\t1 - Enter billing data')
            print('\t2 - Display ad-hoc billing report')

            option = int(input('\nOption ==> '))

            if option == 0:
                loopControl = False
            elif option == 1:
                repWrite.main()
            elif option == 2:
                repAdHoc.main()
            else:
                print('Please enter an available option.\n')

        except ValueError:
            print('Please enter an available option.\n')
            
    print('\nMenu ended successfully')

main()
