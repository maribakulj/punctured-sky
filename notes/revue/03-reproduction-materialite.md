# Revue 03 — Reproduction, photographie d'art, matérialité des images, numérisation

*Volet 3 de la revue de littérature de punctured sky. Rédigé le 17/10/2026. Aucune expérience
ici, seulement de la lecture.*

**Comment lire les marques.** Chaque référence a été cherchée en ligne (notice d'éditeur, DOI,
catalogue de bibliothèque, page de revue). Le lien donné en bibliographie est celui qui a servi.

- Sans marque : titre, auteur, année et lieu de publication vérifiés.
- **[contenu non lu]** : la référence existe, mais je n'ai pas lu le texte. Le résumé vient
  d'un résumé d'éditeur, d'un compte rendu ou de la littérature secondaire.
- **[résumé de mémoire]** : texte classique que je résume de mémoire, sans l'avoir rouvert
  pour cette note. À relire avant toute citation.
- **[non vérifié]** : je n'ai pas pu confirmer la référence ou un détail (pages, DOI, date).

Le budget de recherche web de la session a été épuisé en fin de travail. Deux ou trois détails
(pages d'un recueil, un DOI) sont restés non vérifiés pour cette raison ; ils sont marqués.

Corrections faites à la commande en vérifiant :
- « Patricia Di Bello » s'écrit **Patrizia** Di Bello.
- Le texte de Leonardo Impett et Fabian Offert, « There Is a Digital Art History », est une
  prépublication arXiv d'**août 2023**, pas de 2022. Je n'ai trouvé aucune publication en revue.
- « From photo libraries to photo archives » de Costanza Caraffa est l'introduction du
  volume de **2011** (Deutscher Kunstverlag). Le livre *Photo-Objects* est un autre livre,
  de **2019** (Edition Open Access, Max Planck).
- Le travail de Helm et Kampel sur l'« overscan » porte sur des **films** numérisés
  (perforations de pellicule), pas sur des œuvres d'art.
- « The Great Unseen » (Smits et Asser, 2022) est l'**introduction d'un numéro spécial** de la
  revue néerlandaise *TMG Journal for Media History*, sur le photojournalisme et l'archive.

---

## En bref

1. **Personne, dans cette littérature, ne demande si le support « change le sens » en
   l'enlevant puis en le remettant.** Les auteurs montrent qu'un support compte en relevant des
   **traces** (tampons, annotations, découpes), des **usages** (classer, projeter, vendre), des
   **paratextes** (légendes, numéros, métadonnées) et des **circulations** (qui a copié quoi,
   où, pour qui). C'est un critère historique, pas un critère expérimental.
2. **La reproduction n'est pas un simple accès à l'œuvre. Elle fabrique un autre objet.**
   C'est la thèse commune, de Wölfflin (1896) à Caraffa (2019) et Arnold et Tilton (2026).
   Le cadrage, l'échelle, l'éclairage, le noir et blanc, le carton de montage, la mire de
   couleur : tout cela appartient à l'objet « reproduction ».
3. **Malraux a vu le premier que la photographie crée des « arts fictifs ».** Un détail
   agrandi, une monnaie photographiée comme une statue, deux œuvres de tailles différentes
   mises côte à côte à la même taille. Le cadre de la photo remplace le cadre de l'œuvre.
4. **L'histoire de l'art s'est construite sur des reproductions.** Projection de diapositives,
   comparaison de deux images (Wölfflin), photothèques. Nelson (2000), Fawcett (1983), Bohrer
   (2002), Dilly (1975-1979) montrent que la discipline pense *avec* ces supports.
5. **Les archives photographiques sont des objets, pas seulement des images.** Edwards et Hart
   (2004), Caraffa (2011, 2019), Kamin (2023), Mauuarin (2019, 2022), Blaschke (2016) le
   documentent : le carton, le dos, le classement, le prix, le droit font partie du sens.
6. **La numérisation est une interprétation.** Conway (2015), Prescott et Hughes (2018),
   Thylstrup (2018), Smits et Asser (2022) : le scan choisit ce qu'il garde (le dos ? le
   carton ? la mire ?), ce qu'il coupe, et comment il décrit.
7. **Les normes techniques (FADGI, Metamorfoze, ISO 19264, IIIF) organisent ce cadrage.** Elles
   disent comment mettre une mire dans le champ, comment rogner, comment découper une
   « région ». Elles fixent donc, sans le dire, ce qui est « l'œuvre » dans le fichier.
8. **Le droit fait aussi un cadre.** Une photo fidèle d'un tableau ancien n'est pas une œuvre
   protégée (Bridgeman c. Corel, 1999 ; directive européenne de 2019, art. 14). Le droit
   déclare donc que la reproduction n'ajoute rien. Les historiens disent le contraire.
9. **La vision par ordinateur commence à rencontrer ce problème.** Arnold et Tilton (2026)
   mesurent que le carton et les bords de pellicule couvrent 15 à 43 % des scans de la
   collection FSA-OWI, et que les modèles entraînés sur des images « sans bord » les voient mal.
   Impett et Offert (2023) disent que les grands modèles ont absorbé un canon visuel venu
   d'internet, donc de reproductions.
10. **Le problème que ce volet suggère pour punctured sky** : non pas « le cadre change-t-il la
    réponse ? », mais « la machine sait-elle lire le support comme un document ? ». Par
    exemple : dater la reproduction et non l'œuvre ; dire quelle institution a photographié ;
    compter les générations de copie. C'est mesurable sans inventer d'effet.

---

## 1. Pourquoi ce volet compte pour punctured sky

L'intuition de Marcel : le cadre isole le support et le rend déterminant ; cadre, écran, livre
s'emboîtent comme des poupées russes. Les expériences du dépôt testent ce que chaque
enveloppe fait à la lecture d'une machine. Le résultat actuel (README) : pour ces machines et
ces tâches, le support ne joue pas de rôle propre ; ce qui décide, c'est la **saillance** de
l'œuvre dans l'image.

Ce volet apporte trois choses.

- **Une histoire.** Les poupées russes ne sont pas une construction du chercheur. Elles
  existent dans les archives depuis 1850 : une statue, photographiée, tirée sur papier,
  collée sur un carton, tamponnée, classée, rephotographiée pour un livre, scannée, servie en
  IIIF, affichée sur un écran. Chaque étape a laissé des traces étudiées par des historiens.
- **Des critères.** Ces historiens ont des façons précises de dire qu'un support « compte ». Ce
  ne sont pas les mêmes que celles d'une expérience avec/sans cadre. Les connaître permet de
  savoir ce que nos tests mesurent, et ce qu'ils ne mesurent pas.
- **Un public.** Les institutions (photothèques, musées, consortium PHAROS, Getty) utilisent
  déjà la vision par ordinateur sur ces archives. Elles ont besoin de savoir si la machine
  « voit » le support ou l'efface. C'est une utilité concrète.

Le dépôt a déjà un fait qui rejoint cette littérature : sur 300 images de musée, seules 48
montrent l'œuvre sans rien autour (README, point 1). Les estampes et les photographies
arrivent avec leur feuille, leur montage et leurs inscriptions. C'est exactement l'objet que
Caraffa appelle « photo-objet ».

---

## 2. Les textes fondateurs : reproduire, c'est déjà interpréter

### 2.1 Walter Benjamin, « L'œuvre d'art à l'époque de sa reproduction mécanisée » (1936)

**[résumé de mémoire]** Version française publiée dans la *Zeitschrift für Sozialforschung*,
vol. 5, n° 1, 1936, dans une traduction de Pierre Klossowski revue par Benjamin. Il existe
plusieurs versions allemandes (1935-1939).

- **Thèse.** L'œuvre originale a une « aura » : son « ici et maintenant », son existence unique
  au lieu où elle se trouve. La reproduction technique détache l'œuvre de ce lieu et de cette
  tradition. Elle la fait venir vers le spectateur. La valeur de culte recule, la valeur
  d'exposition avance.
- **Ce qu'il dit du support.** Deux choses souvent oubliées. (a) La reproduction photographique
  peut montrer ce que l'œil ne voit pas (agrandir, choisir l'angle). Elle n'est donc pas une
  simple copie. (b) La perte de l'aura est liée au **lieu** : c'est le contexte, pas la
  matière, qui est perdu. Le cadre au sens large (église, palais, musée) fait partie de
  l'aura.
- **Ce qu'il permet d'observer.** Peu de chose directement. C'est un cadre de pensée. Mais il
  pose une question testable : une reproduction garde-t-elle des signes de son lieu d'origine ?

### 2.2 André Malraux, *Le Musée imaginaire* (1947, puis 1951 et 1965)

**[résumé de mémoire, pour le contenu]** Première partie de *Psychologie de l'art* (Skira,
1947), reprise dans *Les Voix du silence* (Gallimard, 1951), puis en volume « Idées/Arts »
(1965). Les éditions diffèrent.

- **Thèse.** La photographie et l'imprimerie mettent à notre disposition plus d'œuvres
  qu'aucun musée. Ce « musée imaginaire » change notre idée de l'art : il rapproche des
  objets de tous les temps et de tous les lieux, et les compare.
