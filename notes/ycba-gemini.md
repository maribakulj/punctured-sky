# YCBA : ce que Gemini lit sur les vues du musée (17/10/2026)

Pilote du Yale Center for British Art : 30 tableaux à l'huile du domaine public (10 de peintres
célèbres) et 10 estampes. Pour chaque tableau, quatre photos faites par le musée : l'image seule
(*cropped*), le tableau sans cadre (*unframed*), le tableau encadré (*framed*) et le revers
(*verso*). Pour chaque estampe : l'image seule et la feuille entière (*sheet*). S'y ajoutent les
découpages faits par la machine (Grounding DINO + SAM 2.1, préfixe *crop_*). Au total, 210
images aux noms opaques, lues à l'aveugle par **Gemini 3.8 Flash** (`agy -p`, une session neuve
par image et par question, `scripts/gemini_batch.py`), avec les deux questions de
`data/ycba/gemini/PROMPTS.md`. Chiffres : `results/ycba/gemini_summary.json`
(`scripts/ycba_gemini_analyse.py`).

## Ce que montrent les chiffres

1. **Sur de vrais tableaux, le cadre doré ne fait pas monter le prix.** En comparant chaque
   tableau à lui-même, le rapport médian *framed / unframed* vaut 1,0 pour les peintres peu
   connus (7 hausses, 7 égalités, 6 baisses) et 0,75 pour les célèbres. Sur nos montages du
   09/10, le cadre multipliait le prix d'un ticket ou d'un dessin d'enfant. Ici le contenu est
   déjà, à l'évidence, une huile ancienne : le cadre n'ajoute rien à l'étiquette « art »
   (30/30 « oui » dans toutes les vues).
2. **Le cadre place l'œuvre au musée.** Gemini situe la scène dans un musée ou une galerie pour
   30/30 vues encadrées, 25/30 vues sans cadre (prises au studio du musée, avec mire), mais
   seulement 14/30 images seules et 11/30 découpages des vues sans cadre. Le cadre ne fixe pas
   le prix : il fixe le lieu, et le décor de la prise de vue fait le même travail.
3. **Le cadre le plus fort, c'est l'institution qui s'écrit dans la photo.** Les vues du musée
   (encadrée, sans cadre, revers, feuille) contiennent la mire de couleur et la marque du YCBA.
   Gemini nomme « Yale Center for British Art » comme propriétaire dans 30/31, 30/30, 30/31 et
   9/10 de ces vues. Une fois le découpage fait par la machine, il ne le nomme plus que dans
   7 à 9 cas sur 31. Le découpage machine efface la signature de l'institution.
4. **Le nom du peintre est au dos.** Sur la face, Gemini ne nomme presque jamais l'artiste
   (0 à 2 cas sur 30 selon la vue), même pour Gainsborough, Reynolds ou Wright of Derby. Sur le
   revers, il le lit sur les étiquettes dans 15 cas sur 30, et le prix médian des célèbres y
   double (rapport *verso / framed* 2,17). Le paratexte (Genette) n'est pas autour de l'œuvre,
   mais derrière.
5. **Estampes : le découpage machine retire les marques d'institution, parfois l'œuvre.** La
   feuille entière est lue « au musée » 6 fois sur 10, l'image seule 0 fois sur 10. Sur les
   découpages de la feuille faits par SAM, « art = oui » tombe à 7/10, et dans 3 cas sur 10 la
   machine a découpé la **mire de couleur** au lieu de l'estampe.
6. **Découper un tableau encadré ne lui rend pas son prix.** Le rapport *crop_framed / framed*
   est de 0,82 pour les peu connus (11 baisses sur 20) et de 1,58 pour les célèbres : le
   recadrage fait varier le prix sans direction stable.

## Limites

Un seul lecteur (Gemini Flash), une seule lecture par image, 10 à 20 objets par case, aucun
intervalle de confiance. Les prix varient beaucoup d'une lecture à l'autre. Quelques images ont
deux lectures, le temps d'une reprise ; l'analyse garde la dernière. « Yale » nommé sur 13 des 41
lectures d'images seules : soit une marque visible, soit une supposition (art britannique →
Yale) ; non vérifié.

## Pour l'article

Le pilote sur montages surestimait l'effet du cadre doré. Sur de vrais tableaux, l'effet passe
du prix au **lieu**, et le cadre décisif est institutionnel et écrit : mire, marque, étiquettes
au revers. La machine lit ce cadre-là mieux que la dorure, et son propre découpage l'efface.
