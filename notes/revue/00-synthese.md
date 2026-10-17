# Synthèse de la revue : le problème, son utilité, ses critères

*17/10/2026. Synthèse des six volets de la revue de littérature, chacun avec sa bibliographie
vérifiée (environ 480 références au total) :*
[01 théorie du cadre](01-theorie-du-cadre.md) ·
[02 fenêtre, écran, interface](02-fenetre-ecran-interface.md) ·
[03 reproduction et matérialité](03-reproduction-materialite.md) ·
[04 vision machine et contexte](04-vision-machine-contexte.md) ·
[05 institution, valeur, contexte](05-institution-valeur-contexte.md) ·
[06 critique de la vision machine ; problème](06-critique-vision-machine-probleme.md).
*Les volets ont épuisé le quota de recherche web en fin de travail : les références marquées
« de mémoire » ou « [non vérifié] » restent à contrôler en bibliothèque avant toute citation.*

---

## 1. Où en est le projet, honnêtement

La critique de Marcel (17/10) est juste, et les six volets la confirment chacun à sa façon.

- **Nos pilotes ont mesuré des différences, pas des fonctions.** Nous avons fait varier un
  support (avec ou sans cadre, avec ou sans bord) et regardé si la réponse changeait. Or une
  réponse qui change peut venir d'une lecture du cadre ou d'un artefact optique (surface,
  couleur, place). Et une réponse qui ne change pas est compatible avec au moins cinq situations
  (volet 02, §7.5 ; volet 04, §10.8) : le bord n'est pas perçu ; il est perçu puis écarté ; il
  est perçu mais la question ne le sollicite pas ; des effets se compensent ; la mesure est trop
  grossière. Seule la deuxième mérite le mot « traversé ».
- **« Cadre-fenêtre » et « cadre-étiquette » ne sont pas deux sortes d'objets.** Bazin le dit
  déjà : le même tableau est centripète dans son cadre et centrifuge à l'écran. Krauss montre
  que la coupe photographique, cache par excellence, devient un signe quand la composition et le
  discours s'en emparent. Le statut d'un bord n'est pas dans l'objet. Il dépend du lecteur, de
  la tâche et du dispositif (volet 02, §7.3). Le bord de film de la FSA est une fenêtre pour qui
  demande « que se passe-t-il ? » et une étiquette pour qui demande « qu'est-ce que cet
  objet ? ». Cette deuxième question, nous ne l'avons jamais posée.
- **Il n'y avait pas de problème.** Constater que « les machines traitent le cadre autrement que
  la théorie » est vrai, mais trop facile à admettre, et sans enjeu (volet 06, §9). La critique
  de la vision machine (Paglen, Crawford, Parikka) a déjà dit en général que la machine ne
  regarde pas comme nous.

Ce que nos pilotes valent, relus avec ces critères, est détaillé au §6.

---

## 2. Le problème

### 2.1 Ce que la tradition laisse ouvert

La théorie du cadre prête au cadre au moins **dix fonctions** (volet 01, §3) : isoler, unifier
et centrer, désigner et valoriser, fixer le statut, métacommuniquer (« ceci est une image »),
ouvrir (fenêtre, hors-champ), signifier socialement, réfléchir la représentation, porter et
protéger, emboîter. Certaines s'opposent : isoler contre ouvrir (Simmel contre Alberti et
Bazin), désigner l'œuvre contre montrer la représentation (Marin, Stoichita).

L'angle mort principal est le même chez tous les auteurs. **La tradition décrit ce que fait le
cadre ; elle ne dit presque jamais comment vérifier qu'un cadre donné le fait** (volet 01,
§0 et §4). Les arguments reposent sur des exemples choisis, des textes d'artistes ou une
analyse conceptuelle. Louis Marin est l'exception partielle. Et l'expérience décisive est
impossible avec de vrais tableaux : on ne peut pas montrer la même œuvre, avec et sans son
cadre, aux mêmes spectateurs, toutes choses égales par ailleurs. La seule mesure (Redies et
Groß 2013) le fait par photographie, et seulement pour des statistiques d'image.

