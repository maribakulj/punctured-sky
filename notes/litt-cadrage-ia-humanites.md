# Le cadrage des images par les machines : ce qu'en disent les humanités

*14/10/2026. Complément « côté humanités » à [`litterature.md`](litterature.md) (étape E8) et à
[`cadrage-et-valeur.md`](cadrage-et-valeur.md). Question : qu'ont dit la théorie et la critique du
cadrage des images (et de l'art) par les machines et les médias numériques, et en quoi cela
prolonge-t-il la théorie du cadre ?*

**Ce qui n'est pas repris ici**, parce que c'est déjà traité ailleurs dans le projet : Simmel,
Ortega, Schapiro, Derrida, Marin, Stoichita, Duro, Bateson, Goffman, Genette, McLuhan, Bolter et
Grusin, Friedberg, Wölfflin, Benjamin, Malraux, Latour et Lowe, Steyerl (« image pauvre »),
Caraffa, Offert et Bell, MacKenzie et Munster, Zylinska (*The Perception Machine*), Wasielewski
(*Computational Formalism*), Impett, Impett et Offert, Arnold et Tilton (section 2 de l'article et
`litterature.md`) ; Danto, Dickie, Goodman, Bourdieu, Becker (`cadrage-et-valeur.md`, § 1.3-1.4).

**Comment lire les références.** Chaque référence a été ouverte en ligne le 14/10/2026. Le lien
donné est celui qui a servi : notice DOI (Crossref ou DataCite), page d'éditeur, catalogue (Open
Library, bibliothèques de Paris), dépôt d'auteur, ou page de la revue. Quand seule la notice a pu
être ouverte (beaucoup d'éditeurs refusent l'accès automatique), c'est écrit « notice seule » : le
titre et la date sont sûrs, le résumé du contenu vient de ma connaissance de l'ouvrage ou d'une
source secondaire nommée. **[incertain]** marque ce que je n'ai pas pu confirmer. Les citations
entre guillemets ont été lues sur la page indiquée, sauf mention contraire.

**Distinguer.** Dans chaque fiche, la flèche → dit ce que dit l'auteur. Ce que *nous* en tirons
est marqué « *Pour nous :* ». La section finale sépare aussi les deux.

---

## Petit lexique

- **Cadre** : la limite matérielle ou visuelle qui entoure une image (bordure dorée, bord de la
  page, bord de l'écran).
- **Cadrage** : le geste de choisir ce qui entre dans l'image et ce qui en sort.
- **Recadrage** : refaire ce choix après coup, sur une image déjà faite (rogner une photo,
  zoomer sur un détail).
- **Hors-champ** : ce qu'on ne voit pas mais que l'image suppose autour d'elle.
- **Image opératoire** (ou « opérationnelle ») : image faite pour qu'une machine agisse (guider un
  missile, trier des pièces), pas pour être regardée.
- **Jeu de données** : grande collection d'images avec leurs étiquettes, qui sert à entraîner un
  modèle (ImageNet, LAION).
- **Saillance** : ce qui « saute aux yeux » dans une image ; en informatique, une carte calculée
  de l'endroit où un humain regarderait d'abord.

---

## 1. Cadre, écran, hors-champ

La théorie du cinéma a pensé, bien avant le numérique, la différence entre le cadre d'un tableau
et le bord d'un écran. C'est le chaînon qui manque entre Simmel et la vision machine.

