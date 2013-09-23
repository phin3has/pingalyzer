'''
Author: AWhiteHatter 
Contact: awhitehttr@gmail.com
Description: Simple Ping script that I'm using to teach myself Python. Advice is welcomed. 
Version: 0.0 "Getting to know the ropes"

'''
import sys, os, platform, re

logo = '''
 ____ ____  ____    ____   ____  _      __ __  _____    ___  ____  
|    \    ||    \  /    | /    || |    |  |  ||     |  /  _]|    \ 
|  o  )  | |  _  ||   __||  o  || |    |  |  ||__/  | /  [_ |  D  )
|   _/|  | |  |  ||  |  ||     || |___ |  ~  ||   __||    _]|    / 
|  |  |  | |  |  ||  |_ ||  _  ||     ||___, ||  /  ||   [_ |    \ 
|  |  |  | |  |  ||     ||  |  ||     ||     ||     ||     ||  .  \\
|__| |____||__|__||___,_||__|__||_____||____/ |_____||_____||__|\_|
                                                                   


'''

print logo

ostype = platform.system()
print "You are using " + ostype + "\n"

print "What target would you like to ping today? \n"

target = raw_input('--> ')

#validate target is an actual IP Address
reggie = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
host = reggie.match(target)

if host:
	print ""
else:
	print "\nFail Whale, You didn't a enter a valid IPv4 Address YO!"
	raw_input('\nHit enter to exit\n\n')
	exit()

print "How many times would like to ping " + target + "?\n"

hits = int(raw_input('--> '))

print "\nWe will now ping %r a total of %r times:\n" % (target, hits)

#dirty exit from the script
raw_input('\nHit enter to exit\n\n')
exit()