Deuxième angle mort : **la reproduction**. Presque tous ces textes parlent du tableau devant un
spectateur. Or les œuvres circulent en photographie, et la photographie de musée recadre au ras
de la toile. Elle applique Kant sans le dire : le cadre n'est pas l'œuvre (volet 01, §4). Les
historiens de la photographie d'art (Caraffa, Edwards, Kamin, Smits ; volet 03) ont montré que
le support de la reproduction (carton, tampon, mire, légende au dos) porte l'histoire de
l'objet. Mais ils ne l'ont jamais confronté aux machines. Et le droit dit l'inverse : une
reproduction fidèle n'ajouterait rien (Bridgeman c. Corel 1999 ; directive européenne de 2019,
art. 14).

### 2.2 Ce que les machines changent

Une machine qui « lit » une reproduction reçoit un rectangle de pixels. Le cadre, la marge, la
mire, la page et l'écran y sont des pixels comme les autres. Rien ne lui dit où finit l'œuvre.
Pourtant, elle tranche : elle décrit un sujet, donne un prix, trace un bord, range l'image dans
une classe. La question de Kant et de Derrida (le cadre est-il dedans ou dehors ?) devient une
**opération** : qu'est-ce que la machine traite comme l'œuvre ? Et la réponse est unique,
condensée en une sortie (Amoore, *Cloud Ethics* : l'algorithme « condense de multiples
possibles en une sortie unique » ; volet 06, §4.1).

Or l'informatique connaît très bien un phénomène de même structure : l'**apprentissage par
raccourci** (volet 04, §4 ; volet 06, §5.2). Un modèle se fonde sur un indice secondaire présent
dans les images, au lieu de l'objet. Trois cas lus dans le texte :
- une mention de source dans un coin fait reconnaître les chevaux (Lapuschkin et al. 2019) :
  effacée, la décision s'effondre ; collée sur une voiture, la voiture devient un cheval ;
- un modèle de radiographies reconnaît l'hôpital d'origine à 99,95 % grâce à des marques
  métalliques, et s'en sert (Zech et al. 2018) ;
- l'encre chirurgicale autour d'une lésion ajoute environ 40 % de faux positifs au dépistage du
  mélanome (Winkler et al. 2019).

Une mire de musée, une marque d'institution, un cadre doré ou un carton de photothèque ont
exactement cette structure : des signes du support, corrélés dans les données à un statut, une
époque, une valeur.

Enfin, des machines **décident déjà** sur l'art à partir de reproductions (volet 06, §6) :
- **catalogage** (AI Explorer de Harvard, GallicaPix) ;
- **identification d'œuvres volées** (ID-Art d'Interpol) ;
- **estimation de prix** (Aubry et al., *Journal of Finance* 2023) ;
- **attribution** (Art Recognition) ;
- **modération** (nus de musée bloqués : Courbet, Rubens et Visit Flanders) ;
- **génération** (LAION, filigranes Getty reproduits par Stable Diffusion, retenus comme
  contrefaçon de marque, de façon « extremely limited », à Londres le 4/11/2025).

Pour l'art, **aucun cas publié** ne montre un cadre qui aurait faussé une décision réelle
(volet 06, §7). C'est le manque dans la littérature, et le risque du projet.

### 2.3 La problématique proposée

> **Quand une machine lit la reproduction d'une œuvre, les supports qui l'entourent (cadre,
> marge, mire, marque, cartel, bord du fichier) agissent-ils comme des signes conventionnels,
> lus selon ce que la théorie du cadre leur prête, ou comme des corrélats statistiques, des
> raccourcis ? Et qui, dans la chaîne qui va du musée au modèle, trace la limite de l'œuvre ?**

Elle a trois volets, qui reprennent les problématiques candidates du volet 06 :

1. **Le support comme raccourci dans des décisions sur l'art** (P1, le cœur). Quelle part d'une
   décision de machine (prix, attribution, identification, catalogage) vient du support plutôt
   que de l'œuvre ? Le pilote du 09/10 laisse penser que la part est forte quand l'œuvre n'est
   pas reconnue. C'est le cas de la grande masse des œuvres peu connues qui passent en vente,
   là où, selon Aubry et al., la machine apporte le plus.
2. **Lecture ou confusion** (le critère neuf, volet 04, §10.9). Un effet de support est une
   *lecture* s'il est prédit par la sémiotique du support et non par ses propriétés optiques :
   il suit la convention culturelle, augmente avec la richesse du cadre, disparaît avec un faux
   cadre de même surface et de même couleur. Sinon, c'est une *confusion*. Aucune étude de
   robustesse ne fait cette distinction : elles demandent si la sortie change, jamais si elle
   change dans le sens d'une convention. C'est ici que la théorie du cadre devient
   indispensable à l'informatique, et pas seulement l'inverse.
