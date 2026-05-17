"""funció: get_vocabulary()"""
from typing import List

def get_vocabulary() -> List:
	"""
	Genera una llista de paraules a partir del contingut de vocabulari.txt

	Arguments: -

	Returns:
	List: la llista de paraules
	"""
	with open("vocabulari/vocabulari.txt", "r", encoding="utf-8") as f:
			words = [linia.strip() for linia in f if linia.strip()]


	return words
