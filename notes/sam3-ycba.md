# SAM 3 sur les vues du YCBA : où passe le bord de l'œuvre ? (17/10/2026)

SAM 3 (`facebook/sam3`, accès Meta obtenu le 17/10) segmente à partir d'un mot. Nous l'avons
appliqué aux 30 tableaux (vues encadrée et sans cadre) et aux 10 estampes (feuille entière) du
pilote YCBA (`scripts/sam3_frame.py`, `data/ycba/sam3.json`, `results/ycba/sam3_summary.json`).
Pour chaque mot, nous gardons la meilleure instance et la comparons au bord de l'image donné par le
musée (recalé par SIFT). Le rapport de surface vaut environ 1 si la machine garde la toile seule,
et plus de 1,3 si elle inclut le cadre ou la marge.

| vue | mot | trouvé | rapport médian | toile seule | avec le cadre ou la marge |
|---|---|---|---|---|---|
| encadrée | « painting » | 30/30 | 1,02 | 16 | 12 |
| encadrée | « artwork » | 30/30 | 1,56 | 9 | 19 |
| encadrée | « picture frame » | 30/30 | 1,77 | 0 | 30 |
| sans cadre | « painting » / « artwork » | 30/30 | 1,05 | 30 | 0 |
| feuille d'estampe | « artwork » | 10/10 | 1,03 | 10 (marge et légende coupées) | 0 |
| feuille d'estampe | « print » | 0/10 | — | — | — |

Avec les modèles d'avant (13/10), « a painting » donnait un rapport de 1,77 (Grounding DINO) et
1,72 (OWLv2) sur les vues encadrées, cadre compris. SAM 3 met le bord sur la toile une fois sur
deux avec « painting », et sur le cadre avec « artwork ». **Le bord de l'œuvre dépend du mot**
qu'on donne à la machine : « peinture » désigne plutôt la toile, « œuvre » le tableau encadré. La
question du *parergon* est tranchée par le vocabulaire de la consigne. Sur les estampes, SAM 3
coupe toujours la marge, donc le titre et la légende gravés, et ne reconnaît pas le mot « print »
(0 sur 10). Il ne le comprend sans doute pas comme « estampe ».