3. **La délégation du bord** (P2). Quand une institution confie à une machine le recadrage, la
   segmentation ou la vignette de ses œuvres, où la machine met-elle le bord ? Et ce bord
   diffère-t-il de celui que l'institution reconnaîtrait ? Le pilote SAM 3 montre que le bord
   dépend du mot de la consigne (« painting » contre « artwork »). Le pilote YCBA montre que les
   détecteurs coupent la marge des estampes, avec le titre et la légende gravés.

La portée théorique tient en une phrase (P4, volet 06) : la machine ne répond pas à la question
du *parergon* ; elle la tranche en silence, autrement selon l'outil, la tâche et le mot.

---

## 3. L'utilité

| pour qui | ce qu'ils ont besoin de savoir | volet |
|---|---|---|
| maisons de vente, collectionneurs, assureurs | une estimation automatique suit-elle le cadre ou la photo plutôt que l'œuvre ? | 06 (Aubry et al.) |
| experts, musées | une attribution compare-t-elle deux œuvres ou deux photographies ? | 06 (Art Recognition) |
| police | une œuvre volée réencadrée ou rephotographiée échappe-t-elle à la recherche ? | 06 (ID-Art) |
| photothèques, bibliothèques (PHAROS, PhotoTech du Getty, Gallica) | la machine lit-elle le support comme document (tampon, carton, mire) ou l'efface-t-elle comme bruit ? | 03, 06 |
| musées qui publient en ligne | le cadre de musée protège-t-il un nu de la censure automatique ? | 06 (P5) |
| juristes | les signes du support (filigrane, mire, marque) deviennent-ils des usages de marque dans la génération ? | 03, 06 |
| historiens de l'art, théoriciens | pour la première fois, tester les fonctions du cadre toutes choses égales par ailleurs | 01 |

L'utilité pour les humanités est la plus originale. La machine est le premier « spectateur »
devant lequel on peut faire varier un cadre sans rien changer d'autre. Elle ne remplace pas le
spectateur humain : chaque test ne dit que si une fonction prêtée au cadre a un effet mesurable
sur une machine donnée (volet 01, §5). Mais c'est la première fois que ces fonctions peuvent
être testées une à une. Et la même expérience, passée par des humains (l'outil `human_study/`
est prêt), comble un manque de l'esthétique expérimentale. Celle-ci n'a mesuré le cadre matériel
qu'une fois (Koniak et Szubielska 2022, 98 étudiants, peintures abstraites ; un cadre décoratif
y fait *baisser* le jugement) et n'a jamais testé la provenance écrite au cartel (volet 05,
§9.3).

---

## 4. Le cadre conceptuel

### 4.1 Quatre niveaux de « cadre »

Pour éviter l'inflation du concept, que Wolf et Bal ont signalée (volet 01, §2 et §4), le
projet distingue quatre niveaux :
1. **le cadre matériel**, dans l'image : moulure, passe-partout, marge, carton, bord de film ;
2. **le cadre institutionnel visible**, dans l'image : mire, marque, cartel photographié,
   étiquette au revers, mur de salle ;
3. **le cadre du fichier**, opératoire : bord de l'image, format d'entrée (carré de 224 px,
   recadrage central), découpage par un segmenteur, vignette ;
4. **le cadre discursif**, hors de l'image : le nom, la légende, la consigne, le rôle demandé au
   modèle.

Les niveaux 1, 2 et 3 sont des pixels. Le niveau 4 est du texte. La machine ne les distingue
pas d'elle-même : c'est ce qu'on étudie.

### 4.2 Deux régimes de lecture plutôt que deux sortes de cadres

On remplace « cadre-fenêtre / cadre-étiquette » par deux **régimes** d'un lecteur pour une
tâche (volet 02, §8.4) :
- **lecture à travers le support** : la réponse porte sur ce que montre l'image et ne dépend
  pas du support ;
- **lecture du support** : la réponse porte sur l'objet (statut, provenance, date du tirage,
  valeur) et dépend du support.

