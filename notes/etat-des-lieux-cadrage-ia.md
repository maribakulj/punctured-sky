# Le cadrage de l'art par les modèles d'IA — état des lieux et prolongements

*14/10/2026. Synthèse de deux notes détaillées, aux références vérifiées une à une :
[`litt-cadrage-ia-machines.md`](litt-cadrage-ia-machines.md) (côté machines, ~45 références) et
[`litt-cadrage-ia-humanites.md`](litt-cadrage-ia-humanites.md) (côté humanités, ~40 références).
Voir aussi [`cadrage-et-valeur.md`](cadrage-et-valeur.md). Ce qui suit renvoie à ces notes pour
chaque référence ; ce qui est marqué « nous » est notre proposition, pas l'avis des auteurs.*

## 1. Ce que font les machines au cadre (état des lieux)

**Elles recadrent avant de regarder.** CLIP et DINOv2 coupent l'image en carré au centre ; c'est
dans leur code. Les bords et les marges sont perdus avant tout calcul. Une seule étude mesure la
perte, sur des photos de mode (Baldrati et al. 2023). Pour les œuvres, rien.

**Elles recadrent pour montrer.** Le recadrage automatique de Twitter centrait la vignette sur le
point le plus saillant ; les audits (Yee et al. 2021 ; Birhane et al. 2022) y ont trouvé des biais
de race et de genre, et Twitter a fini par montrer les photos entières. Cropper (2025) et ClipCrop
(2023) recadrent selon le goût appris ou sur un mot. La norme IIIF propose le centre par défaut.
Aucun de ces travaux ne porte sur l'art.

**Elles apprennent à ignorer le cadre.** Reconnaître une œuvre photographiée en salle, c'est
apprendre à traverser cadre, reflets et mur (Met Dataset, SynGallery). Les détecteurs découpent
le tableau *avec* son cadre. Le Rijksmuseum a prototypé une recherche par fragments (SAM puis
DINOv2) : l'institution laisse la machine tracer les bords de ses œuvres.

**Elles inventent le hors-cadre.** L'outpainting (DALL·E, 2022) a été présenté en prolongeant la
*Jeune fille à la perle* ; les bandes perdues de la *Ronde de nuit* ont été repeintes par IA en
2021 ; au Mauritshuis, en 2023, une image Midjourney a été accrochée dans la salle de l'original.

**Le cadrage de l'entrée change ce qu'elles disent.** Wang, Larson et Zhao (2026) : la même
consigne, des images cadrées autrement, des descriptions différentes. ViCrop (2025) : recadrer
sur le détail améliore les réponses. Un cercle rouge, une bordure apprise, un mot écrit dans
l'image orientent le modèle (Shtedritski 2023 ; Goh 2021).

**Elles ont appris l'art déjà encadré et mis en vente.** Dans un grand corpus de paysages, près de
1 000 images sur 15 000 avaient encore leur cadre (Lee et al. 2020). Dans le sous-ensemble
« esthétique » de LAION, une part notable vient d'un site qui vend des reproductions (Baio 2022).
Pour CLIP, « le passé lointain est en marbre » (Offert 2023).

**Ce qui manque.** Personne n'a mesuré où un segmenteur met le bord d'une œuvre, ni ce qu'un
recadrage machine change à sa lecture, ni comment un cadre change le prix estimé par un modèle.
Nos pilotes du 09/10 (cadre social) et du 13/10 (cadre de la machine) n'ont pas d'équivalent
publié trouvé.

## 2. Ce que les humanités en ont dit

**Le cadre et l'écran.** Bazin oppose le cadre du tableau, *centripète* (il rassemble le regard
vers l'intérieur), au cache de l'écran de cinéma, *centrifuge* (il laisse supposer que le monde
continue au-delà). Deleuze : cadrer, c'est choisir les parties, et le cadre détermine un
hors-champ. Manovich fait la généalogie de l'écran ; Galloway fait de l'interface un effet.

**Les images faites pour les machines.** Farocki (« images opératoires »), Paglen (« images
invisibles », qui n'ont pas besoin d'être vues), Parikka, Hoel : des images qui servent une
opération plutôt qu'un regard. Crawford et Paglen, Denton, Malevé : les catégories et les
étiquettes des jeux de données sont des choix, faits vite et à grande échelle.

**Le détail et le recadrage en histoire de l'art.** Arasse : le détail découpé par un regard porte
un sens. Fawcett, Nelson : la diapositive fait de l'œuvre un « fait visuel » cadré. Le zoom du
Google Art Project a été critiqué comme un regard sans point de vue.

**La critique de la vision machine appliquée à l'art.** Offert, Wasielewski, Cetinic et She,
Drucker, Bishop, Manovich et Arielli : la machine n'est pas un regard neutre ; elle formalise
l'histoire de l'art à sa manière.