- **Ce qu'il dit du support et du cadre.** C'est le point fort. Malraux sait que la photo
  **cadre**, **éclaire**, **agrandit**, **isole**. Un détail de sculpture, photographié en gros
  plan, devient une œuvre autonome. Une monnaie agrandie ressemble à un bas-relief. Toutes les
  œuvres prennent la même taille sur la page. Le noir et blanc unifie des œuvres de couleurs
  différentes. Il appelle cela des **« arts fictifs »** : des arts que la reproduction invente.
  Malraux choisissait lui-même les prises de vue de ses livres (Zerner, cité par
  l'*Encyclopædia Universalis*).
- **Ce qu'il permet d'observer.** Une liste d'opérations : recadrage sur un détail, perte
  d'échelle, perte de couleur, éclairage dramatique, juxtaposition. Chacune peut devenir une
  variable d'expérience.
- **Lectures critiques.** Walter Grasskamp, *The Book on the Floor* (Getty, 2016), part d'une
  photo de 1954 où Malraux étale ses planches sur le sol. Il montre que le livre d'art
  illustré précède Malraux (encyclopédie photographique d'André Vigneau, 1935). Rosalind
  Krauss, « Postmodernism's Museum Without Walls » (repris dans *Thinking about Exhibitions*,
  Routledge, 1996 **[pages non vérifiées]**), note que la traduction anglaise « museum without
  walls » change l'idée : un espace mental devient un espace physique. Douglas Crimp (1980,
  voir § 4) lit Malraux comme le moment où la photographie réduit tout à du « style ».

### 2.3 Heinrich Wölfflin : comment photographier une sculpture, et la double projection

- **Les textes.** « Wie man Skulpturen aufnehmen soll », *Zeitschrift für bildende Kunst*,
  Neue Folge 7 (1896), p. 224-228 et Neue Folge 8 (1897), p. 294-297 ; puis un troisième
  texte de 1915 (Neue Folge 26, p. 237-244). Scans libres sur ART-Dok (Heidelberg).
- **Thèse [résumé de mémoire].** Les photographes de son temps photographient les statues sous
  des angles arbitraires, avec un éclairage de hasard. Pour Wölfflin, une sculpture a une
  **vue principale** voulue par l'artiste. Une mauvaise photo fausse le jugement de
  l'historien. La reproduction doit donc obéir à une règle : retrouver le point de vue juste.
- **Ce qu'il dit du support.** Que la photo n'est pas neutre, et que l'historien en dépend.
  Le cadrage photographique est un acte d'interprétation, qu'on peut faire bien ou mal.
- **Lecture moderne.** Geraldine A. Johnson, « (Un)richtige Aufnahme: Renaissance Sculpture
  and the Visual Historiography of Art History », *Art History*, 36(1), 2013, p. 12-51
  **[contenu non lu]**. Le même numéro publie la traduction anglaise de trois textes de
  Wölfflin.
- **La double projection.** On attribue à Wölfflin la projection de deux diapositives côte à
  côte, base de la méthode comparative. Heinrich Dilly a défendu l'idée que la projection
  a fait la discipline (« Lichtbildprojektion – Prothese der Kunstgeschichte », 1975 ;
  *Kunstgeschichte als Institution*, Suhrkamp, 1979) **[contenu non lu]**. Point important :
  Dilly a reconnu plus tard qu'**aucun témoignage d'époque** ne prouve que Wölfflin utilisait
  deux projecteurs (selon une recension en ligne). La « double projection » est donc en
  partie un mythe d'origine de la discipline.

### 2.4 Trevor Fawcett, « Visual Facts and the Nineteenth-Century Art Lecture » (1983)

*Art History*, 6(4), 1983, p. 442-460. **[contenu non lu au-delà du résumé]**

- **Thèse.** Fawcett suit la conférence d'art au XIXe siècle. Il part des *Discours* de
  Reynolds à la Royal Academy, qui n'étaient pas illustrés, tout en parlant de tableaux précis.
  Il suit ensuite l'arrivée des aides visuelles (gravures, moulages, photos, lanterne).
- **Ce qu'il dit du support.** La reproduction projetée devient un « fait visuel » : une preuve
  montrée au public. Le support change le statut de l'argument.
- **Ce qu'il permet d'observer.** Le passage d'un savoir parlé à un savoir montré.

### 2.5 Robert S. Nelson, « The Slide Lecture, or the Work of Art History in the Age of Mechanical Reproduction » (2000)

*Critical Inquiry*, 26(3), 2000, p. 414-434. **[résumé de mémoire, texte non relu]**

- **Thèse.** Le cours avec diapositives est une **performance**. Dans le noir, le professeur
  parle et montre ; sa voix et ses gestes (« ici, on voit… ») font exister l'œuvre à partir
  de son image. La diapositive remplace l'œuvre, et cette substitution devient invisible.
- **Ce qu'il dit du support.** La diapositive a ses propres effets : couleur trop vive ou
  trop terne, perte d'échelle, deux images de même taille côte à côte, éclairage par
  transparence. Le titre détourne celui de Benjamin : c'est l'histoire de l'art elle-même qui
  est une « œuvre » de l'époque de la reproduction.
- **Ce qu'il permet d'observer.** Le lien entre un dispositif (projecteur, écran, salle) et
  une manière de parler des œuvres. Pour nous : la machine, comme le professeur, parle
  d'une image projetée en croyant parler de l'œuvre.

### 2.6 Frederick N. Bohrer, « Photographic Perspectives: Photography and the Institutional Formation of Art History » (2002)

Chapitre 15 de *Art History and Its Institutions*, dir. Elizabeth Mansfield, Routledge, 2002,
p. 246 et suivantes. **[contenu non lu]** D'après le volume, Bohrer montre comment la
photographie a façonné l'institution de l'histoire de l'art (enseignement, catalogues,
photothèques). Il a aussi écrit *Photography and Archaeology* (Reaktion, 2011).

### 2.7 Anthony Hamber, « *A Higher Branch of the Art* » (1996)

*Photographing the Fine Arts in England, 1839-1880*, Gordon and Breach, 1996, 542 p.
**[contenu non lu]** Étude de référence sur les débuts de la photographie d'œuvres au British
Museum, à la National Gallery et au South Kensington Museum. Utile pour les choix
techniques concrets (formats, éclairage, retouche) du XIXe siècle.

---

## 3. La photographie d'œuvre comme objet

C'est le cœur de ce volet. Depuis vingt ans, un courant dit **« tournant matériel »** traite
les photographies comme des objets physiques qui ont une vie : on les tire, on les colle, on
les annote, on les classe, on les vend, on les jette.

### 3.1 Elizabeth Edwards et Janice Hart, *Photographs Objects Histories* (2004)

Routledge, 2004, collection « Material Cultures ».

- **Thèse.** Une photographie est à la fois une image et un objet. Sa forme physique
  (format, montage, album, cadre, boîte) façonne son sens et ses usages.
- **Corpus.** Études de cas variées : bijoux en cheveux avec photo, pratiques tibétaines,
  « print club » japonais, et un dernier chapitre sur la reproduction numérique.
- **Le chapitre qui nous concerne.** Joanna Sassoon, « Photographic Materiality in the Age of
  Digital Reproduction », p. 186-202 **[contenu non lu]**. Dans un article proche de 1998,
  Sassoon soutient que la numérisation **efface** la matérialité et le contexte qui donnent
  son sens à une photo d'archive.
- **Ce qu'il permet d'observer.** Une grille : matière, format, présentation, inscription,
  manipulation. Chacun de ces éléments est un « cadre » au sens de Marcel.

Elizabeth Edwards a résumé ce courant dans « Objects of Affect: Photography Beyond the
Image », *Annual Review of Anthropology*, 41, 2012, p. 221-234 **[contenu non lu au-delà du
résumé]**. Elle y dit que l'approche matérielle a fait sortir l'analyse des photos du seul
visuel.

### 3.2 Costanza Caraffa et la Photothek du Kunsthistorisches Institut de Florence

Caraffa dirige depuis 2006 la photothèque du KHI (Institut Max Planck) à Florence. C'est
l'autrice centrale pour notre question.

- **« From “photo libraries” to “photo archives” »** (2011). Introduction du volume *Photo
  Archives and the Photographic Memory of Art History*, Deutscher Kunstverlag, 2011 (« I
  Mandorli », 14), 456 p. **[contenu non lu]** Idée : une « photothèque » est un réservoir
  d'images au service de l'histoire de l'art ; une « archive photographique » est un lieu où
  l'on étudie les photos d'œuvres comme **objets matériels individuels**, avec leur histoire.
  Le passage du premier mot au second est un programme de recherche.
- **« Objects of Value: Challenging Conventional Hierarchies in the Photo Archive »**,
  chapitre 1 de *Photo-Objects*, dir. Bärnighausen, Caraffa, Klamm, Schneider, Edition Open
  Access, 2019 (version allemande *Foto-Objekte*, Kerber, 2020, avec Petra Wodtke). J'ai lu
  ce chapitre.
  - **Corpus.** Un tirage albuminé de 1900 des fouilles de Pergame, collé sur un carton plus
    grand que lui (16,8 × 23 cm sur 25,2 × 33,4 cm). Le carton porte des tampons, des
    numéros, des annotations superposées, dans plusieurs écritures, un coin déchiré.
  - **Thèse.** Prise comme simple image de ce qu'elle montre, cette photo n'apprend rien
    (« on n'y voit rien », dit-elle en citant Daniel Arasse). C'est seulement avec son
    carton, ses tampons et ses annotations, comme **photo-objet**, qu'elle livre son
    histoire : qui l'a prise, pour quelle publication, quelle institution l'a gardée.
  - **Ce qu'elle dit du support.** Les photos ont détaché les objets d'étude de leur milieu,
    les ont mis dans des **formats standard et transportables**, les ont rendus
    **comparables**. Les cartons et leurs inscriptions permettaient de classer les photos dans
    des boîtes et des meubles. Le support n'entoure donc pas seulement l'image : il la rend
    utilisable pour la science.
  - **Sur le numérique.** Elle demande des outils numériques qui « ne réduisent pas les
    photographies à leur pur contenu visuel » mais tiennent compte de leur matérialité. Elle
    renvoie à la **Déclaration de Florence** (2009), qui recommande de conserver les archives
    photographiques analogiques, car les substituts numériques ne les remplacent pas.
  - **Ce qu'il permet d'observer.** Des traces lisibles (tampons, numéros, écritures), une
    « biographie » de l'objet (le modèle vient d'Appadurai, 1986), des hiérarchies de valeur
    (pourquoi une photo « documentaire » vaut moins qu'une photo « d'art »).