Un même bord peut relever des deux selon la question. Bazin, Bolter et Grusin (immédiateté et
hypermédiation), Lanham (*looking through / looking at*) et Wollheim (double conscience de la
surface et de l'image) disent tous que les deux régimes alternent ou coexistent.

### 4.3 Quatre statuts testables d'une machine face à un support

Proposition du volet 04 (§10.9), ici reprise comme définitions de travail :
- **aveugle** : la machine ne peut pas dire qu'il y a un support quand on le lui demande, et
  une sonde ne le retrouve pas dans sa représentation interne ;
- **traverse** : elle *voit* le support ; ses réponses sur le contenu sont *équivalentes* avec
  et sans support (test d'équivalence, marge fixée d'avance) ; cela tient pour plusieurs
  questions et dans des cas ambigus ; *et* elle se sert du support quand la question porte sur
  l'objet (double dissociation, volet 02, §7.5) ;
- **lit** : ses réponses changent de façon systématique, dans le sens de la convention
  culturelle, de façon graduée, et l'effet disparaît avec un faux cadre ;
- **est confondue** : les réponses changent, mais l'effet s'explique par une propriété non
  sémantique (surface, couleur, recadrage, compression) et persiste avec un faux cadre.

« Transparent » a au moins quatre sens (volet 02, §7.2) : attention (le spectateur ne remarque
pas), accès à la chose (Walton), outil qui se fait oublier, sortie invariante. Une machine ne
peut établir que le dernier. On n'écrira donc plus « transparent » sans préciser.

### 4.4 « À l'insu » : ce qui se transpose de la psychologie

Marcel : « ce qui compte, c'est ce qui l'influence sans qu'il le sache ». La psychologie sait
établir qu'un contexte agit à l'insu de quelqu'un, avec douze critères (volet 05, §7.2) :
- même image au pixel près ;
- étiquette tirée au sort ;
- une seule condition par sujet ;
- but masqué et questions leurres ;
- contrôle de l'attention à l'indice ;
- croyance dans l'indice manipulée ;
- interrogatoire en entonnoir ;
- mesures indirectes ;
- dissociation entre ce qui est dit et ce qui est fait ;
- modérateurs ;
- préenregistrement ;
- réplication.

Presque tous ont un équivalent machine. Le plus parlant : on sait déjà que les modèles suivent
un indice sans le dire dans leur justification (Turpin et al. 2023 ; Chen et al. 2025).
**Coder si la justification mentionne le cadre** permet donc de distinguer un effet déclaré (« le
cadre ancien suggère… », un raisonnement) d'un effet non dit (un biais à l'insu). Le pilote du
09/10 relève plutôt du premier cas : Claude date le cadre à part et parle de « cadre
d'antiquaire ».

---

## 5. Les critères observables, rassemblés

Une fonction du cadre se constate en changeant le cadre sans toucher à l'image (volet 01). Pour
chaque fonction ou régime, voici ce qu'il faut observer. Ce sont les critères minimaux avant de
pouvoir écrire une phrase de résultat.

