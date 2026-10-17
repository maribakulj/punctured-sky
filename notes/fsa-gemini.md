# FSA-OWI : le bord du film change-t-il la lecture ? (17/10/2026)

Expérience qu'Arnold et Tilton (*Humanités numériques* 13, 2026) n'ont pas faite. Ils retirent le
« cadre » des photos d'archive (bords du film, carton) en affirmant qu'il perturbe les modèles,
mais sans mesurer cette perturbation. Voir [`litt-cadrage-ia-machines.md`](litt-cadrage-ia-machines.md).

**Protocole.** 60 photos de la FSA-OWI tirées au hasard dans le domaine public (Library of Congress,
JPEG de référence « v », `tile.loc.gov`) : 30 négatifs noir et blanc et 30 diapositives couleur
(`scripts/fsa_pilot.py`, graine 20261017). La zone de la photo est découpée par **leur propre
modèle** : le seul publié sur Zenodo (`project-4.pt`, YOLOv8, classe unique « frame »), alors que
l'article annonce quatre modèles et 45 000 images annotées. Gemini 3.8 Flash lit à l'aveugle la
photo entière (avec le bord) et la photo découpée, sous des noms opaques, avec les deux mêmes
questions que pour le YCBA. Chiffres : `results/fsa/summary.json` (`scripts/fsa_analyse.py`).

## Résultats

1. **Leur modèle marche sur le noir et blanc, beaucoup moins sur la couleur.** Sur les 30 négatifs,
   la confiance va de 0,96 à 1,00, et le découpage garde 63 à 92 % de l'image : le bord retiré est
   donc important. Sur la couleur, rien n'est détecté pour 7 photos sur 30, et 10 autres ont un
   découpage douteux (confiance < 0,9 ou moins de la moitié de l'image). Il en reste 13. On
   retrouve ce que leur article montre d'un support à l'autre.
2. **Pour Gemini, le bord du film est transparent.** Sur 30 négatifs, avec ou sans bord :
   - même datation dans 25 cas sur 30 (médiane « années 1930 » dans les deux cas) ;
   - prix médian identique (rapport 1,0 : 9 hausses, 12 égalités, 8 baisses) ;
   - le support (négatif, film, perforations, archive) n'est **jamais** nommé, ni dans la
     description ni dans les réponses sociales ;
   - l'archive n'apparaît qu'une fois comme propriétaire.
   Gemini lit *à travers* le support : il décrit la moisson ou le filet de pêche, et met un prix
   sur le camion ou le champ. Même chose sur les 13 diapositives couleur (10 datations identiques
   sur 11 comparables).
3. **Rien n'est de l'art.** « Art = oui » dans 0 cas sur 30 en noir et blanc et 1 sur 13 en
   couleur, avec ou sans bord. Ces photos sont pourtant aujourd'hui exposées dans des musées. La
   question « œuvre d'art ? » est tranchée par le genre (documentaire), pas par le support.

## Ce que cela veut dire

- **Contre Arnold et Tilton, sur ce point précis :** pour un modèle de langage multimodal récent et
  pour ces questions, le bord du film ne change pas la lecture.
- **Les encodeurs non plus** (`scripts/fsa_embed.py`, `results/fsa/embed.json`, 43 photos). Pour
  CLIP, SigLIP, DINOv2 et DINOv3, la photo découpée retrouve sa version entière en premier dans
  43 cas sur 43, avec un cosinus de 0,91 à 0,95. Le bord rend les photos à peine plus
  semblables entre elles : de +0,00 (DINOv3, noir et blanc) à +0,03 (CLIP, couleur). C'est un
  effet réel mais minime, loin du « de manière significative » de l'article. Le bord pourrait
  peser davantage sur un corpus où il varie beaucoup (tirages sur carton, que nous n'avons pas).
- **Pour la thèse :** le bord du film fonctionne comme le *cache* de Bazin, une fenêtre que le
  regard traverse. Le cadre doré du musée et la mire avec la marque du YCBA (voir
  [`ycba-gemini.md`](ycba-gemini.md)) fonctionnent comme des cadres *signifiants* : ils déplacent
  le lieu, le propriétaire, le nom. La machine distingue donc en pratique le cadre-fenêtre du
  cadre-étiquette.

## Limites

Un lecteur, une lecture par image ; 30 + 13 photos. Les questions portent sur ce que montre
l'image, et Gemini a répondu sur la scène, pas sur l'objet photographique. Une question « qu'est-ce
que cet objet ? » pourrait faire apparaître le négatif. Le bord des JPEG « v » est peut-être plus
étroit que celui des TIFF complets. Pas de tirages sur carton (le cadre le plus large de leur étude, 43 % de l'image).