- **PHAROS.** Caraffa, Pugh, Stuber et Ruby, « PHAROS: A Digital Research Space for Photo
  Archives », *Art Libraries Journal*, 45(1), 2020, p. 2-11. Quatorze photothèques d'histoire
  de l'art (dont la Frick, le KHI, le Getty) numérisent plus de 20 millions d'images et
  préparent des bonnes pratiques d'analyse automatique. **C'est le terrain réel où la
  question de punctured sky se pose** : ces scans montrent presque toujours le carton.

### 3.3 Geraldine A. Johnson, *Sculpture and Photography* (1998)

*Sculpture and Photography: Envisioning the Third Dimension*, dir. G. A. Johnson, Cambridge
University Press, 1998. **[contenu non lu]** Issu d'un colloque de 1995. Essais sur la
manière dont la photographie a modelé la fabrication et la lecture de la sculpture (Rodin,
Brancusi, Serra, Lin, Jeff Wall…). Pour nous : le cas extrême. Une sculpture a trois
dimensions ; sa photo en choisit une vue, une lumière, un fond, un bord. Le « cadre » y est
un choix de point de vue, pas un objet.

### 3.4 Patrizia Di Bello, *Women's Albums and Photography in Victorian England* (2007)

Ashgate, 2007 (sous-titre *Ladies, Mothers and Flirts*). **[contenu non lu]** Les albums
féminins comme objets : on y colle, découpe, dessine, on les montre, on les touche. Le
dernier chapitre porte sur photographie, vision et **toucher**. Critère utile : un support
compte quand il appelle un **geste** (feuilleter, toucher, montrer). Di Bello a aussi codirigé
des travaux sur le livre de photographie.

### 3.5 Diana Kamin, *Picture-Work* (2023)

*Picture-Work: How Libraries, Museums, and Stock Agencies Launched a New Image Economy*, MIT
Press, 2023. **[contenu lu via un compte rendu (Clarkson, 2024)]**

- **Corpus.** Trois collections : la Picture Collection de la New York Public Library (sous
  Romana Javitz, 1929-1968), la bibliothèque et le service des droits du MoMA (Pearl
  Moeller), l'agence d'images H. Armstrong Roberts. Plus des entretiens (2015-2017) sur la
  numérisation.
- **Thèse.** Le « picture-work » est le **travail** des personnes qui organisent des images
  (bibliothécaires, catalogueurs, documentalistes). Leurs choix de classement, de montage et
  de prêt fixent ce que les usagers peuvent faire des images. Javitz voyait la collection comme
  « vivante », produite par les rencontres avec les usagers.
- **Ce qu'elle dit du support.** Une image découpée dans un magazine, collée sur une fiche,
  rangée sous un sujet, n'a plus le même sens que dans le magazine. Le **classement** est un
  cadre. Au XXIe siècle, Kamin juge que le numérique traite les images comme des « actifs »
  et noie l'usager dans les résultats de recherche.
- **Ce qu'il permet d'observer.** Les catégories et les fiches comme données. Pour nous : un
  modèle qui « lit » une image reçoit aussi une étiquette, un nom de fichier, une légende.
  C'est un cadre de classement.

### 3.6 Anaïs Mauuarin : la photothèque comme agence

- « Une agence au musée : la photothèque du musée de l'Homme (1938-1960) », *Transbordeur*,
  n° 3, 2019, p. 150-161 (copie sur HAL). **[contenu non lu au-delà du résumé]**
- *À l'épreuve des images. Photographie et ethnologie en France (1930-1960)*, Presses
  universitaires de Strasbourg, 2022 (thèse soutenue à Paris 1 en 2018, sous la direction de
  Michel Poivert).
- **Thèse.** La photothèque du musée de l'Homme servait la science, mais aussi des « clients »
  (revues, éditeurs). Elle fonctionnait comme une **agence**. Le même tirage change de
  statut selon qu'il est document de terrain, pièce d'archive ou illustration vendue.
- **Critère.** Un support compte par son **circuit** : qui le demande, qui le paie, où il va.

### 3.7 Estelle Blaschke : de l'archive à la banque d'images

- *Banking on Images: From the Bettmann Archive to Corbis*, Spector Books, 2016 (issu d'une
  thèse EHESS de 2011).
- « Du fonds photographique à la banque d'images. L'exploitation commerciale du visuel via la
  photographie. Le Fonds Bettmann et Corbis », *Études photographiques*, 24, 2009,
  p. 150-181 (en ligne sur OpenEdition).
- **[contenu non lu au-delà des résumés]** **Thèse.** Une agence choisit, classe, met un prix,
  puis numérise une partie de son fonds. La valeur d'une photo vient de son **accessibilité**
  et de son classement, pas seulement de son image. Corbis (fondée par Bill Gates) a acheté
  Bettmann pour constituer une banque numérique.
- **Critère.** Un support compte par sa **valeur d'échange** et par ce qui est sélectionné
  pour la numérisation. Ce qui n'est pas numérisé devient invisible.

### 3.8 Thomas Smits et Saskia Asser, « The Great Unseen » (2022)

« The Great Unseen: Photojournalism and the Archive, from Analogue to Digital »,
introduction au numéro spécial de *TMG Journal for Media History*, 25(1), 2022, p. 1-17.

- **Thèse.** Les chercheurs ont étudié quelques photos de presse célèbres. Des millions de
  photos ordinaires restent « non vues » (sur le modèle du « great unread » de la lecture
  distante). Il faut travailler **entre** l'archive matérielle et l'archive numérique, à trois
  niveaux : l'objet individuel, les réseaux de métadonnées, les grandes masses d'images.
- **Ce qu'ils disent du support.** Le **dos** des tirages de presse porte légendes,
  instructions d'impression, historique de publication. La numérisation peut « cacher
  d'importants aspects matériels » des photos et des archives qui les gardent.
- **Ce qu'il permet d'observer.** Le recto et le verso comme deux sources liées. Une machine
  qui ne voit que le recto perd la moitié du document.

---

## 4. Postmodernisme, musée et archive : la copie comme sujet

### 4.1 Douglas Crimp (1980)

- « On the Museum's Ruins », *October*, 13, été 1980, p. 41-57.
- « The Photographic Activity of Postmodernism », *October*, 15, hiver 1980, p. 91-101.
- Recueil : *On the Museum's Ruins*, MIT Press, 1993, avec des photographies de Louise Lawler.
- **[résumé de mémoire]** **Thèse.** Le musée (lu avec Foucault) est une institution qui
  ordonne des objets hétérogènes en une histoire de l'art cohérente. Le musée imaginaire de
  Malraux fait de même par la photo : tout devient « style ». Mais quand la photographie
  entre au musée **comme art**, le système se fissure. Dans le second texte, les artistes
  « appropriationnistes » (Sherrie Levine rephotographiant Walker Evans, Cindy Sherman,
  Richard Prince) font de la **copie de copie** une œuvre.
- **Ce qu'il dit du support.** Une photo de photo n'est pas « la même image » : elle change de
  statut selon le cadre institutionnel (galerie, livre, archive). C'est l'emboîtement de
  Marcel, mais vu par des artistes.
- **Les photographies de Louise Lawler** sont un cas d'école : elles montrent des œuvres
  **dans** leur cadre réel (salon de collectionneur, salle de vente, réserve), avec étiquettes
  et murs. Elles font du contexte le sujet.

### 4.2 Hal Foster, « The Archive without Museums » (1996)

*October*, 77, été 1996, p. 97-119. **[résumé de mémoire]** Foster réagit à l'essor des
« études visuelles » et des bases de données. Il craint que la mise en archive numérique ne
transforme les œuvres en « images » sans corps, toutes équivalentes. Il prolonge en 2004 avec
« An Archival Impulse » (*October*, 110). **Pour nous** : la crainte de Foster est une
hypothèse testable. Un modèle de vision, entraîné sur des reproductions, traite-t-il un
tableau, une photo de tableau et une photo de photo de tableau comme une seule chose ? Les
résultats du dépôt (recherche top-10 à 99-100 % avec cadre doré) vont dans ce sens.

### 4.3 Hubert Damisch, « Cinq notes pour une phénoménologie de l'image photographique »

Traduit en anglais dans *October*, 5, été 1978, p. 70-72 ; repris dans *La Dénivelée. À
l'épreuve de la photographie*, Seuil, 2001. La première publication dans *L'Arc* (1963) est
**[non vérifiée]**.

**[résumé de mémoire]** Damisch rappelle que la photographie, en théorie, est seulement une
image fixée par la lumière sur une émulsion. L'appareil, lui, est construit selon le modèle
de la perspective de la Renaissance. Il n'est donc pas « naturel » : il est un produit
culturel. **Pour nous** : le bord rectangulaire de la photo, la perspective, le centrage
viennent d'une tradition picturale. Une machine entraînée sur des photos hérite de ce cadre
sans le savoir.

### 4.4 Hito Steyerl, « In Defense of the Poor Image » (2009)

*e-flux journal*, 10, novembre 2009. L'« image pauvre » est une copie dégradée qui circule :
miniature, aperçu, fichier recompressé. Elle perd en qualité ce qu'elle gagne en vitesse.
**Pour nous** : la qualité de la reproduction est une trace de sa circulation. Une image
recompressée et recadrée raconte son trajet. C'est la version contemporaine de la photo de
photo.

### 4.5 Bruno Latour et Adam Lowe, « The Migration of the Aura » (2011)

