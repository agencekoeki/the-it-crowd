---
title: "The IT Crowd — Base de connaissances : présentation, conventions et table de référence"
scope: "Point d'entrée de la base : contenu et limites, convention unique des étiquettes de fiabilité, table des fiches (00 à 10, dossiers episodes/ et _methode/), table de référence des 25 épisodes (fait autorité pour toute la base) avec lien vers le découpage de chaque épisode, mode d'emploi pour une IA qui ingère la base."
last_updated: 2026-10-11
language: fr
fiche: "README"
series: "The IT Crowd (Channel 4, 2006-2013, créée par Graham Linehan)"
---

# The IT Crowd — Base de connaissances

## 1. Ce que contient la base

Dix fiches thématiques Markdown en français sur la sitcom britannique *The IT Crowd* (Channel 4, 3 février 2006 – 27 septembre 2013, 4 saisons de 6 épisodes et 1 épisode spécial, soit 25 épisodes, créée et écrite par Graham Linehan), plus deux fichiers transversaux (ce `README.md` et `00-CONTRADICTIONS-ET-LACUNES.md`), un dossier `episodes/` de découpages scène par scène et un dossier `_methode/`.

- Les fiches 01 à 09 ont été rédigées le 2026-10-10 par neuf rédacteurs qui ne se sont pas concertés, à partir de sources en ligne.
- Une relecture croisée, le même jour, a confronté les neuf fiches, tranché ce qui pouvait l'être par vérification web et corrigé les fiches. Chaque correction est signalée dans le texte par la marque `RC` ; le texte d'origine a été conservé.
- La fiche 10 (analyse image par image du générique) a été rédigée après la relecture croisée, à partir de captures. Ses constats (plantage du générique sous Fedora Core 4 ; Douglas et le crédit « Matt Berry » présents seulement dans le générique du spécial de 2013) sont reportés dans les fiches 01, 02, 05, 06 et 07.
- Le dossier `episodes/` contient 24 découpages scène par scène, établis en regardant les épisodes complets sur la chaîne YouTube officielle (planches d'images échantillonnées et sous-titres automatiques ; son non écouté), et un constat pour S3E4 « The Speech », absent de la chaîne et non visionné. Les en-têtes des fiches d'épisodes datent ce visionnage du 2026-10-10.
- Une passe de report, datée du 2026-10-11, a corrigé les fiches 01 à 09 et le fichier 00 d'après ces découpages. Chaque ajout est signalé par la marque `VIS` ; le texte d'origine et les notes `RC` ont été conservés.

### Réserve à lire avant tout usage

**Les fiches 01 à 09 ont été écrites sur sources, sans visionnage, puis corrigées d'après le visionnage de 24 épisodes sur 25 (passe du 2026-10-11).** Leur texte d'origine vient de sources écrites : Wikipedia EN et FR, British Comedy Guide, Wikiquote, presse, sites de fans (Fandom, TV Tropes). Seules les notes `VIS` et les fiches du dossier `episodes/` reposent sur ce qui a été regardé. Conséquences :

- `[VÉRIFIÉ]` signifie « lu dans la source citée », jamais « vu à l'écran » ni « vrai dans l'absolu ».
- Les pages ont été lues par un outil qui en restitue le contenu sous forme condensée. Les faits courts (dates, noms, crédits) sont fiables ; le mot à mot, la ponctuation et la casse des citations ne sont pas garantis.
- IMDb, le site de Channel 4, la base INA et la plupart des articles de presse payants n'ont pas pu être lus.
- Une ligne sans note `VIS` n'a pas été contrôlée à l'image : soit le visionnage ne portait pas sur ce point (production, diffusion, réception, biographies), soit le fait n'a pas été retrouvé dans les découpages.
- Limites du visionnage lui-même : le son n'a pas été écouté (accents, prononciations, musique, rires, bips) ; les images ont été échantillonnées, un geste bref peut manquer ; les paroles viennent des sous-titres automatiques de YouTube, sans nom de locuteur, non contrôlés à l'oreille ; plusieurs génériques de fin n'ont été lus qu'en partie ; S3E4 n'a pas été visionné.
- Les cartons-titres, les crédits, les décors et les t-shirts lus à l'image sont désormais consignés (fiches 02, 03, 04, 06) ; le texte exact des répliques reste à contrôler à l'écoute.

## 2. Convention des étiquettes de fiabilité

Convention unique pour toute la base. Les fiches 01 à 09 définissent chacune leurs étiquettes dans leur frontmatter, avec des formulations légèrement différentes ; les définitions ci-dessous les remplacent en cas de doute.

| Étiquette | Définition exacte | Ce qu'elle ne veut pas dire |
|---|---|---|
| `[VÉRIFIÉ]` | Le fait a été lu, le 2026-10-10, dans la source dont la clé suit l'étiquette. La valeur du fait est celle de la source : un `[VÉRIFIÉ]` tiré d'un site de fans reste une affirmation de fans. « Recoupé » ou « ≥2 src » : lu dans au moins deux sources. « Source unique » ou « 1 src » : lu dans une seule | Ni « vu à l'image », ni « contrôlé mot à mot », ni « établi par une source primaire » |
| `[PROBABLE]` | Le fait n'a pas été lu tel quel dans une source consultée. Il résulte d'une déduction à partir de faits vérifiés, d'un recoupement indirect (la source donne le fait sans l'épisode, ou l'inverse) ou d'un souvenir cohérent du rédacteur | Ne pas le citer comme un fait établi |
| `[À VÉRIFIER]` | Sources contradictoires, source unique fragile, information non trouvée, ou élément donné de mémoire sans appui. Inclut les contradictions que la relecture croisée n'a pas pu trancher | Ne pas le réutiliser sans contrôle ; ne jamais le transformer en affirmation |
| `[ANALYSE]` | Interprétation, classement ou jugement du rédacteur de la fiche, qui n'est ni sourcé ni présenté comme un fait | Pas une information sur la série |
| `[VU À L'IMAGE]` | Constaté sur une image de l'épisode ou du générique, avec repère (fiche d'épisode et minutage de la vidéo YouTube officielle). Employée dans la fiche 10, dans le dossier `episodes/` et, depuis le 2026-10-11, dans les notes `VIS` des fiches 01 à 09. C'est la seule étiquette qui atteste ce qui est à l'écran | Ne dit rien du son ; un fait « non vu » sur des images échantillonnées n'est pas un fait absent de l'épisode |
| `[SOUS-TITRES AUTO]` | Lu dans les sous-titres automatiques de YouTube pendant le visionnage, avec repère (fiche d'épisode et minutage). Ces sous-titres sont produits par reconnaissance vocale : sans nom de locuteur, sans ponctuation, avec des erreurs, noms propres déformés. Le locuteur est déduit de l'image | Ni contrôlé à l'oreille, ni probant pour le mot à mot, l'orthographe d'un nom ou la graphie d'un mot inventé |
| `[INTERPRÉTATION]` | Dans le dossier `episodes/` seulement : lecture du rédacteur du découpage (mécanique d'un gag, intention, rapprochement) | Pas un constat |

### Variantes locales à connaître

| Fiche | Clé du frontmatter | Particularité |
|---|---|---|
| 01 | `reliability_labels` | Ajoute « recoupé », « Wikipedia seul », « source unique » après `[VÉRIFIÉ]` |
| 02 | `proof_labels` | Les faits lus seulement sur Fandom sont `[VÉRIFIÉ]` s'ils décrivent l'écran, `[À VÉRIFIER]` s'ils relèvent de la déduction de fans |
| 03 | `evidence_labels` | Une étiquette en fin de puce couvre toute la puce ; dans un synopsis, tout le paragraphe |
| 04 | `evidence_tags` | Forme `[VÉRIFIÉ — CLÉ]` : la clé de source est dans l'étiquette |
| 05 | `evidence_labels` | `[PROBABLE]` = recoupement indirect ; les traductions françaises sont libres, ce n'est pas le texte de la VF |
| 06 | `evidence_labels`, `source_tiers` | Niveau de source A (primaire ou institutionnelle), B (encyclopédie, guide), C (fans, forum, blog) ; `[PROBABLE]` couvre aussi une source unique de faible fiabilité |
| 07 | `evidence_labels` | Clés écrites sans accent dans le frontmatter (`VERIFIE`, `A_VERIFIER`) ; mentions « (1 src) » et « (≥2 src) » |
| 08 | `evidence_labels` | Seule fiche à employer `[ANALYSE]` de façon systématique |
| 09 | `conventions_etiquettes` | Clés sans accent dans le frontmatter ; les chiffres « vivants » (notes, vues, abonnés) sont datés du 2026-10-10 |
| 01 à 09 | `viewing_review` | Champ ajouté le 2026-10-11 : résume la passe de visionnage ; les étiquettes `[VU À L'IMAGE]` et `[SOUS-TITRES AUTO]` sont ajoutées aux définitions du frontmatter |

### Marque `RC`

`RC` introduit une correction ou une harmonisation issue de la relecture croisée. Quand une ligne contient un texte d'origine puis une note `RC`, **la note `RC` prévaut**. Le détail de chaque décision est dans `00-CONTRADICTIONS-ET-LACUNES.md`.

### Marque `VIS`

`VIS` introduit une note de la passe de visionnage du 2026-10-11, placée en fin de ligne, de cellule ou de paragraphe. Elle a la forme « VIS : CORRIGÉ, NUANCÉ, CONFIRMÉ ou TRANCHÉ — fait observé, étiquette `[VU À L'IMAGE]` ou `[SOUS-TITRES AUTO]`, renvoi (episodes/SxEy, minutage) ». Le minutage est celui de la vidéo de la chaîne YouTube officielle, dont l'identifiant figure dans `episodes/README.md`.

- **Une note `VIS` prévaut sur le texte qui la précède et sur une note `RC`.** L'ancienne version est laissée en place, avec sa source, pour garder la trace de ce que disaient les sources écrites.
- Quand une étiquette a été relevée, la note le dit par la formule « auparavant `[PROBABLE]` » ou « auparavant `[À VÉRIFIER]` ».
- « NON VU », « non confirmé », « non vérifiable » dans une note `VIS` signifient que le visionnage n'a pas pu établir le fait (image échantillonnée, son non écouté, générique lu en partie) : l'étiquette d'origine reste alors valable.

## 3. Table des fiches

Tailles mesurées le 2026-10-11 après la passe de visionnage. Le niveau de confiance global est une appréciation `[ANALYSE]`, fondée sur la nature des sources de chaque fiche et, depuis le 2026-10-11, sur la part de son contenu contrôlée à l'image.

| Fichier | Périmètre | Taille | Niveau de confiance global |
|---|---|---|---|
| `README.md` | Présentation, conventions, table des 25 épisodes, mode d'emploi | — | Table des épisodes : élevé (trois sources concordantes ; titres lus à l'écran pour 20 épisodes) |
| `00-CONTRADICTIONS-ET-LACUNES.md` | 75 contradictions entre fiches (52 tranchées, dont 10 par le visionnage ; 5 tranchées en partie ; 18 non tranchées), recoupement des titres français, 25 lacunes priorisées | 67 Ko  293 lignes | Journal de méthode |
| `01-production-diffusion.md` | Genèse, sociétés, équipe, studios, diffusion Channel 4, audiences, saison 5 annulée, DVD, streaming, remakes, diffusion et doublage français | 65 Ko  566 lignes | Élevé pour dates et crédits (British Comedy Guide, presse datée ; crédits de réalisation et de générique relus à l'image) ; moyen pour les DVD et la France (Wikipedia, sources dérivées). Peu concernée par le visionnage |
| `02-personnages-casting.md` | Six personnages principaux, personnages secondaires, invités épisode par épisode, biographies et prix des acteurs, changements de distribution | 108 Ko  1 134 lignes | Élevé pour les crédits (British Comedy Guide, confirmés au générique pour la saison 1 en entier et en partie pour les autres) ; moyen pour les biographies (Wikipedia) ; t-shirts de Roy : élevé pour ceux lus à l'image, faible pour ceux que seuls les fans annoncent |
| `03-episodes-saisons-1-2.md` | Épisodes 1 à 12 : synopsis, lieux, invités, gags, répliques, références, réception | 112 Ko  873 lignes | Élevé pour titres et dates ; élevé pour les synopsis là où une note `VIS` les confirme ou les corrige, moyen ailleurs (Wikipedia et Fandom) |
| `04-episodes-saisons-3-4-special.md` | Épisodes 13 à 25 : même structure, plus la conclusion de la série | 126 Ko  1 072 lignes | Comme la fiche 03 ; S3E4 n'a pas été visionné et reste entièrement sur sources |
| `05-repliques-gimmicks-running-gags.md` | 102 répliques (VO d'une ligne, traduction libre), 28 gags récurrents, faux produits et fausses émissions, chansons, mots inventés ; section 1.4 : attributions corrigées par le visionnage | 116 Ko  596 lignes | Moyen : épisode et locuteur confirmés ou corrigés par les sous-titres automatiques pour une grande partie des lignes ; mot à mot non contrôlé à l'oreille ; aucune VF officielle |
| `06-decors-lieux-accessoires.md` | Reynholm Industries, sous-sol, set dressing, matériel rétro, intérieurs, extérieurs réels, studios, costumes, générique, menus DVD ; section 3.8 : textes lus à l'image épisode par épisode ; section 7.2 : t-shirts lus à l'image | 96 Ko  712 lignes | Élevé pour ce qui est lu à l'image (sections 3.8 et 7.2) et pour le matériel prêté (Centre for Computing History) ; faible à moyen pour ce qui ne vient que de sites de fans |
| `07-references-geek-tech-pop-culture.md` | Références informatiques, logiciel libre, jeux, science-fiction, comics, musique, émissions britanniques parodiées, easter eggs, tableau par épisode, controverse « The Speech » | 103 Ko  651 lignes | Moyen : beaucoup de sources uniques ; élevé pour les références confirmées à l'image par une note `VIS` ; l'intention d'une référence n'est jamais vérifiable par l'image |
| `08-accents-langue-humour.md` | Voix et accents, glossaire pour francophones, méthode d'écriture de Linehan, jeu d'acteur, place dans l'humour britannique, VF et titres français | 79 Ko  635 lignes | Élevé pour les déclarations (entretiens cités) ; les descriptions d'accents restent des `[ANALYSE]`, le son n'ayant pas été écouté |
| `09-reception-memes-heritage.md` | Critiques, audiences, prix, classements, mèmes, YouTube, communautés, carrières, projets de suite, controverses jusqu'en 2026 | 71 Ko  558 lignes | Moyen à élevé : presse via la revue de British Comedy Guide ; chiffres en ligne datés et instables ; scènes d'origine des mèmes confirmées à l'image, sauf celles de S3E4 |
| `10-generique.md` | Analyse image par image du générique | 15 Ko  150 lignes | Élevé sur la saison 1 et le spécial 2013 (vus à l'image) ; partiel sur les saisons 2 à 4 ; URL des vidéos non consignées |
| `episodes/README.md` | Index des découpages : fichier, identifiant de la vidéo YouTube, durée, nombre de scènes | 4 Ko  43 lignes | Index |
| `episodes/SxEy-<titre>.md` (24 fichiers) et `episodes/S3E4-the-speech-NON-TRAITE.md` | Un découpage scène par scène par épisode regardé : lieu, personnages, action, gags, décor, costumes, générique de fin lu à l'image, confrontation avec les fiches 03 et 04 ; pour S3E4, simple constat d'absence | 790 Ko au total, de 25 à 50 Ko par épisode | Le plus élevé de la base pour ce qui est à l'écran (`[VU À L'IMAGE]`) ; moyen pour les paroles (`[SOUS-TITRES AUTO]`) ; nul pour le son |
| `episodes/_CORRECTIONS-ISSUES-DU-VISIONNAGE.md` | Épisode par épisode, ce que le visionnage confirme, corrige ou nuance dans les fiches 01 à 09, avec minutage | 86 Ko  622 lignes | Journal de la confrontation ; reporté dans les fiches 01 à 09 le 2026-10-11 |
| `_methode/visionnage.md` | Procédure et outils du visionnage (planches d'images, sous-titres automatiques, sourdine), limites | 6 Ko  65 lignes | Journal de méthode |

## 4. Table de référence des 25 épisodes

**Cette table fait autorité pour toute la base** en matière de numéro global, de code, de titre original et de date de première diffusion sur Channel 4. En cas d'écart avec une fiche, c'est la fiche qui est fautive.

Statut : `[VÉRIFIÉ]` recoupé. Numéros, titres originaux et dates ont été relus le 2026-10-10 dans trois sources concordantes : Wikipedia EN (liste des épisodes), British Comedy Guide (guide des épisodes), TVmaze (interface de données). Le titre a en outre été lu à l'écran pour 20 épisodes (colonne « Titre à l'écran » ; détail dans les précisions). La colonne « Découpage » renvoie à la fiche scène par scène de l'épisode.

| N° global | Code | Titre original | Première diffusion Channel 4 | Date ISO | Titre à l'écran | Découpage |
|---|---|---|---|---|---|---|
| 1 | S1E1 | Yesterday's Jam | vendredi 3 février 2006 | 2006-02-03 | oui (0:30) | [découpage](episodes/S1E1-yesterdays-jam.md) |
| 2 | S1E2 | Calamity Jen | vendredi 3 février 2006 | 2006-02-03 | oui (0:32) | [découpage](episodes/S1E2-calamity-jen.md) |
| 3 | S1E3 | Fifty-Fifty | vendredi 10 février 2006 | 2006-02-10 | oui (0:32) | [découpage](episodes/S1E3-fifty-fifty.md) |
| 4 | S1E4 | The Red Door | vendredi 17 février 2006 | 2006-02-17 | oui (0:32) | [découpage](episodes/S1E4-the-red-door.md) |
| 5 | S1E5 | The Haunting of Bill Crouse | vendredi 24 février 2006 | 2006-02-24 | oui (0:32) | [découpage](episodes/S1E5-the-haunting-of-bill-crouse.md) |
| 6 | S1E6 | Aunt Irma Visits | vendredi 3 mars 2006 | 2006-03-03 | oui (0:32) | [découpage](episodes/S1E6-aunt-irma-visits.md) |
| 7 | S2E1 | The Work Outing | vendredi 24 août 2007 | 2007-08-24 | oui (fiche 10) | [découpage](episodes/S2E1-the-work-outing.md) |
| 8 | S2E2 | Return of the Golden Child | vendredi 31 août 2007 | 2007-08-31 | non relevé | [découpage](episodes/S2E2-return-of-the-golden-child.md) |
| 9 | S2E3 | Moss and the German | vendredi 7 septembre 2007 | 2007-09-07 | non relevé | [découpage](episodes/S2E3-moss-and-the-german.md) |
| 10 | S2E4 | The Dinner Party | vendredi 14 septembre 2007 | 2007-09-14 | non relevé | [découpage](episodes/S2E4-the-dinner-party.md) |
| 11 | S2E5 | Smoke and Mirrors | vendredi 21 septembre 2007 | 2007-09-21 | oui (0:34) | [découpage](episodes/S2E5-smoke-and-mirrors.md) |
| 12 | S2E6 | Men Without Women | vendredi 28 septembre 2007 | 2007-09-28 | oui (2:20, lu sur vignette) | [découpage](episodes/S2E6-men-without-women.md) |
| 13 | S3E1 | From Hell | vendredi 21 novembre 2008 | 2008-11-21 | oui | [découpage](episodes/S3E1-from-hell.md) |
| 14 | S3E2 | Are We Not Men? | vendredi 28 novembre 2008 | 2008-11-28 | oui | [découpage](episodes/S3E2-are-we-not-men.md) |
| 15 | S3E3 | Tramps Like Us | vendredi 5 décembre 2008 | 2008-12-05 | oui (1:09) | [découpage](episodes/S3E3-tramps-like-us.md) |
| 16 | S3E4 | The Speech | vendredi 12 décembre 2008 | 2008-12-12 | épisode non visionné | [non traité](episodes/S3E4-the-speech-NON-TRAITE.md) |
| 17 | S3E5 | Friendface | vendredi 19 décembre 2008 | 2008-12-19 | oui | [découpage](episodes/S3E5-friendface.md) |
| 18 | S3E6 | Calendar Geeks | vendredi 26 décembre 2008 | 2008-12-26 | oui | [découpage](episodes/S3E6-calendar-geeks.md) |
| 19 | S4E1 | Jen the Fredo | vendredi 25 juin 2010 | 2010-06-25 | oui (fiche 10) | [découpage](episodes/S4E1-jen-the-fredo.md) |
| 20 | S4E2 | The Final Countdown | vendredi 2 juillet 2010 | 2010-07-02 | oui | [découpage](episodes/S4E2-the-final-countdown.md) |
| 21 | S4E3 | Something Happened | vendredi 9 juillet 2010 | 2010-07-09 | oui | [découpage](episodes/S4E3-something-happened.md) |
| 22 | S4E4 | Italian for Beginners | vendredi 16 juillet 2010 | 2010-07-16 | oui | [découpage](episodes/S4E4-italian-for-beginners.md) |
| 23 | S4E5 | Bad Boys | vendredi 23 juillet 2010 | 2010-07-23 | non relevé | [découpage](episodes/S4E5-bad-boys.md) |
| 24 | S4E6 | Reynholm vs Reynholm | vendredi 30 juillet 2010 | 2010-07-30 | oui (0:34) | [découpage](episodes/S4E6-reynholm-vs-reynholm.md) |
| 25 | Spécial (noté `SP` dans certaines fiches) | The Internet Is Coming | vendredi 27 septembre 2013 | 2013-09-27 | oui (0:34) | [découpage](episodes/SP-the-internet-is-coming.md) |

### Précisions attachées à la table

| Point | Contenu | Statut |
|---|---|---|
| Double programme | Les épisodes 1 et 2 ont été diffusés le même soir | `[VÉRIFIÉ]` recoupé |
| Graphie de S1E3 | « Fifty-Fifty » (Wikipedia EN, TVmaze) ; « 50/50 » (British Comedy Guide) ; « 50:50 » (TheTVDB) ; « Fifty Fifty » (Wikiquote). VIS : TRANCHÉ — le carton-titre porte « Fifty-Fifty », avec trait d'union (episodes/S1E3, 0:32) ; la chaîne YouTube titre la vidéo « Fifty Fifty » | `[VU À L'IMAGE]` (auparavant carton-titre `[À VÉRIFIER]`) |
| Graphie de S3E4 | « The Speech » (Wikipedia EN, TVmaze) ; « Speech » (British Comedy Guide). VIS : épisode non visionné, carton-titre non vu | Graphie de Wikipedia EN retenue par convention ; carton-titre `[À VÉRIFIER]` |
| Graphie de S4E6 | « Reynholm vs Reynholm » (Wikipedia EN, British Comedy Guide, TVmaze) ; « Reynholm v Reynholm » (Wikiquote, Fandom) ; titre alternatif « Douglas and Divorce » (Wikipedia EN). VIS : TRANCHÉ — le titre incrusté à l'écran est « Reynholm vs Reynholm » (episodes/S4E6, 0:34) ; la chaîne YouTube titre la vidéo « Reynholm v Reynholm » | `[VU À L'IMAGE]` (auparavant carton-titre `[À VÉRIFIER]`) |
| Titres lus à l'écran | VIS : le titre est lu à l'image pour 20 épisodes : S1E1 à S1E6 (cartons-titres, episodes/S1E1 à S1E6, 0:30–0:32), S2E1 et S4E1 (fiche 10), S2E5 « Smoke and Mirrors » (episodes/S2E5, 0:34), S2E6 (2:20, lecture sur vignette à confirmer en plein cadre), S3E1, S3E2, S3E3 (1:09), S3E5, S3E6, S4E2, S4E3, S4E4, S4E6 et le spécial, incrusté « The Internet is Coming » (episodes/SP, 0:34). Non relevé pour S2E2, S2E3, S2E4 et S4E5 ; S3E4 non visionné. Aucun titre lu ne contredit la table, aux capitales près (« Jen The Fredo » et « The Internet is Coming » à l'écran) | `[VU À L'IMAGE]` |
| Titres donnés par la chaîne YouTube | VIS : les titres des vidéos de la chaîne officielle s'écartent du titre à l'écran pour quatre épisodes : « Fifty Fifty » (S1E3), « Aunt Irma Visiting » (S1E6), « Smoke & Mirrors » (S2E5), « Reynholm v Reynholm » (S4E6). Ce sont des titres de mise en ligne, pas des titres d'épisode | `[VU À L'IMAGE]` sur la page de la vidéo (fiches `episodes/`) |
| Autre titre de S2E6 | Annoncé « The Joy Of Sex » dans la grille de Channel 4 selon British Comedy Guide | `[VÉRIFIÉ]` source unique |
| Titres erronés du spécial | « The Last Byte » (erroné selon Wikipedia EN) ; « The Final Episode » (Netflix, Time Out) | `[VÉRIFIÉ]` |
| Numérotation du spécial | Ni saison 5 ni S4E7 : certains agrégateurs (JustWatch, AlloCiné) le rangent pourtant ainsi. VIS : la chaîne YouTube officielle titre elle aussi la vidéo du spécial « Series 5 Episode 1 » (episodes/SP) | `[VÉRIFIÉ]` |
| Heure de diffusion | 21 h pour S1E1 et pour le spécial ; 21 h 30 pour S1E2 à S2E6 ; 22 h pour les saisons 3 et 4, sauf S3E4 (22 h 05) et S3E6 (21 h 50) | `[VÉRIFIÉ]` source unique (British Comedy Guide, fiches 03 et 04). TVmaze affiche 22 h partout : valeur par défaut, à ignorer |
| Durée | Créneau de 30 minutes, environ 24 minutes nettes ; spécial : créneau de 60 minutes, 47 à 48 minutes nettes. VIS : les vidéos de la chaîne officielle durent de 21:14 (S2E4) à 25:17 (S1E6) pour les 23 épisodes de saison regardés, et 48:07 pour le spécial (episodes/README.md) | `[VÉRIFIÉ]` ; durées des vidéos constatées |
| Scénario | Graham Linehan pour les 25 épisodes | `[VÉRIFIÉ]` recoupé |
| Réalisation | Graham Linehan ; British Comedy Guide crédite en plus Ben Fuller (saison 1), Barbara Wiltshire (saison 2), Richard Boden (saisons 3 et 4, spécial). VIS : CORRIGÉ — dans tous les génériques de fin lus, la ligne « Director » ne porte que Graham Linehan. Ben Fuller est crédité « Studio Director » en saison 1 (episodes/S1E1, 21:53–21:59 ; S1E2, 23:01–23:06). Richard Boden est « Series Producer » en saison 3 (episodes/S3E1, 22:58), « Studio Director » (episodes/S3E6, 45:57 ; S4E2, 23:40–23:44 ; S4E6, 24:00) et « Producer » du spécial (episodes/SP, 47:48). Saison 2 : génériques lus en partie, ni ligne « Director » ni Barbara Wiltshire relevées | `[VU À L'IMAGE]` pour les saisons 1, 3, 4 et le spécial ; saison 2 `[À VÉRIFIER]` |
| Autres crédits lus au générique | VIS : « Script Editor Andrew Ellard » (episodes/S4E1 et suivants), « I.T. Consultant Sean D. Sollé », « Title Music Neil Hannon », « Title Design Shynola », « Costume Designer Annie Hardinge » ; dans S4E2, « Countdown Director Derek Hallworth » (episodes/S4E2, générique de fin) | `[VU À L'IMAGE]` |
| Studios | Teddington Studios (saison 1) ; Pinewood Studios (saisons 2 à 4) ; BBC Elstree Centre (spécial, enregistré le 8 juin 2013, British Comedy Guide seul) | `[VÉRIFIÉ]` |

### Titres français

Aucun titre français n'est confirmé par un diffuseur ou un éditeur : tous sont `[À VÉRIFIER]` quant à leur caractère officiel. Colonne « Titre le mieux attesté » : titre donné par au moins deux des trois sources lues (Wikipédia FR, AlloCiné, JustWatch France). Détail en section 3 de `00-CONTRADICTIONS-ET-LACUNES.md`.

| Code | Titre le mieux attesté | Variante | Sources du titre le mieux attesté |
|---|---|---|---|
| S1E1 | Les givrés du sous-sol | Les chaussettes d'hier (Wikipédia FR seule) | AlloCiné, JustWatch, notice INA citée par Wikipédia FR |
| S1E2 | Aïe mes pieds ! | Calamity Jen ! (Wikipédia FR seule) | AlloCiné, JustWatch |
| S1E3 | Le millionnaire | 50-50 (Wikipédia FR seule) | AlloCiné, JustWatch |
| S1E4 | La Porte rouge | — | Les trois |
| S1E5 | Jen est morte | — | Les trois |
| S1E6 | Tante Irma est arrivée | — | Les trois |
| S2E1 | La Soirée gay | — | Les trois |
| S2E2 | Le patron saute | — | Les trois |
| S2E3 | Cuisine à l'allemande | — | Les trois |
| S2E4 | Le Dîner de Jen | — | Les trois |
| S2E5 | Écran de fumée | — | Les trois |
| S2E6 | La Potion magique | — | Les trois |
| S3E1 | Le maçon | — | Les trois |
| S3E2 | Les vrais mecs | Ne sommes-nous pas des hommes ? (Wikipédia FR seule) | AlloCiné, JustWatch |
| S3E3 | Ceinture de chasteté | — | Les trois |
| S3E4 | Le Discours | — | Les trois |
| S3E5 | Friendface | — | Les trois |
| S3E6 | À poil les scientifiques ! | Le Calendrier des geeks (Wikipédia FR seule) | AlloCiné (sans accent ni point d'exclamation), JustWatch |
| S4E1 | Jen et les féministes | — | Les trois |
| S4E2 | Finale sanglante | — | Les trois |
| S4E3 | La Spaciologie | — | Les trois |
| S4E4 | Traduction très spéciale | AlloCiné garde le titre original | Wikipédia FR, JustWatch |
| S4E5 | Les taulards | AlloCiné garde le titre original | Wikipédia FR, JustWatch |
| S4E6 | Douglas devant les tribunaux | AlloCiné et une notice INA gardent le titre original | Wikipédia FR, JustWatch |
| Spécial | L'ultime épisode | The Last Byte (AlloCiné, titre erroné) | Wikipédia FR, JustWatch |

Les fiches 03, 04, 05 et 08 ont été rédigées avec les seuls titres de Wikipédia FR ; leurs tableaux portent une note `RC` qui renvoie ici.

## 5. Mode d'emploi pour une IA qui ingère la base

### Ordre de lecture et de priorité

1. Lire ce `README.md` : conventions et table des épisodes.
2. Lire `00-CONTRADICTIONS-ET-LACUNES.md` : il dit quelles affirmations des fiches ont été corrigées ou restent ouvertes, et ce que le visionnage a tranché.
3. **Pour une question sur un épisode précis, lire d'abord sa fiche dans `episodes/`** (lien dans la colonne « Découpage » de la section 4) : c'est la seule description faite d'après l'image. Lire ensuite la fiche 03 ou 04 pour le contexte, les sources écrites et la réception. Pour S3E4, il n'existe pas de découpage : la fiche 04 est la seule ressource et tout y vient de sources écrites.
4. Pour une question transversale, lire la ou les fiches thématiques utiles (tableau ci-dessous).

En cas de désaccord, dans cet ordre :

1. la table des épisodes du README l'emporte sur tout pour les numéros, titres originaux et dates ;
2. une fiche du dossier `episodes/` l'emporte sur les fiches 01 à 09 pour ce qui se voit à l'écran ;
3. dans une fiche, une note `VIS` l'emporte sur une note `RC`, qui l'emporte sur le texte d'origine ;
4. le fichier 00 l'emporte sur les fiches pour ce que le visionnage n'a pas tranché ;
5. entre deux fiches non arbitrées, préférer celle dont la source est de meilleur niveau (image, puis générique ou presse datée, puis British Comedy Guide, puis Wikipedia, puis Wikiquote, puis sites de fans).

Un fait `[SOUS-TITRES AUTO]` vaut moins qu'un fait `[VU À L'IMAGE]` : il établit qu'une chose est dite, à peu près à tel moment, pas par qui ni dans quels mots exacts.

### Quelle fiche pour quelle question

| Question | Fiche à lire d'abord | Compléments |
|---|---|---|
| Numéro, titre ou date d'un épisode | `README.md`, section 4 | 03, 04 |
| Titre français d'un épisode | `README.md`, section 4 | 00, section 3 ; 08, section 7.3 |
| Que se passe-t-il dans tel épisode ? À quelle minute ? | `episodes/SxEy-….md` (découpage minuté) | 03 (épisodes 1 à 12) ou 04 (épisodes 13 à 25) ; 02 pour les invités |
| Que voit-on dans telle scène : décor, costume, texte à l'écran ? | `episodes/SxEy-….md` | 06, sections 3.8 et 7.2 |
| Qu'est-ce que le visionnage a corrigé dans la base ? | `episodes/_CORRECTIONS-ISSUES-DU-VISIONNAGE.md` | 00, colonne « Apport du visionnage » ; 05, section 1.4 |
| Qui joue tel rôle ? Dans quel épisode apparaît tel acteur ? | 02 | 03, 04 |
| Biographie, prix et carrière d'un acteur | 02, section 5 | 09, section 9 |
| Dans quel épisode et par qui est dite telle réplique ? | 05 (lire la note `VIS` de la ligne et la section 1.4) | fiche `episodes/` de l'épisode ; 03, 04 ; contrôler dans 00 les lignes X19 à X40 |
| Gag récurrent, faux produit, fausse publicité, mot inventé | 05 | 07 |
| Qui a produit, réalisé, monté ? Où la série a-t-elle été tournée ? | 01 | 06 pour les lieux |
| Audiences, DVD, streaming, remakes, diffusion et doublage en France | 01 | 09 pour les audiences ; 08 pour la VF |
| Décor du sous-sol, objets, ordinateurs anciens, t-shirts de Roy | 06 (sections 3.8 et 7.2 pour ce qui est lu à l'image) | 07, 02 ; section « Inventaire du décor » et « Costumes » de chaque fiche `episodes/` |
| Que parodie tel gag ? Quelle référence geek ou britannique ? | 07 | 05, 03, 04 |
| Accents, argot, traduction, procédés comiques, méthode de Linehan | 08 | 05 |
| Critiques, prix, classements, mèmes, postérité | 09 | 05 pour les répliques |
| Retrait de « The Speech », polémiques autour de Graham Linehan | 09, section 10 | 07, section 9.2 ; 01, section 10 |
| Générique d'ouverture | 10 | 06, section 9 ; 07, section 7.2 ; 01, section 5 |
| Générique de fin, crédits d'un épisode | fiche `episodes/` de l'épisode (crédits lus à l'image) | 02 ; 01, section 3 |
| Ce fait est-il sûr ? | 00 | Étiquette de la ligne dans la fiche ; présence ou non d'une note `VIS` |

### Règles de restitution

- Reprendre l'étiquette avec le fait. Ne jamais présenter un `[PROBABLE]` ou un `[À VÉRIFIER]` comme établi.
- Pour tout fait `[VÉRIFIÉ]`, dire « selon telle source », pas « on voit dans l'épisode ».
- Réserver « on voit dans l'épisode » aux faits `[VU À L'IMAGE]`, en donnant l'épisode et le minutage. Pour un fait `[SOUS-TITRES AUTO]`, dire « d'après les sous-titres automatiques ».
- Ne rien affirmer sur un accent, une intonation, une musique ou un rire au nom du visionnage : le son n'a pas été écouté.
- Ne rien affirmer « vu à l'image » sur S3E4 : l'épisode n'a pas été visionné.
- Citer une réplique en VO, une ligne au plus, en précisant que le mot à mot n'a pas été contrôlé à l'écoute.
- Les traductions françaises de la fiche 05 sont libres : ne pas les présenter comme le texte du doublage.
- Pour un titre français, donner le titre le mieux attesté et sa variante, et préciser qu'aucun n'est confirmé par un diffuseur.
- Les chiffres en ligne de la fiche 09 (notes, vues, abonnés) sont datés du 2026-10-10 : les redonner avec leur date.
- Si la base ne contient pas l'information, le dire et renvoyer à la lacune correspondante du fichier 00 (L01 à L25), qui indique comment la combler.

### Codes et conventions communs

| Élément | Convention |
|---|---|
| Épisode | `SxEy` ; « Spécial » ou `SP` pour l'épisode de 2013 ; `#n` ou « n° global » de 1 à 25 |
| Saison | Les fiches écrivent « saison » ou « série » (usage britannique) : même sens |
| Dates | En toutes lettres ou au format ISO (fiche 04) |
| Titres d'œuvres et noms propres | En anglais ; graphies de noms de personnages selon British Comedy Guide (Philip, Johann, Pippin, Jorg, Stephen Premel) ; les graphies des sous-titres automatiques ne sont jamais retenues |
| Minutage | `mm:ss` de la vidéo de la chaîne YouTube officielle, publicité exclue ; pour S3E6, minutage dans la compilation des épisodes 5 et 6 (l'épisode y commence à 22:34) |
| Contradictions | `Xnn` dans le fichier 00 ; `Cn` à l'intérieur d'une fiche |
| Lacunes | `Lnn` dans le fichier 00 ; `Ln` à l'intérieur d'une fiche |
| Sources | Clés propres à chaque fiche (`[S1]`, `[BCG-S1E2]`, `[W-LIST]`…), définies dans sa section « Sources » ; une même clé peut désigner des sources différentes d'une fiche à l'autre |

## 6. Sources de la table de référence

Relues le 2026-10-10.

- [List of The IT Crowd episodes — Wikipedia EN](https://en.wikipedia.org/wiki/List_of_The_IT_Crowd_episodes)
- [Guide des épisodes — British Comedy Guide](https://www.comedy.co.uk/tv/the_it_crowd/episodes/all/)
- [The IT Crowd, épisodes et spéciaux — TVmaze](https://api.tvmaze.com/shows/539/episodes?specials=1)
- [The Internet Is Coming — British Comedy Guide](https://www.comedy.co.uk/tv/the_it_crowd/episodes/2013/1/)
- [The IT Crowd — Wikipédia FR](https://fr.wikipedia.org/wiki/The_IT_Crowd)
- [The IT Crowd, saison 1 — AlloCiné](https://www.allocine.fr/series/ficheserie-3202/saison-5570/)
- [The IT Crowd, saison 3 — AlloCiné](https://www.allocine.fr/series/ficheserie-3202/saison-8260/)
- [The IT Crowd, saison 4 — AlloCiné](https://www.allocine.fr/series/ficheserie-3202/saison-17469/)
- [The IT Crowd, saisons 1 à 5 — JustWatch France](https://www.justwatch.com/fr/serie/the-it-crowd)

## 7. Découpages scène par scène (dossier `episodes/`)

- 24 épisodes sur 25 ont été regardés sur la chaîne YouTube officielle et découpés scène par scène : index dans [`episodes/README.md`](episodes/README.md), liens directs dans la colonne « Découpage » de la section 4.
- S3E4 « The Speech » n'est pas disponible en entier sur la chaîne officielle : non traité ([constat](episodes/S3E4-the-speech-NON-TRAITE.md)).
- Méthode et limites : [`_methode/visionnage.md`](_methode/visionnage.md). Visionnage par échantillonnage d'images et sous-titres automatiques ; le son n'a pas été écouté.
- Les fiches 01 à 09 et le fichier 00 ont été corrigés d'après ce visionnage le 2026-10-11 (notes `VIS`). La liste complète des confirmations, corrections et nuances, épisode par épisode, reste dans [`episodes/_CORRECTIONS-ISSUES-DU-VISIONNAGE.md`](episodes/_CORRECTIONS-ISSUES-DU-VISIONNAGE.md), qui dit aussi ce qui n'a pas été reporté.
- En cas de désaccord résiduel entre une fiche 01 à 09 et une fiche d'épisode, la fiche d'épisode fait foi pour ce qui se voit à l'écran.
