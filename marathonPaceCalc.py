# Program to help a runner calculate expected marathon pace with one of several methods
import datetime
# Ask the user which method they want to use (Magic Mile, Yasso 800, half marathon, 5k); get their answer as input
print("""Hello runner! I'm going to help you project your
 marathon pace based on some information you already know
 (or that you can figure out by going for a run)
 Type "Yasso", "Magic Mile", "5k", or "Half"
 For descriptions of each method, type "Help\"""")

method = input()

# Based on answer, start the calculation. This will be 4 elif blocks, each asking for more input and doing the calcuations
if method == 'Yasso':
    print("""Great! Now for the fun part - you need to run 800m 10 times, with a 400m
    jog as a break between each set. Time all the 800m runs Once you've done that, type
    in the average of all those 800m runs in the format 'm:ss':""")
    yassoAvg = input()
    # Convert m:ss to h:mm
    marathonTime = datetime.timedelta(hours=int(yassoAvg[0:1]), minutes=int(yassoAvg[-2:]))

elif method == 'Magic Mile':
    print("""Good choice! Go run a mile as fast as you can, and enter your time here in the
    format 'm:ss'""")
    magicMile = input()
    marathonTime = datetime.timedelta(minutes=int(magicMile[0:1]), seconds=int(magicMile[-2:])) * 1.3 * 26.2

elif method == '5k':
    print('0')

elif method == 'Half':
    print('0')

elif method == 'Help':
    print('0')

else:
    print('0')

# Print projected pace (marathon time, mile time)
marathonPace = marathonTime / 26.2
print('Based on your input, you should aim to complete your race in %s, which is a %s pace' % (str(marathonTime), str(marathonPace)))