| ce qu'on veut affirmer | preuves nécessaires | sources |
|---|---|---|
| la machine **voit** le support | elle le décrit quand on le lui demande ; une sonde le retrouve dans sa représentation interne | 02 (C4, C6), 04 (§10.3) |
| elle le **traverse** | voit + réponses équivalentes sur le contenu (marge fixée d'avance), image par image, en cas ambigus + support utilisé pour les questions sur l'objet | 02 (§7.5), 04 (§10.8), Lakens 2017 |
| elle le **lit** comme signe | effet systématique, dans le sens de la convention, gradué selon la richesse du cadre, absent avec un faux cadre (même surface, même couleur) | 04 (§10.9) |
| le cadre **désigne** (F3) | à image égale, l'objet encadré devient le sujet de la description | 01 |
| le cadre **ouvre** (F6, fenêtre) | inférence du hors-champ imposée par l'image (corps coupés, regards) ; complétion au-delà du bord ; changement de régime quand on rend le cadre | 01, 02 (Burch, Bazin) |
| le cadre **fixe le statut** (F4) | réponses à « est-ce de l'art ? » posées séparément de « combien ? », et divergences entre les deux | 01, 05 (§9.4-9) |
| le cadre **signifie socialement** (F7) | effet qui change selon le rôle demandé (conservateur, antiquaire, critique contemporain), comme le prédit la structure du champ (Bourdieu) | 05 (§9.4-4) |
| l'effet est **à l'insu** | justification muette sur le cadre ; effet qui persiste quand on dit que le cadre a été « choisi au hasard » | 05 (§7) |
| c'est un **raccourci** institutionnel | marque effacée : l'effet tombe ; marque transplantée sur une photo d'amateur : l'effet apparaît ; marque remplacée par celle d'une autre institution : l'effet suit le prestige | 04 (protocole 2), Lapuschkin 2019 |
| le bord vient de la **machine** | extension de chaque mot (« painting », « artwork », « canvas », « framed painting ») chez plusieurs outils, comparée à une annotation humaine | 04 (protocole 5) |

---

## 6. Ce que valent nos pilotes, relus avec ces critères

| pilote | ce qu'il montre | ce qu'il ne montre pas | statut |
|---|---|---|---|
| cadre et valeur, montages, Claude et Gemini (09/10) | le prix d'un objet banal monte avec un cadre ancien ; pas celui d'une œuvre reconnue | sans faux cadre, impossible de distinguer lecture et confusion ; 1 lecture par image, 4 images par case ; justifications non codées | indice, compatible avec la littérature (le savoir sature la réponse quand l'œuvre est reconnue : Goyal, Agrawal, Mei) |
| YCBA, Gemini (17/10) | sur de vraies photos de musée, le cadre ne change pas le prix mais le lieu ; la marque du musée est lue ; le nom est lu au revers | mire et cadre ne sont jamais séparés (ils varient ensemble entre les vues) ; aucun effacement ni aucune transplantation | candidat raccourci, de type Lapuschkin, à tester par le protocole 2 |
| FSA, bord du film (17/10) | réponses sur la scène invariantes, en moyenne, avec ou sans bord | jamais vérifié que le bord est vu ; aucune question sur l'objet ; aucun test d'équivalence | **aucune conclusion possible** sur traverser ou être aveugle ; la phrase « cadre-fenêtre » est retirée |
| SAM 3, extension des mots (17/10) | « painting » met le bord sur la toile une fois sur deux, « artwork » sur le cadre | un seul outil récent, trois mots, aucune annotation humaine | germe sérieux du volet « délégation du bord » (protocole 5) |
| saillance, article E1-E6 | l'œuvre petite et décentrée cesse d'être le sujet de la description | — | reste valable, mais c'est un résultat sur la saillance, pas sur le cadre |

---

## 7. Programme de recherche

Ordre proposé. Chaque étape est préenregistrée : hypothèses, marges et analyses écrites et
commitées avant de lancer.

1. **Fondations (2 à 3 semaines).** Corriger les notes et l'article (§8). Lire les dix textes
   prioritaires (§9). Fixer les marges d'équivalence. Préparer un corpus de **vraies paires** :
   la même œuvre photographiée avec et sans cadre (YCBA quatre vues, 620 tableaux du domaine
   public ; Met), et des photos de vente.
2. **Protocole « voir avant de traverser » (FSA, YCBA).** Trois temps : (i) la machine voit-elle
   le support ? (ii) ses réponses sur la scène sont-elles équivalentes ? (iii) l'utilise-t-elle
   pour les questions sur l'objet (« négatif ou tirage ? », « date de la photo et date de
   l'œuvre ? ») ? Ajouter des cas ambigus. C'est la réponse directe à la question de Marcel.
3. **Conflit cadre / contenu, avec faux cadre.** Grille contenu (reconnu ou banal) × cadre
   (riche, pauvre, faux cadre de même surface et de même couleur, aucun). Surface du contenu
   constante. Cinquante paires par case au moins, cinq formulations, plusieurs tirages, trois
   familles de modèles (Gemini, Claude, un modèle ouvert de type Qwen-VL). Justifications
   codées (dit ou non dit). Variante de Koniak : « le cadre a été choisi au hasard ». Variante
   de Bourdieu : rôles demandés.
4. **Marque d'institution : effacer, remplacer, transplanter** (à la Lapuschkin), sur les photos
   du YCBA, avec des institutions fictives pour ne pas usurper de vraies marques.
5. **Extension des concepts de segmentation** (SAM 3, Grounding DINO, OWLv2 ; une douzaine de
   mots en trois langues) contre trois annotateurs humains. Conséquences mesurées : légendes
   d'estampes perdues, recherche par fragments qui échoue.
6. **Ouvrir un modèle** (si les étapes 3 et 4 donnent un effet). Retrait des jetons visuels du
   cadre, remplacement d'activations, traits d'autoencodeur sur un modèle ouvert. On saurait
   alors *où* le cadre agit.
7. **Humains en parallèle.** Les mêmes paires passées par des personnes (`human_study/`), pour
   la première comparaison humain-machine sur des images encadrées (volet 04, §12 ; volet 05,
   §9.3).
8. **Le test de vérité de l'utilité** (volet 06). Un estimateur de prix ou un outil
   d'identification réel, ou reconstruit sérieusement à la manière d'Aubry et al., avec de
   vraies paires avec et sans cadre. Si l'écart est grand, le projet a un problème et un
   public. S'il est nul, il faut le savoir vite et se replier sur la délégation du bord ou sur
   l'art appris comme marchandise (P3 : compter les cadres et les murs dans un échantillon de
   LAION re-LAION).

**Ce qui ferait échouer le projet**, à dire d'avance :
- l'effet est petit sur des tâches réelles ;
- une correction triviale suffit (« recadrer avant ») ;
- on ne teste que des modèles généralistes et pas les outils réellement utilisés ;
- les montages ne ressemblent pas aux vraies photos (volet 06, §9).

Les étapes 2, 5 et 8 sont conçues pour le savoir tôt.

---

## 8. Corrections à faire

- **Article et notes.** Retirer « la machine distingue le cadre-fenêtre du cadre-étiquette » et
  le « cache de Bazin » appliqué au bord de film (`notes/fsa-gemini.md`, `article/article.md`
  §4.7 et discussion). Écrire à la place ce qui est mesuré : pour ces questions sur la scène, la
  réponse ne dépend pas du bord ; on ne sait pas si le bord est vu.
- **Faux amis** à écarter dès l'introduction : l'« enframing » de Heidegger (*Gestell*) et les
  *frames* de Minsky ne parlent pas du cadre de l'image (volet 01, §1.17).
- **Références erronées dans nos notes antérieures** (volet 03) :
  - Patrizia (et non Patricia) Di Bello ;
  - Impett et Offert, « There is a digital art history », arXiv août 2023 ;
  - Caraffa, *From Photo Libraries to Photo Archives*, 2011, distinct de *Photo-Objects*,
    2019 ;
  - Helm et Kampel portent sur des films numérisés ;
  - « The Great Unseen » est l'introduction d'un numéro de *TMG Journal for Media History*.
- **Le « +54 % » de Li, Ma et Renneboog (2024)** porte sur la provenance dans des ventes
  humaines, pas sur des modèles (volet 05).
- **« Ingrid Hoel »** désigne en fait deux auteurs : Aud Sissel Hoel et Ingrid Hoelzl
  (volet 06).

---

## 9. Lectures prioritaires (dix)

1. Louis Marin, « Le cadre de la représentation et quelques-unes de ses figures » (1988) — le
   seul auteur qui donne des indices observables (volet 01).
2. Georg Simmel, « Der Bildrahmen » (1902).
3. Meyer Schapiro, « On some problems in the semiotics of visual art: field and vehicle in
   image-signs », *Semiotica* (1969).
4. Jacques Derrida, « Parergon », *La Vérité en peinture* (1978).
5. André Bazin, « Peinture et cinéma » ; Rosalind Krauss, « The photographic conditions of
   surrealism » (1981) — le statut du bord dépend du dispositif (volet 02).
6. Costanza Caraffa (dir.), *Photo-Objects* (2019) ; Diana Kamin, *Picture-Work* (2023) — le
   support de la reproduction comme document (volet 03).
7. Lapuschkin et al., « Unmasking Clever Hans predictors » (*Nature Communications*, 2019) ;
   Geirhos et al., « Shortcut learning » (*Nature Machine Intelligence*, 2020) (volet 04).
8. Koniak et Szubielska (2022), seule expérience sur le cadre matériel chez l'humain ; Turpin et
   al. (2023), l'indice suivi sans être dit (volet 05).
9. Louise Amoore, *Cloud Ethics* (2020) ; Offert et Bell, « Perceptual bias and technical
   metapictures » (2021) (volet 06).
10. Paul Duro, « Frame » (*Art History Now*, 2025) ; thèse de Louise Delbarre (Paris 1, 2025),
    qui oppose « cadre isolant » et « cadre confluent » (volet 01) — à lire pour situer le projet
    dans le débat le plus récent.
