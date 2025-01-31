import os
import numpy as np
from dictio_creator import create_dictio


class WordGenerator:
	def __init__(self,language:str,vision=2,exploration=False):

		if not os.path.exists("dictionnaries/"+language+"-n"+str(vision)+".txt"):
			print(f"Creating a dictionnary for {language} at vision {vision}")
			create_dictio(language,vision)
		
		self.matrix : dict = {}
		self.exploration = exploration

		with open("dictionnaries/"+language+"-n"+str(vision)+".txt","r") as dictio_file:
			self.alphabet = "".join(dictio_file.readline().removesuffix("\n").split("\t"))
			self.general_table = np.zeros(len(self.alphabet))
			for line in dictio_file.readlines():
				line_content = line.removesuffix("\n").split("\t")
				
				table = np.array([int(number) for number in line_content[1:]])
				self.general_table = self.general_table + table
				self.matrix[line_content[0]] = table


		self.vision = len(list(self.matrix.keys())[0])
	

	def create_word(self) -> str:
		root = " "*self.vision
		word = ""

		while len(word) <1000:
			next_letter = self.next_letter(root)
			if next_letter == " ":
				break
			else:
				word += next_letter
				root = root[1:] + next_letter
		return word.capitalize()
	

	def next_letter(self, root:str) -> str:
		if not root in self.matrix.keys():
			table = self.general_table
		else:
			table = np.array(self.matrix[root])
		if self.exploration :
			table = table + [1]*len(table)
		table = table / np.sum(table)
		letter = np.random.choice(list(self.alphabet),p=table)
		return letter


	def write_words(self, number:int):
		words = [self.create_word() for _ in range(number)]
		words.sort(key= lambda x : len(x))
		with open("outfile.txt","w") as outfile:
			outfile.write("\n".join(words))
	