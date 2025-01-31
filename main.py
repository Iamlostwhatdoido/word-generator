from word_generator_class import WordGenerator


if __name__ == "__main__":

	word_generator = WordGenerator("francais",vision=4,exploration=False)
	word_generator.write_words(20)