« The Migration of the Aura, or How to Explore the Original through Its Facsimiles », dans
Thomas Bartscherer et Roderick Coover (dir.), *Switching Codes*, University of Chicago Press,
2011, p. 275-297 ; version aussi dans *Intermédialités*, 17, 2011. J'ai lu des extraits.

- **Corpus.** Le fac-similé des *Noces de Cana* de Véronèse réalisé par Factum Arte (Adam
  Lowe) et installé en 2007 dans le réfectoire de San Giorgio Maggiore, à Venise, pour
  lequel le tableau avait été peint. L'original est au Louvre depuis 1797.
- **Thèse.** La bonne question n'est pas original contre copie. C'est **bonne contre mauvaise
  reproduction**. Une œuvre a une **trajectoire** : restaurations, recadrages, déplacements,
  copies. « Pas de copies, pas d'original » : plus il y a de copies, plus l'original attire.
  L'aura peut **migrer** vers un fac-similé de grande qualité placé dans le bon lieu.
- **Ce qu'ils disent du cadre et du support.** Un tableau doit être « recadré, dépoussiéré,
  parfois restauré, ré-éclairé » pour continuer d'exister. Il semble unique parce qu'il reste
  « dans le même cadre », dans les mêmes pigments, dans la même institution. Le fac-similé de
  Cana a été imprimé sur une toile enduite d'un gesso presque identique à celui de Véronèse :
  le **support physique** compte dans l'effet d'authenticité. Le **lieu** aussi.
- **Ce qu'il permet d'observer.** Une échelle de qualité des reproductions, et une
  trajectoire. Pour nous : on pourrait classer des reproductions d'une même œuvre selon leur
  fidélité, et voir si la machine suit cette échelle.

---

## 5. Normes, mires et régions : les cadres techniques de la reproduction

Les historiens parlent du carton et du tampon. Les normes actuelles en sont les héritières.
Elles décident ce qui entre dans le fichier.

### 5.1 Mires, échelles, étiquettes

Dans la photographie de musée, on place souvent dans le champ une **mire de gris**, une
**charte de couleurs** et une **règle**, parfois une étiquette avec le numéro d'inventaire.
Ces objets servent à contrôler la couleur et l'échelle. Ils forment un cadre technique
**à l'intérieur** de l'image. Selon les institutions, ils sont gardés dans le fichier
d'archive et rognés dans le fichier diffusé, ou gardés partout. Je n'ai pas trouvé d'étude
systématique de cette pratique dans les musées **[angle mort]**. C'est un emboîtement très
concret : l'œuvre, puis la mire, puis le bord du fichier.

### 5.2 FADGI et Metamorfoze

- **FADGI** (Federal Agencies Digital Guidelines Initiative, États-Unis), *Technical
  Guidelines for Digitizing Cultural Heritage Materials*, 3e édition, mai 2023 (après 2016).
  Couvre textes, cartes, tirages et négatifs. Définit des niveaux de qualité (« étoiles ») et
  l'usage de cibles de contrôle.
- **Metamorfoze**, *Preservation Imaging Guidelines*, version 1.0, janvier 2012 (Hans van
  Dormolen), version 2.0 en 2019. Principe : le fichier maître doit pouvoir **remplacer**
  l'original ; tout ce qui est visible sur l'original doit être visible dans le fichier.
- **ISO/TS 19264-1:2017** unifie en partie ces deux référentiels.
- **Ce qu'elles disent du cadre.** Metamorfoze demande de tout montrer de l'objet (y compris
  les bords). C'est la position des historiens de la matérialité. Mais ces normes parlent de
  **qualité d'image**, pas de **sens**. Elles fixent la fidélité, pas ce qui compte comme
  l'œuvre.

### 5.3 IIIF et la « région »

L'**API Image IIIF 3.0** (juin 2020) permet de demander une partie d'une image par l'adresse
web. Le paramètre `region` définit « la portion rectangulaire du contenu de l'image à
renvoyer » : `full` (image entière, sans rognage), `square`, `x,y,w,h` en pixels, ou
`pct:x,y,w,h` en pourcentages.

- **Pourquoi c'est important.** Avec IIIF, le recadrage devient une **adresse**. Un
  chercheur, un site, une machine peut demander « seulement le tableau » ou « seulement le
  détail ». Le cadre devient un paramètre. Mais la norme ne dit pas où est l'œuvre dans
  l'image : c'est à l'institution ou à l'usager de le décider.
- **Pour nous.** Les manifestes IIIF des musées contiennent parfois des annotations de zone.
  Ce serait une source de « vérité terrain » sur ce que l'institution considère comme
  l'œuvre dans sa propre image **[à vérifier sur un corpus]**.

### 5.4 Le droit comme cadre

- **Bridgeman Art Library c. Corel Corp.**, tribunal fédéral de New York, 1999 : une
  photographie fidèle d'un tableau du domaine public n'a pas l'originalité nécessaire pour
  être protégée.
- **Directive (UE) 2019/790, article 14** : la reproduction d'une œuvre d'art visuel du
  domaine public ne peut pas être protégée, sauf si elle est elle-même originale.
- **Cour fédérale allemande, arrêt *Museumsfotos*** (2018) : position différente pour les
  photos de musée en Allemagne (avant la transposition).
- Ellen Euler et Andrea Wallace, « Revisiting Access to Cultural Heritage in the Public
  Domain: EU and International Developments », *IIC*, 51, 2020, p. 823-855 **[contenu non lu]**.
  Elles notent que la pratique ne dit pas clairement quels supports (scan, photo, 3D)
  créent un nouveau droit.
- Kristin Kelly, *Images of Works of Art in Museum Collections: The Experience of Open
  Access*, CLIR, 2013 : enquête dans 11 musées américains et britanniques sur la mise en
  accès libre de leurs images.

**Le paradoxe.** Le droit dit qu'une reproduction fidèle **n'ajoute rien** à l'œuvre. Toute
la littérature des sections 2 à 4 dit qu'elle ajoute beaucoup (cadrage, lumière, montage,
contexte). L'accès libre a pourtant fait des images de musée la matière première des modèles
de vision. Les machines apprennent donc sur des images que le droit déclare « neutres ».

---

## 6. La numérisation comme interprétation (2015-2026)

### 6.1 Paul Conway, « Digital Transformations and the Archival Nature of Surrogates » (2015)

*Archival Science*, 15(1), 2015, p. 51-69. **[contenu non lu au-delà du résumé]** Les
substituts numériques deviennent indépendants de leurs sources. Il faut les traiter comme
des **archives** à part entière, qui gardent la trace de leur fabrication (appareil, réglages,
retouches). Conway a aussi étudié les **erreurs** de numérisation (doigts, pages pliées) dans
les livres numérisés. **Critère** : un substitut compte par les traces de sa production.

### 6.2 Andrew Prescott et Lorna Hughes, « Why Do We Digitize? The Case for Slow Digitization » (2018)

*Archive Journal*, septembre 2018. **[contenu non lu au-delà du résumé]** Une numérisation « à
la chaîne » produit des substituts **trompeurs** qui omettent des caractères de l'objet. Ils
proposent de traiter les manuscrits comme des objets archéologiques, étudiés lentement, avec
plusieurs techniques (lumière rasante, multispectral).

### 6.3 Nanna Bonde Thylstrup, *The Politics of Mass Digitization* (2018)

MIT Press, 2018. **[contenu non lu]** La numérisation de masse (Google Books, Europeana,
bibliothèques « fantômes ») n'est pas un processus technique neutre. C'est une
infrastructure politique. **Pour nous** : le corpus d'entraînement d'un modèle de vision est
le produit de ces choix.

### 6.4 Travaux français : redocumentarisation, appropriation, diapositive

- **Patrick Peccatte**, « PhotosNormandie, un projet collaboratif de redocumentarisation de
  sources patrimoniales iconographiques », *Framespa*, n° 42 **[année non vérifiée]**. Depuis
  2007, Peccatte et Michel Le Querrec recorrigent sur Flickr les légendes de plus de 5 100
  photos du débarquement. Son carnet *Déjà Vu* (Hypothèses) traite de métadonnées (IPTC), de
  recherche d'images inversée, de circulation. **Critère** : la **légende** est un cadre
  corrigeable, et sa correction est un travail d'historien.
- **André Gunthert**, *L'Image partagée. La photographie numérique*, Textuel, 2015 ; et
  « L'œuvre d'art à l'ère de son appropriabilité numérique », *Les Carnets du BAL*, 2, 2011,
  p. 136-149 **[contenu non lu]**. Le titre détourne Benjamin : à l'ère numérique, la question
  n'est plus la reproduction mais l'**appropriation** (copier, recadrer, détourner, partager).
- **Nathalie Boulouch** : « Photographie illégitime, cinéma du pauvre : le destin impossible
  de la diapositive », *Intermédialités*, 24-25, 2014-2015 **[URL non retrouvée]** ; et
  *Diapositive. Histoire de la photographie projetée* (dir. avec A. Lacoste, O. Lugon,
  C. Sandrin), Noir sur Blanc / Musée de l'Élysée, 2017. La diapositive, entre photo et
  cinéma, a donné une réception lumineuse et « dématérialisée » de l'image fixe. Complète
  Nelson pour le monde francophone.
- **Michel Poivert** (Paris 1) : *Brève histoire de la photographie*, Hazan, 2015. Je n'ai pas
  trouvé de texte de lui centré sur la reproduction d'œuvres ; son rôle ici est surtout celui
  de directeur des thèses de Mauuarin et d'autres sur les usages de la photographie
  **[à préciser]**.

### 6.5 Matérialité et vision par ordinateur : Arnold et Tilton (2026)

Taylor Arnold et Lauren Tilton, « Matérialité et vision par ordinateur : des algorithmes de
détection d'objets pour les archives photographiques », *Humanités numériques*, 13 (« Images
et IA »), juillet 2026, DOI 10.4000/16xp6. J'ai lu le résumé détaillé.

