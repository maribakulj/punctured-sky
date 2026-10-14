# Comment les machines cadrent les images (et les images d'art)

*État de la littérature, côté machines. 14/10/2026. Complète `litterature.md` (théorie du cadre,
robustesse) et `cadrage-et-valeur.md` (cadre, prix, prestige).*

**Comment c'est vérifié.** Chaque référence a été ouverte : page arXiv (via son API), page des
actes CVF, notice Crossref, page de l'éditeur, page du musée, ou code source sur GitHub. Le lien
donné est celui qui a servi. Quand un détail n'a pas pu être confirmé, c'est écrit **[incertain]**.
Les passages cités entre guillemets ont été lus dans le texte (PDF ou page).

**Ce que fait la machine au cadre.** Pour chaque travail, une étiquette dit ce que la machine fait :

- **RECADRE** : elle coupe l'image (et parfois le cadre ou les bords) ;
- **IGNORE** : elle apprend à ne pas tenir compte du cadre ;
- **REPRODUIT** : elle garde ou recopie le cadre (ou le bord) comme une partie de l'image ;
- **INVENTE** : elle fabrique ce qu'il y a au-delà du bord.

Rappel du projet : nos détecteurs mettent le bord de « l'œuvre » autour du cadre doré (Grounding
DINO 98-100 %, SAM 2.1 79/80), mais coupent la marge des estampes. Un cadre ancien fait monter le
prix qu'un modèle vision-langage donne à ce qu'il ne reconnaît pas (journal, 09/10 et 13/10).

---

## En bref

1. **Avant même de « voir », la machine recadre.** CLIP et DINOv2 coupent l'image en carré au
   centre. Les bords d'une image allongée sont perdus. C'est écrit dans leur code. Peu d'études
   mesurent ce que cette coupe enlève ; elles viennent de la recherche d'images, pas de l'art.
2. **Le recadrage automatique a été audité, mais pour les visages.** Twitter centrait la vignette
   sur le point le plus « saillant ». Les audits (Yee et al. 2021 ; Birhane et al. 2022) montrent
   des biais de race et de genre. Twitter a fini par afficher les photos entières. Aucun audit sur
   des œuvres d'art.
3. **Pour reconnaître une œuvre en salle, la machine apprend à ignorer le cadre.** Le Met Dataset
   et SynGallery traitent le cadre, les reflets et le mur comme une gêne à surmonter.
4. **Les segmenteurs (SAM, SAM 3) sont utilisés dans les musées pour découper des détails**
   (prototype Rijksmuseum). Personne n'a publié où ils placent le bord d'une œuvre.
5. **La machine sait aussi inventer le hors-cadre** : outpainting de DALL·E (la *Jeune fille à la
   perle* étendue, 2022), bandes perdues de la *Ronde de nuit* recréées au Rijksmuseum (2021).
6. **Le cadrage de l'entrée change ce que disent les modèles vision-langage** (Wang, Larson & Zhao
   2026 ; ViCrop 2025). Une bordure ou un cercle dessinés suffisent à changer la tâche.
7. **Les jeux de données d'art sont faits d'images déjà recadrées**, en général sans cadre. Quand
   un cadre reste, les chercheurs le coupent à la main. Ce choix n'est presque jamais étudié.

---

## 1. Le recadrage comme prétraitement

Tous les grands encodeurs veulent une image carrée de taille fixe (224 × 224 pixels, par
exemple). Il faut donc couper ou déformer. Ce geste est rarement discuté.

- **Alec Radford, Jong Wook Kim, Chris Hallacy et al., « Learning Transferable Visual Models From
  Natural Language Supervision » (CLIP)**, ICML 2021. https://arxiv.org/abs/2103.00020 ; code :
  https://github.com/openai/CLIP/blob/main/clip/clip.py
  → À l'entraînement : « A random square crop from resized images is the only data augmentation
  used ». À l'usage, la fonction `_transform` fait `Resize(n_px)` puis `CenterCrop(n_px)` : le
  petit côté est mis à 224, puis on garde le carré du centre.
  → **RECADRE.** Sur une estampe en hauteur, le haut et le bas (souvent la marge, la lettre, le
  titre gravé) sortent du carré. Sur un tableau en largeur, ce sont les côtés.

- **Mathilde Caron, Hugo Touvron, Ishan Misra, Hervé Jégou, Julien Mairal, Piotr Bojanowski &
  Armand Joulin, « Emerging Properties in Self-Supervised Vision Transformers » (DINO)**, ICCV
  2021. https://arxiv.org/abs/2104.14294 ; code DINOv2 (évaluation) :
  https://github.com/facebookresearch/dinov2/blob/main/dinov2/data/transforms.py
  → DINO apprend avec des « multi-crops » : deux vues globales couvrant « plus de 50 % » de
  l'image, et des petites vues locales (« moins de 50 % »). Le modèle doit dire la même chose
  d'un fragment et de l'ensemble (« local-to-global correspondences »). À l'évaluation, DINOv2
  fait `Resize(256)` puis `CenterCrop(224)`.
  → **RECADRE**, deux fois : le modèle apprend qu'un détail vaut le tout, et on lui montre
  ensuite le centre seulement. (Notre projet complète les images en carré pour éviter cette
  coupe.)

