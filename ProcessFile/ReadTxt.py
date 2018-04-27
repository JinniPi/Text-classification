import re
result = []
count = 1
with open('new_word.txt','r', encoding='utf-8') as f:
	f_w = open('new_word(1).txt','w',encoding='utf-8')
	for i in range(1,2000):
		line = f.readline()
		if re.match(r'#',line,re.M|re.I) != None:
		 line = re.sub(r'#','',line)
		 print(type(line))
		 f_w.write(line)
	f_w.close()
#f.close()
# f_w = open('new_word(1).txt','w',encoding='utf-8')
#   for i in result:
# 	f_w.wirte(i+'\n')
# f_w.close()