- **Corpus.** Environ 170 000 images numérisées de la collection FSA-OWI (Library of
  Congress), 1935-1945.
- **Constat.** Le « cadre » (bords de pellicule, carton de montage) occupe en moyenne
  **42,8 %** des scans de tirages argentiques, 21,2 % des tirages couleur, 18,4 % des
  négatifs plan-film, 15,5 % des négatifs 35 mm. Les modèles entraînés sur des images
  modernes « sans bordure » s'en accommodent mal. La forme matérielle devient « invisible »
  aux modèles.
- **Définition du cadre.** Fonctionnelle : tout ce qui n'est pas photographique dans le scan.
  Les auteurs reconnaissent qu'un archiviste distinguerait bord de film et carton.
- **Méthode.** 100 scans annotés par format ; quatre détecteurs YOLOv8 qui trouvent la zone
  photographique. Évaluation par l'indice de Jaccard (IoU). Plus de 0,95 sur leur format,
  moins bien d'un format à l'autre. Données et modèles sur Zenodo
  (10.5281/zenodo.18652711).
- **Ce que cela apporte.** C'est le texte le plus proche de punctured sky. Mais il va dans
  l'autre sens : il **retire** le cadre pour mieux analyser l'image. Les auteurs appellent
  pourtant à étudier ensuite d'autres traces matérielles (plis, taches). Le dépôt a déjà
  travaillé sur FSA (notes `fsa-gemini.md`).

---

## 7. Histoire de l'art numérique : le débat sur ce que voit la machine

### 7.1 Johanna Drucker

- « Is There a “Digital” Art History? », *Visual Resources*, 29(1-2), 2013, p. 5-13
  **[contenu non lu au-delà de résumés]**. Distinction devenue classique : histoire de l'art
  **numérisée** (accès aux images) contre histoire de l'art **numérique** (méthodes de calcul
  qui changent les questions). En 2013, aucune percée n'avait changé les méthodes de la
  discipline.
- *Graphesis: Visual Forms of Knowledge Production*, Harvard University Press, 2014
  **[contenu non lu]**. Vocabulaire critique pour les formes visuelles du savoir (diagrammes,
  interfaces, pages). **Pour nous** : l'interface (page web, visionneuse, vignette) est un
  cadre qui produit du sens ; Drucker donne des mots pour la décrire.

### 7.2 Claire Bishop, « Against Digital Art History » (2018)

*International Journal for Digital Art History*, 3, 2018 (d'abord en ligne en 2017). Bishop
lie l'histoire de l'art numérique aux métriques néolibérales et à une « lecture distante »
qui écrase l'interprétation. Elle laisse une porte ouverte à un usage critique. Échange avec
Drucker en 2019. **Pour nous** : la critique la plus nette contre l'idée de mesurer le sens.

### 7.3 Pamela Fletcher et Anne Helmreich

« Local/Global: Mapping Nineteenth-Century London's Art Market », *Nineteenth-Century Art
Worldwide*, 11(3), 2012 (avec David Israel et Seth Erickson). Cartographie des galeries
londoniennes 1850-1914 et ventes de Goupil. **Pour nous** : exemple d'histoire de l'art
numérique qui travaille sur les **circuits** (marché) et non sur les pixels. C'est une autre
façon de traiter le « cadre institutionnel ».

### 7.4 Emily Pugh (Getty Research Institute)

- « Photography as Machine Vision: The Role of Imaging Technologies in Art History »,
  *photographies*, 2023 **[DOI non vérifié ; contenu non lu au-delà du résumé]**. Thèse :
  la vision par ordinateur dans les musées et archives n'est pas nouvelle. Elle **reprend**
  l'effort de systématisation de la photothèque d'histoire de l'art. Les présupposés de la
  photothèque sur la photographie peuvent passer **sans bruit** dans l'histoire de l'art
  computationnelle.
- Projet **PhotoTech** (Getty) : vision par ordinateur sur la photothèque du GRI.
- **Pour nous** : Pugh dit exactement que le cadre de la photothèque (vue frontale, fond
  neutre, carton, classement) est devenu le cadre implicite des modèles.

### 7.5 Matthew Lincoln et Peter Leonard

- **Lincoln** : « Data-Driven Art History: Framing, Adapting, Documenting », conversation
  avec Thomas Padilla, série *Data Praxis*, 2015 (billet de blog, pas un article de revue).
  Lincoln y défend l'usage critique de données imparfaites et la documentation des choix.
  Je n'ai pas trouvé de texte de lui sur la vision par ordinateur et le support **[à
  compléter]**.
- **Leonard** (Yale DHLab) : projet **Neural Neighbors**, recherche d'images visuellement
  proches parmi plus de 27 000 photos du XIXe siècle (collection Meserve-Kunhardt), avec un
  réseau Inception entraîné sur ImageNet. Pas d'article de revue trouvé. **Pour nous** : un
  outil de ce type range souvent ensemble des photos qui ont le **même carton** ou le même
  format, plutôt que le même sujet. Je n'ai pas trouvé d'étude publiée de cet effet
  **[non vérifié]**.

### 7.6 Melvin Wevers et Thomas Smits

- « The Visual Digital Turn: Using Neural Networks to Study Historical Images », *Digital
  Scholarship in the Humanities*, 35(1), 2020, p. 194-207. Trois usages de réseaux
  convolutifs sur des journaux néerlandais numérisés : séparer photos et illustrations,
  regrouper des publicités, apprendre des catégories d'experts.
- « A Multimodal Turn in Digital Humanities », *DSH*, 38(3), 2023, p. 1267-1280. Usage de
  CLIP (image + texte) sur des collections historiques.
- Smits, « Revisiting the Kahn Collection… », *Visual Studies*, 40(1), 2025 (en ligne 2024),
  p. 126-142 **[contenu non lu]** : IA multimodale et motifs de présence/absence dans les
  *Archives de la Planète*.
- **Pour nous** : ces travaux montrent que le **type de support** (photo imprimée, gravure,
  dessin) est une des premières choses qu'un réseau distingue. Le support est donc « vu ».
  Mais il est traité comme une catégorie à trier, pas comme un sens.

### 7.7 Leonardo Impett et Fabian Offert

- « There Is a Digital Art History », arXiv:2308.07464, août 2023. Réponse à Drucker dix ans
  après. Les grands modèles de vision (transformers) ont absorbé une grande partie du **canon
  visuel occidental tel que filtré par internet**. Leur usage risque de renforcer ce canon.
  Méthode proposée : lire son corpus **à travers** les données d'entraînement du modèle, et
  inversement.
- Offert et Peter Bell, « Perceptual Bias and Technical Metapictures: Critical Machine
  Vision as a Humanities Challenge », *AI & Society*, 36(4), 2021, p. 1133-1144. Au-delà du
  biais des données, il y a un **biais perceptif** propre aux architectures.
- **Pour nous** : si le canon est appris à partir de **reproductions en ligne** (fichiers de
  musée, Wikimedia, livres scannés), le modèle a appris un certain cadre de reproduction
  (frontal, rogné, éclairé). Un tableau photographié autrement est alors « hors canon ».
  C'est une hypothèse, pas un résultat.

### 7.8 Taylor Arnold et Lauren Tilton, *Distant Viewing* (2019, 2023)

- « Distant Viewing: Analyzing Large Visual Corpora », *DSH*, 34 (suppl. 1), 2019, p. 3-16.
- *Distant Viewing: Computational Exploration of Digital Images*, MIT Press, 2023, accès
  libre, DOI 10.7551/mitpress/14046.001.0001.
- **Thèse.** Avant d'analyser des images, une machine doit les **interpréter et les coder**
  (étiquettes, détections). Ce codage est une interprétation, à rendre explicite. Cas :
  sitcoms des années 1960, affiches de films, photos de la Dépression.
- **Pour nous** : le « cadre » est aussi le **schéma d'annotation** : ce que l'on demande à la
  machine de repérer définit ce qui compte.

### 7.9 Daniel Helm et Martin Kampel, « overscan » (2020)

« Overscan Detection in Digitized Analog Films by Precise Sprocket Hole Segmentation »,
dans *Advances in Visual Computing* (ISVC 2020), Springer LNCS, p. 148-159,
DOI 10.1007/978-3-030-64556-4_12. Projet *Visual History of the Holocaust*.

- **Ce que c'est.** Quand on scanne un film, on scanne plus large que l'image (« overscan ») :
  on voit les perforations et le bord. Les auteurs détectent ces perforations pour recadrer
  automatiquement.
- **Pour nous** : même geste qu'Arnold et Tilton. Le bord du support est traité comme un
  **défaut à retirer**. Mais ce bord porte de l'information (type de pellicule : 16 mm ou
  9,5 mm). Ce que la technique appelle « bruit », l'historien l'appelle « trace ».

---

## 8. Quand un support « compte » : les critères des auteurs

Voici les critères que j'ai retrouvés. Chacun est une façon de **prouver** qu'un support
participe au sens.

| Critère | Ce qu'on regarde | Auteurs | Exemple |
|---|---|---|---|
| **Trace** | Marques physiques sur le support | Caraffa, Edwards, Conway, Prescott & Hughes | Tampon « Pergamon », coin déchiré, numéro au crayon |
| **Paratexte** | Légende, étiquette, métadonnée, dos | Smits & Asser, Peccatte, Kamin, Drucker | Dos d'un tirage de presse ; légende corrigée sur Flickr |
| **Usage / geste** | Ce qu'on fait avec l'objet | Di Bello, Nelson, Fawcett, Dilly | Projeter, comparer, feuilleter, toucher |
| **Classement** | Où l'objet est rangé et sous quel nom | Kamin, Caraffa, Pugh | Fiche « sujet » de la NYPL ; carton de photothèque |
| **Circulation / trajectoire** | Par où l'objet est passé | Latour & Lowe, Mauuarin, Steyerl, Smits | Fac-similé de Cana ; image pauvre recompressée |
| **Valeur** | Prix, droit, rang | Blaschke, Kelly, Bridgeman, Wallace & Euler | Banque d'images Corbis ; accès libre des musées |
| **Point de vue** | Angle, lumière, échelle choisis | Wölfflin, Johnson, Malraux | Vue principale d'une statue ; détail agrandi |
| **Institution** | Qui autorise l'objet comme art ou document | Crimp, Foster, Bohrer | Photo entrée au musée comme art |
| **Fidélité** | Écart mesuré à l'original | Metamorfoze, FADGI, Latour & Lowe | Mire de gris ; « bonne » contre « mauvaise » reproduction |

