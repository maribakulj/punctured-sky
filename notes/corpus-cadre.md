# Corpus pour « le cadre de la machine »

*Note de préparation, 13/10/2026. Aucune mesure ici : seulement le choix des corpus. Elle sert
d'abord à la prochaine expérience (un outil de segmentation qui isole « l'œuvre » trace lui-même
un cadre : où met-il le bord ? que perd-on ?), et aussi aux suites « cadre et valeur ».*

**Règle suivie.** Chaque corpus et chaque référence ont été ouverts en ligne le 13/10/2026 ; le
lien donné est celui qui a servi à vérifier. Quand j'ai interrogé le corpus lui-même (API,
manifeste IIIF, vignette regardée), c'est écrit **[testé]**. Quand une information vient d'une
page que je n'ai pas pu lire en entier, ou reste douteuse, c'est écrit **[incertain]**. Je n'ai
téléchargé que quelques vignettes pour regarder (moins de 1 Mo en tout), rien de plus.

---

## En bref

- Pour savoir **où la machine met le bord**, il faut un corpus où **le bord « officiel » est
  connu autrement** : par le musée lui-même, par une mesure, ou par une autre photo de la même
  œuvre. Sans cela, on ne peut que regarder, pas mesurer.
- **Le meilleur corpus trouvé est celui du Yale Center for British Art (YCBA)** : pour une
  partie des peintures, le musée publie **quatre photos du même tableau** — « recadré sur
  l'image », « sans cadre » (toile avec ses bords), « encadré », et **le dos encadré**. Pour les
  estampes et dessins : l'image seule, puis la feuille entière avec ses marges et inscriptions.
  C'est exactement la question « où est le bord de l'œuvre ? », déjà tranchée par le musée,
  à comparer avec ce que trace la machine. Libre de droits, IIIF, vignettes de 25 Ko : **faisable
  tout de suite**, même avec un réseau à 64 Ko/s. **[testé]**
- **Deuxième : la Witt Library du Courtauld** (plus de deux millions de reproductions **collées
  sur des cartons**, avec légendes manuscrites, tampons, coupures de presse). Même œuvre,
  dizaines de reproductions différentes, chacune dans son montage. C'est le corpus pour
  « que perd-on ? » : la légende, la source, la date. **[testé]** (vignettes 640 × 480,
  licence CC BY-NC).
- **Troisième : les photos de visiteurs du Met dataset** (Ypsilantis et al. 2021 ; plus de
  1 100 photos prises dans le musée, chacune reliée à la photo de studio de l'œuvre ; 34 Mo
  en tout). C'est le terrain « réel » : cadre, mur, reflets, visiteurs.
- Un **petit corpus d'appoint** très net : **le Rhinocéros de Dürer** (une quarantaine de
  fichiers sur Wikimedia Commons, dont quatre éditions de la BnF, de 1515 à 1620, avec leur
  texte typographié au-dessus de l'image). Que garde le segmenteur : la bête, ou la bête et son
  texte ?
- Pour **cadre et valeur**, le corpus le plus prometteur est **German Sales 1901–1945**
  (catalogues de vente numérisés à Heidelberg) **avec les prix du Getty Provenance Index**
  (données CC0). Mais l'accès automatique aux images est aujourd'hui freiné (page anti-robots),
  et je n'ai pas vérifié si les planches montrent les tableaux encadrés **[incertain]**.
- Côté outils, **Grounding DINO (base) et SAM 2.1 (base-plus) sont déjà dans le cache local** de
  Hugging Face sur le Mac **[testé]** : la chaîne « Grounding DINO + SAM 2 » peut tourner sans
  rien télécharger. SAM 3 n'est pas en cache, ses poids sont soumis à demande d'accès, et son
  dépôt officiel demande une carte graphique CUDA.

---

## 1. Ce qu'un bon corpus doit offrir pour cette expérience

La question « où le segmenteur met-il le bord ? » suppose de pouvoir comparer son bord à
**d'autres bords possibles** :

| bord possible | exemple |
|---|---|
| l'image peinte (le « champ ») | le bord de la peinture visible |
| le support entier | la toile avec ses bords de tension, la feuille avec ses marges |
| l'ouverture du cadre (la « vue ») | ce que le cadre laisse voir |
| le cadre extérieur | le bord doré |
| le montage | le carton de la photothèque, la page du livre |
| la scène | le mur, la salle, l'écran |

Un corpus est d'autant meilleur qu'il **fait varier une seule de ces couches à la fois** et que
**le bord de référence est connu sans la machine**. Les variables utiles :

