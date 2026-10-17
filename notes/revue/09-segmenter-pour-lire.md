# Volet 09 — Segmenter pour lire : l'OCR avec et sans cadre

*17/10/2026. Volet de la revue de littérature de « punctured sky ». Il répond à une phrase de
Marcel du même jour :*

> « Je pense que le cadre est le truc fondamental qui fait de nous des êtres intelligents [...]
> Le fait d'avoir conscience de soi implique de se sortir du monde et le cadre formalise ce
> mouvement. C'est pour ça qu'un modèle a besoin de segmenter pour ocriser correctement. »

*Question du volet : la lecture automatique a-t-elle besoin d'un « cadre » donné d'avance
(page découpée en zones, lignes, mots, avec un ordre de lecture) ? Ou bien les modèles « de
bout en bout » s'en passent-ils ? Et dans ce cas, segmentent-ils quand même, en silence, dans
leur attention ?*

*Méthode et limites. Chaque référence a été contrôlée sur sa notice : page arXiv (titre,
auteurs, date, commentaire de l'auteur sur le lieu de publication), notice Crossref pour les
DOI, liste officielle des actes (NeurIPS 2016), ou page de l'éditeur. Les chiffres cités ont
été relus dans le texte intégral des articles (PDF arXiv converti en texte), pas dans des
résumés de seconde main. Le quota de recherche web de la session était épuisé au début de ce
volet : je n'ai donc pas pu *chercher* de nouvelles références, seulement vérifier celles dont
je connaissais l'identifiant. Conséquence : certains manques signalés plus bas (« je n'ai pas
trouvé d'étude qui… ») veulent dire « je n'en connais pas et je n'ai pas pu chercher », pas
« il n'en existe pas ». Les références non vérifiées portent la mention [non vérifié].*

---

## 0. En bref

1. **La chaîne classique découpe d'abord, lit ensuite.** Tesseract, kraken/eScriptorium,
   Transkribus, OCR-D et Pero-OCR détectent des zones et des lignes, les rangent dans un ordre
   de lecture, puis reconnaissent chaque ligne. Le résultat est écrit en ALTO ou en PAGE, deux
   formats XML qui *sont* ce cadre : des boîtes, des lignes, un ordre.
2. **Les erreurs de découpe pèsent lourd.** Une seule fusion de deux lignes peut faire passer le
   taux d'erreur par caractère d'une page de 7,3 % à 20,4 %, alors que la mesure de
   segmentation ne baisse que de 15 % (Boillet, Kermorvant et Paquet 2022).
3. **On sait lire un paragraphe sans le découper.** Depuis Bluche (2016), des modèles lisent
   des paragraphes entiers, puis des pages entières (DAN, 2023), sans aucune annotation de
   ligne. Sur paragraphe, ils font mieux que la chaîne classique avec une segmentation
   automatique, et parfois mieux qu'avec la segmentation parfaite.
4. **Mais ils segmentent quand même.** Tous ces articles montrent, dans les poids d'attention
   ou les cartes d'attribution, une segmentation *implicite* en lignes. Les auteurs l'écrivent
   eux-mêmes : « une sorte de segmentation implicite des lignes ». Le cadre n'a pas disparu :
   il est passé de l'entrée (donné d'avance) à l'intérieur du modèle (appris).
5. **Et l'ordre de lecture ne vient pas de rien.** Il est imposé par la forme de la sortie :
   une suite linéaire de caractères. Le modèle apprend la segmentation *parce qu'il doit
   produire une suite ordonnée*. C'est la lecture qui produit le découpage, plus que l'inverse.
6. **Le cadre explicite revient pour les pages difficiles.** Les meilleurs systèmes de 2025
   (MinerU2.5, PaddleOCR-VL, MonkeyOCR) détectent d'abord la mise en page, puis lisent les
   morceaux. dots.ocr fait tout en un seul modèle, mais en *produisant* les boîtes et l'ordre :
   le retirer de l'apprentissage dégrade l'ordre de lecture. Sur les grandes pages de journaux,
   la chaîne segmentée reste la norme (American Stories, 2023).
7. **Les grands modèles généralistes (VLM) lisent bien les documents historiques, mais
   omettent.** Ils sautent des lignes, réécrivent, complètent, bouclent. Les études de
   2024-2025 mesurent surtout le taux d'erreur global, rarement l'ordre ou les omissions.
8. **La preuve d'une segmentation implicite reste surtout visuelle.** On montre de belles cartes
   d'attention. Presque personne ne *mesure* si l'attention suit les lignes, ni ne *perturbe*
   le modèle pour vérifier qu'il s'en sert. C'est là qu'une expérience sur les machines de
   Marcel peut apporter quelque chose (§9 c).

---

## 1. Les notions utiles, en une phrase chacune

- **OCR** (reconnaissance optique de caractères) : transformer l'image d'un texte imprimé en
  texte. **HTR** : la même chose pour l'écriture manuscrite.
- **Segmentation** : découper l'image en morceaux à traiter. En OCR, il y a plusieurs niveaux :
  la page, les **zones** (colonnes, titres, notes de marge, illustrations), les **lignes**, les
  mots, les caractères.
- **Analyse de mise en page** (*layout analysis*) : trouver et nommer les zones.
- **Ligne de base** (*baseline*) : la ligne sur laquelle « posent » les lettres. Les outils
  récents (kraken, Transkribus, Pero) détectent d'abord ces lignes de base, puis un polygone
  autour de chaque ligne.
- **Ordre de lecture** : l'ordre dans lequel il faut enchaîner les zones et les lignes (colonne
  de gauche avant colonne de droite, note de marge après ou avant le paragraphe, etc.).
- **ALTO** et **PAGE** : deux formats XML de bibliothèque qui décrivent une page comme une
  arborescence de zones, de lignes et de mots, avec leurs coordonnées et un ordre.
- **CTC** (*Connectionist Temporal Classification*) : une façon d'apprendre à lire une ligne
  sans savoir où est chaque lettre. Le modèle lit la ligne de gauche à droite, tranche par
  tranche, et la perte CTC aligne tout seul les tranches et les lettres.
- **Attention** : un mécanisme par lequel un réseau, à chaque pas, donne un poids à chaque
  position de l'image. Une **carte d'attention** montre ces poids sur l'image.
- **Bout en bout** (*end-to-end*) : un seul modèle va de l'image au texte.
- **Sans segmentation** (*segmentation-free*) : le modèle reçoit un paragraphe ou une page
  entière, et on ne lui donne jamais les positions des lignes, ni à l'entraînement ni à l'usage.
- **CER** (*character error rate*) : le nombre de caractères à corriger (ajouter, retirer,
  remplacer) pour passer de la sortie au texte juste, divisé par la longueur du texte juste.
  Il peut dépasser 100 % si le modèle invente beaucoup.
- **VLM** (*vision-language model*) : un grand modèle de langue à qui l'on a greffé un encodeur
  d'images (GPT-4o, Gemini, Claude, Qwen2.5-VL). On lui donne une image et une consigne
  (« transcris ce document »).
- **Segmentation implicite** : le modèle n'a pas de sortie « lignes », mais son calcul interne
  isole les lignes l'une après l'autre. On la cherche dans les cartes d'attention ou par
  **sondage** (un petit classifieur qui lit les états internes du modèle) ou par
  **perturbation** (on modifie l'image et on regarde ce qui change).

Dans la grille du projet (synthèse, §4.1), la segmentation d'OCR est un **cadre du fichier**
(niveau 3) : une découpe opératoire de l'image. Ce n'est ni le cadre matériel (moulure, marge)
ni le cadre discursif. Mais en OCR, ce cadre opératoire *s'appuie* sur des cadres matériels :
la marge blanche, le filet entre deux colonnes, l'interligne. Ce point compte pour la fin.

---

## 2. La chaîne classique : le cadre donné d'avance

### 2.1 Les étapes

Une chaîne d'OCR patrimoniale typique fait, dans l'ordre :
1. prétraitement (redressement, binarisation, recadrage de la page) ;
2. analyse de mise en page (zones et types de zones) ;
3. détection des lignes (lignes de base et polygones) ;
4. ordre de lecture (des zones, puis des lignes dans chaque zone) ;
5. reconnaissance de chaque ligne isolée (CTC le plus souvent) ;
6. écriture en ALTO ou PAGE, parfois post-correction.

Le cadre est donc **donné d'avance au lecteur** : le modèle de reconnaissance ne voit qu'une
bande d'image d'une ligne. Il ne sait rien de la page.

### 2.2 Les outils

- **Tesseract.** Smith (2007) décrit le moteur. Smith (2009) ajoute une analyse de mise en page
  « hybride » fondée sur la détection des **taquets de tabulation** (*tab-stops*) : les bords
  alignés des colonnes. Autrement dit, Tesseract trouve les colonnes en cherchant les bords
  verticaux du texte, c'est-à-dire ses cadres internes.
- **Le format PAGE.** Pletschacher et Antonacopoulos (2010) le définissent pour la vérité
  terrain et les résultats d'analyse de page. **ALTO** est la norme de la Bibliothèque du
  Congrès, utilisée par Gallica et la plupart des bibliothèques [notice de la norme non
  vérifiée ici].
- **Transkribus.** Kahle et al. (2017) présentent la plateforme ; Muehlberger et al. (2019)
  racontent son usage dans les archives. Sa détection de lignes descend de la méthode d'ARU-Net.
- **ARU-Net.** Grüning et al. (2019) détectent les lignes de base en deux temps : un réseau
  classe les pixels (ligne de base, séparateur, autre), puis un regroupement construit les
  lignes. Sur la piste « complexe » de la compétition cBAD 2017, ils portent la mesure F de
  0,859 à 0,922. La compétition cBAD elle-même est décrite par Diem et al. (2017).
- **dhSegment.** Ares Oliveira, Seguin et Kaplan (2018) proposent un seul réseau qui classe les
  pixels, suivi de petits post-traitements, pour plusieurs tâches : extraire la page, les
  lignes de base, les zones, les illustrations.
- **Doc-UFCN.** Boillet, Kermorvant et Paquet (2020) : un réseau en U entraîné de zéro sur des
  documents, et l'idée qu'un préentraînement sur plusieurs jeux de documents aide.
- **Pero-OCR.** Kodym et Hradiš (2021) étendent un détecteur de lignes de base en lui faisant
  prédire aussi la hauteur des lignes et les bords des blocs de texte, et l'orientation du texte
  pixel par pixel.
- **kraken et eScriptorium.** kraken (Kiessling) est le moteur libre derrière eScriptorium. Il
  segmente par lignes de base et polygones, puis lit chaque ligne en CTC. La version installée
  chez Marcel (7.1.1, dans `~/outils-seg/kraken-env`) contient deux ordres de lecture : une
  fonction heuristique (`polygonal_reading_order`, qui range les lignes selon les régions et la
  direction du texte) et un modèle neuronal d'ordre de lecture optionnel (`ro_model`, script
  `add_neural_ro.py`). Vérifié dans le code local, pas dans une publication. L'article de
  présentation d'eScriptorium (Kiessling et al. 2019) n'a pas pu être vérifié [non vérifié].
