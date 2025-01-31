import os
from dictio_creator import create_dictio

LANGUAGE_NAME = "test"
GENERATE_NUMBER = 10

if not os.path.exists("dictionnaries/"+LANGUAGE_NAME+".txt"):
	print(f"Creating a dictionnary for {LANGUAGE_NAME}")
	create_dictio(LANGUAGE_NAME)