- **Hugo Touvron, Andrea Vedaldi, Matthijs Douze & Hervé Jégou, « Fixing the train-test
  resolution discrepancy » (FixRes)**, NeurIPS 2019. https://arxiv.org/abs/1906.06423
  → Montre que le recadrage aléatoire de l'entraînement et le recadrage central du test ne
  montrent pas les objets à la même taille. Cet écart fait baisser les scores ; on le corrige.
  → **RECADRE**, et le prouve : la façon de couper change la taille apparente de l'objet, et donc
  la réponse.

- **Sangdoo Yun, Seong Joon Oh, Byeongho Heo, Dongyoon Han, Junsuk Choe & Sanghyuk Chun,
  « Re-labeling ImageNet: from Single to Multi-Labels, from Global to Localized Labels »**, CVPR
  2021. https://arxiv.org/abs/2101.05022
  → Une image d'ImageNet contient souvent plusieurs objets. Un recadrage aléatoire peut garder
  « un objet entièrement différent » de l'étiquette. L'étiquette ne suit pas la coupe.
  → **RECADRE**, et l'étiquette devient fausse. Transposé à l'art : un recadrage d'un tableau
  peut ne plus montrer ce que dit le titre.

- **Mostafa Dehghani, Basil Mustafa, Josip Djolonga et al., « Patch n' Pack: NaViT, a Vision
  Transformer for any Aspect Ratio and Resolution »**, NeurIPS 2023 [venue : incertain, seule la
  page arXiv a été lue]. https://arxiv.org/abs/2307.06304
  → Qualifie de « demonstrably suboptimal » le choix de redimensionner toutes les images à une
  taille fixe. NaViT accepte n'importe quel rapport d'aspect.
  → La réponse technique au problème : **ne plus recadrer**. Les modèles récents (Qwen-VL,
  Gemini, Claude) acceptent des formats variables, mais leurs détails ne sont pas publics.

- **Haotian Liu, Chunyuan Li, Yuheng Li & Yong Jae Lee, « Improved Baselines with Visual
  Instruction Tuning » (LLaVA-1.5)**, CVPR 2024. https://arxiv.org/abs/2310.03744 ; code :
  https://github.com/haotian-liu/LLaVA/blob/main/llava/mm_utils.py
  → Dans le code, l'option `pad` (fonction `expand2square`) colle l'image au centre d'un carré
  de couleur unie au lieu de la couper ; l'option `anyres` la découpe en tuiles.
  → **Ajoute un cadre** : pour ne rien couper, le modèle pose l'œuvre sur un fond uni, soit
  exactement notre contrôle « gris ».

- **Alberto Baldrati, Marco Bertini, Tiberio Uricchio & Alberto Del Bimbo, « Composed Image
  Retrieval using Contrastive Learning and Task-oriented CLIP-based Features »**, *ACM TOMM*
  20(3), 2023, art. 1-24. https://doi.org/10.1145/3617597 ; https://arxiv.org/abs/2308.11485
  → Seule étude trouvée qui **mesure** le problème : plus de la moitié de leurs images ont un
  rapport d'aspect d'au moins 1,5 ; le recadrage central de CLIP « removes a substantial
  portion of the image ». Ajouter des bandes évite la perte mais réduit la résolution ; ils
  choisissent un compromis.
  → **RECADRE**, mesuré, mais sur des photos de robes et de scènes, pas sur des œuvres.

- **Xiuye Gu, Tsung-Yi Lin, Weicheng Kuo & Yin Cui, « Open-vocabulary Object Detection via
  Vision and Language Knowledge Distillation » (ViLD)**, ICLR 2022.
  https://arxiv.org/abs/2104.13921
  → En annexe : le recadrage de CLIP déforme les régions très allongées. Coller la région sur un
  fond noir aide un modèle convolutif, mais pas CLIP, « probably because CLIP is never trained
  with black image patches ».
  → Indice précieux : **le fond ajouté autour de l'image n'est pas neutre** pour CLIP.

- **Piyapat Saranrittichai, Mauricio Munoz, Volker Fischer & Chaithanya Kumar Mummadi,
  « Zero-Shot Visual Classification with Guided Cropping » (GC-CLIP)**, prépublication arXiv,
  2023. https://arxiv.org/abs/2309.06581
  → CLIP classe moins bien quand l'objet est petit dans l'image. Recadrer autour de l'objet,
  avec un détecteur, améliore les scores.
  → **RECADRE** volontairement : c'est notre résultat sur la saillance, retourné en recette.

- **Ryan Ramos, Vladan Stojnić, Giorgos Kordopatis-Zilos, Yuta Nakashima, Giorgos Tolias & Noa
  Garcia, « Processing and acquisition traces in visual encoders: What does CLIP know about your
  camera? »**, ICCV 2025. https://arxiv.org/abs/2508.10637
  → Le redimensionnement, la compression et l'appareil laissent des traces lisibles dans les
  encodeurs, et ces traces peuvent changer la prédiction.
  → Le prétraitement **n'est pas neutre** : il s'imprime dans la représentation.

## 2. Recadrage automatique et saillance

