# Volet 4 — La vision machine face au contexte, au fond, au bord et au cadre

*Revue de littérature, côté sciences informatiques et sciences cognitives. 17/10/2026.*

**Objet.** Ce volet ne refait pas les deux notes déjà écrites :
[`../litt-cadrage-ia-machines.md`](../litt-cadrage-ia-machines.md) (recadrage avant calcul,
recadrage de Twitter, détection d'œuvres, outpainting, jeux de données d'art) et
[`../etat-des-lieux-cadrage-ia.md`](../etat-des-lieux-cadrage-ia.md) (synthèse). Il ajoute ce qui
leur manquait : **ce que la psychologie et la vision par ordinateur savent du contexte**, et
surtout **les méthodes pour savoir ce qu'un modèle fait d'un élément de l'image** (un cadre, une
marge, une mire, un bord). La question finale est : *comment pourrait-on savoir qu'un modèle
« traverse » un support, ou qu'il le « lit » comme un message ?*

**Comment c'est vérifié.** Chaque référence a été ouverte le 17/10/2026 (page arXiv, notice
Crossref, page des actes, ou texte intégral quand une phrase est citée). Les résumés cités ont été
lus. **[contenu non relu]** : l'affirmation vient du corps d'un article non relu ici. **[non
vérifié]** : détail (souvent le lieu de publication) non confirmé. « (voir note machines) » :
référence déjà vérifiée dans la note précédente. Le budget de recherche web de la session s'est
épuisé en cours de route ; quelques pistes n'ont pas pu être cherchées (voir § 12).

**Rappel sur nos pilotes.** Ils sont cités comme *hypothèses* à tester, jamais comme acquis :
(a) un cadre rocaille ferait monter le prix estimé par un VLM pour un objet banal, pas pour une
œuvre reconnue ; (b) sur des photos de musée, le VLM lit la mire ou la marque de l'institution ;
(c) le bord d'un négatif ne change pas la lecture ; (d) SAM 3 met le bord de « painting » sur la
toile, et celui de « artwork » sur le cadre.

**Petit lexique.**
- *Modèle de vision* : programme qui transforme une image en nombres, puis en réponse (une
  classe, une boîte, un masque).
- *VLM* (modèle vision-langage) : modèle qui prend une image et un texte, et répond en texte
  (GPT-4o, Gemini, Claude, Qwen-VL, LLaVA).
- *Représentation* (ou *embedding*) : la liste de nombres que le modèle fabrique pour une image ;
  deux images « proches » pour lui ont des listes proches.
- *Classe* : l'étiquette que le modèle doit donner (« cheval », « tableau »).
- *Contrefactuel* : la même image, modifiée sur un seul point (on enlève le cadre, on change le
  fond), pour voir si la réponse change.

---

## 1. Pourquoi cette littérature compte pour la question du cadre

L'intuition de Marcel est double. Le cadre « enveloppe une partie du sens ». Et il « permet
d'isoler le support », donc de le rendre déterminant. En vision par ordinateur, ces deux idées ont
un nom ordinaire, sans rapport avec l'art. La première est le **contexte** : ce qui entoure
l'objet aide (ou trompe) la reconnaissance. La seconde est le **domaine** : le support, la
technique, le « style » d'une image (photo, peinture, dessin) est une variable que les modèles
apprennent soit à ignorer (invariance), soit à utiliser (raccourci).

Cette littérature ne parle presque jamais de cadres de tableaux. Mais elle a construit, depuis
quarante ans, des façons rigoureuses de répondre à une question proche : *ce que voit le système,
est-ce l'objet, ou ce qui l'entoure ?* C'est exactement notre question, posée à l'envers : nous
voulons savoir si l'entourage (le cadre) est *lu*.

Trois enseignements dominent, et ils structurent la suite :

1. Le contexte n'est **jamais neutre**, ni pour l'humain ni pour la machine (sections 2 et 3).
2. Les machines prennent volontiers des **raccourcis** : un indice facile (un logo, une marque,
   un fond) remplace l'objet. Un cadre est un candidat idéal (section 4).
3. Savoir ce qu'un modèle « fait » d'un élément demande des **interventions contrôlées**, pas des
   cartes de chaleur ni des explications données par le modèle lui-même (section 9).

---

## 2. Le contexte dans la perception humaine

### 2.1 L'objet se reconnaît dans sa scène

- **Biederman, Mezzanotte & Rabinowitz (1982)**, « Scene perception: Detecting and judging objects
  undergoing relational violations », *Cognitive Psychology* 14(2), p. 143-177. Expérience
  classique : on montre très brièvement des scènes où un objet viole une règle (il flotte au lieu
  d'être posé, il est à la mauvaise taille, il n'a rien à faire là). Les violations ralentissent
  ou gênent la détection [détail des cinq types de violation : contenu non relu, connu par la
  littérature secondaire]. **Leçon :** l'humain n'identifie pas un objet seul ; il le vérifie
  contre une scène attendue.

- **Davenport & Potter (2004)**, « Scene Consistency in Object and Background Perception »,
  *Psychological Science* 15(8). Un objet est mieux identifié sur un fond cohérent que sur un fond
  incongru, même en vision très brève [résultat d'après le titre et la littérature ; texte non
  relu]. **Leçon :** objet et fond sont traités ensemble, très tôt.

- **Bar (2004)**, « Visual objects in context », *Nature Reviews Neuroscience* 5, p. 617-629.
  Synthèse : le cerveau utilise le contexte pour prédire ce qu'il va voir. **Leçon :** le contexte
  agit comme une *attente*, avant l'examen détaillé.

- **Oliva & Torralba (2007)**, « The role of context in object recognition », *Trends in Cognitive
  Sciences* 11(12), p. 520-527. Synthèse qui relie la psychologie et la vision par ordinateur. La
  « gist » (l'essentiel d'une scène, saisi en un coup d'œil) oriente la recherche des objets.
  **Leçon pour nous :** un mur de musée, un cadre doré, une vitrine sont une « gist » : ils disent
  « ici, de l'art » avant que l'objet soit examiné.

### 2.2 Le bord de l'image n'est pas le bord de la scène

- **Intraub & Richardson (1989)**, « Wide-angle memories of close-up scenes », *Journal of
  Experimental Psychology: Learning, Memory, and Cognition* 15(2), p. 179-187. C'est l'article
  fondateur de l'« extension des limites » (*boundary extension*) : on se souvient d'une photo
  comme plus large qu'elle n'était. La mémoire complète le hors-champ.

- **Bainbridge & Baker (2020)**, « Boundaries Extend and Contract in Scene Memory Depending on Image
  Properties », *Current Biology* 30(3), p. 537-543. Le titre dit le résultat : selon l'image, la
  mémoire élargit *ou rétrécit* le cadrage.

**Leçon :** pour l'esprit humain, le bord d'une photographie est poreux. La psychologie confirme
ici, sans le savoir, l'opposition de Bazin entre cadre centripète et cache centrifuge (voir le
volet humanités). Il serait intéressant de savoir si un cadre *peint ou doré* réduit l'extension
des limites (le cadre ferme la scène). Je n'ai trouvé aucune étude sur ce point [recherche
interrompue par la limite de la session : à refaire].

### 2.3 Le regard va au centre

- **Tatler (2007)**, « The central fixation bias in scene viewing… », *Journal of Vision* 7(14),
  art. 4. Les humains regardent d'abord le centre d'une image, même quand les objets intéressants
  sont ailleurs. **Leçon :** le « centre » d'une image est un effet du *cadre* (du bord du
  support), pas seulement du contenu. Les modèles de saillance appris sur le regard humain
  héritent de ce biais (voir les audits de Twitter, note machines).

- **Itti, Koch & Niebur (1998)**, *IEEE TPAMI* 20(11), p. 1254-1259 : modèle fondateur de la
  saillance (ce qui « saute aux yeux » par contraste, couleur, orientation). **Leçon :** une
  dorure contrastée est saillante par construction ; un modèle peut « regarder » le cadre sans
  rien y lire.

### 2.4 Le contexte institutionnel change le jugement esthétique

