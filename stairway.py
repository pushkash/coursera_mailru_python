import sys

steps = int(sys.argv[1])

for step in range(steps):

    print (' ' * (steps - step - 1), '#' * (step + 1), sep = '')

    # line = ''
    #
    # blanks = steps - step
    #
    # for blank in range(1, blanks + 1):
    #     line += ' '
    #
    # for s in range(1, step + 1):
    #     line += '#'
    #
    # print(line)