### En quoi cela diffère d'un test « avec / sans »

Un test avec/sans fait ceci : on prend la même image d'œuvre, on ajoute ou on enlève un cadre,
et on regarde si la réponse de la machine change. C'est utile. Mais ce n'est pas ce que font
ces auteurs. Cinq différences.

1. **Les auteurs ne fabriquent pas les cas. Ils les trouvent.** Le carton de Pergame existe ; on
   ne l'a pas collé pour voir. Un test avec/sans compose des images. Il mesure la réaction à
   un montage, pas à un objet historique.
2. **Pour les auteurs, « compter » veut dire « porter de l'information sur l'histoire de
   l'objet ».** Le tampon dit qui a gardé la photo. Pour un test avec/sans, « compter » veut
   dire « changer la sortie ». Un support peut porter beaucoup d'information sans changer la
   description de l'œuvre (c'est ce que le dépôt a souvent observé). Et il peut changer la
   sortie pour une raison sans intérêt (il prend de la place, il masque).
3. **Les auteurs regardent des trajectoires, pas des états.** Latour et Lowe, Mauuarin, Steyerl
   suivent une image à travers plusieurs supports successifs. Un test avec/sans compare deux
   états.
4. **La vision par ordinateur cherche souvent l'invariance.** Elle veut reconnaître l'œuvre
   *malgré* le support (c'est le but d'Arnold et Tilton, de Helm et Kampel). Les historiens
   cherchent la **variance** : ce qui distingue ce tirage-ci de tous les autres. Un modèle
   qui ignore le cadre est un bon modèle pour l'ingénieur, et un mauvais lecteur pour
   l'historien.
5. **Les auteurs lisent le support séparément de l'œuvre.** Ils datent le tirage, pas la
   statue. Ils attribuent le carton, pas le tableau. Un test avec/sans demande
   généralement ce que montre l'image, donc l'œuvre. Il ne demande pas ce que **le support**
   dit de lui-même.

Le dépôt a déjà un signe que les machines peuvent lire le support à part : dans le pilote
« cadre social », Claude **date le cadre à part** (18/18) et lui donne parfois un
propriétaire de musée (note `cadrage-et-valeur.md`). C'est une lecture de **paratexte**, au
sens de cette littérature. Ce n'est pas un effet du cadre sur l'œuvre.

---

## 9. Débats ouverts

