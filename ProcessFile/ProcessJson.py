import json
import re
import codecs
import pdb
class ProcessJson:
	row_result = []
	list_result = []
	def getRow(self):
		return self.row_result
	def getList(self):
		return self.list_result
	def __init__(self):
		self.row_result = []
		self.list_result = []
	def replaceUnicode(self,str):
		str = str.replace("\u0065\u0309", "\u1EBB")
		str = str.replace("\u0065\u0301", "\u00E9") 
		str = str.replace("\u0065\u0300", "\u00E8") 
		str = str.replace("\u0065\u0323", "\u1EB9") 
		str = str.replace("\u0065\u0303", "\u1EBD") 
		str = str.replace("\u00EA\u0309", "\u1EC3") 
		str = str.replace("\u00EA\u0301", "\u1EBF")
		str = str.replace("\u00EA\u0300", "\u1EC1")
		str = str.replace("\u00EA\u0323", "\u1EC7")
		str = str.replace("\u00EA\u0303", "\u1EC5")
		str = str.replace("\u0079\u0309", "\u1EF7")
		str = str.replace("\u0079\u0301", "\u00FD")
		str = str.replace("\u0079\u0300", "\u1EF3")
		str = str.replace("\u0079\u0323", "\u1EF5")
		str = str.replace("\u0079\u0303", "\u1EF9")
		str = str.replace("\u0075\u0309", "\u1EE7")
		str = str.replace("\u0075\u0301", "\u00FA")
		str = str.replace("\u0075\u0300", "\u00F9")
		str = str.replace("\u0075\u0323", "\u1EE5")
		str = str.replace("\u0075\u0303", "\u0169")
		str = str.replace("\u01B0\u0309", "\u1EED")
		str = str.replace("\u01B0\u0301", "\u1EE9")
		str = str.replace("\u01B0\u0300", "\u1EEB")
		str = str.replace("\u01B0\u0323", "\u1EF1")
		str = str.replace("\u01B0\u0303", "\u1EEF")
		str = str.replace("\u0069\u0309", "\u1EC9")
		str = str.replace("\u0069\u0301", "\u00ED")
		str = str.replace("\u0069\u0300", "\u00EC")
		str = str.replace("\u0069\u0323", "\u1ECB")
		str = str.replace("\u0069\u0303", "\u0129")
		str = str.replace("\u006F\u0309", "\u1ECF")
		str = str.replace("\u006F\u0301", "\u00F3")
		str = str.replace("\u006F\u0300", "\u00F2")
		str = str.replace("\u006F\u0323", "\u1ECD")
		str = str.replace("\u006F\u0303", "\u00F5")
		str = str.replace("\u01A1\u0309", "\u1EDF")
		str = str.replace("\u01A1\u0301", "\u1EDB")
		str = str.replace("\u01A1\u0300", "\u1EDD")
		str = str.replace("\u01A1\u0323", "\u1EE3")
		str = str.replace("\u01A1\u0303", "\u1EE1")
		str = str.replace("\u00F4\u0309", "\u1ED5")
		str = str.replace("\u00F4\u0301", "\u1ED1")
		str = str.replace("\u00F4\u0300", "\u1ED3")
		str = str.replace("\u00F4\u0323", "\u1ED9")
		str = str.replace("\u00F4\u0303", "\u1ED7")
		str = str.replace("\u0061\u0309", "\u1EA3")
		str = str.replace("\u0061\u0301", "\u00E1")
		str = str.replace("\u0061\u0300", "\u00E0")
		str = str.replace("\u0061\u0323", "\u1EA1")
		str = str.replace("\u0061\u0303", "\u00E3")
		str = str.replace("\u0103\u0309", "\u1EB3")
		str = str.replace("\u0103\u0301", "\u1EAF")
		str = str.replace("\u0103\u0300", "\u1EB1")
		str = str.replace("\u0103\u0323", "\u1EB7")
		str = str.replace("\u0103\u0303", "\u1EB5")
		str = str.replace("\u00E2\u0309", "\u1EA9")
		str = str.replace("\u00E2\u0301", "\u1EA5")
		str = str.replace("\u00E2\u0300", "\u1EA7")
		str = str.replace("\u00E2\u0323", "\u1EAD")
		str = str.replace("\u00E2\u0303", "\u1EAB")
		str = str.replace("\u0045\u0309", "\u1EBA")
		str = str.replace("\u0045\u0301", "\u00C9")
		str = str.replace("\u0045\u0300", "\u00C8")
		str = str.replace("\u0045\u0323", "\u1EB8")
		str = str.replace("\u0045\u0303", "\u1EBC")
		str = str.replace("\u00CA\u0309", "\u1EC2")
		str = str.replace("\u00CA\u0301", "\u1EBE")
		str = str.replace("\u00CA\u0300", "\u1EC0")
		str = str.replace("\u00CA\u0323", "\u1EC6")
		str = str.replace("\u00CA\u0303", "\u1EC4")
		str = str.replace("\u0059\u0309", "\u1EF6")
		str = str.replace("\u0059\u0301", "\u00DD")
		str = str.replace("\u0059\u0300", "\u1EF2")
		str = str.replace("\u0059\u0323", "\u1EF4")
		str = str.replace("\u0059\u0303", "\u1EF8")
		str = str.replace("\u0055\u0309", "\u1EE6")
		str = str.replace("\u0055\u0301", "\u00DA")
		str = str.replace("\u0055\u0300", "\u00D9")
		str = str.replace("\u0055\u0323", "\u1EE4")
		str = str.replace("\u0055\u0303", "\u0168")
		str = str.replace("\u01AF\u0309", "\u1EEC")
		str = str.replace("\u01AF\u0301", "\u1EE8")
		str = str.replace("\u01AF\u0300", "\u1EEA")
		str = str.replace("\u01AF\u0323", "\u1EF0")
		str = str.replace("\u01AF\u0303", "\u1EEE")
		str = str.replace("\u0049\u0309", "\u1EC8")
		str = str.replace("\u0049\u0301", "\u00CD")
		str = str.replace("\u0049\u0300", "\u00CC")
		str = str.replace("\u0049\u0323", "\u1ECA")
		str = str.replace("\u0049\u0303", "\u0128")
		str = str.replace("\u004F\u0309", "\u1ECE")
		str = str.replace("\u004F\u0301", "\u00D3")
		str = str.replace("\u004F\u0300", "\u00D2")
		str = str.replace("\u004F\u0323", "\u1ECC")
		str = str.replace("\u004F\u0303", "\u00D5")
		str = str.replace("\u01A0\u0309", "\u1EDE")
		str = str.replace("\u01A0\u0301", "\u1EDA")
		str = str.replace("\u01A0\u0300", "\u1EDC")
		str = str.replace("\u01A0\u0323", "\u1EE2")
		str = str.replace("\u01A0\u0303", "\u1EE0")
		str = str.replace("\u00D4\u0309", "\u1ED4")
		str = str.replace("\u00D4\u0301", "\u1ED0")
		str = str.replace("\u00D4\u0300", "\u1ED2")
		str = str.replace("\u00D4\u0323", "\u1ED8")
		str = str.replace("\u00D4\u0303", "\u1ED6")
		str = str.replace("\u0041\u0309", "\u1EA2")
		str = str.replace("\u0041\u0301", "\u00C1")
		str = str.replace("\u0041\u0300", "\u00C0")
		str = str.replace("\u0041\u0323", "\u1EA0")
		str = str.replace("\u0041\u0303", "\u00C3")
		str = str.replace("\u0102\u0309", "\u1EB2")
		str = str.replace("\u0102\u0301", "\u1EAE")
		str = str.replace("\u0102\u0300", "\u1EB0")
		str = str.replace("\u0102\u0323", "\u1EB6")
		str = str.replace("\u0102\u0303", "\u1EB4")
		str = str.replace("\u00C2\u0309", "\u1EA8")
		str = str.replace("\u00C2\u0301", "\u1EA4")
		str = str.replace("\u00C2\u0300", "\u1EA6")
		str = str.replace("\u00C2\u0323", "\u1EAC")
		str = str.replace("\u00C2\u0303", "\u1EAA")
		return str

	#Đọc file json ,trả về mảng các văn bản đã được xử lí kí tự \n ,\t,\r,trả về file
	#đã xử lí.
	
	def PreRead(self,inputFile):
		
		with open(inputFile,encoding='utf-8') as jsondata:
			datas = json.load(jsondata)
			print(type(datas))
			count = 0
			for index, data in enumerate(datas):
				#dic = dic.fromkeys(key)
				count = count + 1
				title = data["title"]
				sapo = data["sapo"]
				text = data["text"]
				# if index == 68:
				# 	pdb.set_trace()
				title = self.process_string(title)
				sapo = self.process_string(sapo)
				text = self.process_string(text)
				data_result =  title + " " + sapo + " " + text
				self.list_result.append(data_result)
			return self.list_result
	def Rre_process_string(self,str):
		if str == None:
			str = ""
		else:
			str = str.replace('\n'," ").replace('\t'," ").replace('\r'," ")
			str = self.replaceUnicode(str)
			str=re.sub(r'(\')+',"",str)
			str=re.sub(r'(\")+',"",str)
			#-----------------
		return str
	def PreWrite(self,inputFile,outputFile):
		key = ('text',)
		list_data = []
		list_r = self.PreRead(inputFile)
		count = 1
		self.f = open(outputFile,"w", encoding='utf-8')
		self.f.write('[')
		for data in list_r:
			if count == len(list_r):
				dic = dict.fromkeys(key,data)
				line = json.dumps(dic,ensure_ascii=False) + "\n"
			else:
				count = count + 1
				dic = dict.fromkeys(key,data)
				line = json.dumps(dic,ensure_ascii=False) + ",\n"
			self.f.write(line)
		self.f.write(']')
		self.f.close()
		return outputFile

	#input: Đầu vào file đã được tách từ, đầu ra : file đã loại bỏ dấu câu,kí tự thừa.
	def process_string(self,str):
		if str == None:
			str = ""
		else:
			str=re.sub(r'(?is)\W+', ' ', str).strip()
			str = re.sub(r'(?is)[\d+][\D+]', ' ', str)
			str=re.sub(r'(?is)\d+h',' ',str).strip()
			str=re.sub(r'(?is)\d+', ' ',str).strip()
		return str
	def ReadJson(self,inputFile):
		with open(inputFile,encoding='utf-8') as jsondata:
			datas = json.load(jsondata)
			print(type(datas))
			for data in datas:
				text = data[" text "]
				text = self.process_string(text)
				data_result = text
				self.list_result.append(data_result)
		return self.list_result
	def WriteJson(self,inputFile,outputFile):
		key = ('text',)
		list_data = []
		list_r = self.ReadJson(inputFile)
		count = 1
		self.f = open(outputFile,"w", encoding='utf-8')
		self.f.write('[')
		for data in list_r:
			if count == len(list_r):
				dic = dict.fromkeys(key,data)
				line = json.dumps(dic,ensure_ascii=False) + "\n"
			else:
				count = count + 1
				dic = dict.fromkeys(key,data)
				line = json.dumps(dic,ensure_ascii=False) + ",\n"
			self.f.write(line)
		self.f.write(']')
		self.f.close()
		return outputFile

	
	#Hàm set lại cấu trúc file Json.
	def processNew(self,inputFile):
		key=('origin','link','title','sapo','content')
		with open(inputFile,encoding='utf-8') as jsondata:
			datas = json.load(jsondata)
			for data in datas:
				dic = dict.fromkeys(key)
				#print(data)
				dic['origin'] = "group 6"
				dic['link'] = data['link']
				dic['title']=data['title']
				dic['sapo'] =data['sapo']
				dic['content']=data['text']
				self.row_result.append(dic)
			return self.row_result
	def ProcessWriteNew(self,inputFile,outputFile):
		list_r = self.processNew(inputFile)
		count = 1
		self.f = open(outputFile, "w", encoding='utf-8')
		self.f.write('[')
		for data in list_r:
			if count == len(list_r):
			
				line = json.dumps(data,ensure_ascii=False) + "\n"
			else:
				count = count + 1
				line = json.dumps(data,ensure_ascii=False) + ",\n"
			self.f.write(line)
		self.f.write(']')
		self.f.close()
		return outputFile
	#Tách tạo file train và file test.
	def splitFile(self,inputFile,file_train,file_test):
		key = ('text',)
		list_train = []
		count_1 = 1
		list_test = []
		count_2 = 1
		with open(inputFile,encoding='utf-8') as jsondata:
			datas = json.load(jsondata)
			count = 0
			for data in datas:
				count = count + 1
				data_result = data["text"]
				if count <= (80*len(datas))//100:
					list_train.append(data_result)
				else:
					list_test.append(data_result)
		print(len(list_train))
		print('-----------')
		print(list_train[0])
		print('-----------')
		print(len(list_test))
		print(list_test[0])
		self.f_train = open(file_train,"w", encoding='utf-8')
		print("đang ghi file train")
		self.f_train.write('[')
		for data in list_train:
			if count_1 == len(list_train):
				dic = dict.fromkeys(key,data)
				line = json.dumps(dic,ensure_ascii=False) + "\n"
			else:
				count_1 = count_1 + 1
				dic = dict.fromkeys(key,data)
				line = json.dumps(dic,ensure_ascii=False) + ",\n"
			self.f_train.write(line)
		self.f_train.write(']')
		self.f_train.close()
		self.f_test = open(file_test,"w", encoding='utf-8')
		print("đang ghi file test")
		self.f_test.write('[')
		for data in list_test:
			if count_2 == len(list_test):
				dic = dict.fromkeys(key,data)
				line = json.dumps(dic,ensure_ascii=False) + "\n"
			else:
				count_2 = count_2 + 1
				dic = dict.fromkeys(key,data)
				line = json.dumps(dic,ensure_ascii=False) + ",\n"
			self.f_test.write(line)
		self.f_test.write(']')
		self.f_test.close()
		return file_train,file_test


		

					