- **André Bazin, « Peinture et cinéma »** (paru d'abord sous le titre « Le cinéma et la
  peinture », *La Revue du cinéma*, 1949 ; repris dans *Qu'est-ce que le cinéma ?*). Lu dans la
  traduction anglaise citée par Angela Dalle Vacche, « The Art Documentary in the Postwar
  Period », *Aniki* 1(2), 2014, p. 292-313, https://doi.org/10.14591/aniki.v1n2.90 (page ouverte :
  https://www.aim.org.pt/ojs/index.php/revista/article/view/90/html). Référence de Dalle Vacche :
  Bazin, *What Is Cinema?*, vol. 1, trad. Hugh Gray, University of California Press, 2005, p. 116.
  → Les bords de l'écran ne sont pas un cadre mais un **cache** qui ne montre qu'une partie du
  réel. « A frame is centripetal, the screen centrifugal » : le cadre du tableau tourne le regard
  vers l'intérieur ; l'écran laisse supposer que le monde continue au-delà.
  [incertain : texte français et sa page non consultés.]
  *Pour nous :* c'est l'opposition la plus utile pour classer nos couches. La bordure dorée est
  un cadre (centripète). Le bord d'une photo de livre ou d'un écran photographié est un cache
  (centrifuge) : il coupe une scène qui continue.

- **Gilles Deleuze, *Cinéma 1. L'Image-mouvement***, Paris, Minuit, coll. « Critique », 1983,
  298 p. Notice : https://bibliotheques.paris.fr/doc/SYRACUSE/517936. Chapitre 2, « Cadre et plan,
  cadrage et découpage », p. 31-32 pour la synthèse (pages données par l'appel à communication
  « Du cadre à la bordure », https://www.fabula.org/actualites/116648/colloque-lyon-du-cadre-a-la-bordure-arts-plastiques-musique-et-cinema.html).
  → « Le cadrage est l'art de choisir les parties de toutes sortes qui entrent dans un ensemble. »
  Cet ensemble est « relativement et artificiellement clos ». Le cadre « détermine un hors-champ »,
  soit un ensemble plus vaste qui le prolonge, soit un tout qui l'intègre.
  *Pour nous :* la définition de Deleuze est opératoire (choisir des parties). Elle s'applique
  telle quelle à une machine qui recadre (section 5).

- **Pascal Bonitzer, *Décadrages. Peinture et cinéma***, Paris, Cahiers du cinéma / Éditions de
  l'Étoile, 1985. Notice seule : https://openlibrary.org/works/OL4354104W.
  → Le « décadrage » : cadrer à côté, laisser le centre vide, couper les corps au bord ; une
  pratique commune à la peinture moderne et au cinéma. [incertain : résumé de mémoire.]

- **Lev Manovich, *The Language of New Media***, Cambridge (Mass.), MIT Press, 2001. Table des
  matières ouverte : https://archive.neural.it/init/default/show/1629. Chapitre 2, « The
  Interface » ; section « The Screen and the User » (p. 94), avec « A Screen's Genealogy » (p. 95),
  « The Screen and the Body » (p. 103), « Representation versus Simulation » (p. 111).
  → Manovich fait une généalogie de l'écran : l'écran « classique » (du tableau au cinéma) est un
  cadre rectangulaire qui ouvre sur un espace virtuel ; puis viennent l'écran « dynamique »
  (cinéma, télévision) et l'écran « en temps réel » (radar, ordinateur), où l'image se met à jour
  et où plusieurs fenêtres coexistent. [incertain : les termes exacts n'ont été lus que dans la
  table et dans une source secondaire, pas dans le texte.]
  *Pour nous :* notre couche « écran photographié » mêle les deux régimes : une fenêtre de
  navigateur (cadre dynamique) dans une photo (cadre classique).

- **Paul Virilio, *La Machine de vision***, Paris, Galilée, coll. « L'espace critique », 1988.
  Notice : https://openlibrary.org/works/OL542606W ; trad. anglaise *The Vision Machine*, Indiana
  University Press / BFI, 1994 (https://openlibrary.org/works/OL542653W).
  → La « vision sans regard » : des machines produisent et lisent des images qu'aucun humain ne
  regarde. [incertain : expression et page (p. 125) relevées dans une source secondaire, non lues
  dans le livre.] C'est l'ancêtre français du thème de l'image opératoire (section 2).

- **Vivian Sobchack, *The Address of the Eye: A Phenomenology of Film Experience***, Princeton
  University Press, 1992. Notice seule : https://openlibrary.org/works/OL2664327W.
  → Le film comme un « regard » qui se donne à voir : le cadre est la trace d'une perception
  incarnée, pas seulement une limite géométrique. [incertain : résumé de mémoire.]
  *Pour nous :* contraste utile. Le cadrage machine n'est la trace d'aucun corps.

- **Alexander R. Galloway, *The Interface Effect***, Cambridge, Polity, 2012. Notice :
  https://openlibrary.org/works/OL22759649W.
  → « Interfaces are not things, but rather processes that effect a result of whatever kind »
  (citation lue sur une page secondaire, https://whitneyannetrettien.com/whiki/index.php/Galloway_2012,
  [incertain : non vérifiée sur le livre]). Le bord de l'écran n'est pas un objet mais un effet.

- **Lev Manovich, *Cultural Analytics***, Cambridge (Mass.), MIT Press, 2020. Notice :
  https://openlibrary.org/works/OL22166377W.
  → Analyser la culture par grands ensembles d'images ; un chapitre porte sur les « méthodes de
  visualisation des médias » (des milliers d'images disposées côte à côte, en vignettes). [Contenu
  vérifié par la table des matières seulement.]
  *Pour nous :* la vignette est un recadrage systématique : chaque œuvre réduite au même petit
  carré. C'est le « musée imaginaire » de Malraux poussé à l'extrême.

---

## 2. Images opératoires : des images faites pour les machines

Idée commune : beaucoup d'images ne sont plus faites pour être vues. Leur « cadre » est celui de
la tâche, pas celui du regard.

- **Harun Farocki, « Phantom Images »**, trad. Brian Poole, *Public: Art, Culture, Ideas* 29
  (2004), p. 12-22 [incertain : pages 12-22 ; la p. 17 est confirmée par Hoel ci-dessous]. Notice
  de la revue : https://public.journals.yorku.ca/index.php/public/article/view/30354 (page protégée,
  existence confirmée par Tom Holert, e-flux journal 162, avril 2026,
  https://www.e-flux.com/journal/162/6776863/beneath-the-information-the-operation-harun-farocki-and-the-work-of-images).
  Installation et films : *Eye/Machine* I-III (2001-2003).
  → Les images opératoires « do not represent an object, but rather are part of an operation »
  (cité par Hoel, p. 17 de Farocki). Selon les intertitres d'*Eye/Machine*, elles ne sont faites ni
  pour l'édification ni pour la contemplation, ni vraiment pour des yeux humains.

- **Trevor Paglen, « Operational Images »**, *e-flux journal* 59, novembre 2014.
  https://www.e-flux.com/journal/59/61130/operational-images/
  → À propos de Farocki : « Instead of simply representing things in the world, the machines and
  their images were starting to "do" things in the world. »

- **Trevor Paglen, « Invisible Images (Your Pictures Are Looking at You) »**, *The New Inquiry*,
  8 décembre 2016. https://thenewinquiry.com/invisible-images-your-pictures-are-looking-at-you/
  → « The overwhelming majority of images are now made by machines for other machines, with
  humans rarely in the loop. » Une image numérique n'a pas besoin d'être affichée pour qu'une
  machine en fasse quelque chose. D'où : « we need to unlearn how to see like humans ».
  *Pour nous :* une image qu'on ne regarde pas n'a pas de cadre de présentation. Elle n'a qu'un
  bord de fichier.

- **Volker Pantenburg, « Working images: Harun Farocki and the operational image »**, dans
  J. Eder et C. Klonk (dir.), *Image Operations. Visual Media and Political Conflict*, Manchester
  University Press, 2017 (en ligne 2016). https://doi.org/10.7228/manchester/9781526107213.003.0004
  (notice seule) → Généalogie de la notion ; pose la question : les images opératoires sont-elles
  encore des images ?

- **Aud Sissel Hoel, « Operative Images. Inroads to a New Paradigm of Media Theory »**, dans
  L. Feiersinger, K. Friedrich et M. Queisner (dir.), *Image – Action – Space. Situating the
  Screen in Visual Practice*, Berlin, De Gruyter, 2018, p. 11-27 (Crossref : 11-28).
  https://doi.org/10.1515/9783110464979-002 (texte lu sur le PDF en libre accès).
  → Hoel compare quatre approches (Farocki, Manovich, Ernst, et une approche par l'« efficacité »
  des images). Elle montre que la définition de Farocki est surtout négative et suppose une idée
  étroite de l'image « normale » : une représentation fixe, à l'échelle humaine. Elle reproche à
  l'approche purement technique d'oublier que les médias restent des interfaces vers le monde et
  vers les autres.
  *Pour nous :* garde-fou. Opposer « image à voir » et « image pour machine » trop nettement est
  une simplification que Hoel critique.

- **Ingrid Hoelzl & Rémi Marie, *Softimage. Towards a New Theory of the Digital Image***,
  Bristol, Intellect, 2015. https://doi.org/10.2307/j.ctv36xvwzz (notice seule). Et **« Google
  Street View: navigating the operative image »**, *Visual Studies* 29(3), 2014, p. 261-271,
  https://doi.org/10.1080/1472586X.2014.941559 (notice seule).
  → L'image numérique n'est plus une représentation stable mais un processus en mise à jour ;
  Street View en est le cas type : une image faite pour naviguer.

- **Jussi Parikka, *Operational Images: From the Visual to the Invisual***, Minneapolis,
  University of Minnesota Press, 2023. https://doi.org/10.5749/9781452970929 ; libre accès
  https://manifold.umn.edu/projects/operational-images (CC BY-NC-ND).
  → Prolonge Farocki aux images de mesure, de suivi, d'apprentissage automatique, d'IA et d'art.
  Chapitre 2 : « What Is Not an Image? On AI, Data, and Invisuality ». L'« invisuel » : ce qui,
  dans l'image, n'est fait que pour le calcul.

- **Hito Steyerl, « A Sea of Data: Apophenia and Pattern (Mis-)Recognition »**, *e-flux journal*
  72, avril 2016. https://www.e-flux.com/journal/72/60480/a-sea-of-data-apophenia-and-pattern-misrecognition
  → « Not seeing anything intelligible is the new normal. » À propos de DeepDream, elle cite
  Google : un réseau simple peut « over-interpret an image ». La machine voit des formes là où il
  n'y en a pas (apophénie).

- **Matteo Pasquinelli & Vladan Joler, « The Nooscope manifested: AI as instrument of knowledge
  extractivism »**, *AI & Society* 36(4), 2021, p. 1263-1280 (en ligne 2020).
  https://doi.org/10.1007/s00146-020-01097-6 (notice seule).
  → L'IA comme instrument d'optique (un « nooscope ») qui déforme ce qu'il montre, à chaque étape :
  données, étiquetage, modèle.
  **Matteo Pasquinelli, *The Eye of the Master. A Social History of Artificial Intelligence***,
  Londres, Verso, 2023. https://openlibrary.org/works/OL37531579W (notice seule ; page d'auteur :
  https://matteopasquinelli.com/the-eye-of-the-master/).
  → La reconnaissance de formes vient de l'organisation du travail, pas de l'imitation du cerveau.
  [incertain : détail des chapitres non lu.]

- **Joanna Zylinska, *AI Art: Machine Visions and Warped Dreams***, Londres, Open Humanities
  Press, 2020. https://www.openhumanitiespress.org/books/titles/ai-art/
  → Parler de créativité machine oblige à parler de la place de l'humain dans le système
  technique (travail, automatisation).

- **Vilém Flusser, *Für eine Philosophie der Fotografie***, Göttingen, European Photography,
  1983. https://openlibrary.org/works/OL45221642W (notice seule).
  → L'appareil photo a un « programme » ; le photographe joue à l'intérieur des possibilités que
  l'appareil a prévues. [incertain : résumé de mémoire.]
  *Pour nous :* le cadre est déjà prescrit par l'appareil. Un modèle de vision est un appareil au
  sens de Flusser, avec un programme plus étroit encore.

---

## 3. Le détail et le recadrage en histoire de l'art

Recadrer une œuvre est un geste ancien de l'historien de l'art (diapositive, gros plan dans le
livre). Le zoom numérique le prolonge.

- **Daniel Arasse, *Le Détail. Pour une histoire rapprochée de la peinture***, Paris,
  Flammarion, coll. « Idées et recherches », 1992, 287 p. Notice :
  https://www.helveticarchives.admin.ch/detail.aspx?ID=884501 ; rééd. coll. « Champs »
  (https://openlibrary.org/works/OL8975467W).
  → Arasse distingue le *particolare* (une petite partie de l'objet représenté) et le *dettaglio*
  (le résultat du geste de celui qui découpe, peintre ou regardeur). Regarder de près fait voir
  ce que le tableau entier cache. [Distinction de mémoire ; cohérente avec le livre mais non
  relue.]
  *Pour nous :* le *dettaglio* est un recadrage par un sujet. La machine découpe aussi l'image en
  morceaux (les « patchs » de 32 × 32 pixels d'un CLIP ViT-B/32), mais sans regard : c'est un
  découpage, pas un détail au sens d'Arasse.

- **Trevor Fawcett, « Visual facts and the nineteenth-century art lecture »**, *Art History*
  6(4), 1983, p. 442-460. https://doi.org/10.1111/j.1467-8365.1983.tb00094.x (notice seule).
  → La projection photographique transforme les œuvres en « faits visuels » pour l'enseignement.
  Voir aussi Fawcett, « Graphic versus photographic in the nineteenth-century reproduction »,
  *Art History* 9(2), 1986, p. 185-212, https://doi.org/10.1111/j.1467-8365.1986.tb00194.x.

- **Robert S. Nelson, « The Slide Lecture, or the Work of Art "History" in the Age of Mechanical
  Reproduction »**, *Critical Inquiry* 26(3), 2000, p. 414-434. https://doi.org/10.1086/448973
  (notice seule).
  → La conférence à diapositives comme dispositif : l'œuvre y est toujours une image projetée,
  cadrée et mise en regard d'une autre.

- **Frederick N. Bohrer, « Photographic perspectives: photography and the institutional formation
  of art history »**, dans Elizabeth Mansfield (dir.), *Art History and Its Institutions:
  Foundations of a Discipline*, Londres, Routledge, 2002, p. 246 sq. Table des matières :
  https://www.obalkyknih.cz/file/toc/862418/pdf ; volume : https://openlibrary.org/works/OL18438282W.
  → La photographie a façonné la discipline elle-même. [incertain : contenu non lu.]

- **Le zoom numérique (Google Art Project, gigapixels).**
  **Nancy Proctor, « The Google Art Project: A New Generation of Museums on the Web? »**,
  *Curator* 54(2), 2011, p. 215-221, https://doi.org/10.1111/j.2151-6952.2011.00083.x ;
  **Elizabeth Mansfield, « Google Art Project and Digital Scholarship in the Visual Arts »**,
  *Visual Resources* 30(1), 2014, p. 110-117, https://doi.org/10.1080/01973762.2014.879409 ;
  **Werner Schweibenz, « The Work of Art in the Age of Digital Reproduction »**, *Museum
  International* 70(1-2), 2018, p. 8-21, https://doi.org/10.1111/muse.12189 (notices seules).
  → Ces textes discutent la valeur savante des reproductions en très haute définition.
  **Lacune :** je n'ai pas trouvé de critique savante vérifiée portant précisément sur le zoom
  gigapixel comme recadrage (le coup de pinceau isolé de son tableau). La presse de 2011-2012 en
  parle, pas la littérature savante que j'ai pu ouvrir. À chercher encore.
  *Pour nous :* le gigapixel est le *dettaglio* d'Arasse rendu infini et sans auteur : n'importe
  quel recadrage devient possible, aucun n'est proposé.

---

## 4. Critique de la vision artificielle appliquée à l'art

- **Fabian Offert, « On the Concept of History (in Foundation Models) »**, *IMAGE* 37 (2023),
  p. 121-134. https://doi.org/10.25969/mediarep/22316 (notice DataCite, résumé lu).
  → Les modèles comme CLIP dépendent des formes anciennes de (re)médiation. D'où la formule :
  « for cLIP and cLIP-dependent generative models, the recent past is literally black and white,
  and the distant past is actually made of marble ». Le passé y est la somme de ses
  reproductions.
  *Pour nous :* c'est l'argument le plus proche du nôtre. Le support (photo noir et blanc, plâtre,
  marbre) devient le contenu.

- **Fabian Offert & Thao Phan, « A sign that spells… »** (titre court donné par Crossref ; le
  titre complet sur la page de la revue n'a pas été lu), *Journal of Digital Social Research* 6(4),
  2024, p. 49-59. https://doi.org/10.33621/jdsr.v6i440462 (résumé lu).
  → DALL·E opère par « compression sémantique », technique « inhumaine et invisuelle » qui
  reproduit pourtant la blanchité comme trait latent de la culture visuelle dominante.

- **Amanda Wasielewski, « DALL-E in Flatland »**, *Media Theory* 8(1), 2024, p. 185-204.
  https://doi.org/10.70064/mt.v8i1.1073 (résumé lu).
  → Les images générées ont une forme photographique sans expérience de l'espace qui les
  sous-tend. (Son livre *Computational Formalism* est déjà cité dans l'article.)

- **Roland Meyer, « The New Value of the Archive: AI Image Generation and the Visual Economy of
  "Style" »**, *IMAGE* 37 (2023), p. 100-111. https://doi.org/10.25969/mediarep/22314 (résumé
  lu).
  → Les requêtes (« prompts ») sont des commandes de recherche dans l'espace des images
  possibles. Le « style » y devient la catégorie centrale : il mêle manières d'artistes, genres
  commerciaux et anciens aspects techniques (le film argentique).

- **Eva Cetinic & James She, « Understanding and Creating Art with AI: Review and Outlook »**,
  *ACM TOMM* 18(2), 2022, p. 1-22. https://doi.org/10.1145/3475799 (notice seule).
  → Bilan des travaux d'IA sur l'art (classification, recherche, génération), vu depuis
  l'informatique. Utile comme carte du domaine, pas comme critique.

- **Johanna Drucker, « Humanities Approaches to Graphical Display »**, *Digital Humanities
  Quarterly* 5(1), 2011. https://dhq.digitalhumanities.org/vol/5/1/000091/000091.html
  → « we reconceive all data as capta » : la donnée est prise, pas donnée. Les approches réalistes
  supposent des phénomènes « observer-independent ».
  **Johanna Drucker, « Is There a "Digital" Art History? »**, *Visual Resources* 29(1-2), 2013,
  p. 5-13. https://doi.org/10.1080/01973762.2013.761106 (notice seule).
  → Distingue l'histoire de l'art *numérisée* (accès aux images) de l'histoire de l'art
  *numérique* (méthodes de calcul). [Distinction de mémoire.]
  *Pour nous :* une étiquette, un recadrage, une vignette sont des *capta* : des choix.

- **Claire Bishop, « Against Digital Art History »**, *International Journal for Digital Art
  History* 3, 2018. https://doi.org/10.11588/dah.2018.3.49915 (page ouverte :
  https://dahj.org/article/against-digital-art-history).
  → Relie l'histoire de l'art numérique aux métriques néolibérales ; envisage pourtant un usage
  critique de la « lecture à distance ». Suite : **Johanna Drucker & Claire Bishop, « A
  Conversation on Digital Art History »**, dans *Debates in the Digital Humanities 2019*,
  p. 321-334, https://doi.org/10.5749/j.ctvg251hk.30 (notice seule).

- **Lev Manovich & Emanuele Arielli, *Artificial Aesthetics: Generative AI, Art and Visual
  Media***, chapitres en ligne 2021-2024, PDF complet 15/01/2025.
  https://manovich.net/index.php/projects/artificial-aesthetics
  → Neuf chapitres ; voir surtout Arielli, « Human Perception and The Artificial Gaze » (ch. 6) et
  Manovich, « Separate and Reassemble » (ch. 7).

- **Thomas Smits & Melvin Wevers, « The agency of computer vision models as optical
  instruments »**, *Visual Communication* 21(2), 2022 (en ligne 2021),
  p. 329-349. https://doi.org/10.1177/1470357221992097 (résumé lu).
  → Avec Latour et Crary : les modèles de vision sont des instruments d'optique. Ils analysent
  cinq étapes, dont le choix de la tâche et le choix des catégories.

---

## 5. Désignation, plateformes, recadrage automatique

La désignation de l'art par l'institution (Danto, Dickie) est traitée dans `cadrage-et-valeur.md`,
§ 1.4 ; on ne la répète pas. Ce qui suit porte sur le moment où **un algorithme** choisit ce qui
est montré et comment c'est coupé.

- **Tarleton Gillespie, « The Relevance of Algorithms »**, dans T. Gillespie, P. Boczkowski et
  K. Foot (dir.), *Media Technologies*, MIT Press, 2014, p. 167-194.
  https://doi.org/10.7551/mitpress/9042.003.0013 (notice seule).
  → Les algorithmes de sélection jouent un rôle d'évaluation publique : ils décident de ce qui
  est « pertinent ». Texte de référence sur la curation algorithmique.

- **Laura M. Herman & Caterina Moruzzi, « *The Algorithmic Pedestal*: A Practice-Based Study of
  Algorithmic and Artistic Curation »**, *Leonardo* 57(5), 2024, p. 485-492.
  https://doi.org/10.1162/leon_a_02561 (résumé lu) ; page du projet (Oxford Internet Institute) :
  https://www.oii.ox.ac.uk/research/projects/the-algorithmic-pedestal/
  → 800 images de l'Open Access du Met téléversées sur un compte Instagram neuf, sans légende ni
  métadonnée ; le fil d'Instagram choisit et ordonne. L'artiste Fabienne Hess choisit dans la
  même collection. Exposition à Londres (J/M Gallery), 11-17 janvier 2023.
  **Thomas Şerban von Davier, Laura M. Herman & Caterina Moruzzi, « A Machine Walks into an
  Exhibit: A Technical Analysis of Art Curation »**, *Arts* 13(5), 138, 2024.
  https://doi.org/10.3390/arts13050138 (notice seule ; page éditeur refusée).
  → Les images choisies diffèrent nettement de l'ensemble de la collection, mais peu entre
  choix humain et choix d'Instagram (d'après le résumé trouvé par recherche).
  *Pour nous :* c'est l'expérience la plus proche d'un « monde de l'art » algorithmique au sens
  de Dickie : une plateforme qui met des œuvres sur le piédestal.

- **Recadrage automatique par saillance (Twitter, Google, Apple).**
  **Kyra Yee, Uthaipon Tantipongpipat & Shubhanshu Mishra, « Image Cropping on Twitter: Fairness
  Metrics, their Limitations, and the Importance of Representation, Design, and Agency »**,
  *Proc. ACM HCI* 5 (CSCW2), 2021, p. 1-24. https://doi.org/10.1145/3479594 ; arXiv 2105.08667
  (résumé lu).
  → Twitter centrait le recadrage sur le point jugé le plus saillant. Le choix du seul maximum
  (« argmax bias ») amplifie les écarts entre groupes. Conclusion : « We suggest the removal of
  saliency-based cropping in favor of a solution that better preserves user agency. » (Le blog
  de Twitter du 19/05/2021 a refusé l'accès automatique.)
  **Abeba Birhane, Vinay Uday Prabhu & John Whaley, « Auditing saliency cropping algorithms »**,
  WACV 2022, p. 1515-1523 (Crossref) ou 4051-4059 (actes CVF) [incertain : pagination].
  https://doi.org/10.1109/wacv51458.2022.00158 ; PDF :
  https://openaccess.thecvf.com/content/WACV2022/papers/Birhane_Auditing_Saliency_Cropping_Algorithms_WACV_2022_paper.pdf
  → Audit de Twitter, Google et Apple : recadrages de type « male gaze » et biais de race et de
  genre.
  *Pour nous :* c'est le cadrage au sens de Deleuze (choisir les parties) confié à une carte de
  saillance. Notre résultat principal (la saillance de l'œuvre décide) rejoint ce point par un
  autre chemin.

- **Lev Manovich, *Instagram and Contemporary Image***, en ligne, 2017 (CC BY-NC-ND).
  https://manovich.net/index.php/projects/instagram-and-contemporary-image
  → Analyse de 16 millions de photos Instagram ; une partie s'intitule « Instagrammism and
  contemporary cultural identity ».
  **Le format carré d'Instagram : non vérifié.** La page de Manovich ne parle pas du carré. Je
  n'ai pas trouvé de source savante ouverte sur le carré comme « cadre de plateforme ». À ne pas
  citer en l'état.

- **Kyle Chayka, *Filterworld***, 2024 (éditions notées : Vintage, Heligo Books…).
  https://openlibrary.org/works/OL37617503W (notice seule). → Essai journalistique : la
  recommandation des plateformes uniformise le goût. [incertain : sous-titre, éditeur original et
  contenu non vérifiés ; résumé de mémoire.]

---

## 6. Le jeu de données comme cadre

Un jeu de données donne à chaque image une catégorie ou une légende. Il la recadre (souvent en
carré, à basse résolution) et la met dans une série. Ce sont trois opérations de cadre.

- **Kate Crawford & Trevor Paglen, « Excavating AI: The Politics of Images in Machine Learning
  Training Sets »**, AI Now Institute, 19 septembre 2019, https://excavating.ai/ ; version revue
  *AI & Society*, 2021, https://doi.org/10.1007/s00146-021-01162-8.
  → « Datasets aren't simply raw materials to feed algorithms, but are political
  interventions. » Il n'existe pas de point de vue « neutral, natural, or apolitical » pour
  construire des données. Sur ImageNet : « what happens when people are categorized like
  objects ». Et : « Images are open to interpretation and reinterpretation. »
  **Critique :** Michael J. Lyons, « Excavating "Excavating AI": The Elephant in the Gallery »,
  2020, https://doi.org/10.5281/zenodo.4037538 ; et « "Excavating AI" Re-excavated », 2021,
  https://doi.org/10.5281/zenodo.5140556. → Le co-auteur du jeu JAFFE conteste leur récit et leur
  usage des images sans consentement.

- **Emily Denton, Alex Hanna, Razvan Amironesei, Andrew Smart & Hilary Nicole, « On the genealogy
  of machine learning datasets: A critical history of ImageNet »**, *Big Data & Society* 8(2),
  2021. https://doi.org/10.1177/20539517211035955 (résumé lu).
  → Les jeux de données comme infrastructure d'information ; les normes et présupposés
  inscrits dans ImageNet.

- **Nicolas Malevé, « On the data set's ruins »**, *AI & Society* 36(4), 2021, p. 1117-1131 (en
  ligne 2020). https://doi.org/10.1007/s00146-020-01093-w (résumé lu).
  → Des travailleurs précaires étiquettent des photos en quelques millisecondes chacune. Cette
  « échelle » mobilise une culture photographique.
  *Pour nous :* l'étiquette est posée en un coup d'œil. C'est un cadrage du sens aussi rapide
  qu'un recadrage automatique.

- **Abeba Birhane & Vinay Uday Prabhu, « Large image datasets: A pyrrhic win for computer
  vision? »**, WACV 2021, p. 1536-1546. https://doi.org/10.1109/wacv48630.2021.00158 (notice
  seule). → Catégories offensantes et images non consenties dans les grands jeux de données.
  **Birhane, Prabhu & Kahembwe, « Multimodal datasets: misogyny, pornography, and malignant
  stereotypes »**, arXiv 2110.01963, 2021, https://doi.org/10.48550/arxiv.2110.01963 (résumé lu)
  → Audit de LAION-400M. **Birhane et al., « Into the LAION's Den: Investigating Hate in
  Multimodal Datasets »**, NeurIPS 36, 2023, p. 21268-21284, https://doi.org/10.52202/075280-0930.

- **Christoph Schuhmann et al., « LAION-5B: An Open Large-Scale Dataset for Training Next
  Generation Image-Text Models »**, NeurIPS 35, 2022, p. 25278-25294.
  https://doi.org/10.52202/068431-1833 (notice seule).
  → Les légendes de LAION viennent des attributs `alt` des pages web : un paratexte écrit pour
  l'accessibilité ou le référencement, pas pour décrire l'œuvre.

- **Andy Baio, « Exploring 12 Million of the 2.3 Billion Images Used to Train Stable Diffusion's
  Image Generator »**, Waxy.org, 30 août 2022.
  https://waxy.org/2022/08/exploring-12-million-of-the-images-used-to-train-stable-diffusions-image-generator/
  (enquête de blog, pas article savant).
  → Sur le sous-ensemble LAION-Aesthetics v2 6+ (12 millions d'images, score esthétique prédit
  ≥ 6) : Pinterest 8,5 %, WordPress 6,8 %, **Fine Art America 5,8 %** (site qui « sells art prints
  and posters »), Wikimedia seulement 74 000 images. L'artiste le plus fréquent est Thomas
  Kinkade (9 268 images).
  *Pour nous (extrapolation, à vérifier sur les images) :* l'art arrive dans ces données surtout
  par des sites de vente de reproductions, où l'œuvre est souvent montrée encadrée, sur un mur,
  en maquette de produit. Le cadre marchand serait alors dans les données d'entraînement
  elles-mêmes. Cela rejoint notre constat 4.1 (le musée livre déjà des poupées russes).

- **Le hors-champ inventé : l'« outpainting ».** OpenAI, « DALL·E: Introducing outpainting »,
  https://openai.com/index/dall-e-introducing-outpainting/ (page refusée à l'accès automatique,
  403 ; contenu confirmé par la recherche et par Harry Guinness, « DALL-E's latest trick:
  extending the boundaries of paintings », *Popular Science*, 3 septembre 2022,
  https://www.popsci.com/technology/open-ai-dalle-outpainting/).
  → L'outil prolonge une image au-delà de ses bords. Exemple vedette : *La Jeune Fille à la perle*
  de Vermeer étendue « to around 20 times its original size » (illustration créditée « August
  Kamp / OpenAI / Johannes Vermeer »).
  **Lacune :** je n'ai pas trouvé d'article savant vérifié qui lise l'outpainting avec Bazin ou
  Deleuze. Ce rapprochement est le nôtre (section 7, idée 5).

---

## 7. Ce que cela prolonge dans la théorie du cadre

Chaque idée sépare ce que disent les auteurs et ce que nous en tirons.

**1. Cadre de présentation et cadre opératoire.**
*Les auteurs :* Simmel et Ortega pensent un cadre fait pour être vu : il isole l'œuvre pour le
regard. Farocki, Paglen (2014, 2016) et Parikka (2023) décrivent des images faites pour une
opération, souvent sans spectateur. Hoel (2018) avertit que l'opposition est trop nette.
*Nous :* il y a deux familles de cadres. Le cadre de présentation dit « regardez ceci ». Le cadre
opératoire (le carré 224 × 224 d'un encodeur, la vignette, le recadrage d'un fil) dit « traitez
ceci ». Une même reproduction d'œuvre porte souvent les deux à la fois. Nos couches empilent des
cadres de présentation ; l'encodeur leur ajoute un cadre opératoire, le dernier et le seul qu'il
« connaisse ».

**2. Le recadrage machine est un cadrage sans auteur, réglé par la saillance.**
*Les auteurs :* pour Deleuze (1983, p. 31-32), cadrer est « l'art de choisir les parties ». Yee et
al. (2021) et Birhane et al. (2022) montrent que le recadrage automatique choisit le point le plus
saillant, et que ce choix n'est pas neutre. Arasse (1992) distingue le détail découpé par un
regard (*dettaglio*).
*Nous :* le cadrage machine garde la forme du choix mais perd le sujet qui choisit. Il ne
« décadre » jamais (Bonitzer) : il centre toujours sur le maximum. Notre résultat (la saillance de
l'œuvre décide de sa lecture, pas le support) est un cas de ce régime.

**3. La catégorie et la légende sont un cadre.**
*Les auteurs :* Bateson fait du cadre un méta-message ; Genette fait de la légende un paratexte.
Crawford et Paglen (2019), Denton et al. (2021), Malevé (2021) montrent que les catégories et
l'étiquetage des jeux de données sont des choix politiques, faits vite et à grande échelle.
Drucker (2011) : la donnée est *capta*. Schuhmann et al. (2022) : les légendes de LAION sont des
textes `alt`.
*Nous :* pour une machine, le cadre le plus fort n'est pas visuel mais verbal. La catégorie dit
« ceci est un chien », comme la bordure dorée dit « ceci est un tableau ». Les attaques
typographiques déjà citées dans l'article (Goh et al. 2021) sont le cas limite : le mot écrit dans
l'image l'emporte sur l'image.

**4. Le bord du fichier est le seul cadre certain, mais c'est un cache.**
*Les auteurs :* Bazin oppose le cadre centripète du tableau au cache centrifuge de l'écran.
Manovich (2001) fait la généalogie de l'écran ; Galloway (2012) dit que l'interface est un effet,
non une chose. Paglen (2016) : l'image n'a pas besoin d'être affichée.
*Nous :* pour un modèle, aucune bordure dans l'image n'est garantie comme cadre ; seul le bord du
fichier l'est. Or ce bord a le statut d'un cache : il coupe sans signifier. D'où une hypothèse à
tester : la machine lit tout ce qui est dans le fichier comme une seule scène, centrifuge ; elle
ne sait pas qu'une bordure dorée est centripète. Nos résultats vont dans ce sens (le cadre doré
change peu les mesures, le support « fait partie de la scène »).

**5. L'outpainting invente le hors-champ.**
*Les auteurs :* Deleuze : le cadre « détermine un hors-champ ». Bazin : l'écran laisse supposer
que le monde continue. OpenAI (2022) montre Vermeer prolongé vingt fois au-delà de son cadre.
*Nous :* le cadre du tableau, centripète, n'a pas de hors-champ au sens du cinéma. L'outpainting
traite pourtant le tableau comme un cache et remplit le hors-champ avec le probable. C'est la
négation exacte du cadre de Simmel. Aucune source savante vérifiée ne fait encore ce
rapprochement : c'est une proposition.

**6. Le zoom sans fin et la tuile : le détail sans regard.**
*Les auteurs :* Arasse (1992) sur le détail ; Fawcett (1983) et Nelson (2000) sur la diapositive
qui fait de l'œuvre un « fait visuel » cadré ; Proctor (2011) et Mansfield (2014) sur le Google
Art Project.
*Nous :* le gigapixel rend tous les recadrages possibles sans en proposer aucun. À l'inverse, le
modèle découpe l'image en tuiles de taille fixe. Dans les deux cas, le détail perd l'auteur du
découpage qui, pour Arasse, faisait son sens.

**7. La plateforme désigne ; le jeu de données encadre en marchandise.**
*Les auteurs :* Gillespie (2014) sur la « pertinence » décidée par l'algorithme ; Herman et
Moruzzi (2024) font choisir des œuvres du Met par Instagram ; Baio (2022) montre qu'une part
importante de l'art dans LAION-Aesthetics vient d'un site de vente de reproductions ; Meyer (2023)
fait du « style » la monnaie des générateurs ; Offert (2023) : pour CLIP, le passé est « made of
marble ».
*Nous :* Danto et Dickie (voir `cadrage-et-valeur.md`) placent la désignation de l'art dans un
monde de l'art. Une part de cette désignation passe aujourd'hui par la recommandation et par la
composition des données. Et l'image d'art que la machine a apprise est souvent une image déjà
encadrée, posée sur un mur, mise en vente. Si cela se confirme à l'inspection, la machine aurait
appris le cadre comme un attribut ordinaire de « l'art », et non comme une limite.

---

## Ce que je n'ai pas pu vérifier

- Bazin : texte français et page de « Peinture et cinéma » ; seule la traduction anglaise, citée
  par Dalle Vacche, a été lue.
- Manovich 2001 : les expressions « écran classique / dynamique / en temps réel » n'ont pas été
  lues dans le livre (table des matières seule).
- Virilio : « vision sans regard » et la p. 125 viennent d'une source secondaire.
- Galloway : la phrase citée vient d'une page secondaire.
- Farocki, *Public* 29 : pages 12-22 non confirmées (la p. 17 l'est, par Hoel).
- Sobchack, Bonitzer, Flusser, Pasquinelli (livre), Bohrer, Drucker 2013, Arasse (distinction
  *particolare* / *dettaglio*) : notices ouvertes, contenu résumé de mémoire.
- Offert & Phan 2024 : titre complet. Chayka 2024 : sous-titre et éditeur original.
- Birhane, Prabhu & Whaley 2022 : pagination (deux versions).
- Pages refusées à l'accès automatique : blog Twitter (19/05/2021), billet OpenAI sur
  l'outpainting, MDPI (*Arts*), revue *Public*, revue de Heidelberg (Bishop, lu sur le site
  miroir dahj.org).
- **Non trouvés :** une critique savante du zoom gigapixel comme recadrage ; une étude savante du
  format carré d'Instagram comme cadre ; une lecture savante de l'outpainting par la théorie du
  hors-champ. Ce sont peut-être de vrais manques — ou des recherches à refaire.
