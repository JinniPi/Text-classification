import json
import os
import math
FJoin = os.path.join
class CreateDic:

	Dictionary = {}

	def __init__(self):
		self.Dictionary = {}

	#lấy danh sách các stopword
	def getStopWord(self,inputFile):
		stopWords = []
		with open(inputFile,'r', encoding='utf-8') as f:
			for i in range(1,1941):
				if i == 1:
					word = f.readline()
					word = word.replace('\ufeff','')
					word = word.replace('\n','')
					stopWords.append(word)
				else:
					word = f.readline()
					word = word.replace('\n','')
					stopWords.append(word)
		return stopWords
	#Lấy danh sách VB trong file đầu vào
	def readJson(self,inputFile):
		list_result = []
		with open(inputFile,encoding='utf-8') as jsondata:
			datas = json.load(jsondata)
			for data in datas:
				text = data["text"].lower()
				data_result = text
				list_result.append(data_result)
		return list_result
	#lấy tất cả file trong thư mục
	def GetFiles(self,path):

		file_list = []
		for dir, subdirs, files in os.walk(path):
			file_list.extend([FJoin(dir, f) for f in files])
		return file_list
	#Tạo từ điển cho từng VB
	def getDic_VB(self,str):
		dic_VB = set()
		list_word = str.split(' ')
		for word in list_word:
			if word != '': 
				dic_VB.add(word)
		return dic_VB
	#Tạo từ điển raw
	def get_Dic0(self,path):
		file_list = self.GetFiles(path)
		for file in file_list:
			print('đang mở file')
			list_VB = self.readJson(file)
			count_VB = 1
			for VB in list_VB:
				print('------- đang ở file------ : ',file)
				print('-------- đang ở VB--------: ',count_VB)
				count_VB = count_VB + 1
				dic_VB = self.getDic_VB(VB)
				for word in dic_VB:
					if word in self.Dictionary:
						 self.Dictionary[word]=self.Dictionary.get(word)+1
						
					else:
						self.Dictionary[word] = 1
		print(len(self.Dictionary))
		return self.Dictionary
	#tra ve từ điển loại stopword
	def get_Dic1(self):
		list_stop_word = self.getStopWord('Stop_Word.txt')
		for word in list_stop_word:
			if word in self.Dictionary:
				#print(word)
				del self.Dictionary[word]
		print(len(self.Dictionary))
		return self.Dictionary
	def get_Dic2(self):
		Dictionarys = {}
		Dictionarys_2 = {}
		for word in self.Dictionary:
			if self.Dictionary.get(word) >100 and self.Dictionary.get(word) < 20400:
				Dictionarys[word] = self.Dictionary[word]
			else:
				Dictionarys_2[word] = self.Dictionary[word]
		print(len(Dictionarys))
		self.writeDic_key('dic_2.json',Dictionarys)
		# self.writeDic_key('dic_2.json',Dictionarys_2)
		return Dictionarys
	def writeDic_key(self,outputFile,Dictionary):
		key = ('word','df')
		count = 1
		self.f = open(outputFile,"w", encoding='utf-8')
		self.f.write('[')
		for word in Dictionary:
			if count == len(Dictionary):
				data = dict.fromkeys(key)
				data['word'] = word
				data['df']   = Dictionary.get(word)
				line = json.dumps(data,ensure_ascii=False) + "\n"
			else:
				count = count + 1
				data = dict.fromkeys(key)
				data['word'] = word
				data['df']   = Dictionary.get(word)
				line = json.dumps(data,ensure_ascii=False) + ",\n"
			self.f.write(line)
		self.f.write(']')
		self.f.close()
		return outputFile
	def readDiction(self,inputFile):
		dictionary = {}
		with open(inputFile,encoding='utf-8') as jsondata:
			datas = json.load(jsondata)
			for  data in datas:
				dictionary[data['word']] = data['df']
		return dictionary
# a = CreateDic()
# a.get_Dic0('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_training')
# a.get_Dic1()
# a.get_Dic2()
