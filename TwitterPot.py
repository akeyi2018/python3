#coding: UTF-8
import os
from twython import Twython, TwythonError

API_Key = "用意したAPIkey"
API_Secret = "用意したAPIsecret"
Access_Token = "用意したAccessToken"
Access_Token_Secret = "用意したAccess token Secret"

twitter = Twython(API_Key, API_Secret, Access_Token,　Access_Token_Secret)

timestamp = 'date +%F@%H:%M'
time = os.popen(timestamp).readline().strip()

try:
	twitter.update_status(status=time+\
                              '\n おはようございます！'\
                              '\n www.rgm79sf.site'\
                              '\n from raspberry Pi')

except TwythonError as e:

	print error
