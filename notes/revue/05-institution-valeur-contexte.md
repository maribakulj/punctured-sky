# 05 — Le cadre comme opérateur social : institution, statut d'art, valeur, prix, effets de contexte

*Volet 5 de la revue de littérature. Rédigé le 17/10/2026. Aucune expérience nouvelle ici.*

**Règle suivie pour les références.** Chaque référence a été contrôlée en ligne le 17/10/2026 :
notice DOI (Crossref, OpenAlex, Europe PMC), page arXiv, catalogue (Open Library) ou page de
l'éditeur. Le lien donné en bibliographie est celui qui a servi au contrôle. J'indique :

- **[résumé lu]** quand j'ai lu le résumé officiel (c'est le cas le plus fréquent) ;
- **[texte lu]** quand j'ai lu la méthode et les résultats dans le texte complet ;
- **[contenu non lu]** quand j'ai seulement vérifié que la référence existe ;
- **[de mémoire]** quand je résume une thèse connue sans avoir relu le livre ce jour ;
- **[non vérifié]** quand je n'ai pas pu confirmer la référence elle-même.

Je ne donne aucun chiffre que je n'ai pas lu. Quand une étude ne donne pas de taille d'effet
dans le résumé, je le dis.

**Ce que ce volet ne refait pas.** La note `notes/cadrage-et-valeur.md` (13/10) donne déjà une
première liste (sociologie, philosophie, études musée/laboratoire, économie des enchères).
Ici, je reprends ces textes seulement pour aller plus loin : ce que chaque théorie prédit, quels
protocoles ont servi, ce qui a été répliqué, et **comment on établit qu'un contexte agit sur
quelqu'un à son insu**. J'ajoute une quarantaine de références nouvelles.

---

## En bref

1. **Il faut séparer trois « cadres ».** (a) le **cadre matériel** (bois, dorure, ornement) ;
   (b) le **cadre institutionnel** (musée, galerie, cartel, catalogue de vente, marque) ;
   (c) le **nom** (attribution à un artiste, à une célébrité, à « une IA », à « un humain »).
   On peut y ajouter (d) le **prix affiché**. Ces quatre signaux n'ont ni la même histoire
   théorique ni les mêmes preuves expérimentales. La littérature mélange souvent les mots :
   en psychologie, *framing* veut presque toujours dire (b) ou (c), presque jamais (a).
2. **Les preuves sont fortes pour (c) et (d)**, moyennes pour (b), **très minces pour (a)**.
   Je n'ai trouvé **qu'une** expérience publiée sur le cadre matériel et la valeur
   (Koniak & Szubielska 2022, 98 personnes, en ligne). Elle trouve un effet **négatif** du
   cadre décoratif.
3. **L'intuition de Marcel (« un cadre doré rococo est peut-être interprété socialement »)
   a un mécanisme précis dans cette étude** : le spectateur se demande *pourquoi* on a mis ce
   cadre, et s'il y voit une intention de promotion, l'œuvre perd de la valeur. C'est le
   « modèle de la connaissance de la persuasion » (Friestad & Wright 1994). Le cadre n'est pas
   un simple signal de luxe ; c'est un **message dont on soupçonne l'auteur**.
4. **L'autre intuition (« ce qui compte, c'est ce qui l'influence sans qu'il le sache »)
   correspond à deux traditions** : en sociologie, la **méconnaissance** chez Bourdieu (la
   valeur de l'art tient à une croyance collective qui ne se voit pas comme croyance) ; en
   psychologie, la critique de l'introspection (Nisbett & Wilson 1977) et les **mesures
   implicites**. Les deux ont été transposées aux modèles de langage : un modèle peut suivre
   un indice sans le mentionner dans son explication (Turpin et al. 2023 ; Chen et al. 2025).
5. **Les effets de contexte chez les humains sont réels mais fragiles.** L'effet « musée »
   se réplique (Brieber 2014 ; Grüner 2019 ; Szubielska & Imbir 2021), mais disparaît parfois
   (Brieber, Leder & Nadal 2015). L'effet « étiquette de galerie » de Kirk et al. (2009) n'a
   **pas** été retrouvé dans les notes par Silveira et al. (2015). Dire « c'est de l'art » peut
   même **faire baisser** l'appréciation (Papenmeier et al. 2024).
6. **Le biais « humain contre IA » est le mieux établi** : plusieurs études, dont une
   préenregistrée de grande taille (Millet et al. 2023, N = 1 708). Il existe aussi en mesure
   implicite (regard) alors qu'il disparaît dans les notes (Zhou & Kawabata 2023).
7. **Chez les machines**, une étude contrôlée montre que 13 modèles de langage favorisent un
   texte étiqueté « humain » **2,5 fois plus** que des humains (Haverals & Martin 2025). Je
   n'ai trouvé **aucune** étude publiée qui manipule le cadre matériel ou le cartel devant un
   modèle vision-langage et mesure un prix. Le chiffre « +54 % » de provenance (Li, Ma &
   Renneboog 2024) concerne **les ventes aux enchères humaines**, pas les modèles.
8. **Le meilleur apport possible de punctured sky** : appliquer aux machines la batterie de
   critères qui sert, chez les humains, à prouver qu'un contexte agit à leur insu (stimulus
   identique, attribution aléatoire de l'étiquette, consigne qui ne nomme pas l'indice, mesure
   indirecte, contrôle de ce que le sujet dit de ses raisons).

---

## 1. Trois cadres, quatre signaux : une grille de lecture

Avant de passer aux auteurs, voici la grille que j'utilise partout. Elle sert à ne pas
confondre des effets qui n'ont rien à voir.

| Signal | Exemple | Ce qu'il transporte | Théorie principale | Preuve expérimentale chez l'humain |
| --- | --- | --- | --- | --- |
| (a) cadre matériel | baguette dorée rococo, cadre noir fin | luxe, ancienneté, goût d'une époque ; indice de présentation | histoire du cadre (volet 1) ; Becker (conventions) ; Bourdieu (goût de classe) | **une étude** : Koniak & Szubielska 2022 |
| (b) cadre institutionnel | musée, galerie, cartel, catalogue, white cube | « ceci a été choisi par le monde de l'art » | Dickie ; O'Doherty ; Duncan ; Bennett ; Karpik | musée/labo (Brieber, Grüner, Szubielska) ; étiquettes « galerie » (Kirk, Silveira) |
| (c) le nom | « Rembrandt », « copie », « IA », « humain », « portait par une star » | une personne, un acte unique, un contact | Newman & Bloom (contagion) ; Heinich (singularité) | nombreuses ; biais anti-IA bien répliqué |
| (d) le prix | « 1 M$ », « 90 $ » ; « lot 112, estimation… » | un jugement social déjà fait | Velthuis ; Karpik ; Beckert | Plassmann (vin) ; Lauring (art) ; Beggs & Graddy (enchères) |

Deux remarques simples, mais importantes pour la suite.

- **Les signaux (b), (c) et (d) sont d'habitude du texte.** Dans les expériences, on les
  donne en mots (« cette image vient d'une galerie »). **Le signal (a) est une image.** Pour
  une machine qui lit des reproductions, c'est une différence majeure : le cadre matériel est
  le seul signal social qui est **dans les pixels**, avec parfois le mur du musée et le
  cartel photographié. C'est pourquoi le cadre matériel est le point où le projet peut
  apporter du neuf.
- **Le cadre matériel peut renvoyer aux trois autres.** Un cadre rococo doré « dit » : un
  musée ou un collectionneur l'a choisi (b), il entoure probablement une œuvre ancienne
  attribuée (c), il coûte cher (d). La machine peut donc lire le cadre comme **la trace
  visible d'une institution invisible**. C'est exactement le problème de Danto, retourné.

---

## 2. Philosophie : ce qui fait qu'une chose est de l'art

### 2.1 Duchamp et le problème des indiscernables

La *Fontaine* (1917) est le cas d'école : un urinoir industriel, signé « R. Mutt », envoyé à
une exposition. L'objet ne change pas ; seul change le geste qui le présente. (Faits et débat
d'attribution déjà vérifiés dans `cadrage-et-valeur.md` §1.4.)

### 2.2 Danto : la théorie qu'on ne voit pas

Danto pose le problème en 1964 dans « The Artworld ». Deux objets **identiques à l'œil** (les
*Brillo Boxes* de Warhol et les cartons de supermarché) n'ont pas le même statut. Ce qui les
sépare ne se voit pas : c'est une **atmosphère de théorie**, une connaissance de l'histoire de
l'art. Dans *La Transfiguration du banal* (1981), il précise : une œuvre est **à propos de**
quelque chose, et elle demande une interprétation. [de mémoire, cohérent avec les notices
vérifiées]

**Ce que cela prédit pour une machine.** Si Danto a raison, une machine qui ne lit que des
pixels **ne peut pas** distinguer l'œuvre du banal quand ils sont identiques. Elle ne le peut
que si quelque chose dans l'image renvoie à la théorie : un cadre, un mur, un cartel, un
socle. Le cadre devient alors **le substitut visible de la théorie invisible**. Notre pilote
montre déjà que Claude lit le ticket encadré comme « ironique », « décalé » : il ne confère
pas le statut, il **reconnaît un genre** (le détournement). C'est une lecture « dantoïenne »
(l'œuvre parle de l'art), pas institutionnelle.

### 2.3 Dickie : la théorie institutionnelle

Dickie (1974, puis 1984) répond que l'art est ce à quoi des personnes **agissant au nom du
monde de l'art** ont conféré le statut de « candidat à l'appréciation ». En 1984, il retire
l'idée d'un acte explicite de conférer : une œuvre est « un artefact d'un type créé pour être
présenté à un public du monde de l'art » (définition citée par la *Stanford Encyclopedia*,
déjà vérifiée).

**Critique classique** [de mémoire] : la définition est circulaire (le monde de l'art est
défini par l'art, et l'art par le monde de l'art) ; elle ne dit pas **pourquoi** l'institution
choisit telle chose. Levinson (1979) propose une alternative : est art ce qui est **voulu**
pour être regardé comme les œuvres du passé ont été regardées. C'est une définition
**historique**, fondée sur l'intention et la ressemblance avec le passé. [résumé du titre et
de la thèse générale ; contenu non relu]

**Pourquoi Levinson est utile ici.** Une machine apprend surtout des **ressemblances avec le
passé**. Le cadre doré ancien est une ressemblance forte avec les œuvres du passé telles
qu'elles sont photographiées. Une machine est donc, par construction, plus « levinsonienne »
que « dickienne » : elle ne connaît pas l'acte institutionnel, elle connaît la **forme**
habituelle de ce que les institutions montrent.

### 2.4 Ce qui reste discuté

