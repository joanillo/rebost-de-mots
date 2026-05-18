"""
Rebost de mots
Programa principal per testejar diferents LLM i generar els contes
"""
import sys
import argparse

from modules.analize import analize_apis
from modules.rebost_de_mots_production import rebost_de_mots_production

if __name__ == "__main__":

	parser = argparse.ArgumentParser(
		description="Rebost de Mots",
		formatter_class=argparse.RawTextHelpFormatter
	)

	parser.add_argument(
		"--mode",
		type=str,
		default="produccio",
		choices=["analisi", "produccio"],
		help=(
				"Mode.\n"
				"analisi: genera un relat curt amb diferents APIs d'IA generativa.\n"
				"produccio: genera relats curts amb la API escollida"
		)
	)

	parser.add_argument(
		"--api",
		type=str,
		choices=["openai", "anthropic", "xai", "deepseek", "gemini", "test"],
		help=(
				"IA API\n"
				"Només vàlid per mode = produccio"
		)
	)

	parser.add_argument(
		"--num",
		type=int,
		default="10",
		help=(
				"Nombre de relats a generar\n"
				"Només vàlid per mode = produccio"
		)
	)

	if len(sys.argv) == 1:
			parser.print_help()
			sys.exit(1)

	args = parser.parse_args()

	if args.mode == "analisi":
		analize_apis()
	else: # produccio
		if not args.api:
			parser.print_help()
			sys.exit(1)
		rebost_de_mots_production(args.api, args.num)
