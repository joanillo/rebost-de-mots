# rebost-de-mots

Improve your Catalan vocabulary with words worth preserving - Millora el teu vocabulari de català amb mots que no s'han de perdre. Per ex: abassegar
abeurador, abraonar, aclaparar, aclucar, adient, adobar, adreçar-se, àdhuc, afanyar-se, agenollar-se, agosarat, ajornar, ajupir-se,...

Aquest projecte genera relats literaris curts on introduïm diferent vocabulari que volem treballar. Després del relat s'explica el significat del vocabulari i el seu context dins de la narració.

Els relats estan generats amb LLM. Es poden testejar diferents LLM. És necessari tenir l'API Key dels LLM que es vol provar.

## Getting Started

Per començar amb el projecte, segueix els següents passsos:

1. Clona el repositori a la teva màquina local:

```bash
git clone https://github.com/joanillo/rebost-de-mots.git
```

2. Navega al directori del projecte:

```bash
cd rebost-de-mots
```

3. Creació d'un entorn virtual per executar el projecte (recomanable):

```bash
python -m venv venv
source venv/bin/activate
```

4. Instal·la les dependències necessàries (recomanable haver creat prèvialent l'entorn virtual):

```bash
(venv) $ pip install -r requirements.txt
```

Aquest projecte utilitza **pandoc** per convertir els fitxers markdown a pdf. No utilitza la llibreria python associada (*pypandoc*), sinó que s'ha d'instal·lar pandoc. En una màquina Linux:

```bash
sudo apt install pandoc
sudo apt install texlive-latex-base
sudo apt install texlive-latex-recommended texlive-fonts-recommended
```

Per testejar que pandoc funciona:

```bash
$ pandoc document.md -o document.pdf
```


5. Configuració de les API KEYs. Les API KEYs han d'estar en el fitxer ocult *.env*:

```bash
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...
DEEPSEEK_API_KEY=sk-...
XAI_API_KEY=xai-...
GEMINI_API_KEY=...
```

6. Executa el projecte:

```bash
$ python main.py --help
```

**Mode anàlisi:**
Analitza la producció de narracions de diferents APIs de LLM.

```
$ python main.py --mode=analisi
```

**Mode Producció:**
Genera narracions amb la API escollida.

```
$ python main.py --mode=produccio --api=anthropic --num=20
```

## Estructura del Projecte

El repositori té la següent estructura:

- `src/`: codi font del projecte
    - `main.py`: script principal i punt d'entrada
    - `modules/`: conté les diferents funcionalitats
    - `modules/analize.py`: 
    - `modules/models.py`: definició dels models LLM a utilitzar
    - `modules/prompt.py`: generació del prompt que s'envia a la IA
    - `modules/rebost_de_mots_production.py`: 
    - `modules/response_test.py`: mode test per no consumir tokens en fase de desenvolupament
    - `modules/vocabulary.py`: generació del vocabulari a partir de vocabulari/vocabulari.txt

    - `vocabulari/vocabulari.txt`: el vocabulari a utilitzar
    - `output/`: fitxers markdown i pdf generats. El recull de narracions té el format *relats_anthropic_260517_113608.pdf*, on queda reflectit la IA utilitzada i el timestamp.
- `doc/`: documentació generada
- `requirements.txt`: A text file specifying the Python dependencies required for the project.
- `README.md`: This file, providing an overview of the repository and instructions for usage.
- `LICENSE`

## Scores

S'ha testejat les API de OpenAI (gpt-4o, gpt-4o-mini), Anthropic (claude-opus-4-7), XAI (Grok-4.3) i DeepSeek (deepseek-reasoner), Gemini (gemini-2.5-flash) obtenint els següents resultats:

```
score gemini:               9,90
score antropic:             9,60
score deepseek:             8,80
score openai (gpt-4o):      8,65
score xai:                  8,35
score openai (gpt-4o-mini): 6,85
```

Els score s'han calculat amb els següents pesos, i fent el promig sobre dos textos:

```
qualitat literària:           20%
totes les paraules?:          10%
correcció ortogràfica:        10%
correcció gramatical:         20%
definició de les paraules:    20%
context dins de la narració:  10%
format de sortida:            10%
```

Aquests són els models testejats, som conscients de què hi ha models millors a maig de 2026. Però els resultats que hem aconseguit són satisfactoris.

## Resultats

Com a mostra de què aconseguim, pots llegir els 20 relats que s'han generat en el document:

- [src/output/relats_gemini_260518_010551.pdf](src/output/relats_gemini_260518_010551.pdf)

## License

The code in this repository is licensed under the GNU GENERAL PUBLIC LICENSE. Feel free to use and modify the code for your own purposes.

