import os
import numpy as np
from dictio_creator import create_dictio


class WordGenerator:
	def __init__(self,language:str,vision=2):

		if not os.path.exists("dictionnaries/"+language+"-n"+str(vision)+".txt"):
			print(f"Creating a dictionnary for {language} at vision {vision}")
			create_dictio(language,vision)
		
		self.matrix : dict = {}

		with open("dictionnaries/"+language+"-n"+str(vision)+".txt","r") as dictio_file:
			self.alphabet = "".join(dictio_file.readline().removesuffix("\n").split("\t"))
			for line in dictio_file.readlines():
				line_content = line.removesuffix("\n").split("\t")
				
				self.matrix[line_content[0]] = [int(number) for number in line_content[1:]]

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
		table = np.array(self.matrix[root])
		table = table / np.sum(table)
		letter = np.random.choice(list(self.alphabet),p=table)
		return letter


	def write_words(self, number:int):
		words = [self.create_word() for _ in range(number)]
		with open("outfile.txt","w") as outfile:
			outfile.write("\n".join(words))
	