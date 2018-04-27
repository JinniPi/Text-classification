import json
from CreateDic import CreateDic
class Train:

	#Input: 1 VB và Dictionary, Output : 1 tập từ là tập con của từ điển, giá trị của mỗi word là 
	# tf(số lần xuất hiện của từ trong VB)
	def get_tf_VB(self,VB,Dictionary):
		list_word = VB.split(' ')
		list_word_tf = {}
		list_word_tam = {}
		for word in list_word:
			if word in list_word_tam:
				list_word_tam[word] = list_word_tam.get(word) + 1
			else:
				list_word_tam[word] = 1
		for word in list_word_tam:
			if word in Dictionary:
				list_word_tf[word] = list_word_tam[word]
			else:
				continue		
		return list_word_tf

	#Input : 1 file chứa 1 tập VB cùng một chủ đề, gán nhãn cho chủ đề(label_VB), Dictionary
	#Output: 1 Dic có các trường label,sumVB, tf_word : tập từ với mỗi giá trị của word là tf trong  file.
	def get_tf_file(self,inputFile,Dictionary_file,label_VB):
		Dic_tf_File_label = {}
		Dic_tf_File = {}
		Createdic = CreateDic()
		Dictionary = Createdic.readDiction(Dictionary_file)
		list_VB = Createdic.readJson(inputFile)
		count_VB = 0
		for VB in list_VB:
			tf_VB = self.get_tf_VB(VB,Dictionary)
			for word in tf_VB:
				if word in Dic_tf_File:
					Dic_tf_File[word] = Dic_tf_File.get(word) + tf_VB.get(word)
				else:
					Dic_tf_File[word] = tf_VB[word]
			count_VB = count_VB + 1
		Dic_tf_File_label['label_VB'] = label_VB
		Dic_tf_File_label['sumVB'] = count_VB
		Dic_tf_File_label['tf_word'] = Dic_tf_File
		print(len(Dic_tf_File))
		return Dic_tf_File_label

	#Đưa kết quả của phương thức get_tf_file ra định dạng json
	def writeTf_file(self,inputFile,outputFile,Dictionary_file,label_VB):
		tf_file = self.get_tf_file(inputFile,Dictionary_file,label_VB)
		f = open(outputFile,"w", encoding='utf-8')
		f.write('[')
		line = json.dumps(tf_file,ensure_ascii=False) + "\n"
		f.write(line)
		f.write(']')
		f.close()
		return outputFile

	#Đọc file
	def readFile_tf(self,inputFile):
		with open(inputFile,encoding='utf-8') as jsondata:
			datas = json.load(jsondata)
			for data in datas:
				Dic_tf_File_label = {}
				Dic_tf_File_label = data
		return Dic_tf_File_label

	#Tính xác suất P(t|ci) : xác suất từ khóa tj xuất hiện đối với lớp ci 
	def P_word_Ci(self,Dictionary_file,Dictionary):
		P_word_Ci = {}
		sum_tf = 0
		T = len(Dictionary)
		for word in Dictionary_file:
			sum_tf = sum_tf + Dictionary_file.get(word)
		for word in Dictionary:
			if word in Dictionary_file:
				P_word_Ci[word] = (Dictionary_file[word] + 1) / (sum_tf + T)
			else:
				P_word_Ci[word] = 1 / (sum_tf + T)
		return P_word_Ci

	#Input: Tập các file đã được xử lí tính tf, Dictionary 
	#Output: Đưa ra file chứa mảng các json : Mỗi json chứa các key : label_VB,sumVB,P_word_Ci,P_Ci
	def Train_file_path(self,inputFile_path,Dictionary_file):
		list_result = []
		sum_VB_train = 0
		key = "sumVB"
		Createdic = CreateDic()
		list_file = Createdic.GetFiles(inputFile_path)
		Dictionary = Createdic.readDiction(Dictionary_file)
		for file in list_file:
			result = {}
			Dic_tf_File_label = self.readFile_tf(file)
			sum_VB_train = sum_VB_train + Dic_tf_File_label.get(key)
			result['label_VB'] = Dic_tf_File_label['label_VB']
			result['sumVB'] = Dic_tf_File_label['sumVB']
			result['P_word_Ci'] = self.P_word_Ci(Dic_tf_File_label['tf_word'],Dictionary)
			list_result.append(result)
		for result in list_result:
			result['P_Ci'] = (result.get('sumVB')) / (sum_VB_train)
			print(result['P_Ci'])
		return list_result
		
	#Ghi kết quả train
	def writeTrain_result(self,inputFile_path,outputFile,Dictionary_file):
		list_result = self.Train_file_path(inputFile_path,Dictionary_file)
		self.f = open(outputFile,"w", encoding='utf-8')
		self.f.write('[')
		count = 1
		for data in list_result:
			if count == len(list_result):
				line = json.dumps(data,ensure_ascii=False) + "\n"
			else:
				count = count + 1
				line = json.dumps(data,ensure_ascii=False) + ",\n"
			self.f.write(line)
		self.f.write(']')
		self.f.close()
		return outputFile
	def readFile_result_train(self,inputFile):
		list_result = []
		with open(inputFile,encoding='utf-8') as jsondata:
			datas = json.load(jsondata)
			for data in datas:
				Dic_tf_File_label = {}
				Dic_tf_File_label = data
				list_result.append(Dic_tf_File_label)
		return list_result

# train = Train()
# train.writeTf_file('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_training\\giaitri_train.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_tf_label_2\\giaitri_tf_2.json','dic_1.json',1)
# train.writeTf_file('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_training\\giaoduc_train.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_tf_label_2\\giaoduc_tf_2.json','dic_1.json',2)
# train.writeTf_file('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_training\\kinhdoanh_train.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_tf_label_2\\kinhdoanh_tf_2.json','dic_1.json',3)
# train.writeTf_file('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_training\\phapluat-tintuc_train.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_tf_label_2\\phapluat-tintuc_tf_2.json','dic_1.json',4)
# train.writeTf_file('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_training\\thegioi_train.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_tf_label_2\\thegioi_tf_2.json','dic_1.json',5)
# train.writeTf_file('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_training\\thethao_train.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_tf_label_2\\thethao_tf_2.json','dic_1.json',6)
# train.writeTf_file('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_training\\thoisu_train.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_tf_label_2\\thoisu_tf_2.json','dic_1.json',7)
# train.writeTrain_result('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_tf_label_2','resuilt_train_2.json','dic_1.json')