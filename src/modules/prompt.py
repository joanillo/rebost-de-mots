"""funcions get_prompt_fixed() i get_prompt_random()"""
from typing import List

def get_prompt_fixed() -> str:
	"""
	Genera i retorna un prompt que farem servir per analitzar les diferents APIs

	Arguments: -

	Returns:
	str: el prompt
	"""
	prompt = """
	Genera una petita narració literària de 400 paraules que continguin les paraules:

	-nogensmenys
	-rauxa
	-xalar
	-aixopluc
	-enraonar
	-tafaner
	-badoc
	-escarrassar-se
	-xipollejar
	-eixelebrat

	i a continuació posa la definició i explicació de les paraules, i explica el seu context dins de la narració. Vull que el format de la resposta sigui markdown, exacatament de la forma:

	# **[títol]**

	[NARRACIÓ, POSANT EN NEGRETA LES PARAULES TREBALLADES]

	- **[PARAULA 1]**: [Definició i explicació de la paraula 1]\\
	[context dins del text de com s'utilitza la paraula 1]

	- **[PARAULA 2]**: [Definició i explicació de la paraula 2]\\
	[context dins del text de com s'utilitza la paraula 2]

	- etc

	Dos exemples de com han de quedar formatades les paraules:

	- **nogensmenys**: De fet, no obstant això.\\
		Tot i les complicacions, en Joan anima el grup a seguir amb l'excursió: "Nogensmenys, no deixem que una mica de pluja ens aturi!"

	- **rauxa**: Impuls, assaltida. Actuar amb energia impetuosa.\\
		En Joan mostra la seva empenta i entusiasme al començar la caminada.

	- etc.
	"""

	return prompt

def get_prompt_random(words: List) -> str:
	"""
	Genera i retorna un prompt ad-hoc a partir de la llista de paraules que es passen. S'utilitza en mode producció,
	quan generem les narracions.

	Arguments:
	words (List): la llista de paraules

	Returns:
	str: el prompt
	"""
	words_formatted = ""

	for word in words:
		words_formatted += "\t- " + word + "\n"

	prompt = f"""
	Genera una petita narració literària de 400 paraules que continguin les paraules:

	{words_formatted}

	i a continuació posa la definició i explicació de les paraules, i explica el seu context dins de la narració. Vull que el format de la resposta sigui markdown, exacatament de la forma:

	# **[títol]**

	[NARRACIÓ, POSANT EN NEGRETA LES PARAULES TREBALLADES]

	- **[PARAULA 1]**: [Definició i explicació de la paraula 1]\\
	[context dins del text de com s'utilitza la paraula 1]

	- **[PARAULA 2]**: [Definició i explicació de la paraula 2]\\
	[context dins del text de com s'utilitza la paraula 2]

	- etc

	Dos exemples de com han de quedar formatades les paraules:

	- **nogensmenys**: De fet, no obstant això.\\
		Tot i les complicacions, en Joan anima el grup a seguir amb l'excursió: "Nogensmenys, no deixem que una mica de pluja ens aturi!"

	- **rauxa**: Impuls, assaltida. Actuar amb energia impetuosa.\\
		En Joan mostra la seva empenta i entusiasme al començar la caminada.

	- etc.
	"""

	return prompt