- **Lucas Theis & Zehan Wang, « Speedy Neural Networks for Smart Auto-Cropping of Images »**,
  blog d'ingénierie de Twitter, 24 janvier 2018. Lu sur l'archive :
  https://web.archive.org/web/2019/https://blog.twitter.com/engineering/en_us/topics/infrastructure/2018/Smart-Auto-Cropping-of-Images.html
  → Avant 2018, Twitter centrait la vignette sur le visage le plus visible, ou sur le centre. Il
  passe à un modèle de saillance appris sur des données d'oculométrie : la vignette est centrée
  sur la zone où un humain regarderait d'abord.
  → **RECADRE** selon le regard moyen.

- **Kyra Yee, Uthaipon Tantipongpipat & Shubhanshu Mishra, « Image Cropping on Twitter: Fairness
  Metrics, their Limitations, and the Importance of Representation, Design, and Agency »**,
  *Proceedings of the ACM on Human-Computer Interaction* 5 (CSCW2), 2021, p. 1-24 [numéro
  d'article 450 : incertain]. https://doi.org/10.1145/3479594 ; https://arxiv.org/abs/2105.08667
  → Mesure des écarts systématiques (peau claire préférée, etc.). Nomme le « biais argmax » :
  couper autour d'un seul point, le plus saillant, amplifie les écarts. Recommande de supprimer
  le recadrage par saillance.
  → Billet associé (19 mai 2021) : « how to crop an image is a decision best made by people » ;
  Twitter teste l'affichage des photos entières.
  https://web.archive.org/web/2021/https://blog.twitter.com/engineering/en_us/topics/insights/2021/sharing-learnings-about-our-image-cropping-algorithm
  → **RECADRE**, puis **rend le cadrage à l'humain**. Pour l'art, la leçon est directe : une
  œuvre a déjà un cadrage, choisi par l'artiste ; la vignette automatique le remplace.

- **Abeba Birhane, Vinay Uday Prabhu & John Whaley, « Auditing saliency cropping algorithms »**,
  WACV 2022, p. 4051-4059.
  https://openaccess.thecvf.com/content/WACV2022/html/Birhane_Auditing_Saliency_Cropping_Algorithms_WACV_2022_paper.html
  → Audite les recadreurs de Twitter, Google et Apple. Tous ont des biais de race et de genre ;
  celui de Twitter produit souvent un recadrage « male gaze » (corps plutôt que visage), surtout
  sur des photos avec un fond couvert de logos.
  → **RECADRE**, et le fond (logos, texte) attire la coupe. Écho à nos résultats : ce qui entoure
  décide de ce qui est gardé.

- **Zhihang Zhong, Mingxi Cheng, Zhirong Wu et al., « ClipCrop: Conditioned Cropping Driven by
  Vision-Language Model »**, ICCV 2023 Workshops, p. 294-304.
  https://openaccess.thecvf.com/content/ICCV2023W/MMFM/html/Zhong_ClipCrop_Conditioned_Cropping_Driven_by_Vision-Language_Model_ICCVW_2023_paper.html
  → Recadrage « esthétique » guidé par un texte (« le chien », « les deux personnes »), bâti sur
  le détecteur OWL-ViT (de la même famille que notre OWLv2).
  → **RECADRE** sur commande : le mot choisit le cadre.

- **Seung Hyun Lee, Jijun Jiang, Yiran Xu et al., « Cropper: Vision-Language Model for Image
  Cropping through In-Context Learning »**, CVPR 2025, p. 30010-30019.
  https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Cropper_Vision-Language_Model_for_Image_Cropping_through_In-Context_Learning_CVPR_2025_paper.html
  → Un modèle vision-langage (Gemini 1.5 Pro dans leurs essais, selon le supplément) choisit un
  recadrage « agréable » à partir d'exemples, puis l'affine en plusieurs tours. Recadrage libre,
  centré sur un sujet, ou à un rapport d'aspect donné.
  → **RECADRE** avec le goût appris d'un grand modèle. Aucune évaluation sur des œuvres.

- **James Hong, Lu Yuan, Michaël Gharbi, Matthew Fisher & Kayvon Fatahalian, « Learning
  Subject-Aware Cropping by Outpainting Professional Photos » (GenCrop)**, AAAI 2024.
  https://arxiv.org/abs/2312.12080
  → Prend des photos professionnelles (déjà bien cadrées), les **étend** par génération, puis
  apprend à retrouver le cadrage d'origine.
  → **INVENTE puis RECADRE** : le cadrage professionnel devient la norme apprise.

- **Ben St. John, « An eye for detail: Zoom through 1,000 artworks thanks to the new Art Camera
  from the Google Cultural Institute »**, blog Google, 17 mai 2016.
  https://blog.google/outreach-initiatives/arts-culture/art-camera-cultural-institute/
  → Un robot photographie le tableau par morceaux ; le logiciel les assemble en une image d'un
  milliard de pixels. Le zoom serait « the closest thing to walking up to the real thing with a
  magnifying glass ».
  → **RECADRE par le zoom** : la plateforme offre l'œuvre comme un territoire de détails. Le
  billet ne parle pas du cadre physique.

- **IIIF Image API 3.0** (norme d'échange d'images des bibliothèques et musées), section 4.1
  « Region ». https://iiif.io/api/image/3.0/
  → Toute image IIIF peut être demandée par région (`x,y,w,h`, pourcentages) ou en `square`
  (carré dont la place est laissée au serveur, « centered is often a reasonable default »).
  → **RECADRE**, et c'est inscrit dans la norme : le recadrage central est le défaut conseillé
  pour les vignettes carrées.

*Non trouvé* : aucune étude publiée sur la façon dont les sites de musées ou les plateformes
choisissent automatiquement les vignettes d'œuvres. Voir « Ce qui manque ».

## 3. Détecter et découper les œuvres et leurs cadres

- **Nikolaos-Antonios Ypsilantis, Noa Garcia, Guangxing Han, Sarah Ibrahimi, Nanne van Noord &
  Giorgos Tolias, « The Met Dataset: Instance-level Recognition for Artworks »**, NeurIPS Datasets
  and Benchmarks 2021.
  https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/5f93f983524def3dca464469d2cf9f3e-Abstract-round2.html ;
  texte lu : https://arxiv.org/abs/2202.01747
  → Entraînement sur les photos « de studio » du Met ; test sur des photos de visiteurs (cadres,
  reflets, angles). Détail : les images du catalogue « that had a highly skewed aspect ratio
  were excluded ». À l'entraînement, recadrage aléatoire entre 70 et 100 % de l'image.
  → **IGNORE** (le cadre est un « décalage » à surmonter) et **RECADRE**. Les objets trop
  allongés (rouleaux, frises ?) sont simplement retirés.

- **Patryk Bartkowiak, Jakub Markil, Bartosz Kotrys, Dominik Michels, Sören Pirk & Wojtek
  Palubicki, « SynGallery: A Synthetic Gallery of Real Paintings for Instance-Level Artwork
  Recognition »**, prépublication arXiv, juillet 2026. https://arxiv.org/abs/2607.18907
  → Place 4 898 tableaux du Met dans des salles 3D, « inside a frame, sometimes behind glass,
  next to a placard », pour que le modèle apprenne « ignoring the differences between catalog
  and visitor photos ». Ils refusent de détecter puis redresser l'œuvre d'abord, notamment à
  cause des œuvres « non-rectangular or unframed ».
  → **REPRODUIT le cadre pour apprendre à l'IGNORER.** Même matériau que nos couches, but opposé.

- **Sabine Lang & Björn Ommer, « Reconstructing Histories: Analyzing Exhibition Photographs with
  Computational Methods »**, *Arts* 7(4), 2018, art. 64. https://doi.org/10.3390/arts7040064
  (notice Crossref ouverte ; la page de l'éditeur refuse l'accès automatique, contenu lu lors de
  la revue E8, voir `litterature.md`).
  → Retrouve des œuvres accrochées dans les vues d'exposition du MoMA.
  → La machine doit **trouver le bord** de l'œuvre dans le mur. Comment elle le trace n'est pas
  l'objet de l'article.

- **Sabine Lang & Björn Ommer, « Reflecting on How Artworks Are Processed and Analyzed by
  Computer Vision »**, ECCV 2018 Workshops, LNCS 11130, p. 647-652.
  https://doi.org/10.1007/978-3-030-11012-3_49 ; résumé lu :
  https://openaccess.thecvf.com/content_eccv_2018_workshops/w13/html/Lang_Reflecting_on_How_Artworks_Are_Processed_and_Analyzed_by_Computer_ECCVW_2018_paper.html
  → Réflexion d'historienne de l'art sur les « erroneous assumptions » de la vision par
  ordinateur appliquée aux œuvres. Le résumé ne parle pas du recadrage [contenu complet non lu].

- **Zuzana Haladová, « Segmentation and classification of fine art paintings »**, CESCG 2010
  (actes étudiants). https://old.cescg.org/CESCG-2010/papers/HaladovaZuzana.pdf
  → Sur 100 photos de touristes, isole « the painting and its frame » (transformée de Hough).
  → **REPRODUIT** : la méthode classique découpe le tableau **avec** son cadre. Même choix que
  nos détecteurs.

- **Conor Broderick, « Robust Recognition and Identification of Paintings using Computer Vision
  Techniques »**, mémoire de master, Trinity College Dublin, 2016.
  https://publications.scss.tcd.ie/theses/diss/2016/TCD-SCSS-DISSERTATION-2016-005.pdf
  → Application mobile : trouver le tableau dans la photo (détection du cadre par contours),
  l'extraire, puis le reconnaître.
  → Ici le cadre sert de **repère pour couper** ; il est retiré avant la reconnaissance.

- **Alexander Kirillov, Eric Mintun, Nikhila Ravi et al., « Segment Anything » (SAM)**, ICCV
  2023. https://arxiv.org/abs/2304.02643
  → Découpe « n'importe quoi » à partir d'un point, d'une boîte ou d'une grille, sans entraînement
  sur le domaine. 11 millions de photos sous licence.
  → Le segmenteur **choisit un bord** ; rien dans l'article ne dit lequel pour un objet emboîté
  (toile, cadre, mur).

- **Nicolas Carion, Laura Gustafson, Yuan-Ting Hu et al., « SAM 3: Segment Anything with
  Concepts »**, ICLR 2026. https://arxiv.org/abs/2511.16719
  → Découpe toutes les instances d'un concept donné par un nom (« yellow school bus ») ou un
  exemple. Une « tête de présence » décide d'abord si le concept est là.
  → Le mot (« painting », « artwork ») décide du bord. Pas d'évaluation sur des œuvres.
  (Accès restreint pour nous, voir journal du 13/10.)

- **Sebastiaan Kolmschate, « Expanding visual search for online art collections »**, blog Q42
  Engineering, 26 janvier 2026. https://engineering.q42.nl/visual-search/
  → Mémoire de fin d'études pour l'agence Q42, parti d'une demande du Rijksmuseum (« Collection
  Online »). SAM découpe ~17 000-18 000 œuvres en segments ; chaque segment est encodé avec
  DINOv2 ; on clique un détail pour trouver des détails semblables. Prototype seulement ; une
  recherche visuelle officielle était prévue pour 2025-2026 [mise en ligne : incertain].
  → **RECADRE en fragments.** C'est la « recherche par fragments au Rijksmuseum » : elle existe
  comme prototype, pas (encore, à notre connaissance) comme service public.

