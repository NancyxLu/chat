import os

def read_file(filename):
	contant = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			contant.append(line.strip())
	return contant

def assemble(contant):
	new = []
	who = None
	for line in contant:
		if line == 'Allen':
			who = 'Allen'
			continue
		elif line == 'Tom':
			who = 'Tom'
			continue
		if who != None:
			new.append(who + ': ' + line )
	print(new)
	return new
	
def Save_it(filename, new):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in new:
			f.write(line + '\n')
	
def main():
	contant = read_file('input1.txt')
	new = assemble(contant)
	Save_it('output1.txt',new)



if os.path.isfile('input1.txt'):
	print('找到聊天檔檔案，重新排版中:')
	main()
else:
	print('找不到聊天檔案')









