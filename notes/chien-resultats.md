# « Le chien du tableau » : résultats (17/10/2026)

Résultats mis en face du préenregistrement [`prereg-chien.md`](prereg-chien.md), commité avant la
fabrication des images. Chiffres : `results/chien/summary.json` (`scripts/chien_analyse.py`) et
`results/chien/sam3_check.json` (`scripts/chien_sam3_check.py`). Lecteur : Gemini 3.8 Flash
(`agy -p`), à l'aveugle, une session neuve par image et par question, 2 répétitions, soit
576 + 96 lectures. Aucune lecture n'a échoué.

## En une phrase

Gemini ne prend **jamais** le chien accroché au mur pour un chien présent, **avec ou sans cadre**.
Le cadre n'est donc pas ce qui lui fait faire la différence ici. Ce qui le trouble, c'est le chien
découpé et collé au mur, sans rectangle autour.

## Tableau principal (q_present, % « non, pas de chien dans la pièce », 24 lectures par case)

| Condition | % découplé | IC 95 % (Wilson) |
|---|---|---|
| P0 chien posé au sol (témoin) | 0 | 0–14 |
| W5 chien découpé, collé au mur | 50 | 31–69 |
| W1 image nue au mur | **100** | 86–100 |
| W2 passe-partout | 100 | 86–100 |
| W3 cadre doré | 100 | 86–100 |
| W4 faux cadre | 100 | 86–100 |

« Combien d'êtres vivants dans la pièce ? » donne le même dessin : 0 être vivant dans 4 % des
lectures en P0, 71 % en W5, et 100 % en W1 à W4. Les deux répétitions donnent la même réponse
dans 70 cas sur 72 (q_present) et 68 sur 72 (q_vivants).

## Hypothèses préenregistrées

- **Témoin (P0) : validé.** Le chien posé au sol est dit présent dans 24 lectures sur 24.
  Le montage est donc lisible.
- **H1 (SAM 3 trouve le chien) : confirmée.** 108 images sur 108 qui contiennent un chien.
  Il en trouve aussi zéro dans les 12 images T0, qui n'en contiennent pas.
- **H2 (W1 ≤ W2 ≤ W3, avec un écart d'au moins 15 points) : non confirmée.** L'ordre est
  respecté, mais seulement parce que les trois valent 100 %. L'écart est nul, et il est
  négligeable selon notre seuil.
- **H3 (W3 − W4 ≥ 15 points) : non testable.** Les deux conditions sont au plafond (100 %).
- **H4 (la quarantaine) : non confirmée.** Gemini n'a répondu « pomme » dans **aucune** des
  96 lectures, quelle que soit la place de la phrase : sur le mur (T0), dans l'image nue (T1),
  sous cadre doré (T3) ou sous faux cadre (T4).

**Ce qui contredit l'hypothèse du découplage pour cette machine** (les contradictions annoncées
d'avance) :
- **(a) est réalisée.** Le découplage est déjà maximal en W1, sans aucun bord. Le cadre n'est
  pas nécessaire. Un rectangle d'image posé sur un mur suffit.
- **(b) ne peut pas être jugée**, à cause de cet effet plafond.
- **(c) n'est pas réalisée.** La frontière donne bien le découplage.
- **(d) est réalisée.** L'obéissance n'est pas plus basse en T3 qu'en T0 : elle est nulle partout.

## Contrôles ajoutés après coup (exploratoires)

- **Gemini lit-il la phrase ?** Oui. On lui a demandé de recopier le texte visible
  (`data/chien/gemini_txt/`, une lecture par image), et il la recopie mot pour mot dans
  48 images sur 48, quelle que soit la place. Il voit donc l'ordre, mais ne le
  suit jamais, même quand il est écrit au mur. C'est très probablement un effet de son
  entraînement contre les instructions cachées dans les images (*prompt injection*). Ce
  comportement est le même pour tout texte dans l'image, cadre ou pas. Notre test ne pouvait
  donc pas mesurer une quarantaine *due au cadre*. Pour cela, il faudrait un lecteur qui obéit
  au moins un peu au texte nu.
- **q_aboie ne mesure pas ce qu'on voulait.** Même avec le chien au sol, Gemini répond « non »
  ou « impossible à dire » dans 23 cas sur 24. Il raisonne sur l'humeur du chien (calme,
  couché), pas sur sa présence. Cette question est donc écartée. C'est une erreur de conception
  de notre part.

