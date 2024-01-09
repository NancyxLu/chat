import os

def read_file(filename):
	contant = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			contant.append(line.strip())
	return contant

def assemble(contant):
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in contant:
		c = line.split(' ')
		time = c[0]
		who = c[1]
		word = c[2:]
		if who == 'Allen':
			if c[2] == '貼圖':
				allen_sticker_count += 1
			elif c[2] == '圖片':
				allen_image_count += 1
			else:
				allen_word_count = allen_word_count + len(word)
		if who == 'Viki':
			if c[2] == '貼圖':
				viki_sticker_count += 1
			elif c[2] == '圖片':
				viki_image_count += 1
			else:
				viki_word_count = viki_word_count + len(word)
	result = [allen_word_count, allen_image_count, allen_sticker_count, viki_word_count, viki_image_count, viki_sticker_count]			
	return result

def Save_it(filename, result):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		f.write('{},{},{}\n'.format('allen說了', result[0], '句話'))
		f.write('{},{},{}\n'.format('allen傳了', result[1], '個貼圖'))
		f.write('{},{},{}\n'.format('allen傳了', result[2], '張圖片'))
		f.write('{},{},{}\n'.format('viki說了', result[3], '句話')) 
		f.write('{},{},{}\n'.format('viki說了', result[4], '個貼圖'))
		f.write('{},{},{}\n'.format('viki說了', result[5], '張圖片'))

		# f.write('{},{},{}\n'.format('allen說了', result[0], '句話'))
		# f.write('{},{},{}\n'.format('allen傳了', result[1], '個貼圖'))
		# f.write('{},{},{}\n'.format('allen傳了', result[2], '張圖片'))
		# f.write('{},{},{}\n'.format('viki說了', result[3], '句話')) 
		# f.write('{},{},{}\n'.format('viki說了', result[4], '個貼圖'))
		# f.write('{},{},{}\n'.format('viki說了', result[5], '張圖片'))

def main():
	contant = read_file('LINE-Viki.txt')
	result = assemble(contant)
	print(result)
	Save_it('calculation.txt', result)


if os.path.isfile('LINE-Viki.txt'):
	print('找到聊天檔檔案，已重新計算:')
	main()
else:
	print('找不到聊天檔案')

