import re, sys

en = {
	'A':	'2',
	'B':	'22',
	'C':	'222',
	'D':	'3',
	'E':	'33',
	'F':	'333',
	'G':	'4',
	'H':	'44',
	'I':	'444',
	'J':	'5',
	'K':	'55',
	'L':	'555',
	'M':	'6',
	'N':	'66',
	'O':	'666',
	'P':	'7',
	'Q':	'77',
	'R':	'777',
	'S':	'7777',
	'T':	'8',
	'U':	'88',
	'V':	'888',
	'W':	'9',
	'X':	'99',
	'Y':	'999',
	'Z':	'9999',
	' ':	'#',
}

de = {}
for k, v in en.items():
	de[v] = k

def clean(text):
	t = text.split('-')[:-1]
	text = ''
	i = 0
	while 1:
		try:
			if t[i][-1] == t[i+1][0]:
				t[i] += 'P'
			text += t[i]+'-'
		except IndexError: 
			text += t[i]
			break
		i += 1
	return text

def code(line):
	num = re.compile('[0-9]')
	if num.match(line): return decode(line.strip('\n').split('-'))
	else: 
		return clean(encode(line))

def decode(l):
	ch = l
	length = len(ch)
	if length <= 1:
		if ch[0].find('P') > -1: ch[0] = ch[0].strip('P')
		try:
			return de[ch[0]]
		except IndexError: return ''
	elif length == 0: pass
	else:
##############################################################
###############Divide and Conquer#############################
		return decode(ch[0:length/2])+decode(ch[(length/2):])
#############################################################
#############################################################
			
def encode(l):
	length = len(l)
	if length <= 1:
		try:
			return en[l[0]]
		except KeyError:
			return ''
		except IndexError:
			return ''
	else: 
##############################################################
###############Divide and Conquer#############################
		return encode(l[0:length/2])+'-'+encode(l[(length/2):])
#############################################################
#############################################################

if __name__ == '__main__':
	fin = open('p7_input')
	fout = open('p7_output', 'w')
	for line in fin.readlines():
		if line == '*': sys.exit() 
		fout.write(code(line))
		fout.write('\n')
		print code(line)

