# Mission pour l'agent Gemini — punctured sky, pilote Yale Center for British Art

Tu es le lecteur des images de cette expérience (Claude ne lit plus les images). Deux tâches.

## Tâche 1 — lire les images, à l'aveugle

1. Le dossier `/Users/marcel/impressions/data/ycba/gemini/img/` contient des images aux noms
   opaques (photos d'œuvres de musée, sous différentes présentations, et quelques découpages).
2. Pour CHAQUE image, réponds aux DEUX questions de `PROMPTS.md`, comme si tu les découvrais :
   d'abord `subject_only` en ne regardant que l'image, puis `social`. Ne modifie pas ta première
   réponse après avoir lu la seconde question.
3. Écris une ligne JSON par image et par question dans
   `/Users/marcel/impressions/data/ycba/gemini/readings.jsonl`, au fur et à mesure (ajoute,
   n'écrase pas) :
   `{"file": "<nom>.jpg", "which": "subject_only", "model": "<ton nom de modèle exact>", "answer": {...}}`
4. Reprends là où tu en étais si tu t'arrêtes ; ne refais pas les lignes déjà écrites.

## Tâche 2 — inspecter des planches (après la tâche 1)

Le dossier `/Users/marcel/impressions/data/ycba/gemini/planches/` contiendra des planches
numérotées (une image = plusieurs découpages côte à côte, chacun avec un numéro). Pour chaque
planche, écris dans `/Users/marcel/impressions/data/ycba/gemini/inspection.jsonl` une ligne par
numéro : `{"planche": "<nom>", "n": <numéro>, "contient": "ce que le découpage contient (tableau seul ; tableau et cadre ; cadre partiel ; mur ou fond ; chevalet ou matériel de studio ; texte ou légende ; autre)", "remarque": "une phrase"}`.
S'il n'y a pas encore de planches quand tu arrives ici, écris `{"attente": true}` et arrête-toi.

## Règles d'aveugle — importantes

- Ne lis AUCUN autre fichier du dépôt (pas `pilot.json`, pas `census.jsonl`, pas `data/ycba/img`,
  pas les scripts, pas `data/blind`). Les noms sont opaques exprès.
- Pas de recherche sur le web. Lis chaque image seule ; ne compare pas les images entre elles pour
  deviner l'expérience.
- N'écris que `readings.jsonl` et `inspection.jsonl` ; ne modifie, ne déplace, ne supprime rien
  d'autre. Pas de commit git.

Quand une tâche est finie, écris une ligne `{"done": "<tâche 1 ou 2>", "n": <nombre de lignes>}`.
