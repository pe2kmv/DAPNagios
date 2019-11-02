# import some magic stuff
import configparser
import argparse
import logging
import requests
import json
import sys

from functions import StrToBool
# done with libraries

# setup some important vars
config = configparser.ConfigParser()
parser = argparse.ArgumentParser()
parser.add_argument('-r','--recepient',help='DAPNET subscriber')
parser.add_argument('-m','--message',help='Message to send via pager')
parser.add_argument('-t','--txgroup',help='Define TX group to use')
parser.add_argument('-e','--emergency',help='Set emergency call (True/False)')
args = parser.parse_args()
# end setup variables

# read configuration
config.read('DAPNagios.cfg')
dapUser = config['DAPNET.USER']['dapnet_username']
dapPW = config['DAPNET.USER']['dapnet_password']
dapURI = config['DAPNET-SERVER']['dapnet_base_uri']
dapPort = config['DAPNET-SERVER']['dapnet_port']
dapDIR = config['DAPNET-SERVER']['dapnet_directory']
sysLogPath = config['SYSTEM']['log_path']
sysLogLevel = int(config['SYSTEM']['log_level'])
sysLogOn = config['SYSTEM']['log_on']
full_uri = dapURI + ':' + dapPort + '/' + dapDIR
# done reading configuration

# init logging
def switchLogLevel(argument):
	switcher = {
		1: 'DEBUG',
		2: 'INFO',
		3: 'WARNING',
		4: 'ERROR',
		5: 'CRITICAL'
	}
	return switcher.get(argument)
logging.basicConfig(filename=sysLogPath,format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()
logger.setLevel(switchLogLevel(sysLogLevel))
# end init logging

# check if all arguments have been completed
if args.recepient == None:
	logging.critical('No recepient defined - No message sent')
	sys.exit()
if args.message == None:
	logging.critical('No text body defined - No message sent')
	sys.exit()
if args.txgroup == None:
	logging.critical('No TX group defined - No message sent')
	sys.exit()
if args.emergency == None:
	logging.warning('No emergency flag defined - Message sent with default priority')
	args.emergency = False
# end argument check

# trim all necessary variables to a usable format
args.recepient = str(args.recepient).lower()
args.txgroup = str(args.txgroup).lower()
if isinstance(args.emergency,bool) == False:
	args.emergency = StrToBool(args.emergency.capitalize())
# end trimming vars

# function to send actual pager message
def send_page(msg_sub,func,trx,emr,msgtxt):
	logging.debug(full_uri)
	logging.debug(dapUser)
	logging.debug(dapPW)
	logging.debug(msg_sub)
	logging.debug(func)
	logging.debug(trx)
	logging.debug(emr)
	logging.debug(msgtxt)
	req = requests.post(full_uri,auth=(dapUser,dapPW),json={'text':msgtxt,'callSignNames':[msg_sub],'transmitterGroupNames':[trx],'emergency':emr})
	if req.status_code == 201:
		logging.info(req)
	else:
		logging.critical(req)

# end send page

send_page(args.recepient,3,args.txgroup,args.emergency,args.message)