**Ce que personne n'a encore fait.** Lire l'outpainting avec la théorie du hors-champ ; critiquer
le zoom gigapixel ou le format carré des plateformes comme des cadres ; mesurer le cadre machine.

## 3. En quoi cela prolonge la réflexion sur le cadre

La théorie classique pose une question : le cadre fait-il partie de l'œuvre ? Simmel et Ortega
répondent qu'il l'isole ; Derrida (le *parergon*) qu'il n'est ni dedans ni dehors. L'arrivée des
machines ne répond pas à la question : elle la **démultiplie**. Sept prolongements, chacun appuyé
sur la littérature et, quand nous en avons, sur nos mesures.

**1. Deux familles de cadres : pour être vu, pour être traité.** Le cadre de présentation dit
« regardez ceci » ; le cadre opératoire (le carré de 224 pixels d'un encodeur, la vignette, le
découpage d'un segmenteur) dit « traitez ceci » (d'après Farocki et Paglen ; nous). Une
reproduction d'œuvre porte aujourd'hui les deux à la fois, et le cadre opératoire est le dernier,
celui que personne ne voit.

**2. Le *parergon* reçoit des réponses contradictoires selon la machine.** *Nous, mesuré :* pour
les détecteurs et SAM, le cadre est **dans** l'œuvre (ils entourent le cadre doré quand on demande
« le tableau », sur nos montages comme sur 30 vrais tableaux du Yale Center for British Art).
Pour le modèle qui décrit, le cadre est **à part mais signifiant** : il le date séparément, le dit
« ironique » autour d'un ticket, et lui fait porter un prix. La question de Derrida n'a plus une
réponse : elle en a une par outil.

**3. Le cadre agit comme une étiquette, et le nom l'emporte sur la dorure.** Bateson faisait du
cadre un message sur le message ; Genette, de la légende, un seuil. *Nous, mesuré :* un cadre
ancien fait d'un ticket ou d'un dessin d'enfant une œuvre de musée et en multiplie le prix, mais ne
change rien à un Renoir que le modèle reconnaît ; et un Renoir que Gemini ne reconnaît pas voit son
prix suivre le cadre. Pour la machine, le cadre le plus fort est le **nom** (la catégorie, la
reconnaissance) ; le cadre visuel ne compte que là où le nom manque.

**4. Le cadre machine garde l'ornement et coupe le texte.** *Nous, mesuré :* sur les estampes du
YCBA, les détecteurs coupent l'image et laissent la marge, avec le titre et la légende gravés,
7 à 10 fois sur 10. Le recadrage machine conserve le *parergon* décoratif (la dorure) et retire le
paratexte (Genette) : exactement l'inverse de ce dont l'historien a besoin pour identifier une
édition ou une source.

**5. Le cadrage sans auteur, réglé par la saillance.** Le recadrage automatique garde la forme du
choix et perd celui qui choisit ; il centre toujours sur le plus saillant (Yee, Birhane ; Deleuze ;
Arasse). *Nous, mesuré :* c'est aussi ce qui décide de la description — une œuvre petite et
décentrée devient un complément, quel que soit le support.

**6. Le bord du fichier est un cache, non un cadre.** Pour la machine, le seul cadre certain est
le bord de l'image ; mais il coupe sans rien signifier, comme le cache de Bazin. Une bordure
dorée *dans* l'image n'est pas reconnue comme limite centripète : elle est un objet de la scène
(*nous*, d'après nos résultats sur la saillance). Et quand la machine recadre, elle change le sens
dans les deux directions : sur un fond neutre, elle rend le contenu à lui-même ; dans un salon,
elle refait un musée (*nous, mesuré*).

**7. Le hors-champ inventé, et l'art appris comme marchandise encadrée.** L'outpainting traite le
tableau comme un écran de cinéma et remplit le hors-champ avec le probable : c'est la négation
exacte du cadre de Simmel (proposition, aucune source savante ne le dit encore). Et si l'art que
les modèles ont appris est souvent déjà encadré, accroché, mis en vente (Lee 2020 ; Baio 2022),
la machine a pu apprendre le cadre doré comme un **attribut ordinaire de « l'art »** et de son prix
— ce que montrerait notre pilote de valeur (hypothèse à vérifier sur un échantillon de LAION).

## 4. Ce que cela suggère pour la suite

- Mesurer ce que le cadre opératoire (recadrage central, tuiles) retire aux œuvres, sur le YCBA.
- Inspecter un échantillon d'images d'art de LAION : combien sont encadrées, sur un mur, en vente ?
- Tester l'outpainting sur des œuvres à bord connu (la *Ronde de nuit* rognée en 1715).
- Garder la distinction : ce que disent les auteurs ; ce que nous mesurons ; ce que nous proposons.