- **Kévin Réby, Anaïs Guilhelm & Livio De Luca, « Semantic Segmentation Using Foundation Models
  for Cultural Heritage: an Experimental Study on Notre-Dame de Paris »**, ICCV 2023 Workshops,
  p. 1689-1697.
  https://openaccess.thecvf.com/content/ICCV2023W/e-Heritage/html/Reby_Semantic_Segmentation_Using_Foundation_Models_for_Cultural_Heritage_an_Experimental_ICCVW_2023_paper.html
  → SAM + Grounding DINO + CLIP, avec un vocabulaire contrôlé, sur des photos de la cathédrale.
  → Même chaîne d'outils que notre pilote du 13/10, appliquée à l'architecture.

- **Nadav Cohen, Yael Newman & Ariel Shamir, « Semantic Segmentation in Art Paintings »**,
  Eurographics 2022. https://arxiv.org/abs/2203.03238
  → Segmente le **contenu** des tableaux (personnes, chevaux…) par adaptation de domaine.
  → Travaille à l'intérieur du bord ; le bord lui-même est tenu pour acquis.

- **Christoph Redies & Franziska Groß, « Frames as visual links between paintings and the museum
  environment: an analysis of statistical image properties »**, *Frontiers in Psychology* 4,
  2013. https://doi.org/10.3389/fpsyg.2013.00831 (déjà vérifié dans `litterature.md`)
  → Mesure les propriétés statistiques des cadres : ils font la transition entre le tableau et
  la salle.
  → Base pour comprendre pourquoi un détecteur « voit » le cadre comme partie de l'objet.