1. **La reproduction ajoute-t-elle ou retire-t-elle ?** Benjamin (perte de l'aura), Sassoon
   (perte de matérialité) contre Latour et Lowe (l'aura migre), Malraux (arts fictifs). Le
   droit tranche dans le sens « n'ajoute rien ». Les historiens dans le sens « ajoute ».
2. **Le numérique est-il matériel ?** Caraffa et Pinney (dans *Photo-Objects*) disent oui :
   le numérique a ses écrans, ses serveurs, ses formats. D'autres (Kamin, Foster) décrivent
   une perte de corps et de contexte. Le débat n'est pas tranché.
3. **Le modèle biographique est-il le bon ?** Caraffa discute les critiques de la
   « biographie d'objet » (Appadurai, Kopytoff) : une biographie suppose une mort ; les
   archives, elles, renaissent. On parle aussi d'« itinéraires ».
4. **Lecture distante ou interprétation ?** Bishop contre Drucker, Impett et Offert, Arnold et
   Tilton. Peut-on compter sans écraser ? Les « défenseurs » répondent en rendant explicites
   les choix d'annotation.
5. **La double projection a-t-elle fondé la discipline ?** Dilly l'a soutenu, puis a admis
   l'absence de preuve directe. Nelson nuance par la performance. C'est un débat sur le poids
   d'un dispositif dans une méthode, proche du nôtre.
6. **Quelle reproduction est « fidèle » ?** Metamorfoze et FADGI mesurent la fidélité
   colorimétrique. Wölfflin parlait de fidélité au point de vue de l'artiste. Latour et Lowe
   de fidélité au lieu et au support. Ce ne sont pas les mêmes fidélités.

---

## 10. Angles morts

1. **Personne n'étudie la mire de couleur comme cadre.** Elle est dans des millions de
   fichiers de musée. Je n'ai trouvé aucune étude sur ce qu'elle fait à la lecture humaine
   ou machine **[recherche limitée]**.
2. **Peu d'études sur le recto et le verso ensemble par machine.** Smits et Asser le
   réclament. Les photothèques (PHAROS) scannent souvent les deux faces. Les modèles lisent
   presque toujours une seule image.
3. **La reproduction de reproduction n'est pas mesurée.** Crimp et Steyerl en font une
   question esthétique. La criminalistique d'image a des travaux sur la détection de photos
   d'écran (« recapture ») **[références non vérifiées]**, mais pour la fraude, pas pour
   l'histoire. Personne ne compte les « générations » de copie dans une archive d'art.
4. **Les historiens de la matérialité n'ont pas testé les machines.** Caraffa demande des
   outils qui gardent la matérialité, sans dire comment les évaluer. Arnold et Tilton
   mesurent la place du cadre, mais pour l'enlever.
5. **La différence entre « date de l'œuvre » et « date de l'image »** n'est pas un objet
   d'étude explicite. C'est pourtant le geste de base de l'historien des photo-objets.
6. **La littérature francophone sur la photographie de reproduction d'œuvres** (ateliers
   Braun, Giraudon, Bulloz ; photothèques universitaires ; diapothèques) existe mais je ne
   l'ai pas retrouvée en ligne dans ce volet **[à compléter]**.
7. **Le droit et la technique ne se parlent pas.** Le droit déclare la reproduction neutre ;
   les normes techniques la règlent finement ; les modèles l'apprennent en masse. Aucun texte
   trouvé ne relie ces trois niveaux.

---

## 11. Problèmes qu'on pourrait poser aux machines

Ce sont des questions, pas des résultats. Aucune n'a été testée dans ce volet.

1. **Double datation.** Montrer un photo-objet (tirage ancien sur carton) et demander deux
   dates : celle de l'œuvre représentée et celle de la photographie. Mesure : la machine
   sépare-t-elle les deux ? Corpus possible : photothèques PHAROS, Photothek du KHI, FSA.
   C'est le critère « trace » de Caraffa.
2. **Lire le paratexte.** Demander « qui a fait cette image et qui la conserve ? » sur des
   scans avec tampons, étiquettes, mires. Vérité terrain : les notices des institutions.
   C'est le critère « paratexte ».
3. **Compter les générations.** Une œuvre ; sa photo de musée ; une page de livre qui la
   reproduit ; une photo de cette page ; une capture d'écran de la photo. Demander « combien
   d'étapes séparent cette image de l'œuvre ? ». Le dépôt a déjà ces emboîtements. La
   question est nouvelle : non pas « reconnaît-il l'œuvre ? » mais « reconnaît-il la chaîne ? ».
4. **Arts fictifs.** Recadrer sur un détail, sans indice d'échelle. Demander la taille réelle
   de l'objet. Malraux prédit l'erreur (la monnaie devient bas-relief). On peut mesurer
   l'écart sur des œuvres de taille connue.
5. **Point de vue de Wölfflin.** Plusieurs photos d'une même statue sous des angles
   différents. Demander laquelle est la « vue principale ». Comparer avec les choix des
   catalogues. On saurait si le modèle a appris la convention de la photothèque (Pugh).
6. **Mire dans le champ.** Même image avec et sans mire de couleur et règle. Ici le test
   avec/sans est justifié, car la question est précise : la mire fait-elle passer l'image du
   statut « œuvre » au statut « document de musée » dans la description ?
7. **Recto et verso.** Donner les deux faces d'un tirage de presse et voir si la légende du dos
   change la description du recto. Smits et Asser en donnent la raison historique.
8. **Trajectoire de qualité (Latour et Lowe).** Plusieurs reproductions d'une même œuvre, de la
   meilleure à la plus dégradée. La machine classe-t-elle ces images dans l'ordre de fidélité ?
   Où, dans la chaîne, cesse-t-elle de reconnaître l'œuvre ?
9. **Canon et reproduction (Impett et Offert).** Une œuvre célèbre photographiée « à la manière
   de musée » contre la même photographiée de biais, en salle, avec reflets. Si la
   reconnaissance chute surtout pour les œuvres célèbres, c'est que le modèle a appris la
   **reproduction canonique** plus que l'œuvre.
10. **Ce que l'institution appelle « l'œuvre ».** Comparer les régions IIIF annotées par les
    musées (quand elles existent) à la zone que la machine désigne comme l'œuvre. Cela
    donnerait une vérité terrain institutionnelle du cadre.

**Ce qui rendrait ces tests utiles** : ils transforment la question de Marcel (« le cadre
enveloppe-t-il une partie du sens ? ») en questions que les archives posent déjà. Un
photothécaire, un conservateur de photographies, un projet comme PHAROS ou PhotoTech a
besoin de savoir si la machine lit le support comme un document ou l'efface comme du bruit.
C'est là que punctured sky peut avoir un public.

---

## Bibliographie

Une ligne par référence. Le lien est celui qui a servi à vérifier.

### Textes fondateurs
- Benjamin, Walter. « L'œuvre d'art à l'époque de sa reproduction mécanisée », trad. P. Klossowski, *Zeitschrift für Sozialforschung*, 5(1), 1936. https://www.universalis.fr/encyclopedie/l-oeuvre-d-art-a-l-epoque-de-sa-reproduction-mecanisee/3-bibliographie/
- Malraux, André. *Psychologie de l'art. Le Musée imaginaire*, Genève, Skira, 1947 ; repris dans *Les Voix du silence*, Gallimard, 1951 ; éd. « Idées/Arts », 1965. https://en.wikipedia.org/wiki/La_Psychologie_de_l%27Art
- Grasskamp, Walter. *The Book on the Floor: André Malraux and the Imaginary Museum*, Los Angeles, Getty Research Institute, 2016. https://shop.getty.edu/collections/all/products/the-book-on-the-floor-andr-malraux-and-the-imaginary-museum-978-1606065013
- Krauss, Rosalind. « Postmodernism's Museum Without Walls », dans R. Greenberg, B. Ferguson, S. Nairne (dir.), *Thinking about Exhibitions*, Routledge, 1996 [pages non vérifiées]. https://www.cca.qc.ca/en/search/details/library/publication/32310986
- Wölfflin, Heinrich. « Wie man Skulpturen aufnehmen soll (I) », *Zeitschrift für bildende Kunst*, N.F. 7, 1896, p. 224-228. https://archiv.ub.uni-heidelberg.de/artdok/7671
- Wölfflin, Heinrich. « Wie man Skulpturen aufnehmen soll (II) », *Zeitschrift für bildende Kunst*, N.F. 8, 1897, p. 294-297. https://archiv.ub.uni-heidelberg.de/artdok/7672
- Wölfflin, Heinrich. « Wie man Skulpturen aufnehmen soll? », *Zeitschrift für bildende Kunst*, N.F. 26, 1915, p. 237-244. https://archiv.ub.uni-heidelberg.de/artdok/7673
- Johnson, Geraldine A. « (Un)richtige Aufnahme: Renaissance Sculpture and the Visual Historiography of Art History », *Art History*, 36(1), 2013, p. 12-51, DOI 10.1111/j.1467-8365.2012.00917.x. https://ora.ox.ac.uk/objects/uuid:edbc63e4-2f60-4886-86cd-70e6340688a2
- Dilly, Heinrich. « Lichtbildprojektion – Prothese der Kunstgeschichte », dans I. Below (dir.), *Kunstwissenschaft und Kunstvermittlung*, 1975 [titre exact et pages non vérifiés]. https://arthist.net/archive/24580/view=pdf
- Dilly, Heinrich. *Kunstgeschichte als Institution*, Francfort, Suhrkamp, 1979. https://katalog.bibliothek.kit.edu/bib/66653
- Fawcett, Trevor. « Visual Facts and the Nineteenth-Century Art Lecture », *Art History*, 6(4), 1983, p. 442-460, DOI 10.1111/j.1467-8365.1983.tb00094.x. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-8365.1983.tb00094.x
- Nelson, Robert S. « The Slide Lecture, or the Work of Art History in the Age of Mechanical Reproduction », *Critical Inquiry*, 26(3), 2000, p. 414-434, DOI 10.1086/448973. https://www.journals.uchicago.edu/doi/abs/10.1086/448973
- Bohrer, Frederick N. « Photographic Perspectives: Photography and the Institutional Formation of Art History », dans E. Mansfield (dir.), *Art History and Its Institutions*, Routledge, 2002, p. 246 sq. https://www.routledge.com/Art-History-and-Its-Institutions-The-Nineteenth-Century/Mansfield/p/book/9780415228695
- Hamber, Anthony J. *« A Higher Branch of the Art »: Photographing the Fine Arts in England, 1839-1880*, Amsterdam, Gordon and Breach, 1996. https://search.worldcat.org/oclc/35902142

### Photographie comme objet, archives photographiques
- Edwards, Elizabeth, et Janice Hart (dir.). *Photographs Objects Histories: On the Materiality of Images*, Londres, Routledge, 2004. https://cca.qc.ca/en/search/details/library/publication/52799795
- Sassoon, Joanna. « Photographic Materiality in the Age of Digital Reproduction », dans Edwards et Hart (dir.), 2004, p. 186-202. https://biblio.ub.uni-heidelberg.de/camera_work/Record/KXP-PPN1464932891
- Edwards, Elizabeth. « Objects of Affect: Photography Beyond the Image », *Annual Review of Anthropology*, 41, 2012, p. 221-234, DOI 10.1146/annurev-anthro-092611-145708. https://doi.org/10.1146/annurev-anthro-092611-145708
- Caraffa, Costanza (dir.). *Photo Archives and the Photographic Memory of Art History*, Berlin, Deutscher Kunstverlag, 2011 (I Mandorli, 14) ; introduction « From “photo libraries” to “photo archives” ». https://www.cca.qc.ca/en/search/details/library/publication/706650247
- Bärnighausen, Julia, Costanza Caraffa, Stefanie Klamm, Franka Schneider (dir.). *Photo-Objects: On the Materiality of Photographs and Photo Archives in the Humanities and Sciences*, Berlin, Edition Open Access (MPRL Studies 12), 2019. https://mprl-series.mpg.de/studies/12/1/index.html
- Caraffa, Costanza. « Objects of Value: Challenging Conventional Hierarchies in the Photo Archive », dans *Photo-Objects*, 2019, chap. 1. https://www.mprl-series.mpg.de/media/studies/12/2/studies12chap01.pdf
- Bärnighausen, J., C. Caraffa, S. Klamm, F. Schneider, P. Wodtke (dir.). *Foto-Objekte*, Bielefeld, Kerber, 2020. https://katalog.ub.uni-leipzig.de/Record/0-1018550313
- Kunsthistorisches Institut in Florenz. *Florence Declaration – Recommendations for the Preservation of Analogue Photo Archives*, 2009. https://www.khi.fi.it/en/photothek/florence-declaration.php
- Caraffa, Costanza, Emily Pugh, Tracy Stuber, Louisa Wood Ruby. « PHAROS: A Digital Research Space for Photo Archives », *Art Libraries Journal*, 45(1), 2020, p. 2-11. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/AC7D9F996BDA0526AF7EF4072A16C364/S0307472219000348a.pdf/pharos-a-digital-research-space-for-photo-archives.pdf
- Johnson, Geraldine A. (dir.). *Sculpture and Photography: Envisioning the Third Dimension*, Cambridge University Press, 1998. https://catalogue.henry-moore.org/bibliography/5967/sculpture-and-photography-envisioning-the-third-dimension
- Di Bello, Patrizia. *Women's Albums and Photography in Victorian England: Ladies, Mothers and Flirts*, Aldershot, Ashgate, 2007. https://www.routledge.com/Womens-Albums-and-Photography-in-Victorian-England-Ladies-Mothers-and-Flirts/Bello/p/book/9780754658559
- Kamin, Diana. *Picture-Work: How Libraries, Museums, and Stock Agencies Launched a New Image Economy*, Cambridge (MA), MIT Press, 2023. https://newbooksnetwork.com/picture-work
- Clarkson, Amelia. Compte rendu de Kamin, *Picture-Work*, *Canadian Journal of Academic Librarianship*, 10, 2024, DOI 10.33137/cjal-rcbu.v10.44300. https://www.erudit.org/fr/revues/cjalib/2024-v10-cjalib09113/1115626ar.pdf
- Mauuarin, Anaïs. « Une agence au musée : la photothèque du musée de l'Homme (1938-1960) », *Transbordeur*, 3, 2019, p. 150-161. https://halshs.archives-ouvertes.fr/halshs-03439009v1/file/MAUUARIN_Article%20Transbordeur.pdf
- Mauuarin, Anaïs. *À l'épreuve des images. Photographie et ethnologie en France (1930-1960)*, Presses universitaires de Strasbourg, 2022. https://books.openedition.org/pus/35196
- Blaschke, Estelle. « Du fonds photographique à la banque d'images. L'exploitation commerciale du visuel via la photographie. Le Fonds Bettmann et Corbis », *Études photographiques*, 24, 2009, p. 150-181. https://journals.openedition.org/etudesphotographiques/2828
- Blaschke, Estelle. *Banking on Images: From the Bettmann Archive to Corbis*, Leipzig, Spector Books, 2016. https://spectorbooks.com/book/banking-on-images
- Smits, Thomas, et Saskia Asser. « The Great Unseen: Photojournalism and the Archive, from Analogue to Digital », *TMG Journal for Media History*, 25(1), 2022, p. 1-17, DOI 10.18146/tmg.829. https://www.tmgonline.nl/article/10.18146/tmg.829/

### Postmodernisme, musée, archive, copie
- Crimp, Douglas. « On the Museum's Ruins », *October*, 13, 1980, p. 41-57. https://www.monoskop.org/images/4/4e/Crimp_Douglas_1980_On_the_Museums_Ruins.pdf
- Crimp, Douglas. « The Photographic Activity of Postmodernism », *October*, 15, 1980, p. 91-101. https://en.wikipedia.org/wiki/Douglas_Crimp
- Crimp, Douglas, avec Louise Lawler. *On the Museum's Ruins*, Cambridge (MA), MIT Press, 1993. https://www.lensculture.com/books/388-on-the-museum-s-ruins
- Foster, Hal. « The Archive without Museums », *October*, 77, 1996, p. 97-119 (JSTOR 778962). https://edisciplinas.usp.br/pluginfile.php/2763430/mod_resource/content/1/The%20Archive%20without%20Museums.pdf
- Foster, Hal. « An Archival Impulse », *October*, 110, 2004, p. 3-22. https://Monoskop.org/images/6/6b/Foster_Hal_2004_An_Archival_Impulse.pdf
- Damisch, Hubert. « Five Notes for a Phenomenology of the Photographic Image », *October*, 5, 1978, p. 70-72 ; en français dans *La Dénivelée*, Seuil, 2001 [première publication dans *L'Arc*, 1963 : non vérifiée]. https://sholetteseminars.com/wp-content/uploads/2020/08/5-Notes-on-Photography-2.pdf
- Steyerl, Hito. « In Defense of the Poor Image », *e-flux journal*, 10, 2009. https://www.e-flux.com/journal/10/61362/in-defense-of-the-poor-image/
- Latour, Bruno, et Adam Lowe. « The Migration of the Aura, or How to Explore the Original through Its Facsimiles », dans T. Bartscherer et R. Coover (dir.), *Switching Codes*, University of Chicago Press, 2011, p. 275-297. http://www.bruno-latour.fr/node/151
- Latour, Bruno, et Adam Lowe. Même texte, *Intermédialités*, 17, 2011. https://releve.erudit.org/fr/revues/im/2011-n17-im1817262/1005756ar.pdf

### Normes, droit, accès
- FADGI. *Technical Guidelines for Digitizing Cultural Heritage Materials*, 3e éd., mai 2023. https://www.digitizationguidelines.gov/guidelines/digitize-technical.html
- Van Dormolen, Hans. *Metamorfoze Preservation Imaging Guidelines*, version 1.0, janvier 2012 (v. 2.0, 2019) ; présentation IS&T Archiving 2012, p. 186-189. https://library.imaging.org/archiving/articles/9/1/art00041
- ISO/TS 19264-1:2017, *Photography — Archiving systems — Imaging systems quality analysis — Part 1: Reflective originals* [mentionnée via Metamorfoze 2.0, notice ISO non ouverte]. https://library.imaging.org/archiving/articles/16/1/art00003
- IIIF Consortium. *IIIF Image API 3.0*, 2020 (paramètre `region`, § 4.1). https://iiif.io/api/image/3.0/
- *Bridgeman Art Library, Ltd. v. Corel Corp.*, 36 F. Supp. 2d 191 (S.D.N.Y. 1999) ; note de cas. https://btlj.org/data/articles2015/vol15/15_1_AR/15-berkeley-tech-l-j-0003-0024.pdf
- Directive (UE) 2019/790 sur le droit d'auteur dans le marché unique numérique, art. 14. https://eur-lex.europa.eu/eli/dir/2019/790/oj
- Euler, Ellen, et Andrea Wallace. « Revisiting Access to Cultural Heritage in the Public Domain: EU and International Developments », *IIC*, 51, 2020, p. 823-855, DOI 10.1007/s40319-020-00961-8. https://opus4.kobv.de/opus4-fhpotsdam/frontdoor/index/index/docId/2503
- Kelly, Kristin. *Images of Works of Art in Museum Collections: The Experience of Open Access*, Washington, CLIR, 2013. https://www.clir.org/?p=689

### Numérisation comme interprétation
- Conway, Paul. « Digital Transformations and the Archival Nature of Surrogates », *Archival Science*, 15(1), 2015, p. 51-69, DOI 10.1007/s10502-014-9219-z. https://deepblue.lib.umich.edu/bitstream/handle/2027.42/111825/J26%20Conway%20Digital%20Transformations%202014-pers.pdf?sequence=1
- Prescott, Andrew, et Lorna Hughes. « Why Do We Digitize? The Case for Slow Digitization », *Archive Journal*, 2018. https://eprints.gla.ac.uk/165726
- Thylstrup, Nanna Bonde. *The Politics of Mass Digitization*, Cambridge (MA), MIT Press, 2018. https://monoskop.org/log/?p=20862
- Peccatte, Patrick. « PhotosNormandie, un projet collaboratif de redocumentarisation de sources patrimoniales iconographiques », *Framespa*, 42 [année non vérifiée]. https://journals.openedition.org/framespa/14184
- Peccatte, Patrick. *Déjà Vu*, carnet de recherche (Hypothèses). https://dejavu.hypotheses.org/
- Gunthert, André. *L'Image partagée. La photographie numérique*, Paris, Textuel, 2015. https://transbordeur.ch/en/2017/andre-gunthert-image-partagee
- Gunthert, André. « L'œuvre d'art à l'ère de son appropriabilité numérique », *Les Carnets du BAL*, 2, 2011, p. 136-149 [contenu non lu]. https://www.univ-paris8.fr/L-iconoclasme-numerique-a-l-assaut
- Boulouch, Nathalie. « Photographie illégitime, cinéma du pauvre : le destin impossible de la diapositive », *Intermédialités*, 24-25, 2014-2015 [URL de l'article non retrouvée ; sommaire du numéro]. https://www.erudit.org/en/journals/im/2014-n24-25-im02279/
- Boulouch, Nathalie, Anne Lacoste, Olivier Lugon, Carole Sandrin (dir.). *Diapositive. Histoire de la photographie projetée*, Lausanne, Noir sur Blanc / Musée de l'Élysée, 2017. https://www.cca.qc.ca/en/search/details/library/publication/990410485
- Poivert, Michel. *Brève histoire de la photographie*, Paris, Hazan, 2015. https://laviedesidees.fr/Du-daguerreotype-au-numerique.html
- Arnold, Taylor, et Lauren Tilton. « Matérialité et vision par ordinateur : des algorithmes de détection d'objets pour les archives photographiques », *Humanités numériques*, 13, 2026, DOI 10.4000/16xp6. https://journals.openedition.org/revuehn/5405

### Histoire de l'art numérique et vision par ordinateur
- Drucker, Johanna. « Is There a “Digital” Art History? », *Visual Resources*, 29(1-2), 2013, p. 5-13, DOI 10.1080/01973762.2013.761106 [DOI résolu vers Taylor & Francis, titre non affiché]. http://www.tandfonline.com/doi/abs/10.1080/01973762.2013.761106
- Drucker, Johanna. *Graphesis: Visual Forms of Knowledge Production*, Cambridge (MA), Harvard University Press, 2014. https://brooklynrail.org/2015/03/books/seeing-and-knowing-graphesis-visual-forms-of-knowledge-production/
- Bishop, Claire. « Against Digital Art History », *International Journal for Digital Art History*, 3, 2018, DOI 10.11588/dah.2018.3.49915. https://journals.ub.uni-heidelberg.de/index.php/dah/article/view/49915
- Fletcher, Pamela, et Anne Helmreich, avec David Israel et Seth Erickson. « Local/Global: Mapping Nineteenth-Century London's Art Market », *Nineteenth-Century Art Worldwide*, 11(3), 2012. https://19thc-artworldwide.org/autumn12/fletcher-helmreich-mapping-the-london-art-market
- Pugh, Emily. « Photography as Machine Vision: The Role of Imaging Technologies in Art History », *photographies*, 2023 [DOI non vérifié]. https://getty.academia.edu/EmilyPugh
- Lincoln, Matthew, et Thomas Padilla. « Data-Driven Art History: Framing, Adapting, Documenting », *Data Praxis* (dhandlib.org), 2015. https://dhandlib.org/tag/art-history/
- Leonard, Peter (Yale DHLab). *Neural Neighbors* (projet en ligne). https://dhlab.yale.edu/projects/neural-neighbors
- Wevers, Melvin, et Thomas Smits. « The Visual Digital Turn: Using Neural Networks to Study Historical Images », *Digital Scholarship in the Humanities*, 35(1), 2020, p. 194-207, DOI 10.1093/llc/fqy085. https://academic.oup.com/dsh/article/35/1/194/5296356
- Smits, Thomas, et Melvin Wevers. « A Multimodal Turn in Digital Humanities: Using Contrastive Machine Learning Models to Explore, Enrich, and Analyze Digital Visual Historical Collections », *DSH*, 38(3), 2023, p. 1267-1280, DOI 10.1093/llc/fqad008. https://academic.oup.com/dsh/article/38/3/1267/7078540
- Smits, Thomas. « Revisiting the Kahn Collection: Multimodal Artificial Intelligence and Visual Patterns of Presence and Absence in the Archives de la Planète, 1909-1931 », *Visual Studies*, 40(1), 2025, p. 126-142, DOI 10.1080/1472586X.2024.2380859. https://rdt.uva.nl/profile/s/m/t.p.smits/t.p.smits.html
- Impett, Leonardo, et Fabian Offert. « There Is a Digital Art History », arXiv:2308.07464, 2023. https://arxiv.org/abs/2308.07464
- Offert, Fabian, et Peter Bell. « Perceptual Bias and Technical Metapictures: Critical Machine Vision as a Humanities Challenge », *AI & Society*, 36(4), 2021, p. 1133-1144, DOI 10.1007/s00146-020-01058-z. https://open.fau.de/handle/openfau/22906
- Arnold, Taylor, et Lauren Tilton. « Distant Viewing: Analyzing Large Visual Corpora », *DSH*, 34 (suppl. 1), 2019, p. 3-16. https://dblp.uni-trier.de/pid/206/0143.html
- Arnold, Taylor, et Lauren Tilton. *Distant Viewing: Computational Exploration of Digital Images*, Cambridge (MA), MIT Press, 2023, DOI 10.7551/mitpress/14046.001.0001. https://scholarship.richmond.edu/bookshelf/377
- Helm, Daniel, et Martin Kampel. « Overscan Detection in Digitized Analog Films by Precise Sprocket Hole Segmentation », dans G. Bebis (dir.), *Advances in Visual Computing* (ISVC 2020), Springer LNCS, 2020, p. 148-159, DOI 10.1007/978-3-030-64556-4_12. https://repositum.tuwien.at/handle/20.500.12708/58320