Rappel bref (d'autres volets les traitent), car ils donnent le **modèle humain** à comparer :
**Kirk et al. (2009)**, *NeuroImage* 44(3) : les mêmes images sont jugées plus belles quand on les
dit issues d'une galerie que d'un ordinateur [résumé connu ; texte non relu] ; **Brieber, Nadal &
Leder (2015)**, *Acta Psychologica* 154 : le contexte du musée augmente la valeur perçue et la
mémorisation (titre) ; **Millet et al. (2023)**, *Computers in Human Behavior* 143 : l'étiquette
« fait par une IA » fait baisser l'appréciation.

**Leçon :** chez l'humain, un *message sur l'image* (étiquette, lieu, cadre) change sa valeur :
c'est Bateson mis en expérience. D'où la question précise : **un VLM reproduit-il ces effets, et
par quel chemin ?** Les protocoles humains (même image, contexte varié) se transposent tels quels.

---

## 3. Le contexte dans la vision par ordinateur

### 3.1 Le contexte comme aide

- **Torralba (2003)**, « Contextual Priming for Object Detection », *International Journal of
  Computer Vision* 53(2), p. 169-191. Montre qu'on peut prédire la présence, la position et la
  taille probable d'un objet à partir de la scène globale, sans voir l'objet.
- **Divvala, Hoiem, Hays, Efros & Hebert (2009)**, « An empirical study of context in object
  detection », CVPR 2009, p. 1271-1278. Étude systématique de plusieurs sortes de contexte
  (pixels voisins, géométrie de la scène, présence d'autres objets…) et de leur apport à la
  détection [conclusions détaillées : contenu non relu].

**Leçon :** dans les années 2000, le contexte était un *ingrédient voulu*. On l'ajoutait au
détecteur. Avec l'apprentissage profond, il est entré tout seul, sans qu'on le contrôle.

### 3.2 Le contexte comme biais : les jeux de données ont un « style »

- **Torralba & Efros (2011)**, « Unbiased look at dataset bias », CVPR 2011, p. 1521-1528.
  L'article célèbre pour son jeu « Name That Dataset ! » : un classifieur reconnaît de quel jeu de
  données vient une image, alors que tous prétendent montrer « le monde ». Chaque jeu a sa façon
  de cadrer, de centrer, de choisir. **Leçon directe :** une collection a une *signature visuelle*.
  Une photothèque de musée (fond neutre, éclairage, mire, format) en a une. Un modèle peut
  reconnaître « photo de musée » avant de reconnaître l'œuvre. C'est ce que suggère notre pilote
  (b), à vérifier.

### 3.3 Le fond suffit parfois, et peut tromper

- **Zhu, Xie & Yuille (2017)**, IJCAI 2017. Un réseau entraîné sur le **fond seul** (objet effacé) reconnaît la classe
  beaucoup mieux que des humains placés dans la même situation. Avec l'objet seul, les humains
  restent meilleurs. **Leçon :** les machines exploitent le contexte plus que nous.

- **Rosenfeld, Zemel & Tsotsos (2018)**, « The Elephant in the Room ». On colle un objet (un éléphant) dans une scène : cela change la détection d'*autres*
  objets, parfois loin. **Leçon :** un élément ajouté a un effet *non local*. Un cadre ajouté peut
  changer ce que le modèle dit du centre.

- **Shetty, Schiele & Fritz (2019)**, CVPR 2019. On efface
  un objet et on mesure ce qui change ailleurs. **Leçon :** c'est la méthode de l'*ablation*,
  appliquée au contexte.

- **Xiao, Engstrom, Ilyas & Mądry (2021)**, « Noise or Signal », ICLR 2021 (note machines). Résumé lu : les modèles atteignent une
  précision « non triviale » avec le **fond seul** ; un fond choisi exprès fait échouer jusqu'à
  87,5 % des images dont l'objet seul est bien classé ; **les modèles plus précis dépendent moins
  du fond**. Leur boîte à outils sépare objet et fond, puis recombine (même objet, autre fond).
  **C'est le modèle méthodologique le plus proche de ce que nous voulons faire avec les cadres.**

- **Moayeri et al. (2022)**, RIVAL10, CVPR 2022 [lieu non vérifié]. On ajoute du bruit soit à l'objet, soit au fond, avec des masques précis. Résultat
  lu dans le résumé : les modèles entraînés par contraste (comme CLIP) ont une sensibilité
  *relative* à l'objet plus faible. **Leçon :** CLIP, base de nombreux VLM, regarde
  proportionnellement plus le fond que d'autres modèles.

- **Li, Chen, Zhu et al. (2023)**, « ImageNet-E », CVPR 2023 : on édite fond, taille, position,
  orientation ; résumé lu : « a small change in the background can lead to an average of 9.23 %
  drop on top-1 accuracy ». **Zhang et al. (2024)**, « ImageNet-D », CVPR 2024 : même idée avec
  des images générées par diffusion.

**Leçon méthodologique :** depuis 2020, on **fabrique** des variantes contrôlées. Pour les
cadres : même œuvre, même éclairage, cadre changé (aucun, baguette, doré, rocaille), rien d'autre.

### 3.4 Le lieu de prise de vue comme raccourci

- **Beery, Van Horn & Perona (2018)**, « Recognition in Terra Incognita », ECCV 2018. Images de
  pièges photographiques (appareils fixes). Résumé lu : excellents scores au même endroit, mauvaise
  généralisation à de nouveaux lieux, surtout pour la classification. L'article est connu pour
  l'exemple de la vache sur une plage, mal reconnue parce que les vaches sont « sur l'herbe »
  [figure : contenu non relu]. **Leçon :** le *lieu* (ici, l'appareil fixe) est appris avec
  l'animal. Transposé : la *photothèque* (le studio d'un musée) est apprise avec l'œuvre.

- **Sagawa, Koh, Hashimoto & Liang (2020)**, « Distributionally Robust Neural Networks for Group
  Shifts: On the Importance of Regularization for Worst-Case Generalization », ICLR 2020 (arXiv
  1911.08731). Ils introduisent **Waterbirds** : des oiseaux d'eau et de terre collés sur des fonds
  d'eau ou de terre, avec une corrélation forte à l'entraînement. Le modèle apprend le fond. Le
  résumé parle de modèles « highly accurate on average » mais qui échouent sur les groupes
  atypiques. **Leçon :** une *moyenne* bonne peut cacher l'échec sur le cas rare (l'oiseau d'eau
  sur fond de terre). Pour nous : le cas rare est l'objet banal dans un cadre précieux, ou le
  chef-d'œuvre sans cadre. Il faut les mesurer *à part*.

---

## 4. Les raccourcis (« shortcut learning »)

### 4.1 La notion

- **Geirhos, Jacobsen, Michaelis, Zemel, Brendel, Bethge & Wichmann (2020)**, « Shortcut learning
  in deep neural networks », *Nature Machine Intelligence* 2, p. 665-673. Définition (résumé lu) :
  des règles de décision qui marchent sur les tests habituels mais ne se transfèrent pas à des
  conditions plus difficiles. Les auteurs notent que des phénomènes semblables existent chez les
  animaux et les élèves. **Le « cadre comme raccourci »** se formule ainsi : si, dans les données,
  « cadre doré » va souvent avec « œuvre de valeur », le modèle peut apprendre le cadre au lieu de
  l'œuvre.

### 4.2 Trois exemples qui ressemblent à une mire de musée

Ces cas sont précieux parce qu'ils portent sur des **marques d'institution dans le coin de
l'image** : exactement notre pilote (b).

- **Lapuschkin, Wäldchen, Binder, Montavon, Samek & Müller (2019)**, « Unmasking Clever Hans
  Predictors and Assessing What Machines Really Learn », *Nature Communications* 10, 1096. Texte
  lu (arXiv 1902.10178). Un classifieur (« Fisher vector ») entraîné sur PASCAL VOC 2007 reconnaît
  les chevaux grâce à une **mention de source** (« source tag ») dans le coin inférieur gauche,
  présente sur environ un cinquième des images de chevaux. Deux interventions le prouvent :
  « artificially cutting the source tag from horse images significantly weakens the FV model's
  decision », et en ajoutant la mention sur une Ferrari, la prédiction passe de « voiture » à
  « cheval ». Un réseau profond, lui, regardait le cheval. **Leçon double :** (1) une marque de
  provenance peut devenir le signal ; (2) la carte de chaleur *signale* le problème, mais ce sont
  l'**ablation** (enlever) et l'**insertion** (ajouter ailleurs) qui le *prouvent*.

- **Zech, Badgeley, Liu, Costa, Titano & Oermann (2018)**, « Variable generalization performance
  of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study »,
  *PLOS Medicine* 15(11), e1002683. Texte lu : un réseau identifie l'hôpital d'origine d'une
  radio avec 99,95 % (NIH) et 99,98 % (Mount Sinai) de justesse ; il détecte « a metal token that
  radiology technicians place on the patient ». Les marqueurs métalliques apparaissent « in a
  site-specific way ». **Leçon :** une institution laisse dans l'image une signature (jeton,
  format, inversion de couleurs) que la machine lit mieux que le contenu médical. Une mire de
  couleur, une règle graduée, un numéro d'inventaire sont nos jetons métalliques.

- **DeGrave, Janizek & Lee (2021)**, « AI for radiographic COVID-19 detection selects shortcuts
  over signal », *Nature Machine Intelligence* 3, p. 610-619. Même phénomène, à grande échelle :
  les modèles exploitent des marques de bord et de position plutôt que les poumons [détail :
  contenu non relu].

### 4.3 Pourquoi un indice est préféré à un autre