## 4. Le « décadrage » génératif : inventer le hors-champ

- **Piotr Teterwak, Aaron Sarna, Dilip Krishnan et al., « Boundless: Generative Adversarial
  Networks for Image Extension »**, ICCV 2019, p. 10520-10529.
  https://doi.org/10.1109/ICCV.2019.01062 ; https://arxiv.org/abs/1908.07007
  → Étend une photo au-delà de ses bords avec un sens cohérent.
  → **INVENTE**, première génération.

- **Chitwan Saharia, William Chan, Huiwen Chang et al., « Palette: Image-to-Image Diffusion
  Models »**, SIGGRAPH 2022, p. 1-10. https://doi.org/10.1145/3528233.3530757 ;
  https://arxiv.org/abs/2111.05826
  → Un seul modèle de diffusion pour quatre tâches, dont l'« uncropping » (« décadrage »).
  → **INVENTE** : le décadrage devient une tâche standard, évaluée sur ImageNet.

- **OpenAI, « DALL·E: Introducing Outpainting »**, 31 août 2022. Lu sur l'archive (la page
  actuelle bloque l'accès automatique) :
  https://web.archive.org/web/2022/https://openai.com/blog/dall-e-introducing-outpainting/
  → Outil pour continuer une image « beyond its original borders », « in any aspect ratio ».
  Image vitrine : la *Jeune fille à la perle* de Vermeer, étendue par August Kamp en une pièce
  encombrée.
  → **INVENTE**, et la vitrine choisie est un chef-d'œuvre : le bord de l'œuvre est présenté
  comme une limite à dépasser.

- **Romario, « We Asked DALL-E to Imagine What's Just Beyond the Frame of 10 World-Famous Works
  of Art »**, *USA Art News*, 7 septembre 2022.
  https://usaartnews.com/news/we-asked-dall-e-to-imagine-whats-just-beyond-the-frame-of-10-world-famous-works-of-art-heres-what-the-ai-saw
  [reprise probable d'un article d'Artnet News, https://news.artnet.com/art-world/dall-e-outpainting-2171195 :
  incertain, page Artnet inaccessible]
  → *Guernica*, *Le Cri*, *Les Ménines*, *La Cène*… étendus avec la même formule (artiste, titre,
  « background »).
  → **INVENTE** en série. Journalisme, pas d'analyse de ce qui est inventé.

- **Rijksmuseum, « For the first time in 300 years The Night Watch is complete again »**,
  communiqué, 23 juin 2021.
  https://www.rijksmuseum.nl/en/press/press-releases/for-the-first-time-in-300-years-the-night-watch-is-complete-again
  → En 1715, la *Ronde de nuit* a été rognée sur les quatre côtés (64,4 cm à gauche). Des
  réseaux de neurones, entraînés sur la touche de Rembrandt, ont repeint les bandes perdues
  d'après la copie attribuée à Gerrit Lundens. Bandes imprimées, posées temporairement autour
  du tableau ; il n'est pas prévu de les intégrer à la restauration.
  → **INVENTE le bord perdu**, et le musée le présente comme une simulation. Le cas le plus net
  d'un « cadre » refait par une machine, avec un effet sur la composition (le centre se déplace).