- **YOLO pour la mise en page.** Clérice (2023, *JDMDH*) remplace la segmentation de zones de
  kraken par un détecteur d'objets en rectangles (YOLOv5). Il montre qu'avec peu d'exemples
  (1 110 échantillons et moins), YOLO « surpasse nettement » kraken pour les zones. Il insiste
  sur un point qui compte pour nous : distinguer le corps du texte des notes de marge et des
  titres courants « fait la différence » entre un texte intégral et une sortie bruitée.
- **OCR-D.** Neudecker et al. (2019) décrivent le cadre logiciel allemand qui enchaîne des
  « processeurs » (binarisation, segmentation, reconnaissance) sur des imprimés anciens. Il est
  installé chez Marcel (`~/outils-seg/ocrd-env`).

### 2.3 L'ordre de lecture

L'ordre de lecture est un cadre à part entière : il dit dans quel sens on traverse la page.
- Les chaînes classiques le calculent par règles (haut-bas, gauche-droite, colonne par colonne)
  ou par un petit modèle à part (kraken, ci-dessus).
- LayoutReader (Wang et al. 2021, EMNLP) apprend l'ordre de lecture à partir des boîtes de mots
  et de leur texte, sur 500 000 pages tirées de fichiers Word où l'ordre est connu.
- **Mesurer l'ordre.** Le CER classique compare deux suites. Si les colonnes sont lues dans le
  mauvais ordre, le CER explose alors que chaque ligne est juste. Clausner, Pletschacher et
  Antonacopoulos (2020) ont donc proposé une mesure de précision des caractères qui ne dépend pas
  de l'ordre (*flexible character accuracy*). Neudecker et al. (2021) passent en revue les
  outils et mesures d'évaluation de l'OCR. Conséquence pratique : **un même résultat peut
  sembler bon ou mauvais selon que la mesure punit l'ordre ou non.** Il faut toujours dire
  laquelle on utilise.

### 2.4 Ce que coûte une erreur de segmentation

C'est la question centrale pour la phrase de Marcel : si le cadre est mal posé, la lecture
échoue-t-elle ? Trois sources donnent des chiffres.

**(1) Bluche (2016), tableau 2.** Le même lecteur de lignes (un réseau MDLSTM entraîné en CTC)
est appliqué soit aux lignes de la vérité terrain, soit aux lignes trouvées par trois
algorithmes automatiques (projection, *shredding*, énergie). CER sur les jeux de validation :

| base, résolution | lignes vraies | projection | shredding | énergie | modèle sans segmentation (Bluche) |
|---|---|---|---|---|---|
| IAM, 150 dpi | 8,4 | 15,5 | 9,3 | 10,2 | 6,8 |
| IAM, 300 dpi | 6,6 | 13,8 | 7,5 | 7,9 | 4,9 |
| Rimes, 150 dpi | 4,8 | 6,3 | 5,9 | 8,2 | 2,8 |
| Rimes, 300 dpi | 3,6 | 5,0 | 4,5 | 6,6 | 2,5 |

Lecture : avec une segmentation automatique, l'erreur augmente « d'au moins 1 point absolu »
(l'auteur), et elle peut presque doubler (projection sur IAM). Mais le modèle *sans*
segmentation fait mieux que tous, y compris les lignes parfaites. Deux réserves : IAM et Rimes
sont des paragraphes simples, sur une colonne, aux lignes bien séparées (les auteurs le disent
pour IAM) ; et le lecteur de lignes de référence n'est pas le meilleur de l'époque.

**(2) Boillet, Kermorvant et Paquet (2022), *IJDAR*.** Ils comparent trois détecteurs de lignes
(Doc-UFCN, dhSegment, ARU-Net) sur dix jeux historiques, et jugent la détection *par le CER
final*, après reconnaissance. Leurs constats :
- Les mesures de pixels habituelles (intersection sur union) ne voient pas les **fusions** de
  lignes, qui sont pourtant fatales pour le lecteur : une ligne fusionnée « ne sera pas
  reconnue ».
- Un exemple chiffré : une seule fusion de deux lignes fait baisser la mesure de détection
  (mAP) de 15 % (de 60 % à 51,3 %), mais fait **monter le CER de la page de 179 % (de 7,3 à
  20,4)**.
- Sur le jeu HOME (écriture serrée, longues lignes), Doc-UFCN segmente parfaitement environ la
  moitié des pages, mais fusionne deux, trois lignes, voire des paragraphes entiers sur
  d'autres : son CER est alors bien pire que celui de dhSegment, qui localise moins bien mais
  fusionne peu.
- Les conventions d'annotation diffèrent d'un jeu à l'autre (par exemple : la lettrine fait-elle
  partie de la ligne ?) et cela change le résultat final de lecture.

**(3) Le banc local de Marcel (14/09/2026).** Mémoire `outils-segmentation-locaux` : sur 37
pages de la BnL, kraken échoue sur 18 (régions de taille nulle sur les bandeaux étroits),
eynollah sur 22 (bogue au redressement). Sur les agrégats bruts, kraken semblait 3e (CER
0,128) ; sur les 12 pages réussies par les cinq chaînes, il était dernier (0,253). Deux leçons
de méthode, déjà notées par Marcel : le CER de ce banc mesure *segmenteur + Tesseract + ordre*,
pas la segmentation seule ; et il faut comparer sur l'intersection des pages réussies, sinon on
note les moteurs fragiles sur les pages faciles (biais de survie).

**Ce qui manque.** Je ne connais pas d'étude publiée qui décompose l'erreur finale d'un fonds de
presse ancienne (Gallica, NewsEye, Europeana) en part due à la mise en page, part due aux
lignes et part due à la reconnaissance. Les compétitions de mise en page du PRImA mesurent la
mise en page à part. Le chiffre de Boillet est le plus parlant, mais il porte sur des
manuscrits.

**Conclusion partielle.** Dans une chaîne classique, le cadre est un **point de passage obligé
et fragile** : une erreur de découpe ne se rattrape pas en aval. Le lecteur de lignes ne peut
pas dire « cette ligne est en fait deux lignes ». C'est l'argument de départ de toute la lignée
« sans segmentation » : *la segmentation automatique est sujette aux erreurs, qui compromettent
la reconnaissance* (Bluche 2016, résumé).

---

## 3. Lire sans découper : la lignée « sans segmentation »

### 3.1 Les débuts : Bluche (2016) et Bluche, Louradour et Messina (2017)

