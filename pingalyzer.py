'''
Author: awhitehttr@gmail.com
desc:
This is a little tool I'm writing to learn Python. It does (or will) analyze ping...feel free to modify or contribute.
Also, I'm learning Pythonon the fly, so any coding best practices advice you have, please share. 
'''


import sys, os, re
#in Python3.3 there's a sick module called "ipaddress", Nix hasn't pulled 3.3 into the reps and I don't feel like forcing that on people. 
#import ipaddress
 
logo = '''
 ____ ____  ____    ____   ____  _      __ __  _____    ___  ____  
|    \    ||    \  /    | /    || |    |  |  ||     |  /  _]|    \ 
|  o  )  | |  _  ||   __||  o  || |    |  |  ||__/  | /  [_ |  D  )
|   _/|  | |  |  ||  |  ||     || |___ |  ~  ||   __||    _]|    / 
|  |  |  | |  |  ||  |_ ||  _  ||     ||___, ||  /  ||   [_ |    \ 
|  |  |  | |  |  ||     ||  |  ||     ||     ||     ||     ||  .  \\
|__| |____||__|__||___,_||__|__||_____||____/ |_____||_____||__|\_|
                                                                   
 
 
'''
 
print(logo)
 
#Formatting in M$ an Nix Ping replies varies, for now sticking with Nix. 
print('''\n\n***********************************************************************************
****  Important!!!! At this time, PINGALYZER only works on Nix w/Python 3 ****
***********************************************************************************\n\n''')
 
while True: 
  i1 = input('Please enter the Host IP Address: ')
	try:
		#below line only works in ipaddress module in python3.3
		#host = ipaddr.ip_address(i1)
		reggie = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
		host = reggie.match(i1)
		if host:
			break
		else:
			print('Fail Whale! You did not enter a valid IP address YO!')
			continue
	except:
		print('Fail Whale! You did not enter a valid IP address YO!')
		continue
 
while True:
	try:
		pgx = input('How many times would you like to ping this host? \nEnter [c] for continuous: ')
		if pgx[0] == 'c':
			print('\nWe will now ping {0} continuously...'.format(i1))
			os.system('/bin/ping {0}'.format(i1))
			break
		else:
			pgx = int(pgx)
			print('\nWe will now ping {0} {1} times...'.format(i1,pgx))
			os.system('ping {0} -c {1}'.format(i1, pgx))
			break
	except:
    		print('\nPlease enter either a valid number or "c".\n')
    		continue
 
 
exit()
