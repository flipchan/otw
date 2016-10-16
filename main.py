#/*
# * ----------------------------------------------------------------------------
# * "THE BEER-WARE LICENSE" (Revision 42):
# * <flipchan@riseup.net> wrote this file. As long as you retain this notice you
# * can do whatever you want with this stuff. If we meet some day, and you think
# * this stuff is worth it, you can buy me a beer in return Filip Kälebo
# * ----------------------------------------------------------------------------
# */
#python off the record crypto with pgp instead of diffie hellman
#inspierd by https://github.com/python-otr/
#build to provide stronger crypto in the LayerProx project


from Crypto.Hash import SHA256 as _SHA256
from Crypto.Hash import SHA as _SHA1
from Crypto.Hash import HMAC as _HMAC

import gnupg
home = '' #set gpg homedir
gpg = gnupg.GPG(homedir=home)
gpg.encoding = 'utf-8'
fingerprint = ''#fingerprint 
password = ''#gpg passwd

#note: i does not know everything about crypto i am no expert on this is, i only do crypto as a hobby 
#i would probelly not recommend implementing this without modifying the code, anyhow this is -->
#my own version of otr(off the record) i call it otw(off the wire), crypto = pgp with sha256hmac160
#in python-otr u only get a 1024 dsa key and i think that is bad so i added pgp support
#import thisfile the run justencrypt() justdecrypt()
#



data = 'test'#test input
key1 = '1234'#hmac key 1
key2 = '4321'#hmac key 2

def SHA256(data):
    return _SHA256.new(data).digest()

def HMAC(key, data, mod):
    return _HMAC.new(key, msg=data, digestmod=mod).digest()

def SHA256HMAC(key, data):
    return HMAC(key, data, _SHA256)

def SHA256HMAC160(key, data):
    return SHA256HMAC(key, data)[:20]


#gpg fingerprint
def justencrypt(key1, key2, data, fingerprint):
	#pgp
	thedata = gpg.encrypt()
	#sha256hmac160
	#thedate = str(thedata) + SHA256HMAC160(key1, key2)#just gen a hmac
	thedata = str(SHA256HMAC160(key1, key2)) + str(thedata)
	#output
	return thedata

#gpg passwd define
def justdecrypt(key1, key2, data, password):
	#decrypt it
	#verify the hmac
	odata = data
	s = data
	s[:16] = hdata  #pic the first 16chars which should be the hmac
	hdata = str(hdata)
	theh = str(SHA256HMAC160(key1, key2))
	#if the hmac is hmac / verify the hmac
	if theh == hdata:
		#if the hmac is true verify it 
		s = s[16:] #remove hmac
		s = str(s)
		data = gpg.decrypt(s, passphrase=password)
		return data
	else:#if the hmac is false break *
		break
		