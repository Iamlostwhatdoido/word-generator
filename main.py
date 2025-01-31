


SOURCE_NAME = "francais"

with open("sources/"+SOURCE_NAME+".txt","r") as save_file:
		words=[]
		for line_content in save_file.readlines():
			words.append(line_content.removesuffix("\n"))


for i,word in enumerate(words):
	if len(word)==2:
		print(f"{i}, {word}")

# with open("sources/"+SOURCE_NAME+"2.txt", "w") as save_file:
# 		for word in words:
# 			if len(word)==1:
# 				continue
# 			save_file.write("\n" + word.capitalize())
