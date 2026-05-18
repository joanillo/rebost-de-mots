"""funció get_models()"""
def get_models(api: str) -> str:
	"""
	Retorna el model que farem servir per cada API
	Aquest és el fitxer que s'ha d'editar si volem probar altres models

	Arguments:
	str: la api que estem provant

	Returns:
	str: el model associat a la API
	"""
	model = None
	if api == "openai":
		model = "gpt-4o" # "gpt-4o-mini"
	elif api == "anthropic":
		model = "claude-opus-4-7"
	elif api == "xai":
		model = "grok-4.3"
	elif api == "deepseek":
		model = "deepseek-reasoner"
	elif api == "gemini":
		model = "gemini-2.5-flash"

	return model
