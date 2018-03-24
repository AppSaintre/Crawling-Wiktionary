import urllib
import urllib.request as req
import re
import sys
import json
	
def divABlist(fname):
	fh = open(fname,'r')
	dict = {'a':[],'b':[],'c':[],'d':[],'e':[],
			'f':[],'g':[],'h':[],'i':[],'j':[],
			'k':[],'l':[],'m':[],'n':[],'o':[],
			'p':[],'q':[],'r':[],'s':[],'t':[],
			'u':[],'v':[],'w':[],'x':[],'y':[],'z':[]}
	hletters = ['a','b','c','d','e',
			'f','g','h','i','j',
			'k','l','m','n','o',
			'p','q','r','s','t',
			'u','v','w','x','y','z']
	for li in fh:
		dict[li[0]].append(li)
	fh.close()
	for hl in hletters:
		fname = './word_list/'+ hl + '/' + hl + '.txt'
		fh = open(fname,'w+')
		for aw in dict[hl]:
			fh.write(aw)
		fh.close()

def divBigFile(fname,n_pr):
	w_ctr = 0
	with open(fname,'r') as fh:
		for wd in fh:
			w_ctr = w_ctr + 1
	lines = int(w_ctr/n_pr)
	if lines==0:
		return
	fnum = 1
	w_ctr = 0
	parti = []
	with open(fname,'r') as fh:
		for wd in fh:
			if w_ctr==lines:
				fn = './word_list/' + fname[0] + str(fnum) + '.txt'
				with open(fn,'w+') as fhw:
					for word in parti:
						fhw.write(word)
				parti = []
				fnum = fnum + 1
				w_ctr = 0
			parti.append(wd)
			w_ctr = w_ctr + 1
	fn = './word_list/' + fname[0] + str(fnum) + '.txt'
	with open(fn,'w+') as fhw:
		for word in parti:
			fhw.write(word)
			
if __name__=="__main__":
	op_mode = ['-divAB','-divBig']
	if len(sys.argv)<3:
		print('Command Format: python wiktcrl.py [-divAB|-divBig] [filename] [partion]')
		sys.exit(0)
	opm = sys.argv[1]
	if opm == op_mode[0]:
		fn = sys.argv[2]
		divABlist(fn)
	elif opm == op_mode[1]:
		fn = sys.argv[2]
		par = sys.argv[3]		
		divBigFile(fn,par)