**Scan, Attend and Read** (Bluche, Louradour et Messina, arXiv 2016, ICDAR 2017). Un réseau
MDLSTM (un réseau récurrent qui parcourt l'image dans quatre directions) encode l'image. Puis,
à chaque caractère, un module d'attention choisit où regarder. Les auteurs montrent :
- que « l'attention passe d'un caractère au suivant, dans le bon ordre de lecture » (fig. 3) ;
- que sur deux lignes empilées, le modèle « a appris à chercher la deuxième ligne quand la
  première est lue », avec une attention partagée entre la fin de la première ligne et le début
  de la seconde (fig. 4) ;
- sur des paragraphes IAM complets à 150 dpi, après douze époques, un CER de 16,2 %, contre
  10,3 % pour un lecteur de lignes sur les lignes vraies et 11,1 % à 17,2 % sur des lignes
  automatiques (ma lecture de leur tableau 3, mal extrait du PDF) : prometteur, pas encore
  meilleur ;
- un mode d'échec très parlant : pour quelques exemples, « l'attention a sauté en arrière vers
  une ligne précédente », et le système a retranscrit tout un passage. Le CER dépasse alors
  100 %. **Sans cadre, le lecteur peut perdre sa place.**

Ils ajoutent une phrase programmatique : le mécanisme d'attention serait « une façon de faire
l'analyse de mise en page et la reconnaissance dans un seul système ».

**Joint Line Segmentation and Transcription** (Bluche, NIPS 2016). Version plus rapide : au
lieu de suivre caractère par caractère, le modèle remplace la couche qui « écrase » l'image 2D
en une suite 1D par une version récurrente qui reconnaît **une ligne à la fois**. Les poids
d'attention définissent, à chaque pas, une ligne. L'auteur l'écrit : le réseau « effectue une
sorte de segmentation implicite des lignes », et on peut voir ce module « comme un réseau de
segmentation de lignes doux ». C'est le tableau du §2.4 : ce modèle bat la chaîne segmentée.
Deux détails comptent pour nous :
- le modèle « ne peut pas traiter des ordres de lecture arbitraires » : il ne sait faire que des
  lignes de haut en bas ;
- il tourne un nombre fixe de pas ; les pas en trop, il les passe **dans les interlignes**,
  « où le décodeur peut facilement ne prédire aucun caractère ». Le blanc entre les lignes sert
  de lieu de repos. Retenir cette image pour le §7 (les registres).

### 3.2 Paragraphes : OrigamiNet, Start-Follow-Read, SPAN, VAN

- **Start, Follow, Read** (Wigington et al., ECCV 2018) garde une segmentation explicite mais
  apprise : un réseau trouve le début de chaque ligne, un autre suit la ligne, un troisième la
  lit. [Détails de l'architecture de mémoire ; titre, auteurs et lieu vérifiés par Crossref.]
- **OrigamiNet** (Yousef et Bishop, CVPR 2020). Idée : donner à un lecteur de lignes CTC assez
  d'espace pour « déplier » une image de plusieurs lignes en une seule longue ligne. On
  l'entraîne seulement avec des paires image–texte, sans aucune position. Les auteurs font des
  **expériences d'interprétabilité** : pour chaque caractère prédit, ils calculent une carte
  d'attribution (gradients intégrés, lissés), en prennent le centre de masse, et colorent ces
  points selon la ligne de la transcription. Résultat : « une très bonne segmentation implicite
  de l'image en lignes, sans aucun signal de localisation ». C'est la preuve la plus *propre*
  de la lignée, car elle repose sur une attribution plutôt que sur des poids d'attention. Leur
  limite assumée : « apprendre le flux de plusieurs colonnes n'est pas traité directement »,
  car ils jugent la segmentation en zones « triviale » à côté de celle des lignes.
- **SPAN** (Coquenet, Chatelain et Paquet, ICDAR 2021). Un réseau entièrement convolutif prédit
  une carte 2D de caractères, puis on concatène ses rangées et on applique la CTC. Pas
  d'annotation de lignes, pas même de retours à la ligne dans le texte. Limite écrite par les
  auteurs : le modèle est « limité aux images de texte à une seule colonne » à cause de la
  concaténation des rangées, et il gère les lignes qui descendent mais pas celles qui montent.
  **L'architecture elle-même impose un ordre de lecture**, donc une forme de cadre.
- **VAN** (Coquenet, Chatelain et Paquet, *TPAMI* 2023, arXiv 2020). Un module d'attention
  produit, ligne après ligne, un masque *vertical* pondéré qui isole la ligne courante ; un
  décodeur la lit ; un détecteur décide quand le paragraphe est fini. Les auteurs : « de cette
  façon, il effectue une sorte de segmentation implicite des lignes ». CER au niveau du
  paragraphe : 1,91 % (RIMES), 4,45 % (IAM), 3,59 % (READ 2016). Point important, souvent
  oublié : leurs meilleurs résultats utilisent un **préentraînement sur des images de lignes**.
  Ils montrent qu'on peut s'en passer en préentraînant sur un *autre* jeu, mais le
  préentraînement compte beaucoup. Le cadre « ligne » rentre donc par la porte de
  l'apprentissage.

### 3.3 Pages entières : DAN et ses suites

**DAN, Document Attention Network** (Coquenet, Chatelain et Paquet, *TPAMI* 2023). C'est la
référence pour notre question. Un encodeur convolutif lit la page entière ; un décodeur
Transformer produit, un par un, les caractères **et des balises de mise en page** (début et fin
de corps de texte, de note de marge, de page, etc.), dans un ordre de lecture. Aucune
annotation de position n'est utilisée.
- CER : 3,43 % sur READ 2016 en page simple, 3,70 % en double page, 4,54 % sur RIMES 2009 en
  page.
- **Visualisation.** Les poids d'attention de la dernière couche, projetés sur l'image, suivent
  les lignes, même penchées (fig. 1 et 5). Les auteurs : « même si le DAN n'est entraîné avec
  aucune étiquette de segmentation, il effectue une sorte de segmentation implicite, que l'on
  peut retrouver globalement à travers les poids d'attention ».
- **Comment il apprend l'ordre.** Le modèle est d'abord préentraîné sur des **lignes imprimées
  synthétiques**, puis entraîné sur un mélange de vrais documents et de **documents
  synthétiques** fabriqués selon une « feuille de style » du fonds, avec un nombre de lignes qui
  augmente peu à peu (apprentissage par curriculum). Les auteurs : « l'idée est d'apprendre le
  mécanisme d'attention, c'est-à-dire l'ordre de lecture, à travers les documents
  synthétiques ». Leur étude d'ablation montre que retirer les documents synthétiques, le
  curriculum ou le préentraînement dégrade les résultats (pour RIMES, « dramatiquement » sans
  préentraînement).
- **Les balises de mise en page aident à lire.** Sur READ 2016 (avec notes de marge et doubles
  pages), retirer les balises augmente l'erreur de texte. Explication des auteurs : reconnaître
  les zones « aide à apprendre l'ordre de lecture ». Exemple : les annotations sont toujours à
  gauche du corps ; après `</annotation>`, l'attention doit aller à droite. **Nommer les
  zones (un cadre logique) aide à lire.** Sur RIMES, à l'ordre plus simple, c'est l'inverse.
- **Le codage de position 2D compte**, surtout en double page, à cause des grands sauts (de la
  fin de la page de gauche au début de celle de droite).
- **Limites écrites.** (a) Mises en page homogènes seulement ; (b) le DAN suppose qu'il existe
  *un* ordre de lecture bien défini : il ne convient pas aux documents qui en admettent
  plusieurs (schémas, cartes) ; (c) il ne donne aucune position, sauf ce qu'on peut tirer des
  cartes d'attention ; (d) ses résultats dépendent de la ressemblance des documents
  synthétiques avec le fonds réel ; (e) il est lent, car il produit un caractère à la fois.
  Sur le jeu hétérogène MAURDOR, « pour quelques exemples, le modèle se trompe d'ordre de
  lecture », et une fois il ne s'arrête pas avant la limite de 3 000 caractères : le WER
  dépasse alors 100 %.

**Faster DAN** (ICDAR 2023) accélère le DAN d'un facteur au moins 4 : le modèle prédit d'abord
**le premier caractère de chaque ligne**, puis complète toutes les lignes en parallèle. C'est
remarquable pour notre question : pour aller vite, on **réintroduit explicitement l'unité
« ligne »** dans la sortie. Le cadre revient, sous la forme d'une liste de débuts de lignes.

**Singh et Karayev (ICDAR 2021)** entraînent un modèle image→suite sur des pages entières
manuscrites ou imprimées, avec des balises (par exemple un séparateur de colonnes `<col>`). Ils
notent que leur modèle « fonctionne aussi bien sur une colonne que sur deux », alors qu'une
chaîne classique « concaténerait les lignes voisines des deux colonnes » sans module dédié.
Leurs données à deux colonnes sont synthétiques ; le modèle est déployé dans un produit
commercial, pas évalué sur un fonds patrimonial.

**Tarride, Boillet et Kermorvant (ICDAR 2023, arXiv)** utilisent des modèles à attention sur
des pages entières pour extraire des informations (texte et entités nommées) et concluent que
ces modèles sont « particulièrement intéressants sur pages entières, car ils ne demandent aucune
étape de segmentation préalable ». [Lieu ICDAR 2023 non vérifié ; arXiv vérifié.]

### 3.4 Les modèles de documents génériques (2021-2025)

Ici on quitte l'écriture manuscrite pour les documents en général. Ces modèles ont été pensés
pour comprendre des documents modernes (factures, articles, pages web), puis utilisés pour
l'OCR.
- **Donut** (Kim et al., ECCV 2022) : « sans OCR » ; un encodeur d'image et un décodeur de
  texte. Les auteurs visualisent les **cartes d'attention croisée** du décodeur sur une image
  inconnue : « le modèle s'occupe de l'endroit voulu dans l'image », alors qu'il n'a reçu aucune
  supervision de localisation (fig. 8). Ils en font un « indicateur auxiliaire » de position.
- **Pix2Struct** (Lee et al., ICML 2023) : préentraîné à retrouver le HTML (la structure)
  de captures d'écran.
- **Nougat** (Blecher et al. 2023) : articles scientifiques → balisage. Mode d'échec documenté :
  le modèle « dégénère en répétant la même phrase encore et encore », sur 1,5 % des pages de
  test, plus souvent hors domaine ; il saute ou invente parfois des numéros de section.
- **KOSMOS-2.5** (Lv et al. 2023) et **GOT-OCR 2.0** (Wei et al. 2024) : lisent des pages
  entières ; le premier peut sortir des blocs avec coordonnées, le second lire une région
  désignée. Le cadre devient une option.
- **olmOCR** (Poznanski et al. 2025) : un VLM de 7 milliards de paramètres affiné pour
  linéariser des PDF « dans l'ordre naturel de lecture ». Deux faits utiles :
  (a) les auteurs ont constaté que GPT-4o, utilisé seul sur l'image de la page, est « enclin à
  omettre du contenu, à réécrire ou compléter de façon infidèle » ; ils l'ont amélioré en lui
  donnant aussi, dans la consigne, des blocs de texte **avec leurs positions** tirés du PDF
  (*document anchoring*). **Donner un cadre au VLM améliore sa lecture.**
  (b) Leur banc d'essai, olmOCR-Bench, contient des tests de présence, d'**absence** (en-têtes
  et pieds de page qui ne doivent pas être recopiés) et d'**ordre de lecture** (par exemple, la
  première phrase d'un article de journal doit venir après son titre). olmOCR 2 (Poznanski,
  Soldaini et Lo 2025) dit progresser surtout sur les formules, les tableaux et les **mises en
  page à plusieurs colonnes**.
- **dots.ocr** (Li et al., arXiv déc. 2025) : un seul VLM produit, dans l'ordre de lecture, une
  suite de blocs, chacun avec **sa boîte, sa catégorie et son texte**. L'ablation est
  directement pertinente : retirer la tâche de détection de l'entraînement dégrade l'ordre de
  lecture de 34,9 % en anglais (score d'édition de 0,043 à 0,058) et de 25,6 % en chinois. Les
  auteurs : « une détection spatiale précise est une condition préalable pour inférer le flux
  logique du document ». Ici, « bout en bout » ne veut pas dire « sans cadre » : le cadre est
  **une sortie apprise conjointement**.
- **DeepSeek-OCR** (Wei, Sun et Li 2025) : environ 97 % de précision quand le texte compte
  moins de dix fois plus de jetons que l'image, environ 60 % à vingt fois.
- **Qwen2.5-VL** (Bai et al. 2025) : VLM généraliste qui localise par boîtes.
- **Mistral OCR** (billet de blog, 6 mars 2025) : annonce une extraction « dans l'ordre, texte
  et images entremêlés », avec des chiffres sur un banc interne non publié. La page indique
  aujourd'hui que ce modèle « n'est plus maintenu ». Aucune évaluation indépendante citée.

### 3.5 Le retour du cadre explicite (2025)

Trois systèmes de pointe de 2025 font le chemin inverse de la lignée « sans segmentation » :
- **MinerU2.5** (Niu et al. 2025) : « stratégie en deux temps, du grossier au fin, qui
  découple l'analyse globale de la mise en page de la reconnaissance locale ». D'abord la mise
  en page sur une image réduite, puis la lecture de **découpes** à pleine résolution.
- **PaddleOCR-VL** (Cui et al. 2025) : un petit VLM (0,9 milliard de paramètres) pour la
  reconnaissance des éléments, précédé d'une analyse de mise en page.
- **MonkeyOCR** (Li et al. 2025) : trois questions séparées, « Où est-ce ? » (structure),
  « Qu'est-ce que c'est ? » (reconnaissance), « Comment est-ce organisé ? » (relation). Les
  auteurs veulent éviter « l'inefficacité de traiter des pages entières avec des modèles géants
  de bout en bout ».

La raison avancée est surtout **la résolution et le coût** : une page dense en pleine
résolution fait trop de jetons. Mais l'effet est le même : le cadre redevient une étape. Le
paysage de 2025 n'est donc pas « la segmentation est morte ». C'est plutôt : **la segmentation
est apprise, et on la place là où elle coûte le moins** (avant la lecture, ou dans la sortie).

---

## 4. Les évaluations sur documents historiques (2023-2026)

Ce que disent les études qui donnent des pages historiques entières à des VLM.
- **Humphries et al. (2024)** : sur des manuscrits anglais des XVIIIe-XIXe siècles, des VLM du
  commerce obtiennent un CER de 5,7 à 7 % et un WER de 8,9 à 15,9 %, mieux que Transkribus ;
  utilisés pour corriger, ils descendent à 1,8 % de CER.
- **Kim et al. (2025)** : registres manuscrits en tableaux (français, 1919). Ils comparent
  **page entière** et **ligne par ligne**, pour GPT-4o, Claude 3.5 Sonnet et des OCR classiques.
  En moyenne, le ligne par ligne fait mieux (CER et BLEU médians), avec plus de variance. Le
  constat clé : donner la page entière « ne garantit pas le bon nombre de rangées » ; le plus
  souvent, les sorties sont **plus courtes** que la vérité, quel que soit le modèle. **Sans
  cadre, on perd des lignes.** Petit corpus : 20 pages.
- **Greif, Griesshaber et Greif (2025)** : annuaires allemands (1754-1870) ; un VLM corrige la
  sortie d'un OCR classique en regardant l'image, et descend sous 1 % de CER.
- **Levchenko (2025)** : 12 VLM sur des textes russes du XVIIIe siècle. Gemini et Qwen font
  mieux que l'OCR classique, mais « sur-historicisent » : ils insèrent des caractères anciens
  d'une mauvaise époque. La post-correction par VLM dégrade le résultat.
- **CHURRO** (Semnani et al., EMNLP 2025) : un VLM ouvert de 3 milliards de paramètres,
  entraîné sur 99 491 pages de 155 corpus historiques. Similarité de Levenshtein normalisée de
  82,3 % (imprimé) et 70,1 % (manuscrit) sur leur test. Les auteurs notent que les VLM courants
  « ne sont pas équipés » pour les **mises en page irrégulières** des documents anciens.
- **Bancs généraux.** OCRBench (Liu et al. 2023) puis **OCRBench v2** (Fu et al. 2024) :
  « la plupart des grands modèles multimodaux ont moins de 50 sur 100 » et ont cinq faiblesses,
  dont la **perception de la mise en page**. **OmniDocBench** (Ouyang et al., CVPR 2025) inclut
  des **journaux denses** et compare chaînes et VLM de bout en bout, avec une mesure d'ordre de
  lecture. **KIE-HVQA** (He et al., NeurIPS 2025) mesure les
  **hallucinations** d'OCR sur des documents dégradés : les modèles s'appuient sur leurs a
  priori de langue quand l'image est illisible.

**Bilan.** Les VLM lisent bien les documents historiques, souvent mieux que les chaînes
spécialisées non adaptées. Leurs défauts propres sont des défauts **de cadre** : lignes
omises, répétitions, ordre confondu, contenu complété. Mais la plupart des études publient un
CER global. Je n'ai trouvé aucune étude qui compte, sur des pages de presse ancienne, les
lignes omises et les inversions de colonnes d'un VLM, comparées à une chaîne segmentée sur les
mêmes pages (Gallica, NewsEye, Europeana, vérité terrain OCR-D). C'est un vrai manque — sous la
réserve de recherche indiquée en tête.

**Le cas des journaux.** American Stories (Dell et al. 2023) traite près de 20 millions de
pages de Chronicling America avec une **chaîne segmentée** : détection de mise en page,
tri de lisibilité, OCR, puis association des boîtes qui appartiennent au même article. Le
point de départ des auteurs est un constat sur le cadre : les textes existants « mélangent »
articles, titres, légendes et publicités parce que la mise en page n'a pas été reconnue.
L'OCR utilisé (EfficientOCR, Carlson, Bryan et Dell 2023) reconnaît même **caractère par
caractère**, en recherche d'images : une segmentation poussée au plus fin, choisie pour son
efficacité sur des fonds peu dotés.

---

## 5. La preuve d'une segmentation implicite : ce qu'elle vaut

### 5.1 Ce qu'on a

| étude | type de preuve | ce qu'elle montre |
|---|---|---|
| Bluche, Louradour et Messina 2017 | poids d'attention, caractère par caractère | l'attention avance dans l'ordre de lecture et saute à la ligne ; parfois revient en arrière (échec) |
| Bluche 2016 | poids d'attention, ligne par ligne | chaque pas couvre une ligne ; les pas en trop vont dans les interlignes |
| Yousef et Bishop 2020 | attribution (gradients intégrés) | les centres de masse des caractères se rangent en lignes |
| Coquenet et al. 2023 (VAN) | masque vertical appris | une bande par ligne, par construction |
| Coquenet et al. 2023 (DAN) | poids d'attention projetés | suivent les lignes penchées ; balises de zones aident l'ordre |
| Kim et al. 2022 (Donut) | attention croisée | le décodeur regarde la bonne région |
| Baek et al. 2025 (« têtes OCR ») | masquage de têtes d'attention | des têtes précises servent à lire le texte dans l'image des VLM |
| Li et al. 2025 (dots.ocr) | ablation de tâche | sans tâche de détection, l'ordre de lecture se dégrade |

### 5.2 Ce que ces preuves ne montrent pas

1. **Une carte d'attention n'est pas une explication.** Jain et Wallace (2019) ont montré, en
   langue, que des poids d'attention très différents peuvent donner la même sortie. Abnar et
   Zuidema (2020) et Chefer, Gur et Wolf (2021) proposent de meilleures façons de remonter
   l'attention à travers les couches. Adebayo et al. (2018) ont montré que certaines cartes de
   saillance ne changent presque pas quand on rend le modèle aléatoire (voir volet 04, §10).
   Pour l'OCR de bout en bout, presque toutes les preuves sont des **figures choisies**, sans
   mesure.
2. **Il manque une mesure.** Personne, à ma connaissance, ne publie un chiffre du type : « pour
   92 % des caractères, la masse d'attention tombe dans le polygone de la bonne ligne de la
   vérité terrain ». OrigamiNet s'en approche (centres de masse colorés par ligne), mais sans
   score.
3. **Il manque une intervention.** Une segmentation implicite est *utilisée* si la perturber
   change la lecture de façon prévisible. Exemples : effacer un interligne, combler une
   gouttière entre colonnes, déplacer une note de marge. Le seul résultat de ce type est
   l'ablation de dots.ocr (au niveau de l'entraînement, pas de l'image). Les têtes OCR de Baek
   et al. sont causales, mais elles portent sur *lire du texte*, pas sur *découper la page*.
4. **Il manque les VLM généralistes.** Les preuves visuelles portent sur des modèles conçus pour
   segmenter implicitement (VAN, DAN). Je ne connais pas d'étude qui sonde un VLM généraliste
   (Qwen2.5-VL, GPT-4o) pour savoir s'il représente les colonnes d'une page de journal et
   l'appartenance de chaque mot à une colonne.

### 5.3 Ce que ces preuves montrent quand même

Malgré ces limites, le faisceau est cohérent : chaque fois qu'un modèle doit produire un texte
linéaire à partir d'une page, et chaque fois qu'on a regardé, on a trouvé quelque chose qui
ressemble à des lignes. **La tâche impose la structure.** Le modèle n'a pas besoin qu'on lui
donne le cadre, mais il en construit un, parce que sa sortie (une suite ordonnée) l'exige.

Deux nuances :
- Le découpage implicite n'est pas forcément *en lignes*. OrigamiNet « déplie » ; Faster DAN
  repère des débuts de lignes ; Donut regarde des régions. Le format de la sortie et
  l'architecture décident de l'unité.
- Le cadre implicite est **appris sur un cadre explicite** dans presque tous les cas :
  préentraînement sur des lignes (VAN, DAN), documents synthétiques construits à partir d'une
  feuille de style (DAN), boîtes dans la sortie (dots.ocr, KOSMOS-2.5), positions dans la
  consigne (olmOCR). Le « sans segmentation » veut dire « sans annotation de segmentation *du
  fonds cible* », rarement « sans aucun cadre nulle part ».

---

## 6. Quand le cadre explicite reste utile ou nécessaire

D'après la littérature lue, cinq situations :
1. **Grandes pages denses (journaux).** Le nombre de caractères dépasse ce qu'un décodeur
   autorégressif produit sans dériver (répétitions de Nougat, non-arrêt du DAN, lignes perdues
   chez Kim et al.). Les chaînes à grande échelle découpent (American Stories) ; les VLM de
   pointe découpent aussi (MinerU2.5, PaddleOCR-VL).
2. **Plusieurs ordres de lecture acceptables** (cartes, schémas, pages de journaux où l'ordre
   des articles est libre). Le DAN suppose un ordre unique ; olmOCR-Bench évite exprès de
   pénaliser l'ordre des articles entre eux.
3. **Besoin de positions** : surligner un mot dans la visionneuse, réécrire un ALTO. Les
   modèles sans segmentation ne donnent pas de coordonnées, sauf ce qu'on tire de l'attention
   (DAN, limite c). C'est exactement le problème de saknussemm et de hans chez Marcel.
4. **Fonds sans données d'entraînement de pages.** DAN dépend de documents synthétiques proches
   du fonds. Une chaîne segmentée se transfère plus facilement morceau par morceau (Boillet
   2022 : modèles de lignes génériques entraînés sur de nombreux fonds).
5. **Contrôle qualité.** Une chaîne segmentée échoue *localement* (une ligne fusionnée) ; un
   modèle de bout en bout peut échouer *globalement* (boucle, ligne sautée, texte inventé).

À l'inverse, le bout en bout l'emporte quand les lignes se touchent, penchent ou se courbent
(paragraphes manuscrits : Bluche 2016, VAN, DAN), et quand la segmentation automatique est la
première source d'erreur.

**Comparaisons directes sur bancs patrimoniaux.** Ce qui existe : IAM, RIMES (lettres
modernes), READ 2016 (registres allemands anciens, avec notes de marge), où les modèles sans
segmentation égalent ou battent les chaînes. Ce que je n'ai pas trouvé : une comparaison
équivalente sur NewsEye, Europeana Newspapers, Gallica ou la vérité terrain OCR-D, c'est-à-dire
sur **de l'imprimé à plusieurs colonnes**, là où la question du cadre se pose le plus.

---

## 7. Registres, segmentation émergente, et lecture

Le cahier des charges demande les « registres » seulement en lien avec la lecture.
- **Caron et al. (2021, DINO)** : un ViT entraîné sans étiquettes a des cartes d'attention qui
  contiennent « explicitement » une segmentation sémantique de l'image. La segmentation
  **émerge** de l'apprentissage sans qu'on la demande.
- **Darcet et al. (2024, « Vision Transformers Need Registers »)** : des jetons de norme très
  élevée apparaissent dans les **zones de fond peu informatives** de l'image et sont
  « réutilisés pour des calculs internes ». Ajouter des jetons « registres » leur donne une
  place et rend les cartes d'attention plus lisses.
- **Lien avec la lecture.** Sur une page, le fond peu informatif, ce sont **les marges, les
  interlignes, les gouttières entre colonnes** : précisément les cadres matériels de la page.
  Deux observations convergent : Bluche (2016) note que les pas d'attention en trop vont dans
  les interlignes ; Baek et al. (2025) améliorent la lecture en redistribuant la valeur des
  « jetons puits » (*sink tokens*) dans les têtes OCR. Hypothèse, **non testée à ma
  connaissance** : dans un encodeur ViT de VLM, les marges et les gouttières serviraient de
  « registres » sauvages. Si c'est vrai, perturber une gouttière changerait à la fois
  la segmentation implicite et le calcul interne. Je n'ai trouvé aucune étude des registres sur
  des images de documents (réserve de recherche).

---

## 8. Ce que cela dit des projets de Marcel

Situé à partir de sa mémoire (lecture seule) :
- **babaorum, chantier de bout en bout.** La revue du 07/10 notait déjà que « le gradient CTC
  ne récupère pas les lignes manquées » et que Start-Follow-Read manquait à la revue. Le test
  E2E-1 du 17/10 est clos en échec : le bras où le gradient de lecture (CTC) remonte dans le
  détecteur extrait 2,84 lignes par ligne vraie, contre 1,20 sans ce gradient. C'est une
  version locale du résultat général : **un objectif de lecture seul ne suffit pas à poser un
  bon cadre** ; il faut une contrainte de structure (ici, l'affectation absente de la perte).
  La lignée DAN y supplée par un curriculum et des documents synthétiques.
- **Le lecteur ancré (w2:p9)** garde la géométrie et la lecture couplées : c'est la voie de
  dots.ocr (le cadre comme sortie) plutôt que celle de DAN (le cadre dans l'attention).
- **hans et saknussemm.** 84 % des découpes CTC de kraken ont une largeur de 0 pixel : la CTC
  sait *quand* émettre une lettre, pas *où* elle commence et finit. La lecture ne fournit pas
  le cadre fin ; il a fallu le réapprendre sur les boîtes ALTO (largeurs apprises, géométrie
  ancrée). Même leçon, à l'échelle du mot.

---

## 9. Conclusions

### (a) Ce qui est établi sur « segmenter pour lire »

1. **Lire une page demande une structure** : des unités (lignes, zones) et un ordre. Aucun
   système qui marche ne s'en passe. C'est le point solide.
2. **Cette structure n'a pas besoin d'être donnée d'avance.** Pour des paragraphes et des pages
   à mise en page simple ou régulière (IAM, RIMES, READ 2016), des modèles entraînés sans
   aucune position de ligne égalent ou battent la chaîne segmentée, parce qu'ils évitent les
   erreurs de découpe (Bluche 2016 ; VAN ; DAN).
3. **Ces modèles construisent une segmentation implicite**, visible dans l'attention ou
   l'attribution, et les auteurs le disent tous. Mais la preuve est surtout illustrative ; elle
   n'est ni mesurée ni testée par intervention.
4. **Le cadre implicite est presque toujours appris avec l'aide d'un cadre explicite** :
   préentraînement sur lignes, documents synthétiques, balises de zones, boîtes en sortie,
   positions dans la consigne. Et donner ce cadre aide (balises du DAN sur READ, détection de
   dots.ocr, ancrage d'olmOCR).
5. **Pour les grandes pages complexes (journaux), le cadre explicite reste la norme**, et les
   meilleurs systèmes de 2025 y reviennent, surtout pour des raisons de résolution et de coût.
6. **Les défauts propres aux modèles sans cadre explicite sont des défauts de cadre** : perdre
   sa place, sauter des lignes, répéter, ne pas s'arrêter, confondre l'ordre.
7. **Une erreur de cadre coûte plus que ne le dit sa mesure** : une fusion de lignes pèse peu
   en détection mais beaucoup en lecture (Boillet 2022). Il faut juger le cadre par la lecture
   qu'il permet.

### (b) En quoi cela soutient, nuance ou contredit la phrase de Marcel

La phrase a trois étages : (1) le cadre fonde l'intelligence ; (2) la conscience de soi est un
« se sortir du monde » que le cadre formalise ; (3) « c'est pour ça qu'un modèle a besoin de
segmenter pour ocriser correctement ». La littérature d'OCR ne parle que du troisième étage.

**Ce qui soutient.**
- Au sens faible, la phrase est juste : **lire, c'est imposer une structure** à une surface
  continue. Même les modèles « sans segmentation » segmentent, et on le voit. On peut dire que
  le cadre, au sens d'une opération de délimitation et d'ordre, est une condition de la
  lecture.
- Les échecs des modèles sans cadre ressemblent à des **pertes de repère** : revenir en arrière
  (Bluche 2017), ne pas s'arrêter (DAN), boucler (Nougat), omettre (Kim et al.). Le cadre sert
  à savoir *où l'on en est*.
- Les **cadres matériels de la page** (marges, interlignes, gouttières, filets) sont des appuis
  réels : Tesseract trouve les colonnes par leurs bords, Bluche range les pas inutiles dans les
  interlignes, et l'hypothèse des « registres » (§7) en ferait des lieux de calcul.

**Ce qui nuance.**
- **Au sens fort, la phrase est fausse dans l'état de l'art.** Un modèle n'a pas besoin qu'on
  segmente *pour* lui, ni de produire une segmentation explicite, pour bien lire un paragraphe.
  Et ne pas segmenter d'avance est parfois *meilleur*, précisément parce que le cadre imposé
  de l'extérieur se trompe.
- **Le sens de la causalité est inversé.** Dans les modèles de bout en bout, la segmentation
  n'est pas une condition préalable de la lecture : elle **émerge de l'obligation de produire
  une suite ordonnée**. C'est le format de la sortie (un texte linéaire) qui découpe la page.
  On pourrait dire : ce n'est pas le cadre qui permet de lire, c'est l'exigence d'une lecture
  linéaire qui fabrique le cadre.
- **« Correctement » dépend de la mesure.** Avec un CER qui punit l'ordre, le cadre est
  décisif ; avec une mesure indépendante de l'ordre (Clausner et al. 2020), il l'est beaucoup
  moins.

**Où l'analogie glisse.**
- **Le « se sortir du monde ».** La segmentation d'OCR découpe *des objets dans la page* (les
  lignes, les colonnes). Elle ne sépare pas le lecteur de ce qu'il lit. Aucun modèle d'OCR ne
  se représente lui-même, ni sa propre position face à la page. Le geste réflexif que Marcel
  prête au cadre (« avoir conscience de soi ») n'a pas d'équivalent dans ces travaux. Passer de
  « le modèle segmente » à « le modèle se sort du monde » serait un saut sans preuve.
- **Deux sens du mot « cadre ».** Dans la théorie (volet 01), le cadre sépare l'œuvre de ce qui
  n'est pas elle : c'est une **frontière entre deux statuts** (dedans/dehors, image/mur). En
  OCR, la segmentation sépare des **unités de même statut** (une ligne de la suivante). La
  seule frontière de statut, en OCR, est celle qui sépare le texte à lire de ce qu'il faut
  laisser (en-têtes, numéros de page, notes, tampons de bibliothèque : les tests d'« absence »
  d'olmOCR ; la distinction corps/marge de Clérice). C'est là, et seulement là, que
  l'analogie avec le *parergon* tient vraiment : décider si la note de marge, le titre courant
  ou le tampon font partie du texte.
- **Le cadre de l'OCR est conventionnel et appris**, pas fondateur. Il dépend du fonds (la
  « feuille de style » du DAN), des conventions d'annotation (la lettrine chez Boillet) et de
  la tâche. C'est cohérent avec la synthèse du projet (le statut d'un bord dépend du lecteur, de
  la tâche et du dispositif), mais cela va contre l'idée d'un cadre comme structure universelle
  de l'intelligence.
- **Une version défendable de la phrase** serait : *« Un modèle qui lit doit structurer la page ;
  il peut apprendre cette structure lui-même, mais il l'apprend mieux, et plus sûrement sur les
  pages difficiles, quand on lui donne des cadres. »* C'est vrai dans l'état de l'art. Le reste
  (intelligence, conscience de soi) relève d'une autre discussion, que l'OCR n'éclaire pas.

### (c) Trois expériences faisables sur les machines de Marcel

Contraintes : Mac 16 Go ; au plus deux calculs lourds à la fois, via `~/outils-seg/lourd.sh` ;
tout calcul de plus d'1 Go passe par cette file ; pas de dots.ocr en mise en page en local
(Kaggle si besoin, accord de Marcel au-delà de 10 unités Colab). Matériel déjà présent : trois
pages Gallica avec leur ALTO dans `~/corpus-reel/gallica/` (dont *Le Temps*, page 2, à
plusieurs colonnes) ; `microsoft/trocr-small-printed` et `dots-studio/dots.ocr` dans le cache
Hugging Face ; kraken 7.1.1. Pour chaque expérience : seuils fixés **avant** de lancer, et
comparaison sur l'intersection des pages réussies.

**E-A. Mesurer la segmentation implicite du DAN (cartes d'attention chiffrées).**
- *Matériel.* Le code et les poids publiés du DAN (dépôt FactoDeepLearning/DAN, licence
  CeCILL-C ; poids sur Zenodo, page et jeux couverts à vérifier) et les pages de test de READ
  2016, qui ont une vérité terrain PAGE avec polygones de lignes et notes de marge. Petit
  modèle, inférence page par page sur CPU ou MPS via `lourd.sh`. Code écrit pour PyTorch 1.8 :
  prévoir un environnement à part dans `~/outils-seg`.
- *Mesure.* Pour chaque caractère prédit, prendre la carte d'attention de la dernière couche
  (et, en contrôle, une version « rollout » d'Abnar et Zuidema), calculer la part de masse dans
  chaque polygone de ligne vraie. Score de **pureté** : part des caractères dont la ligne qui
  reçoit le plus de masse est la bonne. Score d'**ordre** : corrélation de rang entre l'ordre
  des lignes visitées et l'ordre PAGE.
- *Intervention.* Sur les mêmes pages : (i) effacer les notes de marge ; (ii) combler
  l'interligne entre deux lignes du corps (rapprocher les lignes) ; (iii) peindre un faux
  « interligne » blanc au milieu d'une ligne. Avec un témoin : une perturbation de même surface
  ailleurs (dans le fond).
- *Ce qui confirmerait* une segmentation implicite *utilisée* : pureté élevée (seuil à fixer,
  par exemple ≥ 0,9) ; et quand on rapproche deux lignes, les erreurs de lecture apparaissent
  aux mêmes endroits que la chute de pureté (fusions), pas avec le témoin.
- *Ce qui la contredirait* : une lecture juste avec une attention diffuse (pureté basse), ou
  des erreurs qui ne suivent pas la pureté. On conclurait alors que le modèle lit sans cadre
  localisé, ou que l'attention n'est pas le bon endroit pour le chercher.

**E-B. La gouttière comme cadre : un VLM sur des pages Gallica à colonnes.**
- *Matériel.* Les pages Gallica avec ALTO (colonnes et ordre des blocs connus). Un VLM ouvert
  en mode « texte seul », sans demande de mise en page : sur Kaggle, pas sur le Mac (un VLM de
  3 milliards de paramètres dépasse vite la mémoire avec une page en pleine résolution).
  dots.ocr en mode « OCR seul » ou Qwen2.5-VL-3B conviennent, à vérifier selon le quota.
- *Perturbations graduées* (même page, une variable à la fois) : réduire la gouttière entre
  deux colonnes de 100 % à 0 % de sa largeur ; effacer seulement le filet vertical ; décaler
  verticalement une colonne d'une demi-ligne (les lignes ne s'alignent plus) ; témoin : bande
  blanche de même surface ailleurs.
- *Mesures.* (1) **Taux d'entrelacement** : part des lignes de la sortie qui mêlent des mots
  de deux colonnes (appariement aux lignes ALTO). (2) Lignes omises et répétées. (3) Si l'on
  peut extraire l'attention du décodeur vers les jetons d'image : pour chaque mot produit, la
  colonne ALTO qui reçoit le plus de masse.
- *Ce qui confirmerait* que le modèle s'appuie sur la gouttière comme cadre : l'entrelacement
  reste nul tant que la gouttière existe, puis monte d'un coup sous un seuil de largeur ;
  le filet seul compte peu (ou beaucoup : à noter) ; le témoin ne fait rien.
- *Ce qui contredirait* : aucun entrelacement même sans gouttière (le modèle sépare les
  colonnes par la langue ou la typographie, pas par le blanc), ou un entrelacement qui suit la
  surface blanche retirée quelle que soit sa place (confusion, pas lecture du cadre).
- *Lien avec le projet.* C'est le critère « lecture ou confusion » de la synthèse (§2.3),
  transposé à la page : un effet qui suit la convention typographique (la gouttière sépare
  les colonnes) et disparaît avec un faux blanc de même surface serait une *lecture* du cadre.

**E-C. Combien de cadre faut-il à un lecteur de lignes ? (TrOCR, sur le Mac).**
- *Matériel.* `trocr-small-printed` (déjà en cache, léger) et les lignes ALTO des pages Gallica.
  Modèle de lignes : on lui donne une découpe, et on fait varier la découpe.
- *Perturbation.* Pour chaque ligne, agrandir la boîte verticalement de 0 % à 150 % de la
  hauteur de ligne, pour inclure des morceaux puis la totalité des lignes voisines ; et
  horizontalement, déborder sur la colonne voisine.
- *Mesures.* CER de la ligne centrale ; insertions venues des voisines ; attention croisée du
  décodeur vers les rangées de pixels de la ligne centrale et des voisines.
- *Ce qui confirmerait* une segmentation implicite à petite échelle : CER stable et attention
  concentrée sur la ligne centrale jusqu'à une marge assez grande ; le modèle « se cadre »
  lui-même dans une découpe trop large.
- *Ce qui contredirait* : le CER s'effondre dès qu'un morceau de voisine entre dans la boîte.
  Le modèle a alors besoin d'un cadre exact donné de l'extérieur. Résultat utile pour kraken et
  saknussemm : il dirait quelle précision de polygone suffit.
- Coût : quelques centaines de lignes, quelques minutes de CPU ou MPS, une seule place de
  `lourd.sh`.

Ordre conseillé : E-C (tout est déjà sur la machine), puis E-A, puis E-B sur Kaggle.

---

## Bibliographie

*Statut : « vérifié arXiv » = titre, auteurs et date relus sur la page arXiv (et le texte lu
quand des chiffres sont cités) ; « vérifié Crossref » = notice DOI relue ; « vérifié page »
= page de l'éditeur ou du projet consultée ; [non vérifié] sinon.*

**Chaînes classiques, mise en page, formats, ordre de lecture**
- Ares Oliveira, S., Seguin, B. & Kaplan, F. (2018). dhSegment: A Generic Deep-Learning Approach for Document Segmentation. ICFHR 2018, 7-12. https://doi.org/10.1109/ICFHR-2018.2018.00011 ; https://arxiv.org/abs/1804.10371 — vérifié Crossref + arXiv
- Boillet, M., Kermorvant, C. & Paquet, T. (2020). Multiple Document Datasets Pre-training Improves Text Line Detection With Deep Neural Networks. ICPR 2020. https://arxiv.org/abs/2012.14163 — vérifié arXiv
- Boillet, M., Kermorvant, C. & Paquet, T. (2022). Robust Text Line Detection in Historical Documents: Learning and Evaluation Methods. *IJDAR*. https://arxiv.org/abs/2203.12346 — vérifié arXiv (texte lu)
- Clausner, C., Pletschacher, S. & Antonacopoulos, A. (2020). Flexible character accuracy measure for reading-order-independent evaluation. *Pattern Recognition Letters* 131, 390-397. https://doi.org/10.1016/j.patrec.2020.02.003 — vérifié Crossref
- Clérice, T. (2023). You Actually Look Twice At it (YALTAi): using an object detection approach instead of region segmentation within the Kraken engine. *Journal of Data Mining & Digital Humanities*. https://doi.org/10.46298/jdmdh.9806 ; https://arxiv.org/abs/2207.11230 — vérifié Crossref + arXiv
- Diem, M., Kleber, F., Fiel, S., Grüning, T. & Gatos, B. (2017). cBAD: ICDAR2017 Competition on Baseline Detection. ICDAR 2017, 1355-1360. https://doi.org/10.1109/ICDAR.2017.222 — vérifié Crossref
- Grüning, T., Leifert, G., Strauß, T., Michael, J. & Labahn, R. (2019). A two-stage method for text line detection in historical documents. *IJDAR* 22, 285-302. https://doi.org/10.1007/s10032-019-00332-1 ; https://arxiv.org/abs/1802.03345 — vérifié Crossref + arXiv
- Kahle, P., Colutto, S., Hackl, G. & Mühlberger, G. (2017). Transkribus — A Service Platform for Transcription, Recognition and Retrieval of Historical Documents. ICDAR 2017, 19-24. https://doi.org/10.1109/ICDAR.2017.307 — vérifié Crossref
- Kiessling, B. kraken (logiciel), version 7.1.1 installée localement ; fonctions `polygonal_reading_order` et modèle `ro_model`. https://kraken.re — vérifié dans le code local seulement
- Kiessling, B., Tissot, R., Stokes, P. & Stökl Ben Ezra, D. (2019). eScriptorium: An Open Source Platform for Historical Document Analysis. ICDAR Workshops 2019. — [non vérifié]
- Kodym, O. & Hradiš, M. (2021). Page Layout Analysis System for Unconstrained Historic Documents. ICDAR 2021, LNCS, 492-506. https://doi.org/10.1007/978-3-030-86331-9_32 ; https://arxiv.org/abs/2102.11838 — vérifié Crossref + arXiv
- Library of Congress. ALTO (Analyzed Layout and Text Object), norme XML. https://www.loc.gov/standards/alto/ — [non vérifié]
- Muehlberger, G., Seaward, L., Terras, M. et al. (2019). Transforming scholarship in the archives through handwritten text recognition: Transkribus as a case study. *Journal of Documentation* 75(5), 954-976. https://doi.org/10.1108/JD-07-2018-0114 — vérifié Crossref
- Neudecker, C., Baierer, K., Federbusch, M., Boenig, M., Würzner, K.-M., Hartmann, V. & Herrmann, E. (2019). OCR-D: An end-to-end open source OCR framework for historical printed documents. DATeCH 2019, 53-58. https://doi.org/10.1145/3322905.3322917 — vérifié Crossref (titre court dans la notice)
- Neudecker, C., Baierer, K., Gerber, M., Clausner, C., Antonacopoulos, A. & Pletschacher, S. (2021). A survey of OCR evaluation tools and metrics. HIP 2021, 13-18. https://doi.org/10.1145/3476887.3476888 — vérifié Crossref
- Pletschacher, S. & Antonacopoulos, A. (2010). The PAGE (Page Analysis and Ground-Truth Elements) Format Framework. ICPR 2010, 257-260. https://doi.org/10.1109/ICPR.2010.72 — vérifié Crossref
- Smith, R. (2007). An Overview of the Tesseract OCR Engine. ICDAR 2007, vol. 2, 629-633. https://doi.org/10.1109/ICDAR.2007.4376991 — vérifié Crossref
- Smith, R. (2009). Hybrid Page Layout Analysis via Tab-Stop Detection. ICDAR 2009, 241-245. https://doi.org/10.1109/ICDAR.2009.257 — vérifié Crossref
- Wang, Z., Xu, Y., Cui, L., Shang, J. & Wei, F. (2021). LayoutReader: Pre-training of Text and Layout for Reading Order Detection. EMNLP 2021. https://arxiv.org/abs/2108.11591 — vérifié arXiv

**Reconnaissance sans segmentation de lignes (HTR)**
- Bluche, T. (2016). Joint Line Segmentation and Transcription for End-to-End Handwritten Paragraph Recognition. NIPS 2016. https://papers.nips.cc/paper_files/paper/2016/hash/2bb232c0b13c774965ef8558f0fbd615-Abstract.html ; https://arxiv.org/abs/1604.08352 — vérifié actes NeurIPS + arXiv (texte lu)
- Bluche, T., Louradour, J. & Messina, R. (2017). Scan, Attend and Read: End-to-End Handwritten Paragraph Recognition with MDLSTM Attention. ICDAR 2017, 1050-1055. https://doi.org/10.1109/ICDAR.2017.174 ; https://arxiv.org/abs/1604.03286 — vérifié Crossref + arXiv (texte lu)
- Coquenet, D., Chatelain, C. & Paquet, T. (2021). SPAN: a Simple Predict & Align Network for Handwritten Paragraph Recognition. ICDAR 2021, LNCS 12823. https://arxiv.org/abs/2102.08742 — vérifié arXiv (texte lu)
- Coquenet, D., Chatelain, C. & Paquet, T. (2023). End-to-End Handwritten Paragraph Text Recognition Using a Vertical Attention Network. *IEEE TPAMI* 45(1), 508-524. https://doi.org/10.1109/TPAMI.2022.3144899 ; https://arxiv.org/abs/2012.03868 — vérifié Crossref + arXiv (texte lu)
- Coquenet, D., Chatelain, C. & Paquet, T. (2023). DAN: A Segmentation-Free Document Attention Network for Handwritten Document Recognition. *IEEE TPAMI* 45(7), 8227-8243. https://doi.org/10.1109/TPAMI.2023.3235826 ; https://arxiv.org/abs/2203.12273 — vérifié Crossref + arXiv (texte lu)
- Coquenet, D., Chatelain, C. & Paquet, T. (2023). Faster DAN: Multi-target Queries with Document Positional Encoding for End-to-End Handwritten Document Recognition. ICDAR 2023, LNCS. https://doi.org/10.1007/978-3-031-41685-9_12 ; https://arxiv.org/abs/2301.10593 — vérifié Crossref + arXiv
- FactoDeepLearning. DAN, code et poids (licence CeCILL-C). https://github.com/FactoDeepLearning/DAN — vérifié page
- Li, M., Lv, T., Chen, J. et al. (2021/2023). TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models. AAAI 2023 [lieu non vérifié]. https://arxiv.org/abs/2109.10282 — vérifié arXiv
- Singh, S. S. & Karayev, S. (2021). Full Page Handwriting Recognition via Image to Sequence Extraction. ICDAR 2021. https://arxiv.org/abs/2103.06450 — vérifié arXiv (texte lu)
- Tarride, S., Boillet, M. & Kermorvant, C. (2023). Key-value information extraction from full handwritten pages. ICDAR 2023 [lieu non vérifié]. https://arxiv.org/abs/2304.13530 — vérifié arXiv
- Tensmeyer, C. & Wigington, C. (2019). Training full-page handwritten text recognition models without annotated line breaks. ICDAR 2019. — [non vérifié ; cité d'après la bibliographie de SPAN]
- Wigington, C., Tensmeyer, C., Davis, B., Barrett, W., Price, B. & Cohen, S. (2018). Start, Follow, Read: End-to-End Full-Page Handwriting Recognition. ECCV 2018, LNCS, 372-388. https://doi.org/10.1007/978-3-030-01231-1_23 — vérifié Crossref
- Yousef, M. & Bishop, T. E. (2020). OrigamiNet: Weakly-Supervised, Segmentation-Free, One-Step, Full Page Text Recognition by learning to unfold. CVPR 2020. https://arxiv.org/abs/2006.07491 — vérifié arXiv (texte lu)

**Modèles de documents et VLM d'OCR**
- Bai, S., Chen, K., Liu, X. et al. (2025). Qwen2.5-VL Technical Report. arXiv. https://arxiv.org/abs/2502.13923 — vérifié arXiv
- Blecher, L., Cucurull, G., Scialom, T. & Stojnic, R. (2023). Nougat: Neural Optical Understanding for Academic Documents. arXiv. https://arxiv.org/abs/2308.13418 — vérifié arXiv (texte lu)
- Carlson, J., Bryan, T. & Dell, M. (2023). Efficient OCR for Building a Diverse Digital History. arXiv [ACL 2024 : non vérifié]. https://arxiv.org/abs/2304.02737 — vérifié arXiv
- Cui, C., Sun, T., Liang, S. et al. (2025). PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model. arXiv. https://arxiv.org/abs/2510.14528 — vérifié arXiv
- Dell, M., Carlson, J., Bryan, T. et al. (2023). American Stories: A Large-Scale Structured Text Dataset of Historical U.S. Newspapers. arXiv [NeurIPS 2023 Datasets and Benchmarks : non vérifié]. https://arxiv.org/abs/2308.12477 — vérifié arXiv
- Kim, G., Hong, T., Yim, M. et al. (2022). OCR-free Document Understanding Transformer (Donut). ECCV 2022. https://arxiv.org/abs/2111.15664 — vérifié arXiv (texte lu)
- Lee, K., Joshi, M., Turc, I. et al. (2023). Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding. ICML 2023. https://arxiv.org/abs/2210.03347 — vérifié arXiv
- Li, Y., Yang, G., Liu, H., Wang, B. & Zhang, C. (2025). dots.ocr: Multilingual Document Layout Parsing in a Single Vision-Language Model. arXiv. https://arxiv.org/abs/2512.02498 — vérifié arXiv (texte lu)
- Li, Z., Liu, Y., Liu, Q. et al. (2025). MonkeyOCR: Document Parsing with a Structure-Recognition-Relation Triplet Paradigm. arXiv. https://arxiv.org/abs/2506.05218 — vérifié arXiv
- Lv, T., Huang, Y., Chen, J. et al. (2023). KOSMOS-2.5: A Multimodal Literate Model. arXiv. https://arxiv.org/abs/2309.11419 — vérifié arXiv
- Mistral AI (6 mars 2025). Mistral OCR (billet de blog ; modèle signalé comme non maintenu). https://mistral.ai/news/mistral-ocr — vérifié page
- Niu, J., Liu, Z., Gu, Z. et al. (2025). MinerU2.5: A Decoupled Vision-Language Model for Efficient High-Resolution Document Parsing. arXiv. https://arxiv.org/abs/2509.22186 — vérifié arXiv
- Poznanski, J., Rangapur, A., Borchardt, J. et al. (2025). olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models. arXiv. https://arxiv.org/abs/2502.18443 — vérifié arXiv (texte lu)
- Poznanski, J., Soldaini, L. & Lo, K. (2025). olmOCR 2: Unit Test Rewards for Document OCR. arXiv. https://arxiv.org/abs/2510.19817 — vérifié arXiv
- Wei, H., Liu, C., Chen, J. et al. (2024). General OCR Theory: Towards OCR-2.0 via a Unified End-to-end Model (GOT-OCR 2.0). arXiv. https://arxiv.org/abs/2409.01704 — vérifié arXiv
- Wei, H., Sun, Y. & Li, Y. (2025). DeepSeek-OCR: Contexts Optical Compression. arXiv. https://arxiv.org/abs/2510.18234 — vérifié arXiv

**Évaluations (documents historiques, bancs d'OCR pour VLM)**
- Fu, L., Kuang, Z., Song, J. et al. (2024). OCRBench v2: An Improved Benchmark for Evaluating Large Multimodal Models on Visual Text Localization and Reasoning. arXiv. https://arxiv.org/abs/2501.00321 — vérifié arXiv
- Greif, G., Griesshaber, N. & Greif, R. (2025). Multimodal LLMs for OCR, OCR Post-Correction, and Named Entity Recognition in Historical Documents. arXiv. https://arxiv.org/abs/2504.00414 — vérifié arXiv
- He, Z., Zhang, C., Wu, Z. et al. (2025). Seeing is Believing? Mitigating OCR Hallucinations in Multimodal Large Language Models (KIE-HVQA). NeurIPS 2025. https://arxiv.org/abs/2506.20168 — vérifié arXiv
- Humphries, M., Leddy, L. C., Downton, Q. et al. (2024). Unlocking the Archives: Using Large Language Models to Transcribe Handwritten Historical Documents. arXiv. https://arxiv.org/abs/2411.03340 — vérifié arXiv
- Kim, S., Baudru, J., Ryckbosch, W., Bersini, H. & Ginis, V. (2025). Early evidence of how LLMs outperform traditional systems on OCR/HTR tasks for historical records. arXiv. https://arxiv.org/abs/2501.11623 — vérifié arXiv (texte lu)
- Levchenko, M. (2025). Evaluating LLMs for Historical Document OCR: A Methodological Framework for Digital Humanities. LM4DH 2025 (RANLP). https://arxiv.org/abs/2510.06743 — vérifié arXiv
- Liu, Y., Li, Z., Huang, M. et al. (2023). OCRBench: On the Hidden Mystery of OCR in Large Multimodal Models. arXiv. https://arxiv.org/abs/2305.07895 — vérifié arXiv
- Ouyang, L., Qu, Y., Zhou, H. et al. (2025). OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations. CVPR 2025. https://arxiv.org/abs/2412.07626 — vérifié arXiv
- Semnani, S. J., Zhang, H., He, X., Tekgürler, M. & Lam, M. S. (2025). CHURRO: Making History Readable with an Open-Weight Large Vision-Language Model for High-Accuracy, Low-Cost Historical Text Recognition. EMNLP 2025. https://arxiv.org/abs/2509.19768 — vérifié arXiv

**Interprétabilité, attention, segmentation émergente**
- Abnar, S. & Zuidema, W. (2020). Quantifying Attention Flow in Transformers. ACL 2020 [lieu non vérifié]. https://arxiv.org/abs/2005.00928 — vérifié arXiv
- Adebayo, J., Gilmer, J., Muelly, M., Goodfellow, I., Hardt, M. & Kim, B. (2018). Sanity Checks for Saliency Maps. NeurIPS 2018. https://arxiv.org/abs/1810.03292 — vérifié arXiv
- Baek, I., Chang, H., Ryu, S. & Lee, H. (2025). How Do Large Vision-Language Models See Text in Image? Unveiling the Distinctive Role of OCR Heads. EMNLP 2025. https://arxiv.org/abs/2505.15865 — vérifié arXiv
- Caron, M., Touvron, H., Misra, I., Jégou, H., Mairal, J., Bojanowski, P. & Joulin, A. (2021). Emerging Properties in Self-Supervised Vision Transformers (DINO). ICCV 2021 [lieu non vérifié]. https://arxiv.org/abs/2104.14294 — vérifié arXiv
- Chefer, H., Gur, S. & Wolf, L. (2021). Generic Attention-model Explainability for Interpreting Bi-Modal and Encoder-Decoder Transformers. ICCV 2021 [lieu non vérifié]. https://arxiv.org/abs/2103.15679 — vérifié arXiv
- Darcet, T., Oquab, M., Mairal, J. & Bojanowski, P. (2024). Vision Transformers Need Registers. ICLR 2024 [lieu non vérifié]. https://arxiv.org/abs/2309.16588 — vérifié arXiv
- Jain, S. & Wallace, B. C. (2019). Attention is not Explanation. NAACL 2019. https://arxiv.org/abs/1902.10186 — vérifié arXiv

**Sources internes (mémoire de Marcel, lecture seule)**
- `outils-segmentation-locaux` (banc du 14/09/2026, BnL, 37 pages) ; `hans-h21-largeurs-apprises` (découpes CTC à 0 px) ; `saknussemm-geometrie-ancree` ; `babaorum-end-to-end` (E2E-1, 17/10/2026) ; `babaorum-lecteur-w2p9` ; `axel-limite-calculs-lourds`. Notes de travail, non publiées.