a = ProcessJson()
a.splitFile('data_last\hoso.json','data_training\hoso_train.json','data_test\hoso_test.json')
b = ProcessJson()
b.splitFile('data_last\giaitri.json','data_training\giaitri_train.json','data_test\giaitri_test.json')
c = ProcessJson()
c.splitFile('data_last\giaoduc.json','data_training\giaoduc_train.json','data_test\giaoduc_test.json')
d = ProcessJson()
d.splitFile('data_last\kinhdoanh.json','data_training\kinhdoanh_train.json','data_test\kinhdoanh_test.json')
e = ProcessJson()
e.splitFile('data_last\phapluat-tintuc.json','data_training\phapluat-tintuc_train.json','data_test\phapluat-tintuc_test.json')
g = ProcessJson()
g.splitFile('data_last\\thegioi.json','data_training\\thegioi_train.json','data_test\\thegioi_test.json')
h = ProcessJson()
h.splitFile('data_last\\thethao.json','data_training\\thethao_train.json','data_test\\thethao_test.json')
trang = ProcessJson()
trang.splitFile('data_last\\thoisu.json','data_training\\thoisu_train.json','data_test\\thoisu_test.json')
p=ProcessJson()
p.splitFile('data_last\\tuvan.json','data_training\\tuvan_train.json','data_test\\tuvan_test.json')
# a.PreWrite('data_token\giaitri_split.json','data_last\giaitri.json')
# b.PreWrite('data_token\giaoduc_split.json','data_last\giaoduc.json')
# c.PreWrite('data_token\hoso_split.json','data_last\hoso.json')
# d.PreWrite('data_token\kinhdoanh_split.json','data_last\kinhdoanh.json')
# e.PreWrite('data_token\phapluat-tintuc_split.json','data_last\phapluat-tintuc.json')
# g.PreWrite('thegioi_split.json','thegioi.json')
# h.PreWrite('thethao_split.json','thethao.json')
# trang.PreWrite('thoisu_split.json','thoisu.json')
# p.PreWrite('tuvan_split.json','tuvan.json')
# print(len(lists))
# print(b.getList())
#print(p[68])