1. **même œuvre, plusieurs présentations** (avec / sans cadre, plusieurs reproductions) ;
2. **même cadre ou même montage autour d'œuvres différentes** ;
3. **inscriptions, marges, légendes** près du bord (ce qu'on perd si on coupe) ;
4. **photos datées** (la présentation change avec le temps) ;
5. **mesures** (dimensions de l'ouverture du cadre, de la feuille).

Un point de méthode vaut pour tous les corpus : **le mot qu'on donne au segmenteur est déjà un
cadre.** « painting », « artwork », « picture », « print », « the image » ou « frame » ne
désignent pas le même objet. Il faudra faire varier la consigne et la noter.

---

## 2. Classement

Intérêt = ce que le corpus permet de trancher pour la question du bord. Faisabilité = accès réel
aujourd'hui, avec un Mac 16 Go et un réseau lent.

| corpus | intérêt | faisabilité | bord de référence connu ? |
|---|---|---|---|
| **A. YCBA, vues « recadré / sans cadre / encadré / dos »** | très fort | **très bonne** | **oui, par le musée** |
| **B. Witt Library (Courtauld), cartons de photothèque** | très fort | bonne (vignettes) | non (à annoter), mais le carton est entier |
| **C. Met dataset, photos de visiteurs** | fort | **très bonne** (34 Mo) | indirect (par appariement avec la photo de studio) |
| D. Rhinocéros de Dürer, éditions | moyen (petit) mais très net | **très bonne** | oui (texte au-dessus = hors image) |
| E. Commons, « Framed paintings » par musée | fort | bonne (lent : limite de débit) | indirect |
| F. Cadres du Met (collection Lehman), avec dimensions « Sight » | moyen | très bonne | **oui, mesure de l'ouverture** |
| G. Rijksmuseum, cadres liés à leur ancien tableau | moyen | moyenne | non |
| H. National Gallery, recadrages (Frame Blog) | moyen (avant / après) | faible (images non libres, peu nombreuses) | non |
| I. Frick Photoarchive | fort en principe | **incertaine** (montages visibles ?) | non |
| J. Fototeca Zeri, KHI Florence, PHAROS | fort en principe | faible aujourd'hui | non |
| K. Photos de salles datées (Joconde, Salon carré, MoMA) | fort pour la saillance | variable | non |
| L. German Sales + Getty Provenance Index (prix) | fort pour **cadre et valeur** | moyenne à faible (images) | non |
| M. Livres d'art anciens (Internet Archive, Gallica) | moyen | bonne (IA), bloquée aujourd'hui (Gallica) | non |
| N. Jeux de données de vision (SynGallery, Virtual Gallery, WikiArt, iMet, Human-Art) | faible à moyen | variable | parfois (masques), mais définis par d'autres |
| O. Google Arts & Culture, posters, cartes postales | faible | faible | non |

**Recommandation : commencer par A (tout de suite), puis B, puis C.** D peut servir de test
rapide pendant la mise au point.

---

## 3. Les corpus recommandés

### A. Yale Center for British Art — le même tableau photographié avec et sans cadre

**Ce que c'est.** Le YCBA publie ses images en IIIF. Pour chaque objet, un « manifeste »
liste les photos. J'ai lu une dizaine de manifestes **[testé]** :

- Turner, *Dort, or Dordrecht* (B1977.14.77,
  [manifeste](https://manifests.collections.yale.edu/ycba/obj/34)) : « recto, cropped to
  image », « recto, unframed », « recto, framed », « verso, framed », « x-radiograph ».
- Reynolds, *Frances Abington as Miss Prue*
  ([manifeste](https://manifests.collections.yale.edu/ycba/obj/5005)) : les mêmes cinq vues.
- Sur 8 peintures tirées un peu au hasard (n° 34, 250, 400, 520, 777, 1000, 1234, 5005),
  **toutes** ont « recadré sur l'image » et « sans cadre » ; **4 sur 8** ont aussi « encadré »
  et « dos encadré ». La proportion sur toute la collection reste à compter.
- Pour les estampes et dessins (n° 2001, 4500, 6000), deux vues : « recto, cropped to image »
  et « recto » (la feuille entière). Exemple regardé : une estampe coloriée collée dans un
  album, avec son titre et sa légende gravés sous l'image
  ([manifeste](https://manifests.collections.yale.edu/ycba/obj/4500)).

J'ai regardé les quatre vues du Turner en 500 px. La vue « sans cadre » montre la toile, ses
bords, **et** le studio : fond noir, chevalet, mire de couleurs, étiquette du YCBA. La vue
« encadrée » ajoute le cadre doré. Le dos montre châssis, étiquettes et numéros anciens.

**Pourquoi c'est bon.** C'est le seul corpus trouvé où **le musée a lui-même tracé trois bords
pour la même œuvre** : l'image, le support, le cadre. On peut donc demander au segmenteur
« painting » sur la vue encadrée, et mesurer s'il rend l'image, la toile, ou l'image plus le
cadre — et comparer au recadrage du musée. Comme les vues sont prises par le même
photographe, avec le même éclairage, **seule la couche change**. Pour les estampes : le
segmenteur garde-t-il la légende gravée sous l'image, que le musée exclut de « l'image » ?

**Question qu'il tranche.** Quand on demande « l'œuvre », la machine s'arrête-t-elle au bord de
l'image, au bord du support, ou au bord du cadre ? Et la réponse dépend-elle du mot de la
consigne ? Pour les estampes : la légende fait-elle partie de l'œuvre pour la machine ?

**Mesure possible.** Le bord de référence s'obtient sans annotation : on retrouve la vue
« recadrée sur l'image » dans la vue « encadrée » par appariement de points (homographie,
tableaux plats). On compare ensuite le masque du segmenteur à ce quadrilatère (recouvrement,
écart du bord en pixels, et ce qui reste dehors : signature, coins, bords peints).

**Accès réel.** **[testé]**

- Manifestes : `https://manifests.collections.yale.edu/ycba/obj/<n>` (numéros à la suite ;
  certains n'existent pas).
- Images : service IIIF `https://images.collections.yale.edu/iiif/2/ycba:<uuid>/full/500,/0/default.jpg`.
  En 500 px, chaque vue pèse **23 à 29 Ko** : quatre vues ≈ 100 Ko par tableau, soit environ
  **8 minutes pour 300 tableaux à 64 Ko/s**.
- Droits : le manifeste porte `rights` = CC0 et « Copyright Statement : Public Domain » pour le
  Turner ; le texte précise que des restrictions peuvent s'appliquer à certaines œuvres. Les
  métadonnées sont en CC0.
- Recensement : la page [Collections Data Sharing](https://britishart.yale.edu/collections-data-sharing)
  annonce l'OAI-PMH (LIDO), l'IIIF et « près de soixante-dix mille » images du domaine public.
  L'adresse exacte du serveur OAI n'est pas sur la page **[incertain]** ; parcourir les numéros
  de manifeste fonctionne.

**Difficultés et biais.** Art britannique (surtout XVIIᵉ–XIXᵉ s.), peintures à l'huile.
**La vue « encadrée » n'est pas une salle de musée** : c'est un studio, avec mire et chevalet.
Ces objets de studio sont eux-mêmes des couches (un segmenteur peut prendre la mire pour une
œuvre). Les cadres sont ceux du YCBA aujourd'hui. Les images pleine taille sont énormes (15 000
px) : toujours demander une taille réduite au service IIIF.

### B. Witt Library (Courtauld) — la reproduction collée sur son carton

**Ce que c'est.** Une photothèque d'histoire de l'art : plus de 2 millions de photographies,
reproductions et coupures (catalogues de vente, livres, journaux), **collées sur des cartons**,
classées par école, artiste et sujet. Numérisation achevée en 2025 par Picturae
([annonce du Courtauld](https://courtauld.ac.uk/news-blogs/2025/the-courtauld-completes-major-project-to-digitise-the-witt-library/) ;
[page du projet](https://photocollections.courtauld.ac.uk/witt-library)). L'enquête de 2013
compte 2 151 862 images dans 102 995 dossiers.

J'ai interrogé le dossier « The Blue Boy » de Gainsborough **[testé]** : 111 résultats (boîte,
dossiers, feuilles). J'ai regardé trois cartons :

- une **coupure de presse** avec légende imprimée (« A copy of the famous Gainsborough… »),
  collée petit au milieu d'un grand carton gris, avec un tampon « WITT LIBRARY » et une note
  dactylographiée ;
- une **reproduction en couleur** avec le titre imprimé, des notes manuscrites (« H.E. Huntington
  Art Gal. San Marino »), un tampon ;
- un **tirage noir et blanc** avec une légende manuscrite (artiste, titre, date, dimensions,
  lieu) et un tampon « Witt Library 1897 » [date lue sur la vignette, **incertain**].

Chaque carton porte en bas à droite une **étiquette moderne avec un code QR** ajoutée à la
numérisation : c'est une couche de plus, toute récente.

**Pourquoi c'est bon.** **Même œuvre, dizaines de reproductions**, chacune avec sa source, sa
taille sur le carton, sa légende. Le carton est photographié **entier**, bords compris. La
page « Digitisation and materiality » du Courtauld le revendique pour la Conway Library
(même programme) : « Never crop to neaten. Always show the edges. » et « Photograph backs
containing information » ([page](https://photocollections.courtauld.ac.uk/sec-menu/digitisation-and-materiality)).
Pour la Witt, je n'ai pas pu vérifier si les dos sont photographiés **[incertain]**.

**Question qu'il tranche.** Quand on isole « l'œuvre », la machine garde-t-elle **la
reproduction seule** (et perd légende, source, date, lieu), **la reproduction et sa légende**,
ou **tout le carton** ? Et ce qui est perdu servait-il à identifier l'œuvre ? (C'est aussi le
terrain de la question proposée par Codex : retrouver l'image *et* garder les indices qui en
font une preuve historique.)

**Accès réel.** **[testé]**

- Recherche et navigation sur le site. Le site s'appuie sur l'API Memorix
  (`webservices.memorix.nl/mediabank/media`), avec une clé publique intégrée à la page ; elle
  répond en JSON (titre, type « Box / Folder / Sheet », taille de l'image, vignettes,
  lien de téléchargement). **Ce n'est pas une API documentée pour le public** : pour un usage
  en série, demander l'accord du Courtauld (contact donné sur la page de l'annonce).
- Vignettes 640 × 480 : **28 à 51 Ko** ; 500 cartons ≈ 20 Mo ≈ 5 min à 64 Ko/s. Les images
  pleine taille (environ 4 300 × 5 700 px, JPEG 2000) sont trop lourdes pour le réseau actuel.
- Licence : **CC BY-NC** quand c'est possible
  ([page droits](https://photocollections.courtauld.ac.uk/copyright)) ; une partie (15–20 %
  selon le Courtauld) reste sous droits et n'est consultable que sur place.

**Difficultés et biais.** Art occidental, beaucoup de noir et blanc ; transcription des légendes
pas encore faite (prévue) : il faudra la faire soi-même pour mesurer « ce qui est perdu ». Le
découpage boîte / dossier / feuille demande un tri. L'étiquette QR est présente partout : un
segmenteur pourrait la garder ou la rejeter de façon systématique.

### C. Met dataset — photos de visiteurs reliées à la photo de studio

**Ce que c'est.** Jeu de données de reconnaissance d'œuvres (Ypsilantis, Garcia, Han,
Ibrahimi, van Noord, Tolias, NeurIPS 2021 Datasets and Benchmarks ;
[page](https://cmp.felk.cvut.cz/met),
[résumé](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/5f93f983524def3dca464469d2cf9f3e-Abstract-round2.html),
[texte](https://arxiv.org/abs/2202.01747)). Entraînement : environ 400 000 photos de studio du
Met (224 000 objets). Test : **plus de 1 100 photos prises au Met par des visiteurs**, chacune
étiquetée avec l'objet montré, plus des photos sans rapport (autres œuvres, non-œuvres).

**Pourquoi c'est bon.** C'est le cas réel, à petite échelle : l'œuvre dans sa salle, avec cadre,
cartel, mur, reflets, visiteurs, angle. Et chaque photo est reliée à **la même œuvre en studio**.
Pour les tableaux plats, l'appariement studio → photo de visiteur donne le bord de l'image
peinte dans la photo, donc une référence.

**Question qu'il tranche.** Dans une photo prise « dans la vraie vie », la machine isole-t-elle
l'image, le tableau encadré, ou une région plus large (cadre + cartel, deux tableaux voisins) ?
Et cela change-t-il avec la taille de l'œuvre dans la photo (lien direct avec la thèse de la
saillance) ?

**Accès réel.** **[testé]** Fichiers sur `ptak.felk.cvut.cz/met/dataset/` : photos de
visiteurs `test_met.tar.gz` **34 Mo** (≈ 9 min à 64 Ko/s), vérité terrain
`ground_truth.tar.gz` 2,9 Mo ; images redimensionnées à 500 px de grand côté. Les photos de
studio correspondantes s'obtiennent une à une par l'API du Met (une photo « web-large »
≈ 380 Ko : compter environ 1 h 45 pour 1 100 photos au débit actuel ; on peut se limiter aux
tableaux). Licences : annotations CC BY 4.0 ; photos de visiteurs venant de Flickr (CC) ou
faites par les auteurs (domaine public), selon l'annexe du texte. Code sous licence MIT
([dépôt](https://github.com/nikosips/met)).

**Difficultés et biais.** Tous types d'objets (sculptures, armures, vases) : il faut filtrer les
tableaux et dessins. Photos choisies par des amateurs de musée sur Flickr, souvent bien
cadrées sur l'œuvre (donc l'œuvre est déjà saillante). Un seul musée.

---

## 4. Les autres corpus

### D. Le Rhinocéros de Dürer — même bois, éditions différentes

**Ce que c'est.** Le bois de 1515 a été tiré pendant un siècle. Le British Museum compte sept
éditions, la dernière avec une planche de ton par Willem Janssen après 1620 ; la Royal
Collection et la Library of Congress en comptent huit, la LoC attribuant à Hendrick Hondius
une édition vers 1620 (texte néerlandais, date corrigée, bois fendu). Les sources ne
s'accordent pas **[incertain]** ; voir la
[page de la LoC](https://loc.gov/preservation/conservators/durer/index.html) (lue) — les pages
du British Museum et de la Royal Collection ont refusé mon accès (403).

Sur Wikimedia Commons, la catégorie
[« Dürer's Rhinoceros »](https://commons.wikimedia.org/wiki/Category:D%C3%BCrer%27s_Rhinoceros)
contient **41 fichiers** **[testé]**, dont quatre éditions de la BnF (« 1ère édition »,
« 3e édition (édition allemande) », « 6e édition », « 7e édition, 1620 », identifiants Gallica
`btv1b532153250`, `btv1b53215324j`, `btv1b532163188`, `btv1b53215326f`), l'épreuve en
camaïeu de Janssen (British Museum), et des épreuves de la NGA, du Met, du Rijksmuseum, du SMK,
de Cleveland, de la LoC.

**Pourquoi c'est bon.** Même image, mais **le texte typographié au-dessus**, les marges, le
rognage (l'épreuve de la LoC a perdu son texte du bas) et la planche de ton changent. Le texte
fait partie de la feuille éditée, pas de l'image gravée : **c'est le cas d'école du « que
perd-on ? »**. Petit, déjà en partie connu du projet (6 images dans le corpus réel E6).

**Question qu'il tranche.** Le segmenteur garde-t-il le texte avec la bête ? Si on coupe le
texte, la machine peut-elle encore distinguer les éditions (et donc dater la feuille) ?

**Accès.** Commons (API, avec pauses : j'ai été limité après une série de requêtes trop
rapprochées). Gallica en direct a refusé mes requêtes de recherche le 13/10 (403) **[testé]** :
passer par les copies Commons ou par l'API IIIF de la BnF (voir la note
`bnf-openapi-iiif` hors dépôt).

### E. Wikimedia Commons — tableaux photographiés encadrés

**Ce que c'est.** La catégorie
[« Framed paintings »](https://commons.wikimedia.org/wiki/Category:Framed_paintings) compte
**3 503 fichiers** et 16 sous-catégories **[testé]**. La sous-catégorie « par musée » en a 28 ;
les plus grosses : Met 268, Boijmans 230, Alte Pinakothek 228, Neue Pinakothek 226,
Nasjonalmuseet 198, Valenciennes 179, Tate Britain 131, Gemäldegalerie 103, Rijksmuseum 87,
National Gallery 77, Louvre 55. Il existe aussi « Original painting frames », « Empty picture
frames » (23 fichiers, dont des cadres vides du Met et de Paul Petit) et
« Passepartouts » (31 fichiers).

**Pourquoi c'est bon.** Associé à Wikidata (image « propre » de l'œuvre) ou à l'open access des
musées (Met, Rijksmuseum, NGA), on a **la même œuvre avec et sans cadre**, en photo de visiteur.
Les cadres vides sont utiles comme témoins (« un cadre sans œuvre » : que segmente la machine ?).

**Question qu'il tranche.** Comme C, sur plusieurs musées et plusieurs styles de cadres.

**Difficultés.** Classement fait par des bénévoles, photos de qualité variable, angles, reflets.
Limite de débit stricte de Commons (déjà vue en E6 ; j'ai reçu un refus « too many requests »
pendant cette vérification) : prévoir des pauses de plusieurs secondes.

### F. Cadres du Met (collection Robert Lehman) — l'ouverture mesurée

**Ce que c'est.** Près de 400 cadres (surtout italiens et français, XIVᵉ–XVIIIᵉ s.) légués par
Robert Lehman, catalogués par Timothy Newbery (2007,
[publication du Met](https://www.metmuseum.org/en/met-publications/the-robert-lehman-collection-vol-13-frames) ;
chiffre et auteur lus dans l'extrait du moteur de recherche, la page m'a répondu « 429 »
**[incertain]**).
Chaque fiche de l'API donne **trois dimensions : hors tout, « Rabbet » (feuillure) et
« Sight » (ce que le cadre laisse voir)** **[testé]**. Exemple : *Ogee frame*, France vers 1700,
hors tout 131 × 97 cm, feuillure 107,5 × 73,5 cm, vue 103,7 × 70 cm
([fiche](https://www.metmuseum.org/art/collection/search/460358)). La photo montre le cadre vide
sur fond blanc, domaine public.

**Pourquoi c'est bon.** C'est une **mesure du bord intérieur**, faite par le musée. On peut
insérer des contenus dans ces cadres (comme le pilote « cadre social ») en sachant exactement
où passe l'ouverture, puis voir si la machine s'arrête à la vue, à la feuillure ou au bord
extérieur.

**Accès.** API du Met **[testé]**. Attention : l'ancienne recherche `/v1/search` a été retirée
le 1/10/2026 ; il faut utiliser `/public/collection/v1.1/search` (paginée) ou le fichier CSV
open access. Photos « web-large » ≈ 80–400 Ko.

### G. Rijksmuseum — les cadres et leur ancien tableau

**Ce que c'est.** Les cadres ont leurs propres fiches (numéros RP-L). La fiche
[RP-L-406](https://www.rijksmuseum.nl/en/collection/RP-L-406) (cadre doré style Louis XV, vers
1880–1909) indique qu'il est **l'ancien cadre** d'un tableau de Jacob Maris, avec un ancien
numéro et une plaque « J. MARIS » sur la face ; pas d'image numérique pour cette fiche
**[testé]**. Données ouvertes du musée : [data.rijksmuseum.nl](https://data.rijksmuseum.nl)
(≈ 800 000 objets, ≈ 600 000 avec photo ; les anciennes API sont dépréciées).

Un cas célèbre est documenté : C. J. de Bruyn Kops, « De inlijsting van Rembrandts Nachtwacht
in het verleden en de nieuwe lijst », *Bulletin van het Rijksmuseum* 24 (1976), p. 99–119
([notice](https://bulletin.rijksmuseum.nl/article/view/20959),
[doi:10.52476/trb.20959](https://doi.org/10.52476/trb.20959)) — **[contenu non lu]** (PDF de
plus de 10 Mo).

**Intérêt.** « Même œuvre, cadres successifs » pourrait se reconstruire ici, mais il faudrait
des photos de l'œuvre dans chacun des cadres : je n'en ai pas trouvé en série.

### H. National Gallery (Londres) — avant / après un changement de cadre

**Ce que c'est.** Les comptes rendus de Peter Schade, chef de l'encadrement à la National
Gallery, republiés par *The Frame Blog* ([partie 1](https://theframeblog.com/2022/04/23/reframing-at-the-national-gallery-london-part-1/),
série d'au moins cinq parties). Chaque notice montre **le tableau dans son ancien cadre puis dans
le nouveau** (ex. : Rembrandt, *Autoportrait à 63 ans*, NG 221 ; Botticelli, *Portrait d'un
jeune homme*, NG 626 ; Alvise Vivarini, NG 2672).

**Intérêt.** La variable la plus pure : **même œuvre, deux cadres, presque même photo**.
**Limite** : quelques dizaines de cas, images non libres (droits de la National Gallery) ;
utilisable pour regarder, pas pour un corpus publié.

### I. Frick Photoarchive (New York)

Plus d'un million de reproductions photographiques, montées sur cartons gris de 9 × 12 pouces
avec l'historique d'attribution et de provenance
([page](https://www.frick.org/library/photoarchive) ;
[annonce de 2021](https://frick.org/blogs/photoarchive/175000_new_photoarchive_records) : plus
de 175 000 œuvres ajoutées, documentation numérisée). Consultation et téléchargement de JPEG sur
[digitalcollections.frick.org](https://digitalcollections.frick.org/). **Je n'ai pas pu vérifier
si les images montrent le carton entier ou seulement la photo** (site en JavaScript)
**[incertain]**. Conditions de réutilisation non lues. Intérêt potentiellement égal à la Witt ;
à vérifier dans un navigateur avant de compter dessus.

### J. Autres photothèques : Zeri, KHI Florence, PHAROS

- **Fototeca Zeri (Bologne)** : 290 000 photographies ; jeu de données ouvert
  ([data.fondazionezeri.unibo.it](https://data.fondazionezeri.unibo.it/)) d'environ 19 000
  œuvres et 30 000 photos, **métadonnées seulement** (CC BY 4.0), images sous CC BY-NC-ND 4.0
  et non incluses. Les dos des photos ne seraient visibles que sur place **[incertain]**.
- **Kunsthistorisches Institut in Florenz, Photothek** : environ 550 000 photos d'art italien ;
  la photothèque numérique ([photothek.khi.fi.it](https://photothek.khi.fi.it/)) est protégée
  par une page anti-robots **[testé]**. Une notice reprise par la Deutsche Digitale Bibliothek
  montre une reproduction d'avant 1894 sur un **carton porteur historique**, avec le statut
  « accès libre, pas de réutilisation »
  ([notice](https://www.deutsche-digitale-bibliothek.de/item/2YU7BGYECSVV6CIVU3UYJPQZFT5D6U6C?lang=en)).
- **PHAROS** (consortium de 14 photothèques fondé en 2017) : le site redirige vers
  [artresearch.net](https://artresearch.net/), application en JavaScript que je n'ai pas pu lire
  **[incertain]** sur ce qui est en ligne aujourd'hui.

Intérêt réel, mais accès trop difficile pour commencer.

### K. Photos de salles et d'accrochage datées

- **La Joconde au Louvre**, Commons : catégorie [« Mona Lisa in the Louvre »](https://commons.wikimedia.org/wiki/Category:Mona_Lisa_in_the_Louvre)
  (75 fichiers) et « Visitors of Louvre (Mona Lisa) » (au moins 80) **[testé]**. Surtout 2005–2025
  (vitrine, foule, téléphones), plus une photo de presse de **1929** (« entre deux Raphaël »,
  domaine public) et le mur vide de 1911. Attention : les fichiers nommés « (1861) » et
  « (1862) » sont des photos de 2016, pas des photos anciennes **[testé]**. Bon pour la
  saillance (même œuvre, de plus en plus petite dans l'image), peu pour le cadre.
- **Salon carré**, Commons : quelques images anciennes seulement, dont la mise en place des
  *Noces de Cana* en 1918 (Médiathèque du patrimoine, CC BY-SA 4.0). La base POP a une vue
  « Salon Carré, ensemble » des Archives photographiques d'art et d'histoire (1921–1941), non
  datée, sous © Ministère de la Culture / GrandPalaisRmn
  ([notice](https://pop.culture.gouv.fr/notice/memoire/APMH0099770)). Le Louvre conserve des
  photographies du Service de l'histoire du Louvre (ex. plafond par Lampué, avant 1890,
  [fiche](https://collections.louvre.fr/en/ark:/53355/cl010528255)) ; je n'ai pas trouvé de série
  de vues d'accrochage.
- **MoMA** : l'historique en ligne des expositions (depuis 1929, photographies d'installation)
  existe mais le site m'a refusé l'accès (403, protection anti-robots) **[testé]** ; les données
  ouvertes ([dépôt GitHub, CC0](https://github.com/MuseumofModernArt/exhibitions)) ne
  contiennent que des listes (1 788 expositions 1929–1989), **pas d'images**. Les photos
  d'installation ne sont pas sous licence libre **[incertain]**.

### L. Cadre et valeur — catalogues de vente et prix

- **German Sales 1901–1945** : environ 9 000 catalogues (650 000 pages, plus de 390 maisons de
  vente d'Allemagne, d'Autriche, de Suisse), numérisés par la Kunstbibliothek de Berlin,
  l'université de Heidelberg et le Getty
  ([page des musées de Berlin](https://www.smb.museum/en/museums-institutions/kunstbibliothek/collection-research/research/german-sales-1901-1945/)) ;
  Heidelberg annonce aujourd'hui environ 14 200 catalogues
  ([recherche](https://digi.ub.uni-heidelberg.de/en/germansales/recherche/volltext.html)). Les
  pages de catalogue annoncent des manifestes IIIF, mais **le site est désormais derrière une
  page anti-robots** (Anubis) **[testé]**.
- **Getty Provenance Index, ventes** : données en **CC0** sur
  [GitHub](https://github.com/thegetty/provenance-index-csv) **[testé]**, avec le champ
  `price_amount_1` (« prix d'adjudication ou plus haute enchère ») et le statut du lot (vendu,
  retiré…). Les fiches renvoient aux PDF de Heidelberg pour German Sales.
- **Drouot 1939–1945** : le projet [AUCASE](https://aucase.inha.fr/) de l'INHA exploite les
  catalogues Drouot de cette période de la bibliothèque numérique de l'INHA ; nombre et licence
  non indiqués sur la page **[incertain]**.
- **Christie's** : l'accès extérieur aux archives (catalogues depuis 1766) a été suspendu en 2021
  ([The Art Newspaper](https://www.theartnewspaper.com/news/dealers-and-academics-mourn-suspension-of-access-to-christie-s-huge-archive)) ;
  je n'ai pas trouvé de réouverture.

**Pourquoi c'est bon pour cadre et valeur.** C'est le seul endroit où **la présentation (la
planche, la notice) et le prix réel coexistent**. Question : un modèle à qui on montre la planche
estime-t-il un prix proche de l'adjudication, et cela change-t-il si l'on retire ou ajoute un
cadre ? **Non vérifié** : la part des planches qui montrent les tableaux encadrés.

### M. Livres d'art anciens numérisés

- **Internet Archive** **[testé]** : la recherche avancée répond (≈ 6 200 livres 1880–1925 sur
  la peinture ou le Louvre, sans restriction d'accès, selon ma requête) ; manifestes IIIF
  disponibles (`iiif.archive.org/iiif/3/<identifiant>/manifest.json`). Exemple : la série
  *Masterpieces in colour* (vers 1907–1910 ; Gainsborough, Hals, Leighton, Watts…), où chaque
  planche en couleur est collée sur une page avec légende. Bon pour « œuvre connue dans un livre
  photographié à plat » (déjà étudié en synthèse dans le projet).
- **Gallica** : recherche automatique refusée le 13/10 (403) **[testé]** ; l'IIIF reste
  utilisable selon les essais précédents (hors dépôt), avec ≥ 10 s entre deux requêtes.

### N. Jeux de données de vision existants

| jeu | ce que c'est | utilité ici |
|---|---|---|
| [SynGallery](https://arxiv.org/abs/2607.18907) (Bartkowiak et al., 2026) | 24 490 rendus 3D de 4 898 tableaux du Met dans des galeries générées : pose, mur, cadre, lumière, verre varient, l'œuvre reste fixe | **exactement la variable « cadre »**, mais en synthèse ; publication des données et licence non trouvées **[incertain]** |
| [Virtual Gallery](https://europe.naverlabs.com/research/3d-vision/virtual-gallery-dataset/) (NAVER LABS, 2019) | galerie Unity, 42 tableaux de la NGA, masques d'instance « painting » | les masques disent déjà où finit « le tableau » ; **inclut-il le cadre ?** non dit ; CC BY-NC-ND |
| [Met dataset](https://cmp.felk.cvut.cz/met) | voir C | voir C |
| [iMet 2019](https://arxiv.org/abs/1906.00901) | photos professionnelles du Met, attributs | photos de studio : peu utiles pour le bord |
| WikiArt ([ArtGAN](https://github.com/cs-chan/ArtGAN)) | ~80 000 images recadrées sur l'œuvre | témoin « œuvre sans bord » ; licence des images non claire |
| [Human-Art](https://arxiv.org/abs/2303.02760v1) (CVPR 2023) | 50 000 images, personnes dans des œuvres | hors sujet pour le bord ; utile si l'on étudie les personnes |
| Redies & Groß 2013 ([article](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00831/full)) | 280 photos de tableaux **avec cadre**, la même **sans cadre**, avec le mur, et des salles entières (trois musées allemands) | le bon protocole, déjà cité dans l'article ; **pas de publication des images** trouvée |

### O. À déconseiller pour l'instant

- **Google Arts & Culture** (gigapixels, visites de salles) : les droits restent aux musées
  partenaires ([FAQ partenaires](https://support.google.com/culturalinstitute/partners/answer/6002688?hl=en)),
  pas d'API ni de téléchargement prévu pour les utilisateurs **[incertain]** pour la visite
  virtuelle.
- **Posters et cartes postales** : la catégorie Commons « Postcards of paintings » n'a que 81
  fichiers **[testé]**. Trop peu pour une série ; à garder pour des exemples.

---

## 5. Côté outils (pour mémoire)

- **Déjà sur le Mac** **[testé]** (cache Hugging Face) : `IDEA-Research/grounding-dino-base`,
  `facebook/sam2.1-hiera-base-plus`, `Zigeng/SlimSAM-uniform-77`, plus CLIP, SigLIP, DINOv2.
  La chaîne Grounding DINO + SAM 2 ([Grounded-SAM-2](https://github.com/IDEA-Research/Grounded-SAM-2),
  Apache-2.0) peut donc tourner sans téléchargement.
- **SAM 3** ([dépôt](https://github.com/facebookresearch/sam3) ;
  [Carion et al., arXiv 2511.16719](https://arxiv.org/abs/2511.16719v1), 2025) : 848 M paramètres, consignes
  par groupe nominal (« painting », « frame »), licence propre (« SAM License »), poids sur
  Hugging Face **après demande d'accès**, dépôt prévu pour GPU CUDA. Transformers propose
  `Sam3Model` ([documentation](https://huggingface.co/docs/transformers/model_doc/sam3)) ;
  le fonctionnement sur Mac (CPU / MPS) n'est pas vérifié **[incertain]**. À 64 Ko/s, des poids
  de plusieurs gigaoctets demanderaient des heures (taille exacte du fichier non vérifiée).

---

## 6. Proposition de départ

1. **YCBA, 100 à 300 peintures ayant les quatre vues, plus 100 estampes** (environ 10 Mo à
   télécharger). Consignes : « painting », « artwork », « picture », « frame ». Mesures :
   recouvrement avec le recadrage du musée, écart du bord, part du cadre gardée, objets de
   studio pris pour l'œuvre. Pour les estampes : légende gardée ou non. Regarder les masques
   sur planche **avant** toute mesure.
2. **Witt, 10 œuvres connues × 10 cartons** (vignettes, ≈ 4 Mo), après accord du Courtauld
   pour un usage en série. Annoter à la main ce qui est hors de la reproduction (légende,
   tampon, note, QR). Mesure : ce que le masque laisse dehors, et si la machine identifie
   encore la source et l'œuvre sans ces éléments.
3. **Met, photos de visiteurs des tableaux** (34 Mo + photos de studio des seuls tableaux).
   Mesure : bord trouvé contre bord apparié, en fonction de la surface de l'œuvre dans l'image.

Le Rhinocéros (D) sert de test de mise au point, en une heure.
