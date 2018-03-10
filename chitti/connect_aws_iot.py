
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)


# Read in command-line parameters
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--endpoint", action="store", required=True, dest="host", help="Your AWS IoT custom endpoint")
parser.add_argument("-r", "--rootCA", action="store", required=True, dest="rootCAPath", help="Root CA file path")
parser.add_argument("-c", "--cert", action="store", dest="certificatePath", help="Certificate file path")
parser.add_argument("-k", "--key", action="store", dest="privateKeyPath", help="Private key file path")
parser.add_argument("-id", "--deviceId", action="store", dest="deviceId", help="Targeted client id")

parser.add_argument("-t", "--topic", action="store", dest="topic", default="sdk/test/Python", help="Targeted topic")

args = parser.parse_args()
host = args.host
rootCAPath = args.rootCAPath
certificatePath = args.certificatePath
privateKeyPath = args.privateKeyPath
deviceId = args.deviceId
topic = args.topic

if not args.host:
	parse.error("Missing Host, Your AWS IoT custom endpoint.")
	exit(2)

if not args.rootCAPath:
	parser.error("Missing Root CA Path")
	exit(2)

if not args.deviceId:
    parser.error("Missing Device Id ")
    exit(2)

if  not args.certificatePath:
    parser.error("Missing device certificate path for authentication.")
    exit(2)

if  not args.privateKeyPath:
	parser.error("Missing device private key file path for authentication.")
	exit(2)


