import reportWrite as rw, reportBuild as rb, reportFunctions as rf

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
                rw.main()
            elif option == 2:
                rb.main()
            else:
                print('Please enter an available option.\n')

        except ValueError:
            print('Please enter an available option.\n')
            
    print('\nMenu ended successfully')

main()
