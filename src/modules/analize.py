"""funció analize_apis()"""
import os
import subprocess

from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv

from modules.prompt import get_prompt_fixed
from modules.response_test import get_response_test
from modules.models import get_models

def analize_apis() -> None:
	"""
	Analitza el resultat narratiu de les diferents APIs a partir del prompt que s'especifica.
	Genera un markdown i un pdf per cada api analitzada.

	Arguments: -

	Returns:
	None
	"""
	load_dotenv()

	prompt = get_prompt_fixed()

	# modelAI = "openai" # openai, anthropic, xai, deepseek, test
	# modelsAI = ["test"]
	# modelsAI = ["openai", "anthropic", "xai", "deepseek"]
	modelsAI = ["openai"]

	for modelAI in modelsAI:
		print()
		print(f"======= {modelAI} ================")

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

		else: # test

			content = get_response_test()

		# ------------------

		if content:
			print(content)
			with open(f"output/sortida_{modelAI}.md", "w", encoding="utf-8") as f:
				f.write(content)

			# $ pandoc sortida_anthropic.md -o sortida_anthropic.pdf
			subprocess.run(
					["/usr/bin/pandoc", f"output/sortida_{modelAI}.md", "-o", f"output/sortida_{modelAI}.pdf", "--template", "template.tex"],
					check=True
			)