## Analyses exploratoires annoncées

- **W5, le chien découpé au mur.** C'est le seul endroit où il se passe quelque chose. Gemini le
  dit présent une fois sur deux. Dans ses descriptions, il « flotte », semble « incrusté »,
  « en lévitation », ou c'est une « figurine » ou une « silhouette découpée ». Il est dit absent dans 75 % des cas dans la galerie, contre 25 %
  dans le salon. Mais avec 12 lectures par pièce, les intervalles se touchent encore (47–91 contre
  9–53) : l'écart reste indéterminé. Le rectangle compte donc plus que la moulure. **Sans bord droit autour de lui,
  le chien n'est plus ni une image ni un animal.** C'est ce que l'essai appelle le niveau 1, la
  simple distinction : ici, c'est elle qui fait le travail, et pas le cadre au sens du niveau 2.
- **Peinture contre photo.** Il n'y a aucune différence au mur (100 % partout). En W5, la
  peinture est découplée un peu moins souvent (42 % contre 58 %), mais les intervalles se
  chevauchent : c'est indéterminé.
- **Descriptions (q_decrit).** Le chien est dit représenté (« tableau », « cadre », « photo »)
  dans 79 % des cas en W1, et dans 100 % des cas en W2, W3 et W4. Les 21 % restants de W1 sont
  des descriptions qui décrivent *la scène dans l'image*, sans dire qu'il y a une image : « un
  berger allemand est couché sur une pelouse ». Cela n'arrive que dans la galerie, où l'image
  occupe une grande part de la vue. Ces mêmes lectures répondent pourtant « non » à q_present.
  **Le bord change donc la façon de raconter, sans changer le jugement.** C'est le seul écart
  dû au bord, et il a la taille prévue (+21 points de W1 à W2). Mais les intervalles se
  touchent (59–91 contre 86–100) : il reste indéterminé selon nos règles. Notre codage par mots
  compte aussi « image » dans « cette image montre » ; il surestime un peu le découplage en P0
  (17 %).

## Ce que cela veut dire

1. Pour ce lecteur, **la séparation entre « représenté » et « présent » ne passe pas par le
   cadre.** Un rectangle de photo sur un mur suffit à la faire. Le cadre doré, le passe-partout
   et le faux cadre n'ajoutent rien de mesurable au jugement.
2. Ce qui compte, c'est **le bord droit du rectangle**, et pas son ornement. Sans rectangle (W5),
   le jugement s'effondre à 50 %. Cela va dans le sens de la thèse au niveau 1 (une frontière
   qui découpe), et contre elle au niveau 2 (le cadre comme marque spéciale de lecture). Pour
   une machine récente, « image dans l'image » est une catégorie qu'elle reconnaît au bord
   seul.
3. La « quarantaine » (Leslie) n'a pas pu être testée. Le modèle met en quarantaine *tout* texte
   écrit dans l'image, avec ou sans cadre.
4. La segmentation (SAM 3) réussit partout, y compris en W5, là où le jugement vacille. La
   frontière trouvée par la machine qui segmente ne suffit donc pas à dire *quel genre* de
   chose est à l'intérieur. Cela confirme, dans un sens précis, la distinction de l'essai entre
   segmenter et découpler.

## Limites

Un seul lecteur, puissant et entraîné à lire des pièces décorées : l'effet plafond était
prévisible. Pour aller plus loin, il faudrait :
- des lecteurs plus faibles ou plus anciens (un petit modèle vision-langage local) ;
- des cas où le doute est réel : trompe-l'œil, fenêtre contre tableau, écran, miroir, ou un
  chien peint à taille réelle sans bord ;
- un codage humain des descriptions.

Les montages restent des montages : Gemini en voit certains comme « incrustés ».