- **Taylor Michael, « Museum Under Fire for Showing AI Version of Vermeer Masterpiece »**,
  *Hyperallergic*, 1er mars 2023 (mis à jour le 3 mars).
  https://hyperallergic.com/805030/mauritshuis-museum-under-fire-for-showing-ai-version-of-vermeer-masterpiece/
  → Pendant le prêt de la *Jeune fille à la perle* au Rijksmuseum, le Mauritshuis montre des
  versions de fans. Une image faite avec Midjourney (Julian van Dieken) est imprimée et
  accrochée dans la salle de l'original. Polémique.
  → **REPRODUIT** : l'image générée prend la place de l'œuvre, sur son mur. Ce n'est pas un
  décadrage ; c'est le dispositif d'exposition qui donne son statut à l'image.

- **Junha Kim, Hyunjoon Park & Donghyeon Cho, « High-Resolution Artwork Outpainting with Global
  Blueprint Guidance and Layout Control »**, ECCV 2026 (selon arXiv).
  https://arxiv.org/abs/2607.06162
  → Note que l'outpainting à haute résolution se fait surtout « in artwork scenarios ». Propose
  un plan global avant d'étendre.
  → **INVENTE**, avec l'œuvre d'art comme cas d'usage principal.

*Non trouvé* : aucune étude savante de ce que l'outpainting invente autour des œuvres connues
(décor, époque, stéréotypes).

## 5. Modèles vision-langage : cadrage de l'entrée, contexte, valeur

### Le cadrage de l'entrée change la réponse

- **Xiaomeng Wang, Martha Larson & Zhengyu Zhao, « Visual Input and Its Framing Affect
  Attribute-based Descriptions Produced by Large Vision-Language Models »**, prépublication
  arXiv, septembre 2026. https://arxiv.org/abs/2609.18345
  → Même question sur une race de chien ; la réponse change si on joint une image, et selon que
  le chien est cadré serré ou en situation. Les termes physiques passent de 18 % (texte seul) à
  45 % (cadré serré) ou 40 % (en situation).
  → Le **cadrage de l'entrée** pilote la réponse, même quand la question ne porte pas sur
  l'image. Cadrage photographique, pas cadre physique.

- **Jiarui Zhang, Mahyar Khayatkhoei, Prateek Chhikara & Filip Ilievski, « MLLMs Know Where to
  Look: Training-free Perception of Small Visual Details with Multimodal LLMs » (ViCrop)**, ICLR
  2025. https://arxiv.org/abs/2502.17422 ; https://iclr.cc/virtual/2025/poster/30449
  → La justesse dépend causalement de la taille du sujet dans l'image. Le modèle « sait où
  regarder » (son attention va au bon endroit) mais voit mal les petits détails. ViCrop recadre
  là où regarde le modèle, et garde aussi l'image entière.
  → **RECADRE** pour mieux voir. Proche de notre « saillance » : ce qui est petit compte moins.

- **Aleksandar Shtedritski, Christian Rupprecht & Andrea Vedaldi, « What does CLIP know about a
  red circle? Visual prompt engineering for VLMs »**, ICCV 2023 (oral).
  https://arxiv.org/abs/2304.06712
  → Un cercle rouge dessiné autour d'un objet dirige l'attention de CLIP vers lui, tout en
  gardant le contexte.
  → Une **marque graphique d'encadrement** est comprise par le modèle. Un cadre doré pourrait
  agir de même (non testé par eux).

- **Hyojin Bahng, Ali Jahanian, Swami Sankaranarayanan & Phillip Isola, « Exploring Visual
  Prompts for Adapting Large-Scale Models »**, prépublication arXiv, 2022.
  https://arxiv.org/abs/2203.17274
  → Une perturbation apprise (en pratique, une bordure de pixels) adapte un CLIP gelé à une
  nouvelle tâche.
  → **Le cadre commande la tâche**, au sens propre. (Voir aussi Zolna et al., « Adversarial
  Framing », AAAI 2019, https://arxiv.org/abs/1812.04599 : modifier seulement la bordure suffit à
  tromper un classifieur.)

### Le contexte et le fond

- **Kai Xiao, Logan Engstrom, Andrew Ilyas & Aleksander Mądry, « Noise or Signal: The Role of
  Image Backgrounds in Object Recognition »**, ICLR 2021. https://arxiv.org/abs/2006.09994
  → Sur ImageNet, le fond seul suffit à une partie des bonnes réponses ; un fond choisi exprès
  fait échouer jusqu'à 87,5 % des images pourtant bien classées sur l'objet seul.
  → Le **fond fait partie du signal**. Notre cadre et notre mur sont des « fonds ».

- **Gabriel Goh, Nick Cammarata, Chelsea Voss, Shan Carter, Michael Petrov, Ludwig Schubert,
  Alec Radford & Chris Olah, « Multimodal Neurons in Artificial Neural Networks »**, *Distill*,
  4 mars 2021. https://distill.pub/2021/multimodal-neurons/ ; billet OpenAI (archive) :
  https://web.archive.org/web/2021/https://openai.com/blog/multimodal-neurons/
  → « Typographic attacks » : CLIP lit le texte dans l'image ; « even photographs of hand-written
  text can often fool the model ». (L'exemple de la pomme étiquetée « iPod » est dans les
  figures [non relu dans le texte].)
  → Cartels, légendes, titres gravés en marge d'une estampe peuvent **commander** la lecture.

