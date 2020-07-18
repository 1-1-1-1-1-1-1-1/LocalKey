import os
from time import sleep
from sys import exit as sys_exit


RUN_MODE = 2
SLEEP_FOR = 60  # Seconds


def main():
    with open('Unsolved.txt') as f:
        files = f.read().split('\n')

    def info(j):
        with open('pictures_savings/' + j, 'rb') as f, \
            open('pictures_savings/' + j, 'rb') as g:
            return f.read().count(b'\n')  # It seems to be not really great:
                                          # does it really counts a number
                                          # of lines in the file?

    for j in files:
        print(j, info(j), sep=': ')

    #t:  print(info('00f0446c4ff0a9d72008d744aee94f0b.png'))
    return


if RUN_MODE == 1:
    main()


if RUN_MODE == 2:
    counter = 1
    try:
     while True:
        print("=== Attempt number {:=<4}==================".format(str(counter) + ' '))
        main()
        print()
        sleep(SLEEP_FOR)
        counter += 1
    except KeyboardInterrupt:
        sys_exit(input('Stopped. '))


input('Ready with it.')
