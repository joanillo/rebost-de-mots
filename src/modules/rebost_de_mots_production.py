"""funció rebost_de_mots_production()"""
import os
import subprocess
import random
from datetime import datetime

from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv

from modules.vocabulary import get_vocabulary
from modules.prompt import get_prompt_random
from modules.models import get_models


def rebost_de_mots_production(modelAI: str, num: int) -> None:
	"""
	Generació de les narracions literàries: Rebost de Mots. Genera el markdown i el pdf amb pandoc.

	Arguments:
	modelAI (str): l'API del model LLM que farem servir
	num (int): número de relats a generar

	Returns:
	None
	"""
	load_dotenv()
	words = get_vocabulary()
	timestamp = datetime.now().strftime("%y%m%d_%H%M%S")

	for n in range(num):
		print(f"=== RELAT #{n+1}/{num}")
		words10 = random.sample(words, 10) # sense repetició
		prompt = get_prompt_random(words10)

		client = None

		if modelAI == "openai":
			# OpenAI
			try:
				api_key = os.getenv("OPENAI_API_KEY")
				if not api_key:
					raise ValueError(f"Falta la variable d'entorn de {modelAI}")
				client = OpenAI(api_key=api_key)
				response = client.chat.completions.create(
						model=get_models(modelAI), # gpt-4o, gpt-4o-mini
						messages=[
								{"role": "user", "content": f"{prompt}"}
						]
				)

				content = response.choices[0].message.content
			except Exception as e:
				print(f"Error inesperat: {e}")
				content = None

		elif modelAI == "anthropic":
			# Claude (Anthropic)
			try:
				api_key = os.getenv("ANTHROPIC_API_KEY")
				if not api_key:
					raise ValueError(f"Falta la variable d'entorn de {modelAI}")
				client = Anthropic(api_key=api_key)
				response = client.messages.create(
						model=get_models(modelAI), # claude-opus-4-7
						max_tokens=2000,
						messages=[
								{"role": "user", "content": f"{prompt}"}
						]
				)

				content = response.content[0].text

			except Exception as e:
				print(f"Error inesperat: {e}")
				content = None

		elif modelAI == "xai":
			# XAI (Grok)
			try:
				api_key = os.getenv("XAI_API_KEY")
				if not api_key:
					raise ValueError(f"Falta la variable d'entorn de {modelAI}")
				client = OpenAI(
						api_key=api_key,
						base_url="https://api.x.ai/v1"
				)

				response = client.chat.completions.create(
						model=get_models(modelAI), # grok-4.3
						messages=[
								{
										"role": "user",
										"content": f"{prompt}"
								}
						]
				)

				content = response.choices[0].message.content

			except Exception as e:
				print(f"Error inesperat: {e}")
				content = None

		elif modelAI == "deepseek":
			# DeepSeek
			try:
				api_key = os.getenv("DEEPSEEK_API_KEY")
				if not api_key:
					raise ValueError(f"Falta la variable d'entorn de {modelAI}")

				client = OpenAI(
						api_key=api_key,
						base_url="https://api.deepseek.com"
				)

				response = client.chat.completions.create(
						model=get_models(modelAI), # deepseek-reasoner
						messages=[
								{
										"role": "user",
										"content": f"{prompt}"
								}
						]
				)

				content = response.choices[0].message.content

			except Exception as e:
				print(f"Error inesperat: {e}")
				content = None

		# ------------------

		if content:
			#print(content)
			with open(f"output/relats_{modelAI}_{timestamp}.md", "a", encoding="utf-8") as f:
				f.write(content)
				f.write("\n\n\n")

	# ------------------
	# $ pandoc sortida_anthropic.md -o sortida_anthropic.pdf
	subprocess.run(
			["/usr/bin/pandoc", f"output/relats_{modelAI}_{timestamp}.md", "-o", f"output/relats_{modelAI}_{timestamp}.pdf", "--template", "template.tex"],
			check=True
	)