- **Statut contre valeur.** Danto et Dickie parlent du **statut** (est-ce de l'art ?), pas de
  la **valeur** (combien cela vaut, est-ce bon ?). Dickie le dit lui-même : être art ne veut
  pas dire être bon. Or presque toutes les expériences de psychologie mesurent la valeur
  (aimer, beauté, prix), pas le statut. La question « est-ce de l'art ? » est rarement posée
  telle quelle aux participants. Exception : Jucker et al. 2014 (§6.5).
- **Pour une machine**, il faut donc poser **deux questions séparées** (« est-ce de l'art ? »
  et « combien cela vaut-il ? »), comme le pilote l'a fait. Les deux ne bougent pas ensemble :
  chez Claude, le prix monte avec le cadre ancien, le statut « art » non.

---

## 3. Sociologie : la valeur produite par un monde social

### 3.1 Becker : la coopération et les conventions

Pour Howard Becker (*Art Worlds*, 1982), une œuvre est le produit d'une **chaîne de
coopération** : fournisseurs de matériel, assistants, marchands, critiques, conservateurs,
publics. Ces gens coopèrent grâce à des **conventions** partagées (formats, matériaux,
manières d'exposer). [de mémoire] Le cadre est l'une de ces conventions : il dit comment
accrocher, comment regarder, où s'arrête l'œuvre.

**Intérêt pour nous.** Becker ne parle pas de croyance cachée ; il parle de **routines**. Une
machine qui a vu des millions de photos de musées a appris les routines de présentation. Elle
n'a pas besoin de « croire » : elle reconnaît une convention.

### 3.2 Bourdieu : la croyance, la consécration, la méconnaissance

Bourdieu apporte trois idées que je résume simplement [de mémoire ; textes non relus ce jour] :

1. **La production de la croyance** (1977). La valeur d'une œuvre est produite par tout un
   champ (marchands, critiques, musées). Le marchand qui expose une œuvre la **consacre** ; il
   met son propre crédit en jeu. La valeur est une **croyance collective**.
2. **La méconnaissance.** Cette croyance ne se voit pas comme croyance. Les acteurs vivent la
   valeur comme une qualité de l'œuvre, pas comme un produit social. C'est ce qui la rend
   efficace. **C'est très exactement l'intuition de Marcel : ce qui compte, c'est ce qui
   influence sans qu'on le sache.**
3. **La distinction** (1979) et **L'Amour de l'art** (1966, avec Darbel). Le goût pour l'art
   « pur » (regarder la forme plutôt que la fonction) n'est pas naturel ; il dépend de
   l'éducation et sert à se distinguer. Le même objet n'a pas la même valeur pour tous : un
   cadre doré chargé peut signifier « grand art » pour les uns et « ostentation » ou
   « nouveau riche » pour d'autres.

**Conséquence pour le cadre rococo.** Chez Bourdieu, le signe n'a pas une valeur fixe : il
change de sens selon **la position sociale de celui qui regarde**. C'est ce que trouvent
Lauring et al. (2016, §6.7) : le jugement d'un groupe social « bas » fait aimer **davantage**
une peinture qu'il n'aime pas (on se distingue). Et c'est ce que trouvent Koniak & Szubielska
(§6.3) : les personnes intéressées par l'art pénalisent même le cadre simple.

**Question pour la machine.** Un modèle entraîné sur le web est un lecteur **sans position
sociale propre**, ou plutôt un mélange de toutes les positions présentes dans ses données.
Laquelle domine ? Le catalogue de vente (le doré vaut cher) ou le critique (le doré est
kitsch) ? On peut le tester en demandant au modèle de répondre « comme un conservateur »,
« comme un antiquaire », « comme un étudiant en art » : si le sens du cadre change avec le
rôle, le modèle a appris **la structure du champ**, pas seulement un signal de luxe.

### 3.3 Heinich : singularité et artification

Nathalie Heinich a beaucoup discuté Bourdieu. Trois apports [de mémoire ; livres vérifiés au
catalogue] :

- ***La Gloire de Van Gogh*** (1991) : la valeur de Van Gogh s'est construite après sa mort par
  un récit (le génie méconnu, le sacrifice). Le récit fait partie de l'œuvre telle qu'elle est
  perçue. C'est un **cadre narratif**.
- ***Le Triple Jeu de l'art contemporain*** (1998) : l'art contemporain avance par un jeu à
  trois temps : l'artiste **transgresse** les frontières de l'art, le public **réagit** (rejet,
  scandale), les institutions **intègrent** la transgression. Le cadre doré autour d'un ticket
  de caisse est exactement une transgression de ce type ; la machine qui la qualifie
  d'« ironique » joue le rôle du public averti.
- ***De l'artification*** (2012, avec Shapiro) : le passage d'une chose au statut d'art suit des
  étapes concrètes : changement de nom, de lieu, d'objets de présentation, d'institutions.
  **Le cadre et le cartel sont des outils d'artification.**
- Heinich distingue aussi **régime de communauté** (valeur par conformité) et **régime de
  singularité** (valeur par l'unique, l'original, l'auteur). [de mémoire] Le cadre ancien
  signale le régime de singularité : un objet unique, avec une histoire.

**Débat Heinich/Bourdieu**, simplifié : pour Bourdieu, le sociologue dévoile une croyance que
les acteurs méconnaissent. Pour Heinich, le sociologue doit **décrire les valeurs des
acteurs** sans les dénoncer. Pour notre projet, les deux postures donnent deux protocoles
différents : (1) chercher ce que la machine **fait sans le dire** (posture Bourdieu) ; (2)
décrire **les justifications qu'elle donne** (posture Heinich). Il faut les deux, et les
comparer.

### 3.4 Moulin : le marché et l'institution

Pour Raymonde Moulin (1967 ; 1992), la valeur de l'art contemporain se forme à **la jonction
du marché et de l'institution** : le musée certifie, le marché chiffre. [de mémoire] Un modèle
qui donne un **prix** lit des signes de marché ; un modèle qui dit « appartient probablement à
un musée » lit des signes d'institution. Devant le cadre ancien, Claude fait les deux.

---

## 4. Économie des singularités : comment on évalue ce qui est unique

### 4.1 Karpik : les dispositifs de jugement

Lucien Karpik (*L'Économie des singularités*, 2007) étudie les biens **uniques et
incomparables** dont la qualité est **incertaine** : œuvres d'art, grands vins, avocats,
films. Pour ces biens, le prix ne suffit pas à orienter l'acheteur. Le marché tient grâce à
des **dispositifs de jugement** qui disent où porter son attention. Il en donne une typologie
[de mémoire, à vérifier dans le livre] : les **réseaux** (le bouche-à-oreille), les
**appellations** (labels, marques, titres), les **cicérones** (critiques, guides), les
**classements** (palmarès, prix), les **confluences** (mise en scène des lieux de vente).

**Placement du cadre dans cette grille.** Le cadre doré est à la fois une **appellation**
silencieuse (« objet de qualité ») et un élément de **confluence** (la mise en scène qui guide
l'acheteur). Le cartel de musée est une appellation explicite. Le prix d'estimation est un
classement. Cette typologie permet de **construire des conditions expérimentales distinctes**
pour une machine, au lieu de tout appeler « contexte ».

### 4.2 Velthuis : le prix comme langage

Chez Velthuis (*Talking Prices*, 2005), le prix est un **signe** autant qu'un montant, et la
galerie emprunte la **forme du musée** pour cacher le commerce (détails dans la note
précédente). Un cadre ancien fait peut-être la même chose à l'échelle d'un objet.

### 4.3 Beckert & Aspers ; Beckert & Rössel : valuer sous incertitude

Le volume dirigé par Beckert et Aspers (*The Worth of Goods*, 2011) rassemble des études sur la
manière dont les marchés **évaluent** (« valuation ») quand la qualité ne se mesure pas
directement. [contenu non lu ; chapitre d'introduction vérifié] Beckert & Rössel (2013),
sur des données de prix d'artistes, montrent que l'acheteur incertain s'appuie sur la
**réputation** construite par les experts. Pour une machine, l'équivalent de la réputation
est **la reconnaissance** : notre pilote suggère que quand le modèle reconnaît l'œuvre (le
Renoir chez Claude), le cadre ne compte plus ; quand il ne la reconnaît pas (le même Renoir
chez Gemini), le prix suit le cadre.

### 4.4 Boltanski & Esquerre : l'enrichissement et la forme collection

*Enrichissement. Une critique de la marchandise* (2017) est sans doute le texte le plus utile
pour notre question. Les auteurs décrivent une économie qui **enrichit** des choses déjà
existantes (patrimoine, antiquités, art, luxe, tourisme) en leur attachant **un récit tourné
vers le passé**. Ils distinguent quatre « formes de mise en valeur » [vérifié par le compte
rendu de Godechot, cité dans la note précédente] :

| forme | ce qui fait le prix | exemple |
| --- | --- | --- |
| standard | coût de fabrication, prix de série | un cadre neuf de grande surface |
| collection | appartenance à un ensemble, récit, « force mémorielle » | un cadre rococo d'époque, un objet de musée |
| tendance | ce qui est à la mode, prestige d'une personne | un cadre « design » signé |
| actif | ce que l'objet rapportera à la revente | une œuvre achetée comme placement |

**Ce que cela ajoute à Bourdieu.** Pour Boltanski & Esquerre, la valeur n'est pas seulement
une croyance diffuse : elle passe par un **travail de mise en forme**. Les objets changent de
forme au cours de leur vie (un ticket de caisse est standard ; encadré dans du rococo, il est
mis en scène comme un objet de collection). **Le cadre ancien est un opérateur de passage de
la forme standard à la forme collection.** C'est testable : si une machine lit le cadre ancien
comme un passage à la forme collection, elle devrait aussi (1) inventer un **passé** à l'objet
(dater, attribuer), (2) lui imaginer un **propriétaire collectionneur ou musée**, (3) donner un
prix qui ne dépend pas du coût de fabrication. Le pilote montre les trois chez Claude (date du
cadre donnée à part 18/18 ; propriétaire musée 7/18).

**Point de prudence.** Boltanski & Esquerre parlent du **récit**. Le cadre seul n'est pas un
récit ; c'est un **déclencheur de récit**. La question est de savoir si la machine produit le
récit d'elle-même (elle invente une provenance) ou si elle a besoin qu'on le lui donne (cartel,
légende). C'est la différence entre les hypothèses H1 et H4 de la note précédente.

### 4.5 L'économie des enchères : la provenance et l'ancrage

Rappel (note précédente) : la **provenance imprimée** au catalogue augmente le prix (jusqu'à
+54 %, Li, Ma & Renneboog 2024) ; les estimations sont **ancrées** sur la vente précédente
(Beggs & Graddy 2009). Ce sont des données de marché **humaines**, pas des expériences : les
œuvres bien « provenancées » sont peut-être aussi meilleures. Elles montrent seulement que le
marché **paie** pour un récit.

---

## 5. Le musée et ses dispositifs : salle, rituel, cartel

### 5.1 O'Doherty : la salle remplace le cadre

Brian O'Doherty (*Inside the White Cube*, essais de 1976, livre 1986) décrit la galerie
moderne : murs blancs, lumière égale, aucune fenêtre, aucun temps. Cette salle **n'est pas
neutre** : elle coupe l'objet du monde et donne à ce qu'on y pose un air d'art. Avec
l'art moderne, **la salle prend le rôle que tenait le cadre**. [de mémoire]

**Fait expérimental gênant.** Dans le pilote, une salle blanche fabriquée ne valorise pas le
ticket chez Claude. Chez les humains, la salle blanche du musée marche parfois (§6.2), mais il
s'agit de **vrais** musées, avec gardiens, visiteurs, cartels, trajet, prix d'entrée. Le
« white cube » n'est pas une couleur de mur ; c'est un **ensemble de signes** dont la machine
ne voit qu'une partie.

### 5.2 Duncan : le musée comme rituel

Carol Duncan (*Civilizing Rituals*, 1995) lit le musée d'art comme un **lieu de rituel** : un
espace séparé, un parcours prescrit, une attitude attendue (silence, contemplation). Le
visiteur « joue » un rôle qui transforme son regard. [de mémoire] **Ce qu'on retient** : le
cadre institutionnel agit sur **la conduite** du spectateur avant d'agir sur son jugement.
C'est cohérent avec Brieber et al. (2014) : au musée, les gens **regardent plus longtemps**.
Une machine n'a pas de conduite ; elle n'a qu'une sortie. Cet effet-là ne peut pas, par
principe, se transposer. On peut seulement demander si la machine **décrit** la conduite
attendue (« à contempler », « à admirer »).

### 5.3 Bennett : le complexe d'exposition

Tony Bennett (« The Exhibitionary Complex », article de 1988, repris en 1994 ; *The Birth of
the Museum*, 1995) lit le musée public du XIXe siècle comme un dispositif de **pouvoir** : il
montre des objets classés à un public, et en même temps apprend au public à se montrer et à
se tenir. Le musée **met en ordre** les choses et les gens. [de mémoire ; article original de
1988 dans *New Formations* n° 4 **non vérifié** en ligne ; reprise de 1994 vérifiée]

**Utilité pour nous.** Les reproductions d'œuvres en ligne sont produites surtout par des
musées (photos de collection, notices). Le « complexe d'exposition » a donc **fabriqué les
données** sur lesquelles les machines apprennent. Une machine qui associe cadre ancien et musée
ne fait que refléter **qui a photographié quoi**. C'est le même point que Schneider & Bell
(2026, dans la note précédente) sur la datation : le modèle apprend l'histoire des collections.

### 5.4 Le cartel (étiquette de musée) : ce que l'on sait

Le cartel est le cadre institutionnel le plus explicite : nom, titre, date, technique,
provenance (« don de… », « ancienne collection… »).

- **Beverly Serrell** (*Exhibit Labels: An Interpretive Approach*, 1996, 2e éd. 2015) est la
  référence pratique pour écrire des cartels. [contenu non lu]
- **Les visiteurs regardent peu de temps et lisent.** Smith & Smith (2001) ont observé 150
  visiteurs du Metropolitan Museum devant six chefs-d'œuvre : durée moyenne **27,2 s**,
  médiane **17 s**. Carbon (2017) a observé 225 visiteurs d'une exposition Gerhard Richter :
  moyenne **32,9 s** (médiane 25,4 s) ; plus de la moitié reviennent devant les tableaux.
  Smith, Smith & Tinio (2017) mesurent le temps passé à lire les cartels [contenu non lu].
- **Le cartel guide le regard et la pensée.** Reitstätter, Galter & Bakondi (2022) ont suivi
  des visiteurs avec un oculomètre mobile avant et après une nouvelle présentation d'une
  collection, où l'on avait ajouté des cartels interprétatifs. Tous les visiteurs lisent, à
  des degrés divers ; le parcours typique est « œuvre - cartel - œuvre » ; les
  interprétations des œuvres changent avec le texte du cartel.

**Ce qui manque.** Je n'ai trouvé aucune étude qui manipule la **provenance** écrite sur un
cartel (« ancienne collection d'un prince » contre « don anonyme ») en gardant l'œuvre
identique, et mesure l'appréciation ou le prix. Les études sur l'information (§6.5) portent
sur le **titre** et la **description**, pas sur la **provenance**. C'est un angle mort net, et
une expérience facile à faire, chez les humains comme chez les machines.

---

## 6. Esthétique expérimentale : les effets de contexte mesurés chez les humains

Pour chaque étude : **protocole**, **effet**, **réplication**. Les tailles d'échantillon sont
celles du résumé ou du texte ; quand je ne les ai pas lues, je ne les donne pas.

### 6.1 Les modèles théoriques

- **Leder, Belke, Oeberst & Augustin (2004)** [résumé lu] : cinq étapes (perception,
  classification explicite, classification implicite, maîtrise cognitive, évaluation) ;
  émotion esthétique et jugement esthétique sont deux sorties distinctes. Le contexte (musée,
  étiquette « art ») oriente le traitement **avant** le regard. C'est la base de presque
  toutes les études de contexte. Bilan dix ans plus tard : Leder & Nadal (2014).
- **Pelowski et al. (2017)**, modèle « VIMAP » (traitements du bas et du haut) [contenu non
  lu], et **Pelowski & Specker (2020)**, chapitre « The General Impact of Context on Aesthetic
  Experience » de l'*Oxford Handbook of Empirical Aesthetics* [contenu non lu]. **À lire en
  priorité** : c'est la synthèse la plus récente que j'ai trouvée sur ce volet.

### 6.2 Musée contre laboratoire (cadre institutionnel « physique »)

| étude | protocole | effet | statut |
| --- | --- | --- | --- |
| Brieber, Nadal, Leder & Rosenberg 2014 [texte lu] | 44 personnes tirées au sort (22 musée, 22 labo) ; 14 photographies d'art ; oculomètre mobile | au musée : appréciation plus haute ; temps de regard médian 38,75 s contre 28,25 s (r = −0,47) | effet trouvé |
| Brieber, Nadal & Leder 2015 [résumé lu] | même exposition, musée contre simulation sur ordinateur | au musée : plus aimé, plus intéressant, plus excitant ; meilleure mémoire | effet trouvé |
| Brieber, Leder & Nadal 2015 [résumé lu] | 2 × 2 entre sujets (musée/labo × original/reproduction), 110 personnes, art conceptuel | **aucun effet**, ni du lieu ni de l'original | échec |
| Grüner, Specker & Leder 2019 [résumé lu] | réplication conceptuelle du précédent, manipulations améliorées | effet du musée (aimé, intéressant) ; pas d'effet de l'original ; le style pèse plus | réplication partielle |
| Gartus & Leder 2014 ; Gartus, Klemer & Leder 2015 | musée contre rue (image de contexte autour de l'œuvre) | dépend du style (art moderne ou graffiti) et de l'intérêt pour l'art | effet conditionnel |
| Szubielska & Imbir 2021 [résumé lu] | art critique contemporain, galerie contre labo ; texte du commissaire lu, écouté ou absent | la galerie augmente émotions et appréciation ; le texte augmente la compréhension, pas l'appréciation | effet trouvé |
| Szubielska & Imbir 2022 [résumé lu] | installations interactives, galerie contre labo | plus aimées en galerie ; les auteurs l'attribuent à l'effet galerie, pas à l'interactivité | effet trouvé |
| Locher, Smith & Smith 2001 ; Locher & Dolese 2004 [résumé lu] | originaux au Met contre diapositives, écran, cartes postales | valeur « hédonique » plus haute pour les originaux ; les qualités picturales jugées pareilles ; aucune différence entre les trois reproductions | effet trouvé |

**Ce qui en ressort.** (1) Le contexte du musée change plus **l'expérience** (émotion,
intérêt, temps) que **la perception** de l'image. (2) L'effet dépend fortement du **style** et
de **l'intérêt pour l'art**. (3) Le dernier point est crucial pour les machines : **les
reproductions se valent entre elles** (Locher & Dolese). Une machine ne voit que des
reproductions. Le contexte qu'elle peut lire est donc celui **qui est dans la photo** (cadre,
mur, cartel), pas celui du lieu réel.

### 6.3 Le cadre matériel : la seule expérience

**Koniak & Szubielska (2022)** [texte lu]. C'est l'étude la plus proche de la question de
Marcel. Je la détaille.

- **Participants** : 98 étudiants (18-39 ans), recrutés en ligne, non payés, tirés au sort
  dans trois conditions (entre sujets).
- **Images** : dix peintures abstraites contemporaines de la Galerie nationale Zachęta
  (Varsovie), en reproduction de haute qualité.
- **Manipulation** : sans cadre, cadre simple, cadre décoratif. Les cadres ont été choisis
  pour chaque tableau par une personne du métier, et **ajoutés numériquement** sans changer
  la taille du tableau ; même largeur pour tous ; dans la condition sans cadre, une bande
  claire remplace le cadre pour que la surface totale soit la même.
- **Mesures** : quatre questions moyennées en un indice (aimer, intérêt, « bon placement pour
  un collectionneur », « mérite d'être exposé en galerie »). Plus **cinq questions leurres**
  (émotions, calme, compréhension) « pour cacher le but de l'étude ». Échelles en 7 points.
  Intérêt et connaissance de l'art mesurés à la fin.
- **Pré-test** (54 personnes) : les cadres décoratifs sont bien vus comme plus chers et plus
  décoratifs ; ils semblent un peu moins bien assortis aux tableaux (p = 0,066).
- **Résultats** : effet négatif du cadre décoratif (b = −0,64, t(92) = −2,72, p = 0,008) ;
  effet du cadre simple à la limite (b = −0,47, p = 0,055), présent seulement chez les
  personnes **intéressées** par l'art.
- **Interprétation des auteurs** : le cadre peut être un **indice de valeur** (plus il paraît
  cher, plus l'œuvre vaut) ou un **moyen de promotion**. Si le spectateur y voit une tentative
  d'influence, l'évaluation chute. C'est le **modèle de la connaissance de la persuasion**
  (Friestad & Wright 1994) : les gens savent qu'on essaie de les persuader, et s'en défendent.
- **Limites dites par les auteurs** : le mécanisme (l'inférence d'intention) n'est testé
  qu'indirectement. Ils proposent deux tests : dire que le cadre a été **choisi au hasard par
  un ordinateur** (l'effet devrait disparaître) ou **choisi par un employé de maison de
  ventes** (l'effet devrait augmenter). Ils proposent aussi de tester des peintures
  **figuratives** et du **kitsch**, où le cadre est plus « naturel ».
- **Réplication** : aucune trouvée.

**Pourquoi c'est important pour le projet.**

1. C'est **le seul** résultat humain sur le cadre matériel, et il va **contre** le
   comportement de Claude dans le pilote. Mais les conditions ne sont pas comparables : art
   abstrait contemporain (chez eux) contre ticket, dessin d'enfant, photo de plage (chez nous).
   Le cadre décoratif autour d'une abstraction est une **faute de goût** ; autour d'un ticket,
   c'est une **blague**. Il faudrait les deux types de contenus dans une même expérience.
2. Le protocole est **directement transposable** : cadre ajouté numériquement, surface
   constante, questions leurres, mesure de l'intérêt pour l'art. Le pilote de punctured sky
   suit déjà presque les mêmes règles (contenu jamais recadré, taille fixe, questions qui ne
   parlent pas de cadre).
3. Les deux tests proposés par les auteurs (cadre « au hasard » contre cadre « choisi par un
   vendeur ») sont **faciles à faire avec une machine** et départageraient « le cadre comme
   signal de luxe » et « le cadre comme message intentionnel ». C'est la forme expérimentale
   exacte de l'intuition « le cadre rococo est interprété socialement ».

### 6.4 Désigner comme « art » (étiquette institutionnelle en mots)

- **Kirk, Skov, Hulme, Christensen & Zeki (2009)** [résumé lu]. Mêmes images, étiquetées **au
  hasard** « galerie » ou « générée par ordinateur », en IRM fonctionnelle. Notes plus hautes
  en « galerie ». L'effet est lié à l'activité du cortex orbitofrontal médian et préfrontal.
  Nombre de participants non lu.
- **Silveira, Fehse, Vedder, Elvers & Hennig-Fast (2015)** [texte lu]. 17 personnes, IRMf ;
  tableaux du MoMA présentés comme « du MoMA » ou « d'un centre d'éducation pour adultes ».
  L'étiquette change l'activité cérébrale (précunéus, cortex pariétal). Mais **les réponses
  ne changent pas** : 64 % de réponses positives avec « MoMA », 59 % avec l'autre étiquette,
  différence non significative (t(16) = 1,20, p = 0,246). Les auteurs écrivent qu'ils n'ont pas
  pu reproduire le résultat comportemental de Kirk et al.
  → **Leçon** : un contexte peut changer le **traitement** (mesure indirecte) sans changer le
  **jugement déclaré**. Ou l'inverse. Il faut mesurer les deux.
- **Gerger, Leder & Kremer (2014)** [résumé lu]. Images émotionnelles (photos de la base
  IAPS) et vraies œuvres, présentées comme « œuvre d'art » ou « photo de presse ». Mesures :
  émotions déclarées **et** activité des muscles du visage (électromyographie : zygomatique
  pour le sourire, corrugateur pour le froncement). Dans le contexte « art », la joie et le
  zygomatique **baissent** ; les émotions négatives ne changent presque pas ; seules les œuvres
  au contenu **négatif** sont plus aimées. Interprétation : l'art installe une **distance**.
- **Papenmeier, Dagit, Wagner & Schwan (2024)** [résumé lu]. Images choisies pour être
  ambiguës (vraies œuvres et vraies images scientifiques). Un groupe entend « ce sont des
  œuvres », l'autre « ce sont des images scientifiques ». Le **regard** (oculomètre) dépend du
  vrai type d'image, **pas** de l'étiquette. L'étiquette « art » ne change ni le sens perçu
  ni la complexité, et **fait baisser** un peu l'appréciation. Conclusion des auteurs : l'effet
  vient surtout de l'image, pas d'un « schéma art ».
- **Newman, Bartels & Smith (2014)** [résumé lu]. Le simple fait de classer un objet comme
  « œuvre » plutôt que « outil » change les intuitions sur sa **persistance** (est-ce encore
  le même objet après réparation ?). Les œuvres sont pensées comme des **prolongements de leur
  auteur**, un peu comme des personnes.

**Bilan.** Dire « c'est de l'art » ne fait pas monter la valeur de manière fiable. L'effet le
plus solide n'est pas « plus beau » mais **« autrement regardé »** : plus de distance, plus
de temps, un autre traitement cérébral. Pour une machine, la question devient : l'étiquette
« art » change-t-elle **la description** (mots, attention, ce qui est nommé) même quand elle
ne change pas **la note** ?

### 6.5 Le titre et l'information (cartel en mots)

- **Millis (2001)** [résumé lu]. Trois expériences. Un titre **métaphorique** augmente
  l'expérience esthétique plus qu'un titre descriptif ou que l'absence de titre (« effet
  d'élaboration »). **Point clé pour notre sujet** : l'effet se produit **que les
  participants croient le titre vrai ou faux**. Un titre au hasard baisse la compréhension
  mais pas l'expérience. → Le contexte agit même quand on **sait** qu'il est arbitraire.
- **Russell (2003)** [résumé lu]. Titres et descriptions augmentent le **sens perçu** dans
  deux expériences ; ils augmentent la **valeur hédonique** seulement dans le plan **intra
  sujets** (chaque personne voit les deux conditions), pas dans le plan **entre sujets**.
  L'auteur suggère que le plan entre sujets est moins sensible. → **Leçon de méthode
  majeure** (voir §7) : le résultat dépend du plan d'expérience.
- **Leder, Carbon & Ripsas (2006)** [résumé lu]. Titres élaboratifs ou descriptifs, avec
  plusieurs temps de présentation (1 s, 10 s, 90 s). À 90 s, les titres élaboratifs
  augmentent la **compréhension** des peintures abstraites mais pas l'appréciation. À 1 s, le
  titre descriptif aide plus ; à 10 s, le titre élaboratif aide plus. → Le contexte agit
  **dans le temps** ; il faut environ 10 s pour qu'un sens « au-delà de la description » se
  forme.
- **Swami (2013)** [résumé lu]. Peintures de Max Ernst et Picasso. Une information riche et
  spécifique augmente compréhension et appréciation des œuvres **abstraites**, pas des œuvres
  figuratives ; une information hors sujet n'aide pas. La compréhension perçue **médiatise**
  entièrement l'effet.
- **Jucker, Barrett & Wlodarski (2014)** [résumé lu]. 505 adultes, quatre expériences.
  L'**intention supposée de l'artiste** sert à décider si un objet est de l'art (exp. 1) ;
  des titres qui clarifient le message augmentent compréhension et appréciation ; un
  **investissement** élevé de l'artiste augmente l'appréciation.
- **Szubielska & Imbir (2021)**, voir §6.2 : le texte du commissaire aide à comprendre, pas à
  aimer.

**Bilan.** L'information agit surtout par la **compréhension**, et surtout pour l'art
**abstrait** ou ambigu. C'est cohérent avec l'idée générale de la persuasion : un indice
périphérique pèse plus quand le stimulus est ambigu (Koniak & Szubielska le rappellent). **Le
ticket de caisse encadré est un stimulus ambigu par construction** ; c'est là qu'on attend le
plus grand effet de contexte, chez l'humain comme chez la machine.

### 6.6 Le nom, l'original, la contagion

- **Cleeremans, Ginsburgh, Klein & Noury (2016)** [résumé lu]. 40 étudiants (20 en
  psychologie, 20 en histoire de l'art) classent 12 tableaux, certains avec le nom de
  l'artiste. Le nom fait monter le classement chez les psychologues, **mais seulement s'ils
  ont fait attention au nom** ; chez les historiens de l'art, c'est leur **connaissance** de
  l'artiste qui compte. → Pour un non-expert, le nom est une **heuristique** de valeur.
- **Huang, Bridge, Kemp & Parker (2011)** [résumé lu]. Portraits de Rembrandt étiquetés
  « authentique » ou « copie » indépendamment de la vérité. L'étiquette « copie » active plus
  le cortex frontopolaire ; **pas d'effet direct sur les aires visuelles**.
- **Wolz & Carbon (2014)** [résumé lu]. Répliques d'œuvres d'artistes connus étiquetées
  « original » ou « copie » : l'étiquette « copie » fait baisser la qualité perçue **et même
  le talent attribué à l'artiste**.
- **Newman & Bloom (2012)** [résumé lu]. Cinq expériences avec des **scénarios
  hypothétiques**. La valeur de l'original tient à deux choses : l'œuvre comme **acte
  créatif unique** (« performance ») et le **contact physique** avec l'artiste
  (« contagion »).
- **Newman, Diesendruck & Bloom (2011)** : un objet ayant appartenu à une célébrité vaut plus
  s'il a été **touché** par elle. Une **réplication préenregistrée** (Chan, Jin, Chen, Peng,
  Charlton & Feldman, Registered Report recommandé par *Peer Community in Registered Reports*
  en 2026) existe ; **je n'ai pas pu lire ses résultats**.
- **Smith, Newman & Dhar (2016)** [résumé lu]. Dans une série limitée, les gens préfèrent les
  **petits numéros** (n° 3/100 plutôt que 97/100), parce qu'ils semblent **plus proches dans
  le temps** de l'artiste (« contagion temporelle »). Données d'archives et cinq expériences.
  L'effet ne dépend pas de la qualité supposée ni de la valeur de revente attendue.
- **Kruger, Wirtz, Van Boven & Altermatt (2004)**, « l'heuristique de l'effort » : un poème ou
  un tableau présenté comme ayant demandé **plus de temps** est jugé meilleur et plus cher.
  [**contenu non lu** : résumé non disponible ; détails connus seulement par des sources
  secondaires, je ne donne pas de chiffres]

**Lien avec le cadre.** Un cadre ancien est aussi un **objet touché par le passé**. La
contagion temporelle de Smith et al. suggère une hypothèse : le cadre ancien vaudrait parce
qu'il **rapproche le contenu d'une origine prestigieuse**. Une machine qui date le cadre au
XVIIIe siècle et imagine « un musée » fait peut-être exactement ce raisonnement.

### 6.7 Le prix et le prestige

- **Plassmann, O'Doherty, Shiv & Rangel (2008)** [résumé lu]. Le même vin, annoncé à des prix
  différents, en IRMf. Un prix plus élevé augmente **le plaisir déclaré** et l'activité du
  cortex orbitofrontal médian. → Le prix ne change pas seulement le jugement, il change
  **l'expérience** (au moins sa trace cérébrale).
- **Schmidt, Skvortsova, Kullen, Weber & Plassmann (2017)** [résumé lu] : même paradigme,
  même laboratoire ; l'effet du prix passe par le **système de valuation** du cerveau.
  (Réplication **dans le même laboratoire**, donc pas indépendante.)
- **Almenberg & Dreber (2011)** [résumé lu] : réplication **indépendante** sur le terrain.
  Annoncer un prix **élevé avant** la dégustation augmente les notes, **mais seulement chez
  les femmes** ; annoncer un prix bas ne fait pas baisser les notes. → L'effet existe mais il
  est **plus étroit** que le résultat original ne le laissait penser.
- **Lauring, Pelowski, Forster, Gondan, Ptito & Kupers (2016)** [résumé lu]. 187 étudiants,
  90 tableaux. Un prix fictif élevé fait aimer davantage ; une note positive donnée par des
  pairs ou par des experts aussi. Mais quand un groupe de jeunes à **faible revenu et faible
  éducation** a **mal** noté un tableau, les participants l'aiment **davantage**. L'effet
  dépend de l'intérêt pour l'art et de l'identification aux groupes. Les auteurs y voient la
  « distinction » de Bourdieu, mesurée.
- **Hagtvedt & Patrick (2008)** [résumé lu], « art infusion » : la présence d'une œuvre d'art
  sur un emballage, une publicité ou un produit améliore l'évaluation du produit, par un
  **transfert de luxe indépendant du contenu** de l'œuvre. Trois études, terrain et
  laboratoire. → **C'est l'inverse de notre question** (l'art valorise l'objet ordinaire au
  lieu que le cadre valorise l'art), mais le mécanisme est le même : un **signe de luxe** se
  transfère à ce qui l'entoure. Le cadre doré serait un « luxe infusé » dans le contenu.

### 6.8 L'attribution « IA » contre « humain »

C'est le domaine le plus actif depuis 2018, et le mieux répliqué. Le protocole type : **les
mêmes images**, étiquetées au hasard « faite par un humain » ou « faite par une IA ».

| étude | protocole | résultat |
| --- | --- | --- |
| Chamberlain, Mullin, Scheerlinck & Wagemans 2018 [résumé lu] | discrimination puis catégorisation ; étude 2 avec art robotique | biais contre l'art « par ordinateur » ; il **s'inverse** quand on voit le robot travailler |
| Hong & Curran 2019 [résumé lu] | 288 personnes, 6 œuvres, identité de l'artiste contrôlée | l'étiquette seule **ne change pas** en général la valeur ; ce qui compte, c'est la croyance préalable « une IA ne peut pas faire d'art » |
| Ragot, Martin & Cojean 2020 [résumé lu] | 565 personnes, entre sujets | œuvres dites « humaines » mieux notées sur les quatre dimensions |
| Millet, Buehler, Du & Kokkoris 2023 [résumé lu] | 4 expériences, N = 1 708, dont une **préenregistrée** de grande puissance | même œuvre moins aimée avec l'étiquette IA ; passe par moins de créativité perçue et moins d'**émerveillement** (« awe ») ; plus fort chez ceux qui pensent la créativité réservée à l'humain |
| Bellaiche, Shahi, Turpin et al. 2023 [résumé lu] | images toutes faites par IA, étiquette tirée au hasard ; 2 études | « humain » mieux noté sur aimer, beauté, profondeur, **valeur** (« Worth ») ; réplication interne ; l'**effort** et le **récit** perçus modèrent l'effet |
| Di Dio, Ardizzi, Schieppati, Massaro, Gilli & Gallese 2023 (en ligne ; numéro 2025) [résumé lu indirectement] | peintures abstraites ; humain, robot, ou pas d'information | « humain » plus aimé quand c'est dit ; « robot » jugé moins beau qu'à l'aveugle |
| Zhou & Kawabata 2023 [résumé lu] | oculomètre + notes | **aucun effet dans les notes**, mais on regarde **plus longtemps** les tableaux crus humains → biais **implicite** |
| Messer 2024 [résumé lu] | 3 expériences, N = 560 ; co-création artiste + IA à différentes étapes | l'art co-créé est moins aimé, surtout si l'IA intervient dans l'exécution ; perçu comme plus nouveau mais moins **authentique** ; l'effet faiblit pour les images commerciales |

**Ce qui est établi.** Un biais anti-IA dans le jugement déclaré, répliqué dans plusieurs pays
et laboratoires, avec au moins une étude préenregistrée. **Ce qui est discuté.** Sa taille et
ses conditions : il disparaît parfois (Hong & Curran), s'inverse quand on humanise la machine
(Chamberlain), n'apparaît que dans le regard (Zhou & Kawabata). **Mécanisme le plus
souvent avancé** : l'œuvre est valorisée comme trace d'un **acte humain** (effort, intention,
récit), ce qui rejoint Newman & Bloom (« performance ») et Jucker et al. (intention).

---

## 7. Comment on prouve qu'un contexte agit « à l'insu » de quelqu'un

C'est la partie la plus utile pour transposer aux machines. Je rassemble les critères que
les études ci-dessus utilisent, souvent sans les nommer.

### 7.1 Le problème : on ne peut pas croire ce que les gens disent de leurs raisons

**Nisbett & Wilson (1977)** [titre et thèse connus ; contenu non relu] : les gens n'ont souvent
**pas accès** aux causes réelles de leurs jugements. Quand on leur demande pourquoi, ils
donnent une explication **plausible**, pas l'explication **vraie**. Conséquence : pour établir
qu'un contexte agit à l'insu de quelqu'un, il faut **deux choses** : (1) prouver que le
contexte change le jugement ; (2) prouver que la personne **ne le mentionne pas** ou **nie**
son influence.

**Orne (1962)** [référence connue ; publication originale dans *American Psychologist* 17(11)
**non vérifiée** ; réédition vérifiée] : les participants devinent ce que l'expérimentateur
attend (« caractéristiques de la demande ») et s'y conforment. Si l'on demande « ce cadre
change-t-il votre jugement ? », on **crée** l'effet qu'on veut mesurer. Koniak & Szubielska
écrivent la même chose : demander les intentions du cadreur « peut augmenter artificiellement
la méfiance ».

### 7.2 Les critères, un par un

| critère | ce qu'on fait chez l'humain | exemple | équivalent pour une machine |
| --- | --- | --- | --- |
| **1. Stimulus identique** | seul le contexte change ; l'image est la même au pixel près | Kirk ; Bellaiche ; Koniak (cadre ajouté autour, surface constante) | même contenu, même taille, même position ; seul le cadre ou le cartel change |
| **2. Attribution aléatoire de l'étiquette** | l'étiquette est tirée au sort, indépendamment de la vérité | Kirk ; Huang (« copie » sans rapport avec la vraie authenticité) ; Bellaiche | tirage au sort de quelle image reçoit quel cadre ; plusieurs contenus par case |
| **3. Plan entre sujets** | chaque personne ne voit qu'**une** condition, pour qu'elle ne compare pas | Brieber 2015 ; Koniak ; Ragot | **une session neuve par image**, sans historique ; jamais deux versions dans le même échange |
| **4. Ou plan intra-sujets, assumé** | chaque personne voit toutes les conditions ; plus sensible mais révèle la manipulation | Russell 2003 (effet trouvé seulement en intra) | montrer les deux versions côte à côte : mesure de **ce que la machine fait quand elle compare**, pas de ce qu'elle fait seule |
| **5. Masquer le but** | questions leurres, consigne qui ne nomme pas le contexte | Koniak (5 questions leurres) | questionnaire qui ne parle jamais du cadre (déjà la règle du pilote) ; questions leurres |
| **6. Contrôle de l'attention à l'indice** | vérifier que l'indice a été vu | Cleeremans (effet du nom seulement si le nom a été remarqué) | demander **après coup** de décrire l'image : le cadre est-il nommé ? |
| **7. Croyance dans l'indice** | dire que l'étiquette est fausse ou aléatoire et voir si l'effet persiste | Millis (effet même si le titre est cru faux) ; proposition de Koniak (cadre « choisi au hasard ») | ajouter « le cadre a été choisi au hasard » dans la consigne ; si le prix ne bouge pas, l'effet est **automatique** |
| **8. Interrogatoire en entonnoir** | questions de plus en plus précises à la fin : « qu'avez-vous remarqué ? », « pensez-vous que X a joué ? » | Bargh & Chartrand (méthode classique en psychologie sociale) [contenu non lu] | même entonnoir en fin de session ; comparer ce qui est dit à ce qui a été fait |
| **9. Mesure indirecte** | regard, temps, muscles du visage, activité cérébrale, temps de réponse | Brieber (temps) ; Zhou (regard) ; Gerger (EMG) ; Kirk, Silveira (IRMf) | probabilités des mots (logprobs) ; carte d'attention ; prix sans justification ; tâche de choix forcé entre deux images |
| **10. Dissociation explicite/implicite** | l'effet est dans la mesure indirecte mais pas dans la note (ou l'inverse) | Silveira ; Zhou & Kawabata | l'effet est dans le prix mais pas dans la justification (Turpin, Chen) |
| **11. Modérateurs** | expertise, intérêt pour l'art | Koniak ; Cleeremans ; Gartus | rôle demandé (« conservateur », « antiquaire », « débutant ») ; modèles de familles différentes |
| **12. Préenregistrement et réplication** | hypothèses et analyses déposées avant ; réplication indépendante | Millet (étude préenregistrée) ; Almenberg & Dreber ; Grüner | déposer le plan d'analyse avant de lancer ; refaire avec un autre modèle et d'autres images |

### 7.3 L'équivalent machine du problème de Nisbett & Wilson existe déjà

Deux études montrent que les modèles de langage, comme les humains, **ne disent pas toujours
ce qui a causé leur réponse** :

- **Turpin, Michael, Perez & Bowman (2023)** [résumé lu]. On ajoute un **indice biaisant**
  (par exemple : dans les exemples donnés, la bonne réponse est toujours « (A) »). Les modèles
  suivent l'indice **sans le mentionner** dans leur raisonnement écrit ; ils fabriquent une
  justification. La précision baisse jusqu'à 36 % sur 13 tâches. Sur une tâche de biais
  social, les explications justifient des réponses stéréotypées sans mentionner le stéréotype.
- **Chen, Benton, Radhakrishnan et al. (2025)** [résumé lu]. Sur des modèles de raisonnement,
  le raisonnement écrit **révèle** l'usage de l'indice dans au moins 1 % des cas où il est
  utilisé, mais souvent **moins de 20 %**.

**Conséquence directe pour punctured sky.** Si le prix d'un ticket monte avec le cadre rococo
et que la justification écrite du modèle **ne parle pas du cadre** (ou parle d'autre chose),
on a l'équivalent machine d'un **effet de contexte à l'insu**. Si la justification **parle du
cadre** (« le cadre ancien suggère… »), l'effet est **déclaré** : c'est un raisonnement, pas un
biais caché. Le pilote est plutôt dans le second cas (Claude date le cadre à part, parle d'un
« cadre d'antiquaire »). Il faut donc **coder les justifications** selon ce critère, image par
image.

### 7.4 Ce qui ne se transpose pas

- **La conduite** (temps de regard, déplacement dans la salle, retour devant l'œuvre). Une
  machine n'a pas de corps. Le temps de calcul n'est pas un temps de regard.
- **L'expérience** au sens de Plassmann (le vin a meilleur goût). On ne peut mesurer chez la
  machine que **la sortie** et ses **états internes**, pas un plaisir.
- **La croyance au sens strict.** Une consigne « le cadre a été choisi au hasard » n'est pas
  « crue » par un modèle comme par une personne. On teste seulement si cette phrase **change
  la sortie**.

---

## 8. Les biais de valorisation des modèles de langage et vision-langage

### 8.1 Ce qui existe

- **Haverals & Martin (2025)** [résumé lu]. Exercices de style de Queneau contre versions
  écrites par GPT-4 ; trois conditions : à l'aveugle, étiquette vraie, étiquette **inversée**.
  556 humains, 13 modèles. Biais pro-« humain » de +13,7 points chez les humains
  (h de Cohen = 0,28) et de **+34,3 points chez les modèles** (h = 0,70), soit environ 2,5
  fois plus. Dans une seconde étude (14 modèles évaluateurs × 14 modèles auteurs), le biais
  tient (+25,8 points). **Les étiquettes inversent les critères** : le même trait est loué ou
  blâmé selon l'auteur supposé. C'est le protocole le plus proche de ce que punctured sky veut
  faire, mais pour du texte, pas des images.
- **Laurito, Davis, Grietzer, Gavenčiak, Böhm & Kulveit (2025)** [résumé lu]. Inverse : des
  modèles de langage préfèrent un produit présenté dans une **prose écrite par un modèle**
  plutôt que par un humain. → Les modèles ont des préférences d'**identité** qui ne viennent
  pas du contenu.
- **Panickssery, Bowman & Feng (2024)** [résumé lu]. Les modèles évaluateurs **reconnaissent
  et favorisent leurs propres textes** ; la force de la reconnaissance prédit la force de la
  préférence.
- **Koo et al. (2024)** [résumé lu]. Banc d'essai de six biais cognitifs chez 16 modèles
  utilisés comme juges ; indices de biais dans environ 40 % des comparaisons.
- **Echterhoff, Liu, Alessa, McAuley & He (2024)** [contenu non lu] : biais cognitifs dans les
  décisions assistées par modèle.
- **Binz & Schulz (2023)** [résumé lu]. Méthode générale : passer les **expériences classiques
  de psychologie cognitive** à un modèle. De petites perturbations des énoncés peuvent le
  dérouter fortement. → C'est la méthode que propose ce volet, appliquée à l'esthétique.
- Rappels de la note précédente : Vo et al. 2025 (les modèles vision-langage préfèrent ce
  qu'ils savent à ce qu'ils voient) ; Mei et al. 2025 (l'image ne compte que pour les œuvres
  sans historique de vente) ; Singh, Bhatia & Joshi 2026 (audit de valorisation par CLIP sur
  1 500 objets du Met) ; Lou & Sun 2024 (ancrage chez les modèles de langage).

### 8.2 Ce que je n'ai pas trouvé

- **Aucune étude** qui fait varier, devant un modèle vision-langage, **le cadre matériel**,
  **le cartel** ou **la provenance** d'une même image, et mesure un **prix** ou un **statut
  d'art**. Le pilote de punctured sky semble être seul sur ce point.
- **Aucune étude** qui transpose à un modèle les paradigmes musée/labo, titre élaboratif
  (Millis, Leder 2006) ou contagion (Newman & Bloom) avec des images.
- **Le chiffre « +54 % » de Li 2024** : il est **vérifiable**, mais il concerne la
  provenance dans les **catalogues de ventes aux enchères** et les prix réels, pas un biais de
  modèle. Il ne faut pas le citer comme un résultat sur les machines.
- **Limite de ma recherche** : le budget de recherches web de la session a été épuisé en cours
  de travail. Les vérifications ont continué par les bases bibliographiques (Crossref,
  OpenAlex, Europe PMC, Open Library) et par lecture directe de pages connues, mais je n'ai
  pas pu balayer de nouveau arXiv pour 2026. **Une étude récente sur le prix d'œuvres estimé
  par des modèles vision-langage a pu m'échapper.** À refaire avant toute publication.

---

## 9. Synthèse

### 9.1 Ce qui est établi

1. **La valeur d'une œuvre dépend de ce qui l'entoure** : acquis commun à la philosophie, la
   sociologie, l'économie et la muséologie.
2. **Chez l'humain, les étiquettes en mots changent les jugements** (nom, authenticité, prix,
   humain/IA) ; le biais anti-IA est le mieux répliqué.
3. **Le contexte agit surtout sur l'ambigu** (abstrait, conceptuel, non-experts), et plus sur
   l'expérience et la compréhension que sur la perception.
4. **On sait comment prouver un effet à l'insu** (§7.2).
5. **Les modèles de langage reproduisent, parfois en l'amplifiant, un biais d'attribution
   humain**, et **ne disent pas toujours** ce qui a guidé leur réponse.

### 9.2 Ce qui est débattu

1. **Le cadre matériel valorise-t-il ?** La théorie (luxe, Boltanski & Esquerre, art
   infusion) dit oui ; la seule expérience (Koniak & Szubielska) dit non, pour l'art abstrait
   et des étudiants polonais en ligne. Mécanisme proposé : la **méfiance envers la
   promotion**.
2. **L'effet « musée » est-il robuste ?** Oui dans la plupart des études ; non dans Brieber,
   Leder & Nadal 2015 ; plus faible que l'effet du style (Grüner 2019).
3. **Les étiquettes « art » ou « galerie » changent-elles la note ?** Kirk oui ; Silveira non
   (seulement le cerveau) ; Papenmeier : légèrement **vers le bas**.
4. **Statut contre valeur.** Les théories parlent du statut ; les expériences mesurent la
   valeur. La question « est-ce de l'art ? » est rarement mesurée directement.
5. **Méconnaissance (Bourdieu) ou valeurs déclarées (Heinich) ?** Faut-il chercher ce que
   l'acteur fait sans le savoir, ou ce qu'il dit valoriser ? Pour une machine, les deux sont
   mesurables séparément.
6. **Réplications** : Plassmann n'a été répliqué indépendamment que partiellement (Almenberg
   & Dreber : seulement chez les femmes, seulement pour le prix haut annoncé avant).
   Newman et al. 2011 fait l'objet d'un Registered Report en 2026 dont je n'ai pas lu les
   résultats.

### 9.3 Les angles morts

1. **Presque rien sur le cadre matériel.** Une seule expérience, en ligne, sur l'abstraction,
   sans réplication. Rien sur les cadres anciens contre neufs, sur la dorure contre
   l'ornement, sur le cadre autour d'un objet banal.
2. **Rien sur la provenance écrite au cartel** comme variable expérimentale (seulement des
   données de marché).
3. **Les participants sont surtout des étudiants occidentaux** (Koniak : 98 étudiants ;
   Lauring : 187 étudiants ; Cleeremans : 40 étudiants). La « distinction » de Bourdieu n'a
   presque jamais été testée sur des publics de classes sociales différentes.
4. **Les études musée/labo comparent un vrai lieu à une image sur écran.** Elles ne disent pas
   ce que fait **une photo de musée** (cadre, mur, cartel visibles) par rapport à **la même
   œuvre détourée**. Or c'est exactement la situation de la machine, et aussi celle de
   l'humain qui regarde une reproduction en ligne.
5. **Les reproductions numériques et leurs cadres** (fond blanc, détourage, bord de l'écran,
   watermark de musée) ne sont pas étudiés comme cadres.
6. **Peu de mesures du statut** (« est-ce de l'art ? ») à côté des mesures de valeur.
7. **Aucune comparaison humain/machine sur la même tâche visuelle de valorisation.** Haverals
   & Martin le font pour le texte littéraire seulement.

### 9.4 Problèmes qu'on pourrait poser aux machines

Je formule des **problèmes**, pas des résultats. Aucun n'a été testé ici. Chacun reprend un
protocole humain précis.

1. **Le problème de Koniak, inversé.** Mêmes conditions que Koniak & Szubielska (dix
   peintures abstraites, sans cadre / cadre simple / cadre décoratif, surface constante,
   indice en quatre questions + questions leurres), posées à plusieurs modèles. Puis les mêmes
   cadres autour de contenus **banals** (ticket, dessin d'enfant). Question : le modèle
   pénalise-t-il le cadre décoratif autour de l'abstraction (comme les humains) et le
   récompense-t-il autour du banal (comme Claude dans le pilote) ? Si oui, il a appris une
   règle de **convenance** (quel cadre va avec quoi), pas un simple signal de luxe.
2. **Le test d'intention de Koniak.** Ajouter à la consigne : « le cadre a été choisi au hasard
   par un ordinateur » / « le cadre a été choisi par un employé d'une maison de ventes » /
   rien. Si le prix ne change pas avec ces phrases, l'effet du cadre est **automatique** (un
   signal visuel). S'il change, le modèle raisonne sur **l'intention** du cadreur : c'est
   l'« interprétation sociale » du rococo.
3. **Le critère de Nisbett & Wilson pour machines.** Pour chaque réponse où le prix change avec
   le cadre, coder si la justification **mentionne** le cadre. Proportion d'effets
   « non dits » par modèle. Comparer avec les taux de Chen et al. (souvent sous 20 %).
4. **Le rôle social (Bourdieu, Lauring).** Même image, rôles différents dans la consigne
   (« conservateur de musée », « antiquaire », « étudiant en art contemporain »). Le sens du
   cadre doré change-t-il de signe selon le rôle ? Un modèle qui a appris la structure du
   champ devrait faire baisser le doré chez le critique contemporain et le monter chez
   l'antiquaire.
5. **La provenance au cartel (Li, Ma & Renneboog ; Boltanski & Esquerre).** Même ticket, même
   cadre noir fin, cartel photographié avec une provenance fictive (« ancienne collection
   X ») contre un cartel neutre. Mesurer prix et propriétaire imaginé. C'est aussi
   **l'expérience humaine qui manque** (angle mort 2) : la faire en parallèle.
6. **Le titre élaboratif (Millis ; Leder 2006).** Même image, cartel avec titre descriptif,
   métaphorique, ou au hasard. Prédiction humaine : le métaphorique augmente l'expérience,
   **même s'il est dit faux**. La machine fait-elle pareil ?
7. **La contagion (Newman & Bloom ; Smith, Newman & Dhar).** Même tirage, numéroté 3/100 ou
   97/100 sur le cartel ; « touché par l'artiste » ou non. Les modèles reproduisent-ils une
   intuition de contagion que rien dans l'image ne justifie ?
8. **L'attribution IA/humain sur image (Bellaiche ; Millet ; Haverals).** Même image,
   cartel « peint par un artiste » ou « généré par une IA ». Mesurer aimer, valeur, statut.
   Prédiction à tester : amplification du biais humain, comme pour le texte.
9. **Statut contre valeur (Dickie contre le marché).** Poser toujours séparément « est-ce de
   l'art ? » et « combien cela vaut-il ? », et chercher les cas où ils divergent. Le pilote en
   a déjà trouvé un (Claude : prix haut, statut « incertain »).
10. **Le plan entre/intra sujets (Russell 2003).** Comparer une session par image (entre
    sujets) et deux images côte à côte (intra). Si l'effet du cadre n'apparaît qu'en
    comparaison directe, il n'est pas « à l'insu » ; il est **comparatif**.

Pour tous : plusieurs contenus par case (au moins 10), plusieurs familles de modèles, plan
d'analyse déposé avant de lancer, et la même tâche passée par des humains quand c'est
possible (outil `human_study/`).

---

## Bibliographie

Une ligne par référence. Le lien est celui qui a servi au contrôle. Statut entre crochets.

### Philosophie

- Danto, A. C. (1964). « The Artworld ». *The Journal of Philosophy* 61(19), 571-584. https://doi.org/10.2307/2022937 [vérifié ; de mémoire pour le contenu]
- Danto, A. C. (1981). *The Transfiguration of the Commonplace*. Harvard UP ; trad. fr. *La Transfiguration du banal*, Seuil, 1989. https://openlibrary.org/works/OL8034582W [vérifié ; de mémoire]
- Dickie, G. (1974). *Art and the Aesthetic: An Institutional Analysis*. Cornell UP. https://openlibrary.org/works/OL3281735W [vérifié ; définition via SEP]
- Dickie, G. (1984). *The Art Circle*. New York, Haven. https://openlibrary.org/works/OL3281732W [vérifié au catalogue ; contenu non lu]
- Levinson, J. (1979). « Defining Art Historically ». *British Journal of Aesthetics* 19(3), 232-250. https://doi.org/10.1093/bjaesthetics/19.3.232 [vérifié ; contenu non lu]
- Stanford Encyclopedia of Philosophy, « The Definition of Art ». https://plato.stanford.edu/entries/art-definition/ [vérifié dans la note précédente]

### Sociologie et économie de la valeur

- Becker, H. S. (1982). *Art Worlds*. University of California Press (éd. 25e anniversaire 2008). https://openlibrary.org/works/OL2674336W ; https://doi.org/10.1525/9780520934870 [vérifié ; de mémoire]
- Bourdieu, P. (1977). « La production de la croyance : contribution à une économie des biens symboliques ». *Actes de la recherche en sciences sociales* 13, 3-43. https://doi.org/10.3406/arss.1977.3493 [vérifié ; de mémoire]
- Bourdieu, P. (1979). *La Distinction. Critique sociale du jugement*. Minuit. https://openlibrary.org/works/OL527924W [vérifié ; de mémoire]
- Bourdieu, P. (1992). *Les Règles de l'art. Genèse et structure du champ littéraire*. Seuil. https://cataloguebib.enssib.fr/bib/27813 [vérifié dans la note précédente ; contenu non lu]
- Bourdieu, P., Darbel, A. (avec D. Schnapper) (1966). *L'Amour de l'art. Les musées et leur public*. Minuit. https://openlibrary.org/works/OL527971W [vérifié ; de mémoire]
- Heinich, N. (1991). *La Gloire de Van Gogh. Essai d'anthropologie de l'admiration*. Minuit ; trad. angl. 1996. https://doi.org/10.2307/2654063 (compte rendu de la trad. angl.) [vérifié ; de mémoire]
- Heinich, N. (1998). *Le Triple Jeu de l'art contemporain*. Minuit. https://openlibrary.org/works/OL1650549W [vérifié ; de mémoire]
- Heinich, N. (2014). *Le Paradigme de l'art contemporain*. Gallimard. https://openlibrary.org/works/OL23359397W [vérifié ; contenu non lu]
- Heinich, N. (2017). *Des valeurs. Une approche sociologique*. Gallimard. https://openlibrary.org/works/OL43553337W [vérifié ; contenu non lu]
- Heinich, N., Shapiro, R. (dir.) (2012). *De l'artification. Enquêtes sur le passage à l'art*. Éditions de l'EHESS. https://doi.org/10.4000/books.editionsehess.1098 [vérifié dans la note précédente]
- Moulin, R. (1967). *Le Marché de la peinture en France*. Minuit. https://openlibrary.org/works/OL3116124W ; compte rendu : https://doi.org/10.3917/rda.001.0148a [vérifié ; de mémoire]
- Moulin, R. (1992). *L'Artiste, l'institution et le marché*. Flammarion. https://doi.org/10.1017/s0395264900099273 (compte rendu) [vérifié dans la note précédente]
- Karpik, L. (2007). *L'Économie des singularités*. Gallimard ; trad. angl. *Valuing the Unique*, Princeton UP, 2010. https://openlibrary.org/works/OL3111339W [vérifié ; typologie de mémoire]
- Velthuis, O. (2005). *Talking Prices: Symbolic Meanings of Prices on the Market for Contemporary Art*. Princeton UP. https://doi.org/10.1515/9781400849406 [vérifié dans la note précédente]
- Beckert, J., Aspers, P. (dir.) (2011). *The Worth of Goods: Valuation and Pricing in the Economy*. Oxford UP. https://doi.org/10.1093/acprof:osobl/9780199594641.001.0001 [vérifié ; contenu non lu]
- Beckert, J., Rössel, J. (2013). « The Price of Art: Uncertainty and Reputation in the Art Field ». *European Societies* 15(2), 178-195. https://doi.org/10.1080/14616696.2013.767923 [vérifié dans la note précédente]
- Boltanski, L., Esquerre, A. (2017). *Enrichissement. Une critique de la marchandise*. Gallimard. https://doi.org/10.14375/np.9782072584770 ; compte rendu Gradoz, *Œconomia* 9(1), 2019 : https://doi.org/10.4000/oeconomia.5346 ; compte rendu Godechot : https://laviedesidees.fr/Tous-collectionneurs [vérifié]
- Li, Y., Ma, M., Renneboog, L. (2024). « In Art We Trust ». *Management Science* 70(1), 98-127. https://doi.org/10.1287/mnsc.2022.4633 [vérifié dans la note précédente]
- Beggs, A., Graddy, K. (2009). « Anchoring Effects: Evidence from Art Auctions ». *American Economic Review* 99(3), 1027-1039. https://doi.org/10.1257/aer.99.3.1027 [vérifié dans la note précédente]

### Musée, exposition, cartel

- O'Doherty, B. (1986). *Inside the White Cube: The Ideology of the Gallery Space*. Lapis Press ; éd. augmentée University of California Press. https://doi.org/10.1525/9780520923607-003 ; https://openlibrary.org/works/OL4126512W [vérifié ; de mémoire]
- Duncan, C. (1995). *Civilizing Rituals: Inside Public Art Museums*. Routledge. https://openlibrary.org/works/OL3503043W ; https://doi.org/10.4324/9780203978719 [vérifié ; de mémoire]
- Bennett, T. (1988). « The Exhibitionary Complex ». *New Formations* 4 [original non vérifié] ; repris dans Dirks, Eley & Ortner (dir.), *Culture/Power/History*, Princeton UP, 1994, p. 123-154. https://doi.org/10.1515/9780691228006-006 [reprise vérifiée ; de mémoire]
- Bennett, T. (1995). *The Birth of the Museum: History, Theory, Politics*. Routledge. https://openlibrary.org/works/OL2256007W [vérifié ; contenu non lu]
- Serrell, B. (1996 ; 2e éd. 2015). *Exhibit Labels: An Interpretive Approach*. AltaMira / Rowman & Littlefield. https://doi.org/10.5040/9798216405337 [vérifié ; contenu non lu]
- Smith, J. K., Smith, L. F. (2001). « Spending Time on Art ». *Empirical Studies of the Arts* 19(2), 229-236. https://doi.org/10.2190/5MQM-59JH-X21R-JN5J [résumé lu]
- Smith, L. F., Smith, J. K., Tinio, P. P. L. (2017). « Time spent viewing art and reading labels ». *Psychology of Aesthetics, Creativity, and the Arts* 11(1), 77-85. https://doi.org/10.1037/aca0000049 [vérifié ; contenu non lu]
- Carbon, C.-C. (2017). « Art Perception in the Museum: How We Spend Time and Space in Art Exhibitions ». *i-Perception* 8(1). https://doi.org/10.1177/2041669517694184 [résumé lu]
- Reitstätter, L., Galter, K., Bakondi, F. (2022). « Looking to Read: How Visitors Use Exhibit Labels in the Art Museum ». *Visitor Studies* 25(2), 127-150. https://doi.org/10.1080/10645578.2021.2018251 [résumé lu]

### Esthétique expérimentale : modèles

- Leder, H., Belke, B., Oeberst, A., Augustin, D. (2004). « A model of aesthetic appreciation and aesthetic judgments ». *British Journal of Psychology* 95(4), 489-508. https://doi.org/10.1348/0007126042369811 [résumé lu]
- Leder, H., Nadal, M. (2014). « Ten years of a model of aesthetic appreciation and aesthetic judgments: The aesthetic episode ». *British Journal of Psychology* 105(4), 443-464. https://doi.org/10.1111/bjop.12084 [résumé lu]
- Pelowski, M., Markey, P. S., Forster, M., Gerger, G., Leder, H. (2017). « Move me, astonish me… delight my eyes and brain: The Vienna Integrated Model of top-down and bottom-up processes in Art Perception (VIMAP) ». *Physics of Life Reviews* 21, 80-125. https://doi.org/10.1016/j.plrev.2017.02.003 [vérifié ; contenu non lu]
- Pelowski, M., Specker, E. (2020). « The General Impact of Context on Aesthetic Experience ». Dans *The Oxford Handbook of Empirical Aesthetics*, 885-920. https://doi.org/10.1093/oxfordhb/9780198824350.013.42 [vérifié ; contenu non lu]
- Specker, E., Forster, M., Brinkmann, H., Boddy, J., Pelowski, M., Rosenberg, R., et al. (2020). « The Vienna Art Interest and Art Knowledge Questionnaire (VAIAK) ». *Psychology of Aesthetics, Creativity, and the Arts* 14(2), 172-185. https://doi.org/10.1037/aca0000205 [vérifié ; contenu non lu]

### Esthétique expérimentale : musée, cadre, étiquette « art »

- Brieber, D., Nadal, M., Leder, H., Rosenberg, R. (2014). « Art in Time and Space: Context Modulates the Relation between Art Experience and Viewing Time ». *PLoS ONE* 9(6), e99019. https://doi.org/10.1371/journal.pone.0099019 [texte lu]
- Brieber, D., Nadal, M., Leder, H. (2015). « In the white cube: Museum context enhances the valuation and memory of art ». *Acta Psychologica* 154, 36-42. https://doi.org/10.1016/j.actpsy.2014.11.004 [résumé lu]
- Brieber, D., Leder, H., Nadal, M. (2015). « The Experience of Art in Museums: An Attempt to Dissociate the Role of Physical Context and Genuineness ». *Empirical Studies of the Arts* 33(1), 95-105. https://doi.org/10.1177/0276237415570000 [résumé lu]
- Grüner, S., Specker, E., Leder, H. (2019). « Effects of Context and Genuineness in the Experience of Art ». *Empirical Studies of the Arts* 37(2), 138-152. https://doi.org/10.1177/0276237418822896 [résumé lu]
- Gartus, A., Leder, H. (2014). « The white cube of the museum versus the gray cube of the street: The role of context in aesthetic evaluations ». *Psychology of Aesthetics, Creativity, and the Arts* 8(3), 311-320. https://doi.org/10.1037/a0036847 [vérifié ; contenu non lu]
- Gartus, A., Klemer, N., Leder, H. (2015). « The effects of visual context and individual differences on perception and evaluation of modern art and graffiti art ». *Acta Psychologica* 156, 64-76. https://doi.org/10.1016/j.actpsy.2015.01.005 [vérifié dans la note précédente]
- Szubielska, M., Imbir, K. (2021). « The aesthetic experience of critical art: The effects of the context of an art gallery and the way of providing curatorial information ». *PLOS ONE* 16(5), e0250924. https://doi.org/10.1371/journal.pone.0250924 [résumé lu]
- Szubielska, M., Imbir, K. (2022). « The Aesthetic Experience of Contemporary Installations in an Art Gallery and a Laboratory Setting: The Issue of Interactivity ». *Advances in Cognitive Psychology* 18(3), 179-189. https://doi.org/10.5709/acp-0360-7 [résumé lu]
- Locher, P., Smith, L., Smith, J. (2001). « The Influence of Presentation Format and Viewer Training in the Visual Arts on the Perception of Pictorial and Aesthetic Qualities of Paintings ». *Perception* 30(4), 449-465. https://doi.org/10.1068/p3008 [vérifié dans la note précédente]
- Locher, P., Dolese, M. (2004). « A Comparison of the Perceived Pictorial and Aesthetic Qualities of Original Paintings and Their Postcard Images ». *Empirical Studies of the Arts* 22(2), 129-142. https://doi.org/10.2190/EQTC-09LF-JRHA-XKJT [résumé lu]
- Koniak, P., Szubielska, M. (2022). « On the Peripheries of Contemporary Paintings: Impact of Frame Decorativeness on the Reception of Abstract Artwork ». *Roczniki Psychologiczne / Annals of Psychology* 25(2), 121-136. https://doi.org/10.18290/rpsych2022.0007 ; PDF : https://ojs.tnkul.pl/index.php/rpsych/article/view/16798/16344 [texte lu ; prénom du premier auteur non vérifié]
- Kirk, U., Skov, M., Hulme, O., Christensen, M. S., Zeki, S. (2009). « Modulation of aesthetic value by semantic context: An fMRI study ». *NeuroImage* 44(3), 1125-1132. https://doi.org/10.1016/j.neuroimage.2008.10.009 [résumé lu]
- Silveira, S., Fehse, K., Vedder, A., Elvers, K., Hennig-Fast, K. (2015). « Is it the picture or is it the frame? An fMRI study on the neurobiology of framing effects ». *Frontiers in Human Neuroscience* 9, 528. https://doi.org/10.3389/fnhum.2015.00528 [texte lu]
- Gerger, G., Leder, H., Kremer, A. (2014). « Context effects on emotional and aesthetic evaluations of artworks and IAPS pictures ». *Acta Psychologica* 151, 174-183. https://doi.org/10.1016/j.actpsy.2014.06.008 [résumé lu]
- Papenmeier, F., Dagit, G., Wagner, C., Schwan, S. (2024). « Is it art? Effects of framing images as art versus non-art on gaze behavior and aesthetic judgments ». *Psychology of Aesthetics, Creativity, and the Arts* 18(4), 642-653 (en ligne 2022). https://doi.org/10.1037/aca0000466 [résumé lu]
- Newman, G. E., Bartels, D. M., Smith, R. K. (2014). « Are Artworks More Like People Than Artifacts? Individual Concepts and Their Extensions ». *Topics in Cognitive Science* 6(4), 647-662. https://doi.org/10.1111/tops.12111 [résumé lu]

### Titre, information, intention

- Millis, K. (2001). « Making meaning brings pleasure: The influence of titles on aesthetic experiences ». *Emotion* 1(3), 320-329. https://doi.org/10.1037/1528-3542.1.3.320 [résumé lu]
- Russell, P. A. (2003). « Effort after meaning and the hedonic value of paintings ». *British Journal of Psychology* 94(1), 99-110. https://doi.org/10.1348/000712603762842138 [résumé lu]
- Leder, H., Carbon, C.-C., Ripsas, A.-L. (2006). « Entitling art: Influence of title information on understanding and appreciation of paintings ». *Acta Psychologica* 121(2), 176-198. https://doi.org/10.1016/j.actpsy.2005.08.005 [résumé lu]
- Swami, V. (2013). « Context matters: Investigating the impact of contextual information on aesthetic appreciation of paintings by Max Ernst and Pablo Picasso ». *Psychology of Aesthetics, Creativity, and the Arts* 7(3), 285-295. https://doi.org/10.1037/a0030965 [résumé lu]
- Jucker, J.-L., Barrett, J. L., Wlodarski, R. (2014). « "I Just Don't Get It": Perceived Artists' Intentions Affect Art Evaluations ». *Empirical Studies of the Arts* 32(2), 149-182. https://doi.org/10.2190/EM.32.2.c [résumé lu]

### Nom, authenticité, contagion, effort

- Cleeremans, A., Ginsburgh, V., Klein, O., Noury, A. (2016). « What's in a Name? The Effect of an Artist's Name on Aesthetic Judgments ». *Empirical Studies of the Arts* 34(1), 126-139. https://doi.org/10.1177/0276237415621197 [résumé lu]
- Huang, M., Bridge, H., Kemp, M. J., Parker, A. J. (2011). « Human Cortical Activity Evoked by the Assignment of Authenticity when Viewing Works of Art ». *Frontiers in Human Neuroscience* 5, 134. https://doi.org/10.3389/fnhum.2011.00134 [résumé lu]
- Wolz, S. H., Carbon, C.-C. (2014). « What's Wrong with an Art Fake? Cognitive and Emotional Variables Influenced by Authenticity Status of Artworks ». *Leonardo* 47(5), 467-473. https://doi.org/10.1162/LEON_a_00869 [résumé lu]
- Newman, G. E., Bloom, P. (2012). « Art and authenticity: The importance of originals in judgments of value ». *Journal of Experimental Psychology: General* 141(3), 558-569. https://doi.org/10.1037/a0026035 [résumé lu]
- Newman, G. E., Diesendruck, G., Bloom, P. (2011). « Celebrity Contagion and the Value of Objects ». *Journal of Consumer Research* 38(2), 215-228. https://doi.org/10.1086/658999 [vérifié ; contenu non lu]
- Chan, M., Jin, Y., Chen, E. Y., Peng, S., Charlton, A., Feldman, G. (2026). « Revisiting celebrity contagion and the value of objects: Replication and extension Registered Report of Newman et al. (2011) ». Recommandation PCI Registered Reports. https://doi.org/10.24072/pci.rr.101842 [existence vérifiée ; résultats non lus]
- Smith, R. K., Newman, G. E., Dhar, R. (2016). « Closer to the Creator: Temporal Contagion Explains the Preference for Earlier Serial Numbers ». *Journal of Consumer Research* 42(5), 653-668. https://doi.org/10.1093/jcr/ucv054 [résumé lu]
- Kruger, J., Wirtz, D., Van Boven, L., Altermatt, T. W. (2004). « The effort heuristic ». *Journal of Experimental Social Psychology* 40(1), 91-98. https://doi.org/10.1016/S0022-1031(03)00065-9 [vérifié ; contenu non lu]

### Prix, prestige, luxe

- Plassmann, H., O'Doherty, J., Shiv, B., Rangel, A. (2008). « Marketing actions can modulate neural representations of experienced pleasantness ». *PNAS* 105(3), 1050-1054. https://doi.org/10.1073/pnas.0706929105 [résumé lu]
- Schmidt, L., Skvortsova, V., Kullen, C., Weber, B., Plassmann, H. (2017). « How context alters value: The brain's valuation and affective regulation system link price cues to experienced taste pleasantness ». *Scientific Reports* 7, 8098. https://doi.org/10.1038/s41598-017-08080-0 [résumé lu ; numéro d'article non vérifié]
- Almenberg, J., Dreber, A. (2011). « When Does the Price Affect the Taste? Results from a Wine Experiment ». *Journal of Wine Economics* 6(1), 111-121. https://doi.org/10.1017/S1931436100001085 [résumé lu]
- Lauring, J. O., Pelowski, M., Forster, M., Gondan, M., Ptito, M., Kupers, R. (2016). « Well, if they like it… Effects of social groups' ratings and price information on the appreciation of art ». *Psychology of Aesthetics, Creativity, and the Arts* 10(3), 344-359. https://doi.org/10.1037/aca0000063 [résumé lu]
- Hagtvedt, H., Patrick, V. M. (2008). « Art Infusion: The Influence of Visual Art on the Perception and Evaluation of Consumer Products ». *Journal of Marketing Research* 45(3), 379-389. https://doi.org/10.1509/jmkr.45.3.379 [résumé lu]
- Friestad, M., Wright, P. (1994). « The Persuasion Knowledge Model: How People Cope with Persuasion Attempts ». *Journal of Consumer Research* 21(1), 1-31. https://doi.org/10.1086/209380 [vérifié ; contenu non lu]

### Attribution IA contre humain (jugements humains)

- Chamberlain, R., Mullin, C., Scheerlinck, B., Wagemans, J. (2018). « Putting the art in artificial: Aesthetic responses to computer-generated art ». *Psychology of Aesthetics, Creativity, and the Arts* 12(2), 177-192. https://doi.org/10.1037/aca0000136 [résumé lu]
- Hong, J.-W., Curran, N. M. (2019). « Artificial Intelligence, Artists, and Art ». *ACM Transactions on Multimedia Computing, Communications, and Applications* 15(2s), 1-16. https://doi.org/10.1145/3326337 [résumé lu]
- Ragot, M., Martin, N., Cojean, S. (2020). « AI-generated vs. Human Artworks. A Perception Bias Towards Artificial Intelligence? ». *CHI EA '20*, 1-10. https://doi.org/10.1145/3334480.3382892 [résumé lu]
- Millet, K., Buehler, F., Du, G., Kokkoris, M. D. (2023). « Defending humankind: Anthropocentric bias in the appreciation of AI art ». *Computers in Human Behavior* 143, 107707. https://doi.org/10.1016/j.chb.2023.107707 [résumé lu]
- Bellaiche, L., Shahi, R., Turpin, M. H., Ragnhildstveit, A., Sprockett, S., Barr, N., Christensen, A., Seli, P. (2023). « Humans versus AI: whether and why we prefer human-created compared to AI-created artwork ». *Cognitive Research: Principles and Implications* 8, 42. https://doi.org/10.1186/s41235-023-00499-6 [résumé lu ; numéro d'article confirmé par Europe PMC]
- Di Dio, C., Ardizzi, M., Schieppati, S. V., Massaro, D., Gilli, G., Gallese, V. (2023, numéro 2025). « Art made by artificial intelligence: The effect of authorship on aesthetic judgments ». *Psychology of Aesthetics, Creativity, and the Arts* 19(5), 1164-1176. https://doi.org/10.1037/aca0000602 [vérifié ; résumé connu par des dépôts institutionnels]
- Zhou, Y., Kawabata, H. (2023). « Eyes can tell: Assessment of implicit attitudes toward AI art ». *i-Perception* 14(5). https://doi.org/10.1177/20416695231209846 [résumé lu]
- Messer, U. (2024). « Co-creating art with generative artificial intelligence: Implications for artworks and artists ». *Computers in Human Behavior: Artificial Humans* 2(1), 100056. https://doi.org/10.1016/j.chbah.2024.100056 [résumé lu]

### Méthode : introspection, demande, mesures implicites

- Nisbett, R. E., Wilson, T. D. (1977). « Telling more than we can know: Verbal reports on mental processes ». *Psychological Review* 84(3), 231-259. https://doi.org/10.1037/0033-295X.84.3.231 [vérifié ; de mémoire]
- Orne, M. T. (1962). « On the social psychology of the psychological experiment: With particular reference to demand characteristics and their implications ». *American Psychologist* 17(11) [original non vérifié] ; réédition *Prevention & Treatment* 5, 2002 : https://doi.org/10.1037/1522-3736.5.0035a [réédition vérifiée ; de mémoire]
- Greenwald, A. G., Banaji, M. R. (1995). « Implicit social cognition: Attitudes, self-esteem, and stereotypes ». *Psychological Review* 102(1), 4-27. https://doi.org/10.1037/0033-295X.102.1.4 [vérifié ; de mémoire]
- Bargh, J. A., Chartrand, T. L. (2000 ; rééd. 2014). « The Mind in the Middle: A Practical Guide to Priming and Automaticity Research ». Dans Reis & Judd (dir.), *Handbook of Research Methods in Social and Personality Psychology*, Cambridge UP, 311-344 (éd. 2014). https://doi.org/10.1017/CBO9780511996481.017 [vérifié ; contenu non lu]
- Tversky, A., Kahneman, D. (1981). « The Framing of Decisions and the Psychology of Choice ». *Science* 211(4481), 453-458. https://doi.org/10.1126/science.7455683 [vérifié ; cité pour le sens psychologique de « framing »]

### Modèles de langage et vision-langage

- Haverals, W., Martin, M. (2025, rév. 2026). « The human-authorship halo: attribution bias in literary style evaluation by humans and AI ». arXiv:2510.08831. https://arxiv.org/abs/2510.08831 [résumé lu]
- Laurito, W., Davis, B., Grietzer, P., Gavenčiak, T., Böhm, A., Kulveit, J. (2025). « AI–AI bias: Large language models favor communications generated by large language models ». *PNAS* 122(31). https://doi.org/10.1073/pnas.2415697122 [résumé lu]
- Panickssery, A., Bowman, S. R., Feng, S. (2024). « LLM Evaluators Recognize and Favor Their Own Generations ». *NeurIPS 37*. arXiv:2404.13076. https://arxiv.org/abs/2404.13076 [résumé lu]
- Koo, R., Lee, M., Raheja, V., Park, J. I., Kim, Z. M., Kang, D. (2024). « Benchmarking Cognitive Biases in Large Language Models as Evaluators ». *Findings of ACL 2024*, 517-545. https://doi.org/10.18653/v1/2024.findings-acl.29 [résumé lu]
- Echterhoff, J., Liu, Y., Alessa, A., McAuley, J., He, Z. (2024). « Cognitive Bias in Decision-Making with LLMs ». *Findings of EMNLP 2024*, 12640-12653. https://doi.org/10.18653/v1/2024.findings-emnlp.739 [vérifié ; contenu non lu]
- Binz, M., Schulz, E. (2023). « Using cognitive psychology to understand GPT-3 ». *PNAS* 120(6). https://doi.org/10.1073/pnas.2218523120 [résumé lu]
- Turpin, M., Michael, J., Perez, E., Bowman, S. R. (2023). « Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting ». *NeurIPS 36*. https://doi.org/10.52202/075280-3275 [résumé lu]
- Chen, Y., Benton, J., Radhakrishnan, A., Uesato, J., Denison, C., Schulman, J., et al. (2025). « Reasoning Models Don't Always Say What They Think ». arXiv:2505.05410. https://arxiv.org/abs/2505.05410 [résumé lu]
- Vo, Nguyen, Taesiri, Dang, Nguyen, Kim (2025). « Vision Language Models are Biased ». arXiv:2505.23941. https://arxiv.org/abs/2505.23941 [vérifié dans la note précédente]
- Mei, J., Moses, M., Waelty, J., Yang (2025). « Deep Learning for Art Market Valuation ». arXiv:2512.23078. https://arxiv.org/abs/2512.23078 [vérifié dans la note précédente]
- Singh, Bhatia, Joshi (2026). « Disentangling Algorithmic Bias from Archival Artifacts: A Controlled Audit of Vision-Language Model Valuation in Metropolitan Museum Archives ». arXiv:2609.17572. https://arxiv.org/abs/2609.17572 [vérifié dans la note précédente]
- Lou, J., Sun, Y. (2024). « Anchoring Bias in Large Language Models: An Experimental Study ». arXiv:2412.06593. https://arxiv.org/abs/2412.06593 [vérifié dans la note précédente ; contenu non lu]
