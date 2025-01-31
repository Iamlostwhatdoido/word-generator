import os


def create_dictio(language:str,vision:int):
	if not os.path.exists("sources/"+language+".txt"):
		print(f"Error : Language source missing for {language}")
		return
	
	alphabet = ""
	matrix : dict[str,dict[str,int]] = {}
	root_set = set()

	with open("sources/"+language+".txt","r") as source_file:
		for i,word in enumerate(source_file.readlines()):
			root = " "*vision

			for letter in word.lower().removesuffix("\n")+" ":
				if not letter in alphabet:
					alphabet += letter
					alphabet = "".join(sorted(alphabet))

				if not root in root_set:
					root_set.add(root)
					matrix[root] = {}
				
				if not letter in matrix[root].keys():
					matrix[root][letter] = 0
				
				matrix[root][letter] += 1

				root = root[1:] + letter

	print("source read")

	with open("dictionnaries/"+language+"-n"+str(vision)+".txt","w") as dictio_file:
		for letter in alphabet:
			dictio_file.write("\t"+letter)

		dictio_file.write("\n")

		to_write = ""
		for root in matrix.keys():
			to_write += root

			for letter in alphabet:
				if letter in matrix[root].keys():
					to_write += "\t"+str(matrix[root][letter])
				else:
					to_write += "\t0"
			to_write += "\n"

		dictio_file.write(to_write.removesuffix("\n"))