- **An Vo, Khai-Nguyen Nguyen, Mohammad Reza Taesiri, Vy Tuong Dang, Anh Totti Nguyen &
  Daeyoung Kim, « Vision Language Models are Biased »**, prépublication arXiv, 2025.
  https://arxiv.org/abs/2505.23941
  → Les modèles répondent par ce qu'ils savent plutôt que par ce qu'ils voient (logo Adidas à
  quatre bandes). Retirer le fond fait gagner 21 points.
  → Le contexte visuel **déclenche le savoir appris**. Même mécanisme que le cadre doré qui
  « fait musée ».

### Esthétique, valeur et prix

- **Mathieu Aubry, Roman Kräussl, Gustavo Manso & Christophe Spaenjers, « Biased Auctioneers »**,
  *Journal of Finance* 78(2), 2023, p. 795-833. https://doi.org/10.1111/jofi.13203 (notice
  Crossref ; contenu lu dans `cadrage-et-valeur.md`)
  → Un réseau de neurones prédit les prix d'adjudication à partir de l'image et des métadonnées ;
  ses écarts révèlent des biais des experts.
  → L'image entre dans le prix, mais l'article ne dit rien du cadrage des photos de catalogue.

- **Jianping Mei, Michael Moses, Jan Waelty & Yucheng Yang, « Deep Learning for Art Market
  Valuation »**, prépublication arXiv, décembre 2025. https://arxiv.org/abs/2512.23078
  → L'artiste et l'historique des ventes dominent ; l'image aide surtout pour les œuvres jamais
  vendues. Grad-CAM montre une attention à la composition et au style.
  → Écho de notre pilote : **l'image compte quand le modèle ne sait pas**.

- **Manpreet Singh, Rhythm Bhatia & Rahul Joshi, « Disentangling Algorithmic Bias from Archival
  Artifacts: A Controlled Audit of Vision-Language Model Valuation in Metropolitan Museum
  Archives »**, prépublication arXiv, 2026. https://arxiv.org/abs/2609.17572
  → Scores CLIP « chef-d'œuvre / qualité / influence » sur 1 500 objets du Met : pas d'effet du
  genre de l'artiste ; le modèle contrôle le **rapport d'aspect** comme facteur possible ; les
  scores n'expliquent presque rien (R² < 2 %).
  → Un des rares travaux qui pense au format de l'image comme variable de confusion.

- **Ran Yi, Haoyuan Tian, Zhihao Gu, Yu-Kun Lai & Paul L. Rosin, « Towards Artistic Image
  Aesthetics Assessment: a Large-scale Dataset and a New Method » (BAID)**, CVPR 2023.
  https://arxiv.org/abs/2303.15166
  → 60 337 images d'art notées par plus de 360 000 votes en ligne ; un modèle apprend à prédire
  la note esthétique.
  → La note est donnée à une image numérique déjà cadrée ; l'effet d'un cadre n'est pas étudié.

- **Ombretta Strafforello, Derya Soydaner, Michiel Willems, Anne-Sofie Maerten & Stefanie De
  Winter, « Have Large Vision-Language Models Mastered Art History? »**, prépublication arXiv,
  2024. https://arxiv.org/abs/2409.03521
  → CLIP, LLaVA, GPT-4o devinent style, auteur et date de tableaux, sans entraînement.
  → Ces bancs d'essai utilisent des reproductions « propres » ; le cadre n'est pas une variable.

*Non trouvé* : aucune étude qui mesure si un cadre, un mur de musée ou une page de catalogue
changent le **prix** qu'un modèle donne à une œuvre. Notre pilote du 09/10 semble être le premier.

## 6. Les jeux de données d'art et leurs cadrages

- **Babak Saleh & Ahmed Elgammal, « Large-scale Classification of Fine-Art Paintings: Learning
  The Right Metric on The Right Feature »**, prépublication arXiv, 2015 [publication en revue :
  incertain]. https://arxiv.org/abs/1505.00855
  → Un des premiers usages massifs de WikiArt pour classer style, genre, artiste.
  → Le texte ne dit rien du recadrage des images (vérifié par recherche dans le PDF).

- **Ahmed Elgammal, Bingchen Liu, Diana Kim, Mohamed Elhoseiny & Marian Mazzone, « The Shape of
  Art History in the Eyes of the Machine »**, AAAI 2018. https://doi.org/10.1609/aaai.v32i1.11894 ;
  https://arxiv.org/abs/1801.07729
  → Classe 77 000 tableaux de WikiArt par style. Les auteurs le disent : le redimensionnement à
  taille fixe « is bound to introduce geometric distortions, which can affect the composition » ;
  « we do not address solving these issues ». Pour un second corpus (visualisation), ils
  excluent les images « containing partial details of paintings ».
  → **RECADRE** en le sachant, et retire les détails : le jeu de données veut l'œuvre entière,
  sans plus ni moins.

