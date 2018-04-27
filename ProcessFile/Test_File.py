import json
from Train import Train
from CreateDic import CreateDic
import math
class Test_File:

	#Xử lí file test về dạng gán label, đưa ra danh sách tf-word
	def processFile_test(self,inputFile,Dictionary_file,label):
		list_result = []
		train = Train()
		Createdic = CreateDic()
		Dictionary = Createdic.readDiction(Dictionary_file)
		list_VB = Createdic.readJson(inputFile)
		count_VB = 0
		for VB in list_VB:
			VB_test = {}
			count_VB = count_VB + 1
			VB_test['index_ci'] = count_VB
			VB_test['label'] = label
			VB_test['tf_word'] = train.get_tf_VB(VB,Dictionary)
			list_result.append(VB_test)
		return list_result

	#Ghi ra file , đưa các VB test về dạng cuối cùng
	def write_filetest(self,inputFile,outputFile,Dictionary_file,label):
		list_result = self.processFile_test(inputFile,Dictionary_file,label)
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

    #Phương thức chọn Phân lớp phù hợp
	def option_Ci(self,list_P_VB_Ci):
		result = list_P_VB_Ci[0].get('P_VB_Ci')
		result_ci = 0
		for ci in list_P_VB_Ci:
			if ci.get('P_VB_Ci') >= result:
				result = ci.get('P_VB_Ci')
				result_ci = ci.get('label')
			else:
				continue
		return result_ci

    #phương thức test cho từng VB.
	def test_VB(self,VB,list_Ci):
		list_P_VB_Ci = []
		tf_word_VB = VB.get('tf_word') #lấy ra danh sách tf của vb
		for Ci in list_Ci:
			P_ci = {}
			P_ci['label'] = Ci.get('label_VB')
			P_VB_Ci = math.log10(Ci.get('P_Ci'))
			P_word_Ci = Ci.get('P_word_Ci')
			for word in tf_word_VB:
				P_VB_Ci = P_VB_Ci + math.log10(P_word_Ci.get(word)*tf_word_VB.get(word))
			P_ci['P_VB_Ci'] = P_VB_Ci
			list_P_VB_Ci.append(P_ci)
		label_result = self.option_Ci(list_P_VB_Ci)
		return label_result

	#Test cho một tập các file	
	def test_file_path(self,inputFile_path,file_train):
		list_result = []
		train = Train()
		Createdic = CreateDic()
		list_file = Createdic.GetFiles(inputFile_path)
		list_Ci = train.readFile_result_train(file_train)
		for file in list_file:
			print('Đang ở file',file)
			list_VB = train.readFile_result_train(file)
			for VB in list_VB:
				result = {}
				result['label'] = VB.get('label')
				result['label_result'] = self.test_VB(VB,list_Ci)
				list_result.append(result)
			# print(list_result)
		return list_result

	#Đánh giá độ chính xác
	def Accuracy_test(self,list_result):
		count_true = 0
		for result in list_result:
			if result['label'] == result['label_result']:
				count_true = count_true + 1
			else:
				continue
		accuracy = (count_true)/(len(list_result))
		return accuracy
	# def FP_ci(self,list_result_cj,ci):
	# 	#cj#ci
	# 	count = 0
	# 	for result in list_result_cj:
	# 		if result['label_result'] == ci:
	# 			count = count + 1
	# 		else:
	# 			continue
	# 	return count
	# def TPi_ci(self,list_result_ci):
	# 	count_true = 0
	# 	for result in list_result:
	# 		if result['label'] == result['label_result']:
	# 			count_true = count_true + 1
	# 		else:
	# 			continue
	# 	return count_true
	def Precision(self,list_result):
		result_TPi = {'1': 0,'2': 0, '3': 0,'4': 0,'5': 0,'6': 0,'7': 0}
		result_FPi = {'1': 0,'2': 0, '3': 0,'4': 0,'5': 0,'6': 0,'7': 0}
		for result in list_result:
			if result['label'] == result['label_result']:
				ci = str(result['label'])	
				result_TPi[ci] = result_TPi.get(ci) + 1
			else :
				ci = str(result['label_result'])
				result_FPi[ci] = result_FPi.get(ci) + 1
		print(result_TPi)
		print(result_FPi)
		sum_TPi = 0
		sum_FPi = 0
		for ci in result_TPi:
			sum_TPi = sum_TPi + result_TPi.get(ci)
		for ci in result_FPi:
			sum_FPi = sum_FPi + result_FPi.get(ci)

		Precision = sum_TPi / (sum_FPi + sum_TPi)
		return Precision
	def F1(self,Recall,Precision):
		F1 = (2*Recall*Precision)/(Recall+Precision)
		return F1


		




def main():
	a = Test_File()
	# a.write_filetest('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test\\giaitri_test.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test_tf\\giaitri_test_tf.json','dic_2.json',1)
	# a.write_filetest('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test\\giaoduc_test.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test_tf_2\\giaoduc_test_tf_2.json','dic_1.json',2)
	# a.write_filetest('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test\\kinhdoanh_test.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test_tf_2\\kinhdoanh_test_tf_2.json','dic_1.json',3)
	# a.write_filetest('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test\\phapluat-tintuc_test.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test_tf_2\\phapluat-tintuc_test_tf_2.json','dic_1.json',4)
	# a.write_filetest('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test\\thegioi_test.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test_tf_2\\thegioi_test_tf_2.json','dic_1.json',5)
	# a.write_filetest('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test\\thethao_test.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test_tf_2\\thethao_test_tf_2.json','dic_1.json',6)
	# a.write_filetest('C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test\\thoisu_test.json','C:\\Users\\DELL\\Downloads\\Project_NLP\\ProcessFile\\data_test_tf_2\\thoisu_test_tf_2.json','dic_1.json',7)
	list_result = a.test_file_path('data_test_tf','result_train.json')
	print(list_result)
	print(len(list_result))
	Accuracy = a.Accuracy_test(list_result)
	Precision = a.Precision(list_result)
	F1 = a.F1(Accuracy,Precision)
	print(Accuracy)
	print(Precision)
	print(F1)
	
if __name__ == "__main__":
	main()








		