- **Geirhos, Rubisch, Michaelis, Bethge, Wichmann & Brendel (2019)**, « ImageNet-trained CNNs are
  biased towards texture; increasing shape bias improves accuracy and robustness », ICLR 2019
  (oral). Méthode du **conflit d'indices** (*cue conflict*) : une image a la forme d'un chat et la
  texture d'un éléphant ; on regarde laquelle « gagne ». Résumé lu : les réseaux entraînés sur
  ImageNet suivent la texture, les humains la forme (97 observateurs, 48 560 essais). **C'est la
  méthode décisive pour nous** : mettre en conflit le cadre et le contenu (objet banal dans cadre
  rocaille ; chef-d'œuvre dans cadre en plastique) et voir lequel commande le jugement.

- **Hermann & Lampinen (2020)**, « What shapes feature representations? Exploring datasets,
  architectures, and training », NeurIPS 2020 (arXiv 2006.12433) [lieu de publication : non
  vérifié ; seul arXiv lu]. Et **Hermann, Mobahi, Fel & Mozer (2024)**, « On the Foundations of
  Shortcut Learning », ICLR 2024. Résumé lu : le modèle choisit un indice selon sa
  **prédictivité** (est-il fiable ?) et sa **disponibilité** (est-il facile à extraire ?). Un
  indice très disponible et moins fiable peut l'emporter. **Leçon :** un cadre doré est très
  disponible (gros, contrasté, au bord, toujours au même endroit). Il est donc un raccourci
  probable *même s'il n'est pas très fiable*.

- **Ritter, Barrett, Santoro & Botvinick (2017)**, « Cognitive Psychology for Deep Neural Networks:
  A Shape Bias Case Study », ICML 2017. Résumé lu : la force du biais de forme « varies greatly
  among architecturally identical, but differently seeded » réseaux. **Leçon :** deux modèles
  identiques, entraînés avec un autre tirage au hasard, peuvent traiter un indice différemment. Un
  résultat sur *un* modèle ne dit rien de « la machine ».

---

## 5. Domaines, invariance, robustesse : le support comme variable

En vision par ordinateur, un **domaine** est une famille d'images qui partagent une façon d'être
faites : photo, peinture, croquis, clipart. Changer de domaine sans changer de contenu est un
*décalage de distribution* (*distribution shift*) : les données de test ne ressemblent pas à
celles de l'entraînement. Le support matériel d'une œuvre (toile, papier, négatif) est très
proche de cette notion.

- **PACS** (Li et al., ICCV 2017) : quatre domaines, Photo, **Art painting**, Cartoon, Sketch. La
  peinture y est un domaine dont le modèle doit se libérer pour reconnaître le chien.
  **DomainNet** (Peng et al., ICCV 2019) : six domaines, dont « painting ». **ImageNet-Sketch**
  (Wang et al., NeurIPS 2019) : des croquis. **ImageNet-R** (Hendrycks et al., ICCV 2021) : des
  « renditions » (peintures, sculptures, broderies). **ImageNet-C** (Hendrycks & Dietterich, ICLR
  2019) : flou, bruit, compression, autrement dit les défauts du support.
- **Recht et al. (2019)** : un nouveau jeu de test fait « à l'identique » fait baisser la
  précision ; de petits écarts de collecte comptent. **ObjectNet** (Barbu et al., NeurIPS 2019) :
  fond, rotation et point de vue **contrôlés** par l'expérimentateur ; forte chute des
  performances (environ 40 à 45 points selon la page du laboratoire).
- **Fang et al. (2022)** : la robustesse de CLIP aux changements de domaine vient de la diversité
  de ses données, pas de sa méthode (résumé).

**Ce que cela implique pour notre question.** Toute cette tradition considère le support comme
une **nuisance** : un bon modèle doit le *traverser*. L'œuvre d'art y apparaît d'ailleurs comme
un domaine parmi d'autres (« art painting », « renditions »). Personne, dans ces jeux, ne demande
si le support porte un *sens*. C'est exactement l'angle mort de Marcel : quand le support *est*
le sens (une estampe dont la marge porte la lettre, un ready-made dont le socle fait l'œuvre),
l'invariance devient une **erreur**. La littérature n'a pas de mot pour « l'invariance qu'il ne
faudrait pas avoir ». La note machines (Met Dataset, SynGallery) montre la même logique pour la
reconnaissance d'œuvres : le cadre y est un obstacle à franchir.

**Un point de vocabulaire utile.** Les deux attitudes possibles s'appellent en apprentissage
*invariance* (la sortie ne change pas quand le support change) et *équivariance* ou
*sensibilité* (la sortie change de façon réglée). « Traverser » le support = invariance ; « le
lire » = sensibilité *orientée par le sens*. La section 10 en tire des définitions testables.

---

## 6. Recadrage, taille de l'objet, plusieurs objets

La note machines couvre déjà le recadrage central (CLIP, DINOv2), FixRes, Baldrati et al. 2023,
GC-CLIP et ViCrop 2025. On ajoute trois points.

- **Tsipras, Santurkar, Engstrom, Ilyas & Mądry (2020)**, « From ImageNet to Image Classification:
  Contextualizing Progress on Benchmarks », ICML 2020 [lieu : non vérifié ; arXiv lu]. Et
  **Beyer, Hénaff, Kolesnikov, Zhai & van den Oord (2020)**, « Are we done with ImageNet? »,
  prépublication arXiv 2006.07159. Beaucoup d'images contiennent plusieurs objets ; une seule
  étiquette est une simplification. **Leçon :** une photo de tableau encadré contient au moins
  trois objets (toile, cadre, mur). Demander « qu'est-ce que c'est ? » suppose déjà un choix du
  bon niveau. Le désaccord entre « painting » et « artwork » (pilote d) est de cet ordre.
- **ViCrop** (Zhang et al., ICLR 2025, voir note machines) montre que la justesse d'un VLM dépend
  *causalement* de la taille du sujet. **Conséquence pour les protocoles :** ajouter un cadre
  autour d'une œuvre réduit sa taille relative dans l'image. Un effet du « cadre » peut donc être
  un simple effet de **taille**. Tout protocole doit contrôler la surface occupée par l'œuvre
  (même nombre de pixels de toile avec et sans cadre).
- **Zolna et al. (2019)**, « Adversarial Framing » (voir note machines). Résumé relu : on garde
  l'image intacte et on ajoute seulement une **bordure** calculée ; cela suffit à tromper des
  classifieurs, de façon universelle. **Leçon :** le bord de l'image est un canal d'influence
  puissant, techniquement prouvé. Ce n'est pas encore une *lecture* : c'est une prise de contrôle
  par des pixels dénués de sens.

---

## 7. Les VLM : texte dans l'image, marques visuelles, a priori

### 7.1 Le modèle lit le texte dans l'image

- **Goh et al. (2021)**, *Distill* (note machines) : les « attaques typographiques » ; un mot écrit sur un objet
  change la classe donnée par CLIP.
- **Materzynska, Torralba & Bau (2022)**, CVPR 2022 [lieu non vérifié]. Résumé lu : l'encodeur d'images de CLIP associe
  l'image d'un *mot écrit* à des scènes que décrit ce mot ; on peut isoler un « sous-espace » de
  l'orthographe et l'enlever. **Leçon :** lire le texte est une capacité *séparable* dans le
  modèle ; on peut donc tester si une réponse dépend de cette capacité.
- **TextVQA** (Singh et al., CVPR 2019) et **OCRBench** (Liu et al., 2024). Les
  VLM sont désormais *entraînés* à lire le texte des images. Une mire, un cartel, un numéro
  d'inventaire seront donc lus, par construction.
- **Cheng et al. (2024)**, ECCV 2024, et **Qraitem et al. (2024)**. Les grands VLM restent sensibles aux
  textes ajoutés dans l'image.

**Leçon pour le pilote (b).** Qu'un VLM lise la marque d'une institution n'est pas surprenant :
c'est ce pour quoi il est entraîné. La question intéressante est autre : **la marque change-t-elle
le jugement sur l'œuvre** (valeur, authenticité, date) ? C'est la différence entre *voir* un
élément et *s'en servir*. Seul un contrefactuel (même image, mire retirée ou remplacée par une
mire d'une autre institution) peut répondre.

### 7.2 Une marque graphique dirige l'attention

La note machines cite Shtedritski et al. (cercle rouge, ICCV 2023) et Bahng et al. (bordure
apprise, 2022). Ajout : ces travaux montrent que les VLM ont appris des **conventions graphiques
humaines** (le cercle rouge = « regardez ici »), sans doute parce qu'elles abondent sur le web.
Hypothèse pour nous (non testée par eux) : le cadre doré est une convention graphique du même
type (« ceci est une œuvre »). Le cercle rouge fournit le **gabarit d'expérience** : mêmes
images, avec et sans marque, et l'on mesure le déplacement de la réponse.

### 7.3 Le modèle répond par ce qu'il sait plutôt que par ce qu'il voit

- **Goyal et al. (2017)**, « Making the V in VQA Matter », et **Agrawal et al. (2018)**, CVPR. Les
  systèmes de questions-réponses visuelles répondent souvent à partir de la question seule
  (« de quelle couleur est la banane ? » → jaune). Remède : des **paires minimales** d'images
  qui demandent des réponses différentes.
- **Li et al. (2023)**, POPE, EMNLP 2023. Les VLM « voient » des objets absents, surtout ceux qui vont
  souvent avec les objets présents [mécanisme de co-occurrence : contenu non relu en détail].
- **Tong et al. (2024)**, « Eyes Wide Shut? », CVPR 2024 [lieu non vérifié]. Résumé lu : des « CLIP-blind
  pairs », images que CLIP juge semblables malgré des différences nettes ; GPT-4V se trompe sur
  des questions simples à leur sujet.
- **Rahmanzadehgervi et al. (2024)**, « Vision language models are blind » ; **Vo et al.
  (2025)**, « Vision Language Models are Biased » (note machines) : le savoir l'emporte sur la vue.

**Leçon décisive pour le pilote (a).** Quand le VLM reconnaît un Renoir, il sait déjà que « Renoir
vaut cher ». Le cadre ne peut rien ajouter : la réponse est **saturée** par le savoir. Quand il ne
reconnaît pas l'objet, il n'a que des indices visuels, et le cadre devient un indice fort. Ce
schéma (« le contexte compte quand l'objet est ambigu ») est *exactement* celui que la
psychologie décrit chez l'humain (section 2.1) et que Mei et al. (2025) trouvent pour les prix
(l'image compte surtout pour les œuvres jamais vendues ; voir note machines). Notre pilote (a)
n'est donc pas une curiosité : il est **prédit** par la littérature. C'est une force (il est
plausible) et une faiblesse (il faut montrer qu'il dit quelque chose de spécifique au cadre).

---

## 8. Valeur, esthétique, jugement par les modèles

### 8.1 Modèles d'esthétique

**AVA** (Murray, Marchesotti & Perronnin, CVPR 2012) : des centaines de milliers de photos notées
par une communauté de photographes amateurs. **NIMA** (Talebi & Milanfar, *IEEE TIP* 2018) : un
réseau prédit la *distribution* de ces notes. **AesBench** (Huang et al., 2024) : banc d'essai
esthétique pour VLM. **BAID** (note machines) : notes sur des images d'art. **Leçon :** ces
modèles apprennent un « goût moyen » sur des images *déjà cadrées* ; le cadre physique n'y est
jamais une variable. Le goût appris porte sans doute sur la composition, donc sur le rapport du
sujet au bord : c'est un goût du cadrage.

### 8.2 Le VLM comme juge ou comme critique

- **Jiang & Chen (2025)**, « Multimodal LLMs Can Reason about Aesthetics in Zero-Shot », ACM
  Multimedia 2025 (DOI 10.1145/3746027.3754961). Résumé lu : les VLM ont tendance à
  l'« hallucination » dans le jugement esthétique, avec des opinions subjectives et des
  interprétations « unsubstantiated » ; un raisonnement guidé par des preuves visuelles (ArtCoT)
  réduit ce défaut.
- **Yu, Ruiz-Dolz & Yi (2025)**, « A Structured Framework for Evaluating and Enhancing
  Interpretive Capabilities of Multimodal LLMs in Culturally Situated Tasks », *Findings of EMNLP
  2025*, p. 1945-1971. Critique de peinture chinoise traditionnelle par des VLM, comparée à des
  critiques d'experts.
- **Li, Po, Yang et al. (2025)**, « AesBiasBench: Evaluating Bias and Alignment in Multimodal
  Language Models for Personalized Image Aesthetic Assessment », EMNLP 2025 (selon arXiv).
  Résumé lu : donner au modèle l'identité (genre, âge, éducation) de la personne dont il doit
  prédire le goût « often exacerbates bias ».
- **Xiao, Lin & Chiu (2024)**, « Behavioral Bias of Vision-Language Models: A Behavioral Finance
  View », atelier ICML 2024. Résumé lu : biais de récence et d'**autorité** chez plusieurs VLM
  ouverts ; GPT-4o y est peu sensible. **Leçon :** le « biais d'autorité » est un proche parent de
  l'effet d'une marque d'institution.
- **Zheng et al. (2023)**, « Judging LLM-as-a-Judge… », NeurIPS 2023 ; **Koyama et al. (2026)**,
  arXiv 2604.11589 : les modèles juges ont des biais propres (position, longueur, préférence
  pour certains modèles) [détail : contenu non relu].
- **Sclar, Choi, Tsvetkov & Suhr (2024)**, « Quantifying Language Models' Sensitivity to Spurious
  Features in Prompt Design… », ICLR 2024. De petits changements de *mise en forme* de la
  consigne changent beaucoup les scores. **Leçon méthodologique majeure :** l'effet d'un cadre
  doit être plus grand que l'effet d'une virgule dans la consigne. Il faut donc mesurer la
  variabilité due à la consigne *avant* d'interpréter l'effet du cadre.

### 8.3 Prix

La note machines a déjà vérifié Aubry et al. (*Journal of Finance* 2023), Mei, Moses, Waelty &
Yang (2025, arXiv 2512.23078) et Singh et al. (2026, arXiv 2609.17572). On n'a trouvé **aucune
étude** qui demande à un VLM généraliste d'estimer le prix d'une œuvre en faisant varier le cadre,
le mur ou la page (recherche web du 17/10 ; résultat négatif, à confirmer quand le budget de
recherche le permettra).

---

## 9. Segmentation à vocabulaire ouvert : qui décide du bord ?

### 9.1 Les outils

- **Liu, Zeng, Ren et al. (2023)**, « Grounding DINO: Marrying DINO with Grounded Pre-Training for
  Open-Set Object Detection », prépublication arXiv 2303.05499 [publiée à ECCV 2024 : non vérifié].
  Détecteur qui prend un mot et renvoie des boîtes.
- **Minderer, Gritsenko, Stone et al. (2022)**, « Simple Open-Vocabulary Object Detection with
  Vision Transformers » (OWL-ViT), ECCV 2022. Et **Minderer, Gritsenko & Houlsby (2023)**,
  « Scaling Open-Vocabulary Object Detection » (OWLv2), NeurIPS 2023 [lieu : non vérifié sur la
  page]. Les détecteurs « à vocabulaire ouvert » héritent du sens des mots appris par un modèle
  de type CLIP.
- **Kirillov et al. (2023)**, SAM (voir note machines). Point utile ici : SAM renvoie **plusieurs
  masques** pour un même clic, parce qu'un point peut désigner un tout, une partie ou une
  sous-partie [contenu non relu dans le texte cette fois ; connu de l'article]. Le modèle est donc
  *conçu* pour l'ambiguïté « toile / tableau encadré / mur ».
- **Ravi, Gabeur, Hu et al. (2024)**, « SAM 2: Segment Anything in Images and Videos »,
  prépublication arXiv 2408.00714 [publié à ICLR 2025 : non vérifié].
- **Carion et al. (2025-2026)**, « SAM 3: Segment Anything with Concepts » (voir note machines).
  Le *concept* est donné par un mot ; une « tête de présence » décide si le concept est là.

### 9.2 L'ambiguïté des concepts

- **Gupta, Dollár & Girshick (2019)**, LVIS, CVPR 2019. Avec plus de mille catégories, les catégories se
  recouvrent (un objet peut être deux choses à la fois) ; les auteurs adaptent l'annotation et
  l'évaluation pour en tenir compte [détail : contenu non relu].

**Ce que cela dit du pilote (d).** Si SAM 3 met le bord de « painting » sur la toile et celui de
« artwork » sur le cadre, ce n'est pas un défaut de segmentation. C'est une **extension de
concept** apprise des légendes du web : « painting » y désigne souvent l'image peinte (une
reproduction sans cadre), « artwork » l'objet exposé. Le segmenteur rend visible une frontière
*conceptuelle* que les humains négocient sans y penser. Deux réserves : (1) un seul couple de mots
ne fait pas une théorie ; il faut une gamme de mots (« canvas », « framed painting »,
« picture », « object », « tableau ») et plusieurs langues ; (2) il faut vérifier que le résultat
ne dépend pas du seuil de confiance ni de la taille de l'image.

### 9.3 Détecter le support : page, marge, bord de film

- **dhSegment** (Oliveira, Seguin & Kaplan, ICFHR 2018) et **PageNet** (Tensmeyer et al., 2017) :
  extraire la page d'une photo de document.
- **Arnold & Tilton (2026)** (voir note machines) : des YOLOv8 par support (négatif, tirage,
  carton de montage) ; le cadre y est un bruit à retirer.

**Leçon :** dans la tradition documentaire, trouver le support est une *tâche en soi*, entraînée
exprès. Les modèles généralistes ne l'apprennent pas. Pour eux, le bord du négatif (pilote c)
peut être soit invisible, soit vu mais jugé sans importance. **On ne sait pas lequel** tant qu'on
n'a pas fait le test de la section 10 (« le modèle sait-il qu'il y a un bord ? »).

---

## 10. Comment savoir ce qu'un modèle « fait » d'un élément de l'image

C'est le cœur du volet. Il y a quatre familles de méthodes, de la plus extérieure à la plus
intérieure. Aucune ne suffit seule.

### 10.1 Le comportement : interventions contrefactuelles

**Principe.** On change *un seul* élément de l'image et on mesure la réponse. C'est l'équivalent
de l'expérience contrôlée en psychologie.

- **Lapuschkin et al. (2019)**, section 4.2 : enlever la marque, la recoller ailleurs.
- **Xiao et al. (2021)**, section 3.3 : objet seul, fond seul, objet sur autre fond.
- **Goyal et al. (2019)**, « Counterfactual Visual Explanations ». On cherche la plus petite région à échanger avec une
  autre image pour que la décision change.
- **Howard et al. (2024)**, « SocialCounterfactuals », CVPR 2024. Des images générées qui ne diffèrent que par un attribut (genre, origine) pour mesurer
  les biais d'un VLM. **C'est le gabarit à copier pour les cadres** : un jeu d'images qui ne
  diffèrent que par le cadre.
- **Geirhos et al. (2019)**, conflit d'indices (section 4.3).

**Forces.** C'est la seule méthode qui établit un **effet causal** de l'élément sur la réponse.
Elle marche aussi sur les modèles fermés (GPT, Gemini, Claude), qu'on ne peut pas ouvrir.

**Limites.** (1) Modifier l'image crée des **artefacts** (bords de collage, lumière incohérente) ;
le modèle peut réagir à l'artefact et non au cadre. Il faut des contrôles : un « faux cadre »
(une bande de même couleur, même surface, sans moulure), un collage sans cadre. (2) On mesure un
effet sur *une* tâche ; un autre libellé de question peut donner un autre effet (Sclar et al.).
(3) Un effet n'est pas une explication : il dit *que* le cadre compte, pas *comment*.

### 10.2 L'attribution : les cartes de chaleur et leurs limites

**Principe.** Une carte colore les pixels selon leur « importance » pour la réponse.

- **Grad-CAM** (Selvaraju et al., ICCV 2017 ; *IJCV* 2019) : carte tirée des gradients du réseau.
- **SHAP** (Lundberg & Lee, NIPS 2017) : attribue à chaque élément sa part de la décision.
- **Perturbation** (Fong & Vedaldi, ICCV 2017) : le plus petit masque qui détruit la décision.

**Limites établies.**
- **Adebayo et al. (2018)**, « Sanity Checks for Saliency Maps », NeurIPS 2018. Résumé lu : certaines méthodes produisent des cartes « independent both
  of the model and of the data » ; elles ressemblent à de la détection de contours.
- **Kindermans et al. (2017)**, « The (Un)reliability of saliency methods ». **Hooker et al.
  (2019)**, ROAR, NeurIPS 2019. Résumé lu : beaucoup de méthodes ne font « not better
  than a random designation of feature importance ».

**Leçon pour nous.** Une carte qui « allume » le cadre doré ne prouve pas que le cadre commande
le prix. Le cadre est un contour très contrasté : certaines méthodes l'allumeront de toute façon.
Mei et al. (2025) utilisent Grad-CAM pour dire que leur modèle regarde « la composition » : c'est
une *indication*, pas une preuve. Les cartes servent à **formuler** des hypothèses (comme chez
Lapuschkin) ; l'intervention sert à les **tester**.

### 10.3 Les représentations : sondes, concepts, autoencodeurs

**Principe.** On ouvre le modèle et l'on regarde les nombres intermédiaires.

- **Sondes (probing).** **Alain & Bengio (2016)**. On entraîne un petit classifieur
  sur les représentations : « y a-t-il un cadre ? ». S'il réussit, l'information est *présente*.
  **Limite essentielle** (**Belinkov 2022**, *Computational Linguistics* 48(1)) : qu'une information soit *lisible* par la sonde
  ne prouve pas que le modèle *s'en sert*. La sonde peut apprendre elle-même la tâche.
- **Concepts (TCAV).** **Kim et al. (2018)**, ICML 2018. On
  définit un concept par des exemples (« cadre doré ») et l'on mesure combien la sortie
  (« cher ») est sensible à la direction de ce concept. Utile, mais limité aux modèles ouverts et
  dépendant du choix des exemples.
- **Comparer deux représentations.** **Kornblith et al. (2019)**, CKA, ICML 2019. Permet de dire à quel point la
  représentation d'une œuvre change quand on ajoute le cadre, couche par couche.
- **Unités et concepts.** **Bau et al. (2017)**, « Network Dissection », CVPR 2017 : associe des
  unités internes à des concepts visuels annotés.
- **Décomposer CLIP.** **Gandelsman, Efros & Steinhardt (2024)**, ICLR 2024 [lieu non vérifié].
  Résumé lu : la représentation est une somme sur les **morceaux d'image** (patches), les couches
  et les « têtes d'attention » ; certaines têtes ont des rôles lisibles (lieu, forme) ; on peut
  retirer des traits parasites. **Pour nous :** on peut mesurer directement quelle part de la
  représentation vient des morceaux qui couvrent le cadre. C'est l'outil le plus direct
  disponible sur un modèle ouvert.
- **Autoencodeurs parcimonieux (SAE).** Un SAE est un petit réseau qui réécrit la représentation
  comme une somme de quelques « traits » choisis dans un grand dictionnaire, souvent plus
  lisibles. Langage : **Cunningham et al. (2023)**. Vision : **Rao et al. (2024)**,
  « Discover-then-Name », ECCV 2024 (SAE sur CLIP) ; **Lim et al. (2025)**, ICLR 2025 ;
  **Stevens et al. (2025)**. Résumé lu de Stevens et al. : chaque trait a des exemples
  réels *et* un vecteur qu'on peut **manipuler** pour voir son effet, ce qui permet des
  « patch-level causal edits ». **Pour nous :** chercher s'il existe un trait « cadre doré » ou
  « mur de musée » dans un CLIP ou un DINOv2, puis l'**éteindre** et voir si le jugement change.
- **Circuits.** **Olah et al. (2020)**, « Zoom In: An Introduction to Circuits », *Distill* :
  retrouver des « circuits » d'unités qui calculent quelque chose de précis. Très coûteux ;
  irréaliste sur un grand VLM dans le cadre de ce projet.

### 10.4 Les interventions internes : la médiation causale

**Principe.** On remplace une partie des calculs internes pour une image (avec cadre) par ceux
d'une autre image (sans cadre), et on regarde si la sortie suit. C'est l'*activation patching*.

- **Zhang & Nanda (2024)**, ICLR 2024 : bonnes pratiques et pièges.
- **Geiger et al. (2021)**, « Causal Abstractions of Neural Networks », NeurIPS 2021. Cadre théorique : un modèle « implémente » une hypothèse si l'on peut aligner ses variables
  internes sur celles de l'hypothèse, interventions comprises.
- **Neo et al. (2025)**, ICLR 2025. Résumé lu : dans LLaVA, retirer les
  « jetons » visuels propres à l'objet fait chuter l'identification de plus de 70 %. **Pour
  nous :** on peut retirer les jetons qui correspondent au cadre et voir si la réponse « valeur »
  bouge, *sans toucher l'image*. Cela évite les artefacts de collage (10.1).
- **Golovanevsky et al. (2024)**, « What Do VLMs NOTICE? ». Résumé lu : des **paires minimales sémantiques**
  d'images pour faire de la médiation causale proprement.

**Limite commune.** Ces méthodes demandent un modèle *ouvert* (LLaVA, Qwen-VL, Idefics) ; elles
ne disent rien directement de GPT-4o ou Gemini. Il faut donc reproduire l'effet comportemental
sur un modèle ouvert avant de l'ouvrir.

### 10.5 Ce que le modèle dit de lui-même ne compte pas comme preuve

- **Turpin et al. (2023)**, « Language Models Don't Always Say What They Think », NeurIPS 2023.
  Résumé lu : on biaise le
  modèle par un indice caché ; il change de réponse et **ne mentionne pas** l'indice dans son
  explication, il rationalise.
- **Jacovi & Goldberg (2020)**, ACL 2020. Distingue une explication *plausible* d'une
  explication *fidèle* au calcul réel.

**Leçon.** Demander à Gemini « avez-vous tenu compte du cadre ? » donne une réponse plausible,
pas un témoignage. Quand un VLM dit qu'un cadre est « ironique » autour d'un ticket (cf. état
des lieux), c'est une **donnée** sur ce qu'il produit, pas une preuve de ce qui l'a fait produire.

### 10.6 La psychophysique des modèles

**Principe.** Étudier un modèle comme un sujet d'expérience : stimuli contrôlés, répétitions,
statistiques, comparaison avec des humains.

- **Rahwan et al. (2019)**, « Machine behaviour », *Nature* 568. Programme fondateur : étudier les machines comme on étudie le comportement animal, avec ses
  méthodes (observation, expérience, variation des conditions).
- **Ritter et al. (2017)**, section 4.3.
- **Binz & Schulz (2023)**, *PNAS* 120(6). Des tâches classiques de psychologie (vignettes de décision, raisonnement causal)
  posées au modèle.
- **Schulze Buschoff et al. (2025)**, *Nature Machine Intelligence*. Résumé lu :
  expériences contrôlées sur la physique intuitive, la causalité et la psychologie intuitive ;
  les VLM restent en deçà des humains.
- **Geirhos et al. (2021)**, « Partial success… », NeurIPS 2021 : comparaison humains / modèles
  avec un **accord au niveau de l'essai** (le modèle se trompe-t-il sur les *mêmes* images que
  l'humain ?). Synthèse : **Wichmann & Geirhos (2023)**, *Annual Review of Vision Science* 9.
- **Firestone (2020)**, *PNAS* 117(43) : un échec peut venir des *conditions* du test
  (performance) et non d'une incapacité (compétence) ; il faut des conditions comparables.
- **Bowers et al. (2023)**, *Behavioral and Brain Sciences* 46, e385 : de bons scores ne montrent
  pas qu'un modèle *fonctionne* comme l'humain ; il faut manipuler des facteurs. **Mitchell &
  Krakauer (2023)**, *PNAS* 120(13) : prudence avec le mot « comprendre ».

**Leçon.** « Traverser » et « lire » sont des mots de psychologie. Les appliquer à un modèle
exige les standards de la psychologie expérimentale : prédictions faites *avant*, stimuli
contrôlés, plusieurs modèles et plusieurs tirages, et si possible un groupe humain comparé sur les
mêmes images.

### 10.7 La validité de construit : mesure-t-on ce qu'on croit ?

- **Jacobs & Wallach (2021)**, « Measurement and Fairness », FAccT 2021. Résumé lu : un concept non observable (ici « valeur », « statut
  d'œuvre ») n'est atteint que par une *opérationnalisation* (ici « le prix en dollars donné par
  Gemini ») ; l'écart entre les deux crée des erreurs. Ils proposent de vérifier la **validité**
  (la mesure suit-elle le concept ?) et la **fiabilité** (la mesure est-elle stable ?).
- **Raji et al. (2021)**, « AI and the Everything in the Whole Wide World Benchmark ». Un banc d'essai étroit est souvent
  présenté comme une mesure générale.
- **Salaudeen et al. (2025)**, « Measurement to Meaning » : un cadre d'évaluation centré sur la
  validité.

**Leçon pour nous.** « Le prix estimé par un VLM » n'est pas « la valeur que le modèle attribue
à l'œuvre ». Il dépend de la consigne, de la devise, de la tendance du modèle à refuser, de son
ancrage sur des nombres ronds. Avant de dire « le cadre fait monter la valeur », il faut montrer
que la mesure (le prix) bouge aussi avec des facteurs dont on *sait* qu'ils comptent (signature
célèbre, mention « copie », état de conservation). C'est la **validité convergente**. Et qu'elle
ne bouge pas avec des facteurs sans rapport (couleur du fond gris, rotation de 2°). C'est la
**validité discriminante**.

### 10.8 Pourquoi une absence de différence ne suffit pas

Le pilote (c) dit : le bord du négatif ne change pas la lecture. Il est tentant d'en conclure que
« le modèle traverse le support ». Six raisons de ne pas le faire.

1. **Absence de preuve n'est pas preuve d'absence.** **Altman & Bland (1995)**, *BMJ* 311. Un test non
   significatif sur peu d'images dit seulement qu'on n'a pas vu d'effet.
2. **Il faut un test d'équivalence.** **Lakens (2017)**, « Equivalence Tests ». On fixe d'avance une **marge** (par
   exemple : « une différence de moins de 5 % du prix est négligeable ») et l'on montre que
   l'intervalle de confiance tient *dans* la marge. Sans marge fixée d'avance, « pas de
   différence » n'a pas de sens.
3. **Cécité ou traversée ?** Si le modèle n'a jamais *perçu* le bord (trop fin, coupé par le
   recadrage central, écrasé par la réduction à 224 pixels), son invariance ne dit rien. Il faut
   d'abord prouver qu'il le voit : lui demander de le décrire, ou sonder sa représentation
   (10.3). « Traverser » suppose « voir ». Un modèle aveugle au bord n'est pas « au-delà » du
   support ; il est en deçà.
4. **Plafond.** Si la tâche est trop facile (le modèle reconnaît l'image à coup sûr), la réponse
   est saturée ; aucun indice ne peut la déplacer (section 7.3). Il faut des cas ambigus, où un
   indice *pourrait* compter.
5. **Effets qui s'annulent.** Le bord peut tirer la lecture vers « archive ancienne » sur
   certaines images et vers « photo amateur » sur d'autres ; la moyenne ne bouge pas. Il faut
   regarder la **distribution** des changements, image par image, pas seulement la moyenne
   (même logique que les groupes de Waterbirds).
6. **Présent n'est pas utilisé, et inversement.** Le modèle peut garder l'information « bord de
   film » dans sa représentation sans s'en servir pour *cette* question, et s'en servir pour une
   autre (« de quand date cette photo ? »). Il faut varier les questions. Hermann et al. (2024)
   montrent que l'usage d'un indice dépend de sa disponibilité *et* de son utilité pour la tâche.

### 10.9 Définitions opérationnelles : traverser, lire, être aveugle, être confondu

À partir de tout ce qui précède, voici des définitions **testables** (proposition de cette revue,
pas des auteurs cités).

- **Aveugle au support** : le modèle ne peut pas dire qu'il y a un cadre / un bord quand on le lui
  demande, et une sonde ne le retrouve pas dans sa représentation.
- **Traverse le support** : il *voit* le support (critère précédent passé) ; *et* ses réponses sur
  le contenu sont **équivalentes** avec et sans support (test d'équivalence, marge fixée
  d'avance) ; *et* cela tient pour plusieurs questions et dans des cas ambigus (pas de plafond).
- **Lit le support comme message** : il voit le support ; ses réponses changent de façon
  **systématique** ; le sens du changement suit la **convention culturelle** (cadre doré → plus
  ancien, plus cher, plus « musée » ; carton de montage → archive) ; l'effet suit une
  **gradation** (plus le cadre est riche, plus l'effet est fort) ; il disparaît quand on garde la
  forme mais retire le sens (même surface, même couleur, sans moulure : « faux cadre ») ; et,
  sur un modèle ouvert, il passe par une **voie interne identifiable** (trait SAE, tête
  d'attention, jetons visuels du cadre) dont la suppression supprime l'effet.
- **Confondu** : la réponse change, mais l'effet s'explique par un facteur non sémantique
  (taille de l'œuvre dans l'image, recadrage, contraste, compression) ; il persiste avec un faux
  cadre.

La distinction entre « lire » et « être confondu » est le point qui manque à toute la
littérature. Les études de robustesse demandent seulement : *la sortie change-t-elle ?* Elles ne
demandent pas : *change-t-elle dans le sens d'une convention ?* C'est là que la thèse de Marcel
peut apporter un critère nouveau : **un effet de support est une « lecture » s'il est prédit par
la sémiotique du support (Simmel, Bateson, Genette) et non par ses propriétés optiques.**

---

## 11. Ce qui est établi

1. **Le contexte agit sur la reconnaissance**, chez l'humain (Biederman, Davenport & Potter, Bar,
   Oliva & Torralba) comme chez la machine (Torralba, Divvala, Zhu, Xiao). Chez la machine, plus
   fortement, et parfois à la place de l'objet.
2. **Les modèles prennent des raccourcis vers des marques d'institution** placées dans l'image :
   mention de source (Lapuschkin), jeton métallique d'hôpital (Zech), marques de bord (DeGrave).
   Ces cas sont structurellement identiques à une mire ou une marque de musée.
3. **Le bord de l'image est un canal d'influence** : une bordure de pixels suffit à tromper un
   classifieur (Zolna) ou à l'adapter à une tâche (Bahng) ; un cercle rouge dirige un VLM
   (Shtedritski).
4. **Les VLM lisent le texte dans l'image** et peuvent en être trompés (Goh, Materzynska, Cheng,
   Qraitem).
5. **Les VLM répondent par leur savoir quand ils reconnaissent**, et par les indices visuels
   quand ils ne reconnaissent pas (Goyal 2017, Agrawal, Vo, Mei). Notre pilote (a) suit ce schéma.
6. **Le support est traité comme un « domaine » dont il faut se libérer** (PACS, DomainNet,
   ImageNet-R) ; la peinture y est un domaine parmi d'autres.
7. **Les cartes de chaleur ne prouvent rien seules** (Adebayo, Kindermans, Hooker) ; **les
   explications des modèles ne sont pas fidèles** (Turpin).
8. **Les méthodes causales existent** : interventions contrefactuelles, conflit d'indices,
   ablation de jetons, médiation causale, autoencodeurs manipulables. Elles n'ont jamais été
   appliquées au cadre d'une œuvre.

## 12. Ce qui manque

1. **Aucune étude sur le cadre physique d'une œuvre comme variable** pour un modèle de vision ou
   un VLM : ni pour la reconnaissance, ni pour le jugement, ni pour le prix.
2. **Aucun critère publié pour distinguer « lecture » et « confusion »** : la robustesse mesure
   le changement, pas son sens.
3. **Aucun test d'équivalence** dans les études d'invariance : on y lit « pas d'effet » sans
   marge fixée d'avance.
4. **Aucune étude de l'extension des concepts « painting », « artwork », « picture »** dans les
   segmenteurs à vocabulaire ouvert.
5. **Aucune comparaison humains / machines sur les mêmes images encadrées.** Les protocoles
   humains existent (Kirk, Brieber) ; le pendant machine manque.
6. **Rien sur l'extension des limites (Intraub) face à un cadre peint** ; ni chez l'humain (à
   confirmer, recherche interrompue), ni chez la machine.
7. **Pistes non vérifiées faute de budget de recherche** : études récentes (2025-2026) sur les
   VLM et l'attribution d'œuvres en fonction de l'étiquette (« attribué à », « atelier de ») ;
   travaux sur l'ancrage numérique des LLM dans les estimations de prix ; SAE appliqués à des
   images d'art. À reprendre.

---

## 13. Cinq protocoles concrets

Chaque protocole est conçu pour être faisable sur nos moyens (Mac 16 Go, API Gemini, modèles
ouverts petits), avec préenregistrement des prédictions et des marges.

### Protocole 1 — Conflit d'indices cadre / contenu (comportemental, modèles fermés et ouverts)

**Dispositif.** Grille 2 × 2 × 3. Contenu : œuvre reconnue / objet banal de même format. Cadre :
riche (rocaille doré) / pauvre (baguette noire) / aucun. Plus un **faux cadre** (bande unie de
même surface, même couleur moyenne, sans moulure). La surface occupée par le contenu est
**identique** dans toutes les versions (on agrandit l'image, pas on réduit l'œuvre). Questions :
prix, date, « œuvre de musée ? » (oui / non), description libre. Cinq formulations par
question, plusieurs tirages, trois VLM au moins, et cinquante paires au moins par case.

**Conclusion possible.** Si le cadre riche fait monter le prix de l'objet banal **plus** que le
faux cadre, et pas celui de l'œuvre reconnue, on a un effet de cadre **sémantique** et
**conditionnel à la reconnaissance**, distinct d'un effet de surface ou de couleur.

**Limites.** Un montage reste un montage (artefacts). Le prix est une mesure fragile (10.7) :
il faut vérifier sa validité convergente (signature célèbre ajoutée → hausse attendue). Un modèle
fermé peut changer d'une version à l'autre : dater chaque appel.

### Protocole 2 — Retirer, remplacer, transplanter la marque d'institution (comportemental, à la Lapuschkin)

**Dispositif.** Photos de musée avec mire ou marque. Quatre versions : originale ; marque
**effacée** (remplie par le fond) ; marque **remplacée** par celle d'une autre institution
(prestige différent) ; marque **transplantée** sur une photo d'amateur du même objet. Questions :
provenance, authenticité (« original ou reproduction ? »), date, prix.

**Conclusion possible.** Si la marque transplantée fait passer une photo d'amateur pour une
« pièce de musée », la marque fonctionne comme **certificat** (raccourci au sens de Geirhos).
Si la marque remplacée change le prix selon le prestige de l'institution, le modèle lit un
**message institutionnel**, pas une simple étiquette.

**Limites.** L'effacement laisse des traces ; prévoir un contrôle « effacement d'une zone vide de
même taille ». Lire le nom d'une institution (OCR) et en déduire un prestige sont deux étapes ;
le protocole ne dit pas laquelle cède. Le Protocole 4 peut séparer les deux sur un modèle ouvert.

### Protocole 3 — Voir avant de traverser : le test du bord en trois temps (pour le pilote c)

**Dispositif.** Négatifs et tirages avec et sans bord de film ou carton. (i) **Détection** : « y
a-t-il un bord de film ? quel type ? » (le modèle voit-il le support ?). (ii) **Invariance** :
mêmes questions de contenu avec et sans bord ; test d'**équivalence** avec une marge fixée
d'avance. (iii) **Usage** : questions où le support *devrait* compter (« ceci est-il un négatif
ou un tirage ? », « de quelle décennie ? »). On ajoute des cas **ambigus** (images floues, sujets
peu reconnaissables) pour éviter le plafond.

**Conclusion possible.** Bord vu + contenu équivalent + bord utilisé quand c'est pertinent =
**traversée sélective** (le modèle sait quand le support compte). Bord non vu = **cécité** :
l'invariance ne veut rien dire. Bord vu + utilisé partout = **lecture** (ou confusion, à trancher
par le faux bord).

**Limites.** La réponse à (i) est verbale et peut être fausse sans que la perception le soit ;
compléter par une sonde sur un modèle ouvert (Protocole 4). Le recadrage interne des modèles
fermés est inconnu : le bord peut être coupé avant le calcul.

### Protocole 4 — Ouvrir un modèle : jetons du cadre, traits SAE, patching (mécaniste, modèle ouvert)

**Dispositif.** Reproduire d'abord l'effet du Protocole 1 sur un VLM ouvert (LLaVA ou Qwen-VL de
petite taille). Puis : (a) **ablation de jetons** : retirer les jetons visuels qui couvrent le
cadre, garder l'image (à la Neo et al.) ; (b) **patching** : remplacer les activations de l'image
encadrée par celles de l'image non encadrée, couche par couche (Zhang & Nanda) ; (c) côté
encodeur, **décomposition de Gandelsman** (part de la représentation venant des morceaux du
cadre) et **SAE** (chercher un trait « cadre doré », l'éteindre, voir l'effet, à la Stevens et
al.).

**Conclusion possible.** Si l'effet du cadre sur le prix disparaît quand on retire ses jetons ou
qu'on éteint un trait précis, on a une **voie causale interne** : le cadre est utilisé, et l'on
sait où. Si l'effet subsiste, il passe ailleurs (par exemple par une impression globale de
« photo de musée »).

**Limites.** Coûteux en calcul (respecter la limite de deux calculs lourds en parallèle sur le
Mac). Ne dit rien des modèles fermés. Les traits SAE ne sont pas toujours lisibles ; un trait
« cadre » peut aussi coder « or » ou « ornement ».

### Protocole 5 — Extension des concepts de segmentation (segmenteurs à vocabulaire ouvert)

**Dispositif.** Sur des photos de salle et de catalogue (YCBA, Met), demander à SAM 3, Grounding
DINO et OWLv2 une douzaine de mots : « painting », « artwork », « framed painting », « canvas »,
« picture », « frame », « print », « sheet of paper », « object », et leurs équivalents en
français et en allemand. Pour chaque mot, mesurer où passe le bord : sur la toile, sur le cadre,
sur le passe-partout, sur la feuille. Faire varier le seuil de confiance et la résolution.
Comparer à une annotation humaine (trois annotateurs, même consigne).

**Conclusion possible.** Une **carte de l'extension** de chaque mot pour chaque outil : quel mot
« inclut » le cadre, lequel l'« exclut », et si cela suit l'usage humain. Si « artwork » inclut le
cadre et « painting » non, de façon stable et chez plusieurs outils, c'est une frontière
conceptuelle apprise des légendes du web, et non un hasard de seuil.

**Limites.** Ne dit pas *pourquoi* (données d'entraînement non publiques). Dépend des seuils.
Les mots composés (« framed painting ») peuvent être mal compris par l'encodeur de texte. Le
résultat porte sur des outils, pas sur « la machine » en général.

---

## Bibliographie

*Une ligne par référence. « (note machines) » = vérifiée dans `../litt-cadrage-ia-machines.md`.
Les autres ont été ouvertes le 17/10/2026 (page arXiv, notice Crossref, page des actes ou texte).*

**Sciences cognitives et psychologie**
- Altman, D. G. & Bland, J. M. (1995). Statistics notes: Absence of evidence is not evidence of absence. *BMJ* 311, 485. https://doi.org/10.1136/bmj.311.7003.485
- Bainbridge, W. A. & Baker, C. I. (2020). Boundaries Extend and Contract in Scene Memory Depending on Image Properties. *Current Biology* 30(3), 537-543. https://doi.org/10.1016/j.cub.2019.12.004
- Bar, M. (2004). Visual objects in context. *Nature Reviews Neuroscience* 5, 617-629. https://doi.org/10.1038/nrn1476
- Biederman, I., Mezzanotte, R. J. & Rabinowitz, J. C. (1982). Scene perception: Detecting and judging objects undergoing relational violations. *Cognitive Psychology* 14(2), 143-177. https://doi.org/10.1016/0010-0285(82)90007-X
- Binz, M. & Schulz, E. (2023). Using cognitive psychology to understand GPT-3. *PNAS* 120(6), e2218523120. https://doi.org/10.1073/pnas.2218523120
- Bowers, J. S., Malhotra, G., Dujmović, M. et al. (2023). Deep problems with neural network models of human vision. *Behavioral and Brain Sciences* 46, e385. https://doi.org/10.1017/S0140525X22002813
- Brieber, D., Nadal, M. & Leder, H. (2015). In the white cube: Museum context enhances the valuation and memory of art. *Acta Psychologica* 154, 36-42. https://doi.org/10.1016/j.actpsy.2014.11.004
- Davenport, J. L. & Potter, M. C. (2004). Scene Consistency in Object and Background Perception. *Psychological Science* 15(8), 559-564. https://doi.org/10.1111/j.0956-7976.2004.00719.x
- Firestone, C. (2020). Performance vs. competence in human–machine comparisons. *PNAS* 117(43), 26562-26571. https://doi.org/10.1073/pnas.1905334117
- Intraub, H. & Richardson, M. (1989). Wide-angle memories of close-up scenes. *JEP: Learning, Memory, and Cognition* 15(2), 179-187. https://doi.org/10.1037/0278-7393.15.2.179
- Itti, L., Koch, C. & Niebur, E. (1998). A model of saliency-based visual attention for rapid scene analysis. *IEEE TPAMI* 20(11), 1254-1259. https://doi.org/10.1109/34.730558
- Kirk, U., Skov, M., Hulme, O., Christensen, M. S. & Zeki, S. (2009). Modulation of aesthetic value by semantic context: An fMRI study. *NeuroImage* 44(3), 1125-1132. https://doi.org/10.1016/j.neuroimage.2008.10.009
- Lakens, D. (2017). Equivalence Tests. *Social Psychological and Personality Science* 8(4), 355-362. https://doi.org/10.1177/1948550617697177
- Millet, K., Buehler, F., Du, G. & Kokkoris, M. D. (2023). Defending humankind: Anthropocentric bias in the appreciation of AI art. *Computers in Human Behavior* 143, 107707. https://doi.org/10.1016/j.chb.2023.107707
- Mitchell, M. & Krakauer, D. C. (2023). The debate over understanding in AI's large language models. *PNAS* 120(13). https://doi.org/10.1073/pnas.2215907120
- Oliva, A. & Torralba, A. (2007). The role of context in object recognition. *Trends in Cognitive Sciences* 11(12), 520-527. https://doi.org/10.1016/j.tics.2007.09.009
- Rahwan, I., Cebrian, M., Obradovich, N. et al. (2019). Machine behaviour. *Nature* 568, 477-486. https://doi.org/10.1038/s41586-019-1138-y
- Schulze Buschoff, L. M., Akata, E., Bethge, M. & Schulz, E. (2025). Visual cognition in multimodal large language models. *Nature Machine Intelligence*. https://doi.org/10.1038/s42256-024-00963-y ; https://arxiv.org/abs/2311.16093
- Tatler, B. W. (2007). The central fixation bias in scene viewing. *Journal of Vision* 7(14), 4. https://doi.org/10.1167/7.14.4
- Wichmann, F. A. & Geirhos, R. (2023). Are Deep Neural Networks Adequate Behavioral Models of Human Visual Perception? *Annual Review of Vision Science* 9, 501-524. https://doi.org/10.1146/annurev-vision-120522-031739

**Contexte, fond, biais de jeux de données**
- Barbu, A., Mayo, D., Alverio, J. et al. (2019). ObjectNet: A large-scale bias-controlled dataset for pushing the limits of object recognition models. NeurIPS 2019, 9448-9458. https://papers.nips.cc/paper/2019/hash/97af07a14cacba681feacf3012730892-Abstract.html
- Beery, S., Van Horn, G. & Perona, P. (2018). Recognition in Terra Incognita. ECCV 2018. https://arxiv.org/abs/1807.04975
- Beyer, L., Hénaff, O. J., Kolesnikov, A., Zhai, X. & van den Oord, A. (2020). Are we done with ImageNet? arXiv. https://arxiv.org/abs/2006.07159
- Divvala, S. K., Hoiem, D., Hays, J. H., Efros, A. A. & Hebert, M. (2009). An empirical study of context in object detection. CVPR 2009, 1271-1278. https://doi.org/10.1109/CVPR.2009.5206532
- Li, X., Chen, Y., Zhu, Y., Wang, S., Zhang, R. & Xue, H. (2023). ImageNet-E: Benchmarking Neural Network Robustness via Attribute Editing. CVPR 2023. https://arxiv.org/abs/2303.17096
- Moayeri, M., Pope, P., Balaji, Y. & Feizi, S. (2022). A Comprehensive Study of Image Classification Model Sensitivity to Foregrounds, Backgrounds, and Visual Attributes. CVPR 2022 [lieu non vérifié]. https://arxiv.org/abs/2201.10766
- Rosenfeld, A., Zemel, R. & Tsotsos, J. K. (2018). The Elephant in the Room. arXiv. https://arxiv.org/abs/1808.03305
- Sagawa, S., Koh, P. W., Hashimoto, T. B. & Liang, P. (2020). Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization. ICLR 2020 [lieu non vérifié sur la page]. https://arxiv.org/abs/1911.08731
- Shetty, R., Schiele, B. & Fritz, M. (2019). Not Using the Car to See the Sidewalk — Quantifying and Controlling the Effects of Context in Classification and Segmentation. CVPR 2019. https://doi.org/10.1109/CVPR.2019.00841
- Torralba, A. (2003). Contextual Priming for Object Detection. *IJCV* 53(2), 169-191. https://doi.org/10.1023/A:1023052124951
- Torralba, A. & Efros, A. A. (2011). Unbiased look at dataset bias. CVPR 2011, 1521-1528. https://doi.org/10.1109/CVPR.2011.5995347
- Tsipras, D., Santurkar, S., Engstrom, L., Ilyas, A. & Mądry, A. (2020). From ImageNet to Image Classification: Contextualizing Progress on Benchmarks. ICML 2020 [lieu non vérifié]. https://arxiv.org/abs/2005.11295
- Xiao, K., Engstrom, L., Ilyas, A. & Mądry, A. (2021). Noise or Signal: The Role of Image Backgrounds in Object Recognition. ICLR 2021. https://arxiv.org/abs/2006.09994
- Zhang, C., Pan, F., Kim, J., Kweon, I. S. & Mao, C. (2024). ImageNet-D: Benchmarking Neural Network Robustness on Diffusion Synthetic Object. CVPR 2024. https://arxiv.org/abs/2403.18775
- Zhu, Z., Xie, L. & Yuille, A. L. (2017). Object Recognition with and without Objects. IJCAI 2017. https://arxiv.org/abs/1611.06596

**Raccourcis**
- DeGrave, A. J., Janizek, J. D. & Lee, S.-I. (2021). AI for radiographic COVID-19 detection selects shortcuts over signal. *Nature Machine Intelligence* 3, 610-619. https://doi.org/10.1038/s42256-021-00338-7
- Geirhos, R., Jacobsen, J.-H., Michaelis, C., Zemel, R., Brendel, W., Bethge, M. & Wichmann, F. A. (2020). Shortcut learning in deep neural networks. *Nature Machine Intelligence* 2, 665-673. https://doi.org/10.1038/s42256-020-00257-z
- Geirhos, R., Rubisch, P., Michaelis, C., Bethge, M., Wichmann, F. A. & Brendel, W. (2019). ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness. ICLR 2019. https://arxiv.org/abs/1811.12231
- Geirhos, R., Narayanappa, K., Mitzkus, B. et al. (2021). Partial success in closing the gap between human and machine vision. NeurIPS 2021. https://arxiv.org/abs/2106.07411
- Hermann, K. L. & Lampinen, A. K. (2020). What shapes feature representations? Exploring datasets, architectures, and training. arXiv [NeurIPS 2020 : non vérifié]. https://arxiv.org/abs/2006.12433
- Hermann, K. L., Mobahi, H., Fel, T. & Mozer, M. C. (2024). On the Foundations of Shortcut Learning. ICLR 2024. https://arxiv.org/abs/2310.16228
- Lapuschkin, S., Wäldchen, S., Binder, A., Montavon, G., Samek, W. & Müller, K.-R. (2019). Unmasking Clever Hans Predictors and Assessing What Machines Really Learn. *Nature Communications* 10. https://doi.org/10.1038/s41467-019-08987-4 ; https://arxiv.org/abs/1902.10178
- Ritter, S., Barrett, D. G. T., Santoro, A. & Botvinick, M. M. (2017). Cognitive Psychology for Deep Neural Networks: A Shape Bias Case Study. ICML 2017. https://arxiv.org/abs/1706.08606
- Zech, J. R., Badgeley, M. A., Liu, M., Costa, A. B., Titano, J. J. & Oermann, E. K. (2018). Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs. *PLOS Medicine* 15(11), e1002683. https://doi.org/10.1371/journal.pmed.1002683

**Domaines et robustesse**
- Fang, A., Ilharco, G., Wortsman, M. et al. (2022). Data Determines Distributional Robustness in Contrastive Language Image Pre-training (CLIP). ICML 2022 [lieu non vérifié]. https://arxiv.org/abs/2205.01397
- Hendrycks, D. & Dietterich, T. (2019). Benchmarking Neural Network Robustness to Common Corruptions and Perturbations. ICLR 2019. https://arxiv.org/abs/1903.12261
- Hendrycks, D., Basart, S., Mu, N. et al. (2021). The Many Faces of Robustness: A Critical Analysis of Out-of-Distribution Generalization. ICCV 2021. https://arxiv.org/abs/2006.16241
- Li, D., Yang, Y., Song, Y.-Z. & Hospedales, T. M. (2017). Deeper, Broader and Artier Domain Generalization. ICCV 2017. https://arxiv.org/abs/1710.03077
- Peng, X., Bai, Q., Xia, X., Huang, Z., Saenko, K. & Wang, B. (2019). Moment Matching for Multi-Source Domain Adaptation. ICCV 2019. https://arxiv.org/abs/1812.01754
- Recht, B., Roelofs, R., Schmidt, L. & Shankar, V. (2019). Do ImageNet Classifiers Generalize to ImageNet? ICML 2019 [lieu non vérifié]. https://arxiv.org/abs/1902.10811
- Wang, H., Ge, S., Xing, E. P. & Lipton, Z. C. (2019). Learning Robust Global Representations by Penalizing Local Predictive Power. NeurIPS 2019. https://arxiv.org/abs/1905.13549

**VLM : texte, marques, a priori**
- Agrawal, A., Batra, D., Parikh, D. & Kembhavi, A. (2018). Don't Just Assume; Look and Answer: Overcoming Priors for Visual Question Answering. CVPR 2018. https://arxiv.org/abs/1712.00377
- Cheng, H., Xiao, E., Gu, J. et al. (2024). Unveiling Typographic Deceptions: Insights of the Typographic Vulnerability in Large Vision-Language Model. ECCV 2024. https://arxiv.org/abs/2402.19150
- Goh, G., Cammarata, N., Voss, C. et al. (2021). Multimodal Neurons in Artificial Neural Networks. *Distill* (note machines). https://distill.pub/2021/multimodal-neurons/
- Goyal, Y., Khot, T., Summers-Stay, D., Batra, D. & Parikh, D. (2017). Making the V in VQA Matter. CVPR 2017 [lieu non vérifié]. https://arxiv.org/abs/1612.00837
- Li, Y., Du, Y., Zhou, K., Wang, J., Zhao, W. X. & Wen, J.-R. (2023). Evaluating Object Hallucination in Large Vision-Language Models. EMNLP 2023. https://arxiv.org/abs/2305.10355
- Liu, Y., Li, Z., Huang, M. et al. (2024). OCRBench: On the Hidden Mystery of OCR in Large Multimodal Models. *Science China Information Sciences*. https://doi.org/10.1007/s11432-024-4235-6 ; https://arxiv.org/abs/2305.07895
- Materzynska, J., Torralba, A. & Bau, D. (2022). Disentangling visual and written concepts in CLIP. CVPR 2022 [lieu non vérifié]. https://arxiv.org/abs/2206.07835
- Qraitem, M., Tasnim, N., Teterwak, P., Saenko, K. & Plummer, B. A. (2024). Vision-LLMs Can Fool Themselves with Self-Generated Typographic Attacks. arXiv. https://arxiv.org/abs/2402.00626
- Rahmanzadehgervi, P., Bolton, L., Taesiri, M. R. & Nguyen, A. T. (2024). Vision language models are blind. arXiv [ACCV 2024 : non vérifié]. https://arxiv.org/abs/2407.06581
- Shtedritski, A., Rupprecht, C. & Vedaldi, A. (2023). What does CLIP know about a red circle? ICCV 2023 (note machines). https://arxiv.org/abs/2304.06712
- Singh, A., Natarajan, V., Shah, M. et al. (2019). Towards VQA Models That Can Read. CVPR 2019. https://arxiv.org/abs/1904.08920
- Tong, S., Liu, Z., Zhai, Y., Ma, Y., LeCun, Y. & Xie, S. (2024). Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs. CVPR 2024 [lieu non vérifié]. https://arxiv.org/abs/2401.06209
- Vo, A., Nguyen, K.-N., Taesiri, M. R. et al. (2025). Vision Language Models are Biased. arXiv (note machines). https://arxiv.org/abs/2505.23941
- Zolna, K. et al. (2019). Adversarial Framing for Image and Video Classification. AAAI 2019 (note machines). https://arxiv.org/abs/1812.04599
- Bahng, H., Jahanian, A., Sankaranarayanan, S. & Isola, P. (2022). Exploring Visual Prompts for Adapting Large-Scale Models. arXiv (note machines). https://arxiv.org/abs/2203.17274
- Zhang, J., Khayatkhoei, M., Chhikara, P. & Ilievski, F. (2025). MLLMs Know Where to Look (ViCrop). ICLR 2025 (note machines). https://arxiv.org/abs/2502.17422

**Esthétique, jugement, valeur**
- Huang, Y., Yuan, Q., Sheng, X. et al. (2024). AesBench: An Expert Benchmark for Multimodal Large Language Models on Image Aesthetics Perception. arXiv. https://arxiv.org/abs/2401.08276
- Jiang, R. & Chen, C. (2025). Multimodal LLMs Can Reason about Aesthetics in Zero-Shot. ACM MM 2025. https://doi.org/10.1145/3746027.3754961 ; https://arxiv.org/abs/2501.09012
- Koyama, S., Wada, Y., Yashima, D. & Sugiura, K. (2026). MLLM-as-a-Judge Exhibits Model Preference Bias. arXiv. https://arxiv.org/abs/2604.11589
- Li, K., Po, L.-M., Yang, H. et al. (2025). AesBiasBench: Evaluating Bias and Alignment in Multimodal Language Models for Personalized Image Aesthetic Assessment. EMNLP 2025 (selon arXiv). https://arxiv.org/abs/2509.11620
- Mei, J., Moses, M., Waelty, J. & Yang, Y. (2025). Deep Learning for Art Market Valuation. arXiv (note machines). https://arxiv.org/abs/2512.23078
- Murray, N., Marchesotti, L. & Perronnin, F. (2012). AVA: A large-scale database for aesthetic visual analysis. CVPR 2012, 2408-2415. https://doi.org/10.1109/CVPR.2012.6247954
- Sclar, M., Choi, Y., Tsvetkov, Y. & Suhr, A. (2024). Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design. ICLR 2024. https://arxiv.org/abs/2310.11324
- Singh, M., Bhatia, R. & Joshi, R. (2026). Disentangling Algorithmic Bias from Archival Artifacts: A Controlled Audit of Vision-Language Model Valuation in Metropolitan Museum Archives. arXiv (note machines). https://arxiv.org/abs/2609.17572
- Strafforello, O., Soydaner, D., Willems, M., Maerten, A.-S. & De Winter, S. (2024). Have Large Vision-Language Models Mastered Art History? arXiv (note machines). https://arxiv.org/abs/2409.03521
- Talebi, H. & Milanfar, P. (2018). NIMA: Neural Image Assessment. *IEEE TIP* 27(8), 3998-4011. https://doi.org/10.1109/TIP.2018.2831899
- Wang, X., Larson, M. & Zhao, Z. (2026). Visual Input and Its Framing Affect Attribute-based Descriptions Produced by Large Vision-Language Models. arXiv (note machines). https://arxiv.org/abs/2609.18345
- Xiao, Y., Lin, Y. & Chiu, M.-C. (2024). Behavioral Bias of Vision-Language Models: A Behavioral Finance View. Atelier ICML 2024. https://arxiv.org/abs/2409.15256
- Yu, H., Ruiz-Dolz, R. & Yi, Q. (2025). A Structured Framework for Evaluating and Enhancing Interpretive Capabilities of Multimodal LLMs in Culturally Situated Tasks. Findings of EMNLP 2025, 1945-1971. https://doi.org/10.18653/v1/2025.findings-emnlp.103
- Zheng, L., Chiang, W.-L., Sheng, Y. et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. NeurIPS 2023 (Datasets and Benchmarks). https://arxiv.org/abs/2306.05685

**Segmentation, détection, support**
- Arnold, T. & Tilton, L. (2026). Matérialité et vision par ordinateur. *Humanités numériques* 13 (note machines). https://doi.org/10.4000/16xp6
- Carion, N., Gustafson, L., Hu, Y.-T. et al. (2025). SAM 3: Segment Anything with Concepts. ICLR 2026 (note machines). https://arxiv.org/abs/2511.16719
- Gupta, A., Dollár, P. & Girshick, R. (2019). LVIS: A Dataset for Large Vocabulary Instance Segmentation. CVPR 2019. https://arxiv.org/abs/1908.03195
- Kirillov, A., Mintun, E., Ravi, N. et al. (2023). Segment Anything. ICCV 2023 (note machines). https://arxiv.org/abs/2304.02643
- Liu, S., Zeng, Z., Ren, T. et al. (2023). Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection. arXiv [ECCV 2024 : non vérifié]. https://arxiv.org/abs/2303.05499
- Minderer, M., Gritsenko, A., Stone, A. et al. (2022). Simple Open-Vocabulary Object Detection with Vision Transformers (OWL-ViT). ECCV 2022. https://arxiv.org/abs/2205.06230
- Minderer, M., Gritsenko, A. & Houlsby, N. (2023). Scaling Open-Vocabulary Object Detection (OWLv2). NeurIPS 2023 [lieu non vérifié]. https://arxiv.org/abs/2306.09683
- Oliveira, S. A., Seguin, B. & Kaplan, F. (2018). dhSegment: A generic deep-learning approach for document segmentation. ICFHR 2018. https://doi.org/10.1109/ICFHR-2018.2018.00011 ; https://arxiv.org/abs/1804.10371
- Ravi, N., Gabeur, V., Hu, Y.-T. et al. (2024). SAM 2: Segment Anything in Images and Videos. arXiv [ICLR 2025 : non vérifié]. https://arxiv.org/abs/2408.00714
- Tensmeyer, C., Davis, B., Wigington, C., Lee, I. & Barrett, B. (2017). PageNet: Page Boundary Extraction in Historical Handwritten Documents. arXiv (HIP 2017). https://arxiv.org/abs/1709.01618

**Interprétabilité et méthodes**
- Adebayo, J., Gilmer, J., Muelly, M., Goodfellow, I., Hardt, M. & Kim, B. (2018). Sanity Checks for Saliency Maps. NeurIPS 2018. https://arxiv.org/abs/1810.03292
- Alain, G. & Bengio, Y. (2016). Understanding intermediate layers using linear classifier probes. arXiv. https://arxiv.org/abs/1610.01644
- Bau, D., Zhou, B., Khosla, A., Oliva, A. & Torralba, A. (2017). Network Dissection: Quantifying Interpretability of Deep Visual Representations. CVPR 2017. https://arxiv.org/abs/1704.05796
- Belinkov, Y. (2022). Probing Classifiers: Promises, Shortcomings, and Advances. *Computational Linguistics* 48(1), 207-219. https://doi.org/10.1162/coli_a_00422 ; https://arxiv.org/abs/2102.12452
- Cunningham, H., Ewart, A., Riggs, L., Huben, R. & Sharkey, L. (2023). Sparse Autoencoders Find Highly Interpretable Features in Language Models. arXiv. https://arxiv.org/abs/2309.08600
- Fong, R. & Vedaldi, A. (2017). Interpretable Explanations of Black Boxes by Meaningful Perturbation. ICCV 2017. https://doi.org/10.1109/ICCV.2017.371
- Gandelsman, Y., Efros, A. A. & Steinhardt, J. (2024). Interpreting CLIP's Image Representation via Text-Based Decomposition. ICLR 2024 [lieu non vérifié]. https://arxiv.org/abs/2310.05916
- Geiger, A., Lu, H., Icard, T. & Potts, C. (2021). Causal Abstractions of Neural Networks. NeurIPS 2021. https://arxiv.org/abs/2106.02997
- Golovanevsky, M., Rudman, W., Palit, V., Singh, R. & Eickhoff, C. (2024). What Do VLMs NOTICE? A Mechanistic Interpretability Pipeline for Gaussian-Noise-free Text-Image Corruption and Evaluation. arXiv [NAACL 2025 : non vérifié]. https://arxiv.org/abs/2406.16320
- Goyal, Y., Wu, Z., Ernst, J., Batra, D., Parikh, D. & Lee, S. (2019). Counterfactual Visual Explanations. ICML 2019 [lieu non vérifié]. https://arxiv.org/abs/1904.07451
- Hooker, S., Erhan, D., Kindermans, P.-J. & Kim, B. (2019). A Benchmark for Interpretability Methods in Deep Neural Networks. NeurIPS 2019. https://arxiv.org/abs/1806.10758
- Howard, P., Madasu, A., Le, T. et al. (2024). SocialCounterfactuals: Probing and Mitigating Intersectional Social Biases in Vision-Language Models with Counterfactual Examples. CVPR 2024. https://arxiv.org/abs/2312.00825
- Jacovi, A. & Goldberg, Y. (2020). Towards Faithfully Interpretable NLP Systems: How should we define and evaluate faithfulness? ACL 2020. https://arxiv.org/abs/2004.03685
- Kim, B., Wattenberg, M., Gilmer, J. et al. (2018). Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV). ICML 2018. https://arxiv.org/abs/1711.11279
- Kindermans, P.-J., Hooker, S., Adebayo, J. et al. (2017). The (Un)reliability of saliency methods. arXiv. https://arxiv.org/abs/1711.00867
- Kornblith, S., Norouzi, M., Lee, H. & Hinton, G. (2019). Similarity of Neural Network Representations Revisited. ICML 2019. https://arxiv.org/abs/1905.00414
- Lim, H., Choi, J., Choo, J. & Schneider, S. (2025). Sparse autoencoders reveal selective remapping of visual concepts during adaptation. ICLR 2025. https://arxiv.org/abs/2412.05276
- Lundberg, S. & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. NIPS 2017. https://arxiv.org/abs/1705.07874
- Neo, C., Ong, L., Torr, P., Geva, M., Krueger, D. & Barez, F. (2025). Towards Interpreting Visual Information Processing in Vision-Language Models. ICLR 2025. https://arxiv.org/abs/2410.07149
- Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M. & Carter, S. (2020). Zoom In: An Introduction to Circuits. *Distill*. https://doi.org/10.23915/distill.00024.001
- Rao, S., Mahajan, S., Böhle, M. & Schiele, B. (2024). Discover-then-Name: Task-Agnostic Concept Bottlenecks via Automated Concept Discovery. ECCV 2024. https://arxiv.org/abs/2407.14499
- Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R., Parikh, D. & Batra, D. (2017/2019). Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization. ICCV 2017 ; *IJCV* 2019. https://doi.org/10.1007/s11263-019-01228-7 ; https://arxiv.org/abs/1610.02391
- Stevens, S., Chao, W.-L., Berger-Wolf, T. & Su, Y. (2025). Interpretable and Testable Vision Features via Sparse Autoencoders. arXiv. https://arxiv.org/abs/2502.06755
- Turpin, M., Michael, J., Perez, E. & Bowman, S. R. (2023). Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. NeurIPS 2023. https://arxiv.org/abs/2305.04388
- Zhang, F. & Nanda, N. (2024). Towards Best Practices of Activation Patching in Language Models: Metrics and Methods. ICLR 2024. https://arxiv.org/abs/2309.16042

**Validité de la mesure**
- Jacobs, A. Z. & Wallach, H. (2021). Measurement and Fairness. FAccT 2021. https://doi.org/10.1145/3442188.3445901
- Raji, I. D., Bender, E. M., Paullada, A., Denton, E. & Hanna, A. (2021). AI and the Everything in the Whole Wide World Benchmark. NeurIPS 2021 (Datasets and Benchmarks). https://arxiv.org/abs/2111.15366
- Salaudeen, O., Reuel, A., Ahmed, A. et al. (2025). Measurement to Meaning: A Validity-Centered Framework for AI Evaluation. arXiv. https://arxiv.org/abs/2505.10573