- **Byunghwee Lee, Min Kyung Seo, Daniel Kim, In-seob Shin, Maximilian Schich, Hawoong Jeong &
  Seung Kee Han, « Dissecting landscape art history with information theory »**, *PNAS* 117(43),
  2020, p. 26580-26590. https://doi.org/10.1073/pnas.2011927117 ; supplément lu :
  https://cudan.tlu.ee/pub/2020_PNAS_Lee-et-al_Dissecting-landscape_Supp.pdf
  → Sur 15 092 paysages (WikiArt et Web Gallery of Art), **998 images contenaient encore un
  cadre rectangulaire** ; les auteurs l'ont coupé à la main. Ils ont exclu les cadres courbes,
  les éventails, les images penchées et les « ambiguity in frame ».
  → **Le seul chiffre trouvé** sur la présence de cadres dans un grand corpus d'art : environ
  6,6 %. Le cadre y est traité comme une impureté.

- **Chenyang Zhang, Christine Kaeser-Chen, Grace Vesom, Jennie Choi, Maria Kessler & Serge
  Belongie, « The iMet Collection 2019 Challenge Dataset »**, prépublication arXiv, 2019.
  https://arxiv.org/abs/1906.00901
  → Photos professionnelles du Met, annotées par des experts du musée (attributs fins).
  → Le texte court ne dit rien du cadre [contenu du PDF mal extrait : incertain].

- **Xiuyu Li, Peiyuan Liao et al., « The ArtBench Dataset: Benchmarking Generative Models with
  Artworks »**, prépublication arXiv, 2022 [liste complète des auteurs non recopiée].
  https://arxiv.org/abs/2206.11404
  → 60 000 œuvres, 10 styles. Pour les versions 32 × 32 et 256 × 256 : « we apply center-crop on
  the original images ». Signale doublons et déséquilibre dans WikiArt.
  → **RECADRE au centre** : les modèles génératifs d'art apprennent sur des œuvres coupées.

- **Panos Achlioptas, Maks Ovsjanikov, Kilichbek Haydarov, Mohamed Elhoseiny & Leonidas Guibas,
  « ArtEmis: Affective Language for Visual Art »**, CVPR 2021. https://arxiv.org/abs/2101.07396
  → 439 000 émotions et explications sur 81 000 œuvres de WikiArt.
  → Les émotions sont données à l'image telle que WikiArt la cadre ; jamais à l'objet en salle.

- **Le Met Dataset** (section 3) exclut les images trop allongées. **Notre propre relevé** (README,
  point 1) : sur 300 images de musée, 48 seulement montrent l'œuvre sans rien autour ; estampes
  et photographies arrivent avec feuille, montage, inscriptions. Les jeux de données d'art
  publiés partent donc d'une sélection que les musées eux-mêmes ne pratiquent pas toujours.

---

## Ce qui manque

1. **Où un segmenteur met le bord d'une œuvre.** Aucune étude trouvée. SAM, SAM 3, Grounding
   DINO, OWLv2 sont utilisés pour « isoler l'œuvre » (prototype Rijksmuseum, Notre-Dame), mais
   personne n'a mesuré s'ils gardent le cadre, la marge de l'estampe, le passe-partout, le
   montage. Notre pilote du 13/10 (cadre inclus 79/80 ; marge d'estampe coupée) est, à notre
   connaissance, le premier.
2. **Ce qu'un recadrage machine change à l'interprétation d'une œuvre.** Les audits de Twitter
   portent sur des visages et des corps ; Wang et al. sur des chiens ; ViCrop sur des questions
   factuelles. Personne n'a comparé la lecture d'une œuvre entière et de sa version recadrée
   (centre CLIP, vignette carrée, détail SAM), ni chez un humain ni chez un modèle.
3. **Le recadrage central sur les formats d'art.** Les rouleaux, frises, prédelles, estampes en
   hauteur perdent beaucoup au recadrage carré. Mesuré pour la mode (Baldrati et al.), pas pour
   l'art. Le Met Dataset retire simplement les formats extrêmes.
4. **Les vignettes des musées et des plateformes.** Comment les sites de collections et Google
   Arts & Culture choisissent leurs vignettes (centre ? saillance ? humain ?) n'est documenté
   nulle part de façon vérifiable. La norme IIIF suggère le centre par défaut.
5. **Ce que l'outpainting invente autour des chefs-d'œuvre.** Beaucoup de démonstrations
   (OpenAI, presse), une reconstruction savante (*Ronde de nuit*), aucune analyse de ce qui est
   ajouté : quel décor, quelle époque, quels clichés.
6. **Le cadre physique comme indice de valeur pour les modèles.** Les travaux de prix utilisent
   l'image, mais jamais en faisant varier le cadre ou le lieu. Notre pilote du 09/10 (le cadre
   fait monter le prix de ce que le modèle ne reconnaît pas) est sans équivalent publié trouvé.
7. **La part des images encadrées dans les données d'entraînement.** Un seul chiffre trouvé
   (998/15 092 dans le corpus de Lee et al.). On ne sait pas combien d'œuvres encadrées, de
   vues de salle ou de pages de catalogue contiennent LAION ou les données des grands modèles.
8. **Le rôle de l'artiste dans le cadrage.** Toute cette littérature traite le bord comme un
   choix technique (où couper ?) et jamais comme une décision de l'auteur que la machine
   écrase. C'est la question que Yee et al. posent pour les usagers de Twitter (« agency ») ;
   elle reste ouverte pour les œuvres.
