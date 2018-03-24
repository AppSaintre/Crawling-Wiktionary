import urllib
import urllib.request as req
import re
import sys, os
import json
import time

base_url = 'https://en.wiktionary.org/wiki/'

hex_tbl = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
def stripNUbyte(cont):
	clist = list(cont)
	ctr = 0
	bnd = len(clist)
	for it in clist:
		flg = (it=='\\')and((ctr+3)<bnd)and(clist[ctr+1]=='x')and(clist[ctr+2] in hex_tbl)and(clist[ctr+3] in hex_tbl)
		if(flg):
			clist[ctr] = ''
			clist[ctr+1] = ''
			clist[ctr+2] = ''
			clist[ctr+3] = ''
		ctr = ctr + 1
	return ''.join(clist)

def getRaw(keyword):
	url = base_url + keyword 
	try:
		resp = req.urlopen(url)
	except urllib.error.HTTPError as e:
		return ''
	cont = resp.read()
	resp.close()
	return str(cont)

def getFineDesc(keyword,content,cleaner):
	pat_strt1 = '"Latn headword" lang="en">'
	pat_strt2 = '"Latn headword" lang="en" xml:lang="en">'
	pat_end = '(.*?)/ol'
	res = re.findall(pat_strt1+keyword+pat_end,content)
	res1 = re.findall(pat_strt2+keyword+pat_end,content)
	ftxt = ''
	for r in res:
		ftxt = ftxt + r
	for r in res1:
		ftxt = ftxt + r
	ftxt = re.sub(cleaner, '', ftxt)
	ftxt = ftxt.replace('\\n','')
	ftxt = stripNUbyte(ftxt)
	return ftxt

def tstWebAPI(key):	
	rawhtml = getRaw(key)
	clr = re.compile('<.*?>|<|>')
	return getFineDesc(key,rawhtml,clr)

def wikt2json(list,fname):
	start = time.time()
	clr = re.compile('<.*?>|<|>')	
	d = {}
	totwk, crtwk, ctr = len(list), 0 ,0
	print("Download 0.00%...")
	for k in list:
		desc = getFineDesc(k,getRaw(k),clr)
		if(desc!=''):
			d[k], crtwk, ctr = desc, crtwk + 1, ctr + 1
			print('Write ',k,' in Dictionary')
		else:
			totwk = totwk - 1
		if ctr == 100:
			ctr, prc = 0, float(crtwk*100/totwk)
			print("Download ",str(prc)[0:4],"%...")
	with open(fname, 'w+') as fp:
		json.dump(d, fp)
	end = time.time()
	print("Download ",crtwk," words in ",(end-start), " seconds")
		
def dlDictByltr(ltr,bdir_in,bdir_out):
	fnin = bdir_in + ltr + '.txt'
	fnout = bdir_out + ltr + '.json'
	lst = []
	raw_ttw = 0
	with open(fnin,'r') as fh:
		for word in fh:
			lst.append(word[0:-1])
	print("Begin to crawl...")
	wikt2json(lst,fnout)
	
if __name__=="__main__":
	op_mode = ['-lookup','-download']
	if len(sys.argv)<3:
		print('Command Format: python wiktcrl.py [-lookup|-download] [keyword|keyletter]')
		sys.exit(0)
	opm = sys.argv[1]
	kw = sys.argv[2]
	if opm == op_mode[0]:
		res = tstWebAPI(kw)
		if res=='':
			print('No Definition for ', kw, ' in Wiktionary (Online)')
		else:
			print('Definition for ', kw, ' in Wiktionary (Online)')
			print(res)
	elif opm == op_mode[1]:
		bdin = './word_list/' + kw[0] + '/'
		bdout = './word_dict/' + kw[0] + '/'
		for fn in os.listdir(bdin):
			fname = str(fn)
			depos = fname.find('.')
			dlDictByltr(fname[0:depos],bdin,bdout)
	else:
		print('Command Format: python wiktcrl.py [-lookup|-download] [keyword|keyletter]')