---
title: "The IT Crowd — Base de connaissances : présentation, conventions et table de référence"
scope: "Point d'entrée de la base : contenu et limites, convention unique des étiquettes de fiabilité, table des 10 fiches, table de référence des 25 épisodes (fait autorité pour toute la base), mode d'emploi pour une IA qui ingère la base."
last_updated: 2026-10-10
language: fr
fiche: "README"
series: "The IT Crowd (Channel 4, 2006-2013, créée par Graham Linehan)"
---

# The IT Crowd — Base de connaissances

## 1. Ce que contient la base

Dix fiches Markdown en français sur la sitcom britannique *The IT Crowd* (Channel 4, 3 février 2006 – 27 septembre 2013, 4 saisons de 6 épisodes et 1 épisode spécial, soit 25 épisodes, créée et écrite par Graham Linehan), plus deux fichiers transversaux.

- Les fiches 01 à 09 ont été rédigées le 2026-10-10 par neuf rédacteurs qui ne se sont pas concertés, à partir de sources en ligne.
- Une relecture croisée, le même jour, a confronté les neuf fiches, tranché ce qui pouvait l'être par vérification web et corrigé les fiches. Chaque correction est signalée dans le texte par la marque `RC` ; le texte d'origine a été conservé.
- La fiche 10 (analyse image par image du générique) a été rédigée après la relecture croisée, à partir de captures : elle n'a pas été recoupée avec les autres fiches, sauf sur un point qu'elle tranche (le plantage du générique est un noyau Fedora Core 4, voir fiche 10 §3 et fiche 06).

### Réserve à lire avant tout usage

**Aucun épisode n'a été visionné pour les fiches 01 à 09.** Tout ce qu'elles contiennent vient de sources écrites : Wikipedia EN et FR, British Comedy Guide, Wikiquote, presse, sites de fans (Fandom, TV Tropes). Conséquences :

- `[VÉRIFIÉ]` signifie « lu dans la source citée », jamais « vu à l'écran » ni « vrai dans l'absolu ».
- Les pages ont été lues par un outil qui en restitue le contenu sous forme condensée. Les faits courts (dates, noms, crédits) sont fiables ; le mot à mot, la ponctuation et la casse des citations ne sont pas garantis.
- IMDb, le site de Channel 4, la base INA et la plupart des articles de presse payants n'ont pas pu être lus.
- Les cartons-titres, les génériques, les décors, les t-shirts et le texte exact des répliques restent à contrôler au visionnage.

## 2. Convention des étiquettes de fiabilité

Convention unique pour toute la base. Les fiches 01 à 09 définissent chacune leurs étiquettes dans leur frontmatter, avec des formulations légèrement différentes ; les définitions ci-dessous les remplacent en cas de doute.

| Étiquette | Définition exacte | Ce qu'elle ne veut pas dire |
|---|---|---|
| `[VÉRIFIÉ]` | Le fait a été lu, le 2026-10-10, dans la source dont la clé suit l'étiquette. La valeur du fait est celle de la source : un `[VÉRIFIÉ]` tiré d'un site de fans reste une affirmation de fans. « Recoupé » ou « ≥2 src » : lu dans au moins deux sources. « Source unique » ou « 1 src » : lu dans une seule | Ni « vu à l'image », ni « contrôlé mot à mot », ni « établi par une source primaire » |
| `[PROBABLE]` | Le fait n'a pas été lu tel quel dans une source consultée. Il résulte d'une déduction à partir de faits vérifiés, d'un recoupement indirect (la source donne le fait sans l'épisode, ou l'inverse) ou d'un souvenir cohérent du rédacteur | Ne pas le citer comme un fait établi |
| `[À VÉRIFIER]` | Sources contradictoires, source unique fragile, information non trouvée, ou élément donné de mémoire sans appui. Inclut les contradictions que la relecture croisée n'a pas pu trancher | Ne pas le réutiliser sans contrôle ; ne jamais le transformer en affirmation |
| `[ANALYSE]` | Interprétation, classement ou jugement du rédacteur de la fiche, qui n'est ni sourcé ni présenté comme un fait | Pas une information sur la série |
| `[VU À L'IMAGE]` | Constaté par visionnage de l'épisode ou du générique, avec repère (épisode et, si possible, minutage). **Aucune occurrence dans les fiches 01 à 09.** Étiquette réservée à la fiche 10 et aux contrôles futurs ; c'est la seule qui atteste ce qui est à l'écran | — |

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

### Marque `RC`

`RC` introduit une correction ou une harmonisation issue de la relecture croisée. Quand une ligne contient un texte d'origine puis une note `RC`, **la note `RC` prévaut**. Le détail de chaque décision est dans `00-CONTRADICTIONS-ET-LACUNES.md`.

## 3. Table des fiches

Tailles mesurées le 2026-10-10 après la relecture croisée. Le niveau de confiance global est une appréciation `[ANALYSE]` de la relecture, fondée sur la nature des sources de chaque fiche.

| Fichier | Périmètre | Taille | Niveau de confiance global |
|---|---|---|---|
| `README.md` | Présentation, conventions, table des 25 épisodes, mode d'emploi | — | Table des épisodes : élevé (trois sources concordantes) |
| `00-CONTRADICTIONS-ET-LACUNES.md` | 75 contradictions entre fiches (42 tranchées, 33 non tranchées), recoupement des titres français, 20 lacunes priorisées | 50 Ko, 275 lignes | Journal de méthode |
| `01-production-diffusion.md` | Genèse, sociétés, équipe, studios, diffusion Channel 4, audiences, saison 5 annulée, DVD, streaming, remakes, diffusion et doublage français | 56 Ko, 562 lignes | Élevé pour dates et crédits (British Comedy Guide, presse datée) ; moyen pour les DVD et la France (Wikipedia, sources dérivées) |
| `02-personnages-casting.md` | Six personnages principaux, personnages secondaires, invités épisode par épisode, biographies et prix des acteurs, changements de distribution | 86 Ko, 1 126 lignes | Élevé pour les crédits (British Comedy Guide) ; moyen pour les biographies (Wikipedia) ; faible pour les détails de fans (t-shirts, âges, dates fictives) |
| `03-episodes-saisons-1-2.md` | Épisodes 1 à 12 : synopsis, lieux, invités, gags, répliques, références, réception | 72 Ko, 864 lignes | Élevé pour titres et dates ; moyen pour les synopsis (Wikipedia et Fandom) ; S1E1 sous-documenté |
| `04-episodes-saisons-3-4-special.md` | Épisodes 13 à 25 : même structure, plus la conclusion de la série | 86 Ko, 1 057 lignes | Élevé pour titres et dates ; moyen à élevé pour les synopsis (critiques d'époque Den of Geek et A.V. Club) |
| `05-repliques-gimmicks-running-gags.md` | 102 répliques (VO d'une ligne, traduction libre), 28 gags récurrents, faux produits et fausses émissions, chansons, mots inventés | 86 Ko, 554 lignes | Moyen : attribution par épisode d'après Wikiquote ; mot à mot non contrôlé ; aucune VF officielle |
| `06-decors-lieux-accessoires.md` | Reynholm Industries, sous-sol, set dressing, matériel rétro, intérieurs, extérieurs réels, studios, costumes, générique, menus DVD | 52 Ko, 597 lignes | Élevé pour le matériel prêté (Centre for Computing History) et les studios ; faible à moyen pour le reste (sites de fans, niveau C) |
| `07-references-geek-tech-pop-culture.md` | Références informatiques, logiciel libre, jeux, science-fiction, comics, musique, émissions britanniques parodiées, easter eggs, tableau par épisode, controverse « The Speech » | 80 Ko, 647 lignes | Moyen : beaucoup de sources uniques, dont une copie de Wikipedia datée de 2007 |
| `08-accents-langue-humour.md` | Voix et accents, glossaire pour francophones, méthode d'écriture de Linehan, jeu d'acteur, place dans l'humour britannique, VF et titres français | 65 Ko, 629 lignes | Élevé pour les déclarations (entretiens cités) ; les descriptions d'accents sont des `[ANALYSE]` |
| `09-reception-memes-heritage.md` | Critiques, audiences, prix, classements, mèmes, YouTube, communautés, carrières, projets de suite, controverses jusqu'en 2026 | 64 Ko, 554 lignes | Moyen à élevé : presse via la revue de British Comedy Guide ; chiffres en ligne datés et instables |
| `10-generique.md` | Analyse image par image du générique | 12 Ko | Élevé sur la saison 1 et le spécial 2013 (vus à l'image) ; partiel sur les saisons 2 à 4 ; URL des vidéos non consignées |

## 4. Table de référence des 25 épisodes

**Cette table fait autorité pour toute la base** en matière de numéro global, de code, de titre original et de date de première diffusion sur Channel 4. En cas d'écart avec une fiche, c'est la fiche qui est fautive.

Statut : `[VÉRIFIÉ]` recoupé. Numéros, titres originaux et dates ont été relus le 2026-10-10 dans trois sources concordantes : Wikipedia EN (liste des épisodes), British Comedy Guide (guide des épisodes), TVmaze (interface de données). Aucun carton-titre n'a été vu à l'image.

| N° global | Code | Titre original | Première diffusion Channel 4 | Date ISO |
|---|---|---|---|---|
| 1 | S1E1 | Yesterday's Jam | vendredi 3 février 2006 | 2006-02-03 |
| 2 | S1E2 | Calamity Jen | vendredi 3 février 2006 | 2006-02-03 |
| 3 | S1E3 | Fifty-Fifty | vendredi 10 février 2006 | 2006-02-10 |
| 4 | S1E4 | The Red Door | vendredi 17 février 2006 | 2006-02-17 |
| 5 | S1E5 | The Haunting of Bill Crouse | vendredi 24 février 2006 | 2006-02-24 |
| 6 | S1E6 | Aunt Irma Visits | vendredi 3 mars 2006 | 2006-03-03 |
| 7 | S2E1 | The Work Outing | vendredi 24 août 2007 | 2007-08-24 |
| 8 | S2E2 | Return of the Golden Child | vendredi 31 août 2007 | 2007-08-31 |
| 9 | S2E3 | Moss and the German | vendredi 7 septembre 2007 | 2007-09-07 |
| 10 | S2E4 | The Dinner Party | vendredi 14 septembre 2007 | 2007-09-14 |
| 11 | S2E5 | Smoke and Mirrors | vendredi 21 septembre 2007 | 2007-09-21 |
| 12 | S2E6 | Men Without Women | vendredi 28 septembre 2007 | 2007-09-28 |
| 13 | S3E1 | From Hell | vendredi 21 novembre 2008 | 2008-11-21 |
| 14 | S3E2 | Are We Not Men? | vendredi 28 novembre 2008 | 2008-11-28 |
| 15 | S3E3 | Tramps Like Us | vendredi 5 décembre 2008 | 2008-12-05 |
| 16 | S3E4 | The Speech | vendredi 12 décembre 2008 | 2008-12-12 |
| 17 | S3E5 | Friendface | vendredi 19 décembre 2008 | 2008-12-19 |
| 18 | S3E6 | Calendar Geeks | vendredi 26 décembre 2008 | 2008-12-26 |
| 19 | S4E1 | Jen the Fredo | vendredi 25 juin 2010 | 2010-06-25 |
| 20 | S4E2 | The Final Countdown | vendredi 2 juillet 2010 | 2010-07-02 |
| 21 | S4E3 | Something Happened | vendredi 9 juillet 2010 | 2010-07-09 |
| 22 | S4E4 | Italian for Beginners | vendredi 16 juillet 2010 | 2010-07-16 |
| 23 | S4E5 | Bad Boys | vendredi 23 juillet 2010 | 2010-07-23 |
| 24 | S4E6 | Reynholm vs Reynholm | vendredi 30 juillet 2010 | 2010-07-30 |
| 25 | Spécial (noté `SP` dans certaines fiches) | The Internet Is Coming | vendredi 27 septembre 2013 | 2013-09-27 |

### Précisions attachées à la table

| Point | Contenu | Statut |
|---|---|---|
| Double programme | Les épisodes 1 et 2 ont été diffusés le même soir | `[VÉRIFIÉ]` recoupé |
| Graphie de S1E3 | « Fifty-Fifty » (Wikipedia EN, TVmaze) ; « 50/50 » (British Comedy Guide) ; « 50:50 » (TheTVDB) ; « Fifty Fifty » (Wikiquote) | Graphie de Wikipedia EN retenue par convention ; carton-titre `[À VÉRIFIER]` |
| Graphie de S3E4 | « The Speech » (Wikipedia EN, TVmaze) ; « Speech » (British Comedy Guide) | Idem |
| Graphie de S4E6 | « Reynholm vs Reynholm » (Wikipedia EN, British Comedy Guide, TVmaze) ; « Reynholm v Reynholm » (Wikiquote, Fandom) ; titre alternatif « Douglas and Divorce » (Wikipedia EN) | Idem |
| Autre titre de S2E6 | Annoncé « The Joy Of Sex » dans la grille de Channel 4 selon British Comedy Guide | `[VÉRIFIÉ]` source unique |
| Titres erronés du spécial | « The Last Byte » (erroné selon Wikipedia EN) ; « The Final Episode » (Netflix, Time Out) | `[VÉRIFIÉ]` |
| Numérotation du spécial | Ni saison 5 ni S4E7 : certains agrégateurs (JustWatch, AlloCiné) le rangent pourtant ainsi | `[VÉRIFIÉ]` |
| Heure de diffusion | 21 h pour S1E1 et pour le spécial ; 21 h 30 pour S1E2 à S2E6 ; 22 h pour les saisons 3 et 4, sauf S3E4 (22 h 05) et S3E6 (21 h 50) | `[VÉRIFIÉ]` source unique (British Comedy Guide, fiches 03 et 04). TVmaze affiche 22 h partout : valeur par défaut, à ignorer |
| Durée | Créneau de 30 minutes, environ 24 minutes nettes ; spécial : créneau de 60 minutes, 47 à 48 minutes nettes | `[VÉRIFIÉ]` |
| Scénario | Graham Linehan pour les 25 épisodes | `[VÉRIFIÉ]` recoupé |
| Réalisation | Graham Linehan ; British Comedy Guide crédite en plus Ben Fuller (saison 1), Barbara Wiltshire (saison 2), Richard Boden (saisons 3 et 4, spécial) | Second crédit `[À VÉRIFIER]` au générique |
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
2. Lire `00-CONTRADICTIONS-ET-LACUNES.md` : il dit quelles affirmations des fiches ont été corrigées ou restent ouvertes.
3. Lire la ou les fiches utiles à la question.

En cas de désaccord : la table des épisodes du README l'emporte sur tout ; le fichier 00 l'emporte sur les fiches ; dans une fiche, une note `RC` l'emporte sur le texte qui la précède ; entre deux fiches non arbitrées, préférer celle dont la source est de meilleur niveau (générique ou presse datée, puis British Comedy Guide, puis Wikipedia, puis Wikiquote, puis sites de fans).

### Quelle fiche pour quelle question

| Question | Fiche à lire d'abord | Compléments |
|---|---|---|
| Numéro, titre ou date d'un épisode | `README.md`, section 4 | 03, 04 |
| Titre français d'un épisode | `README.md`, section 4 | 00, section 3 ; 08, section 7.3 |
| Que se passe-t-il dans tel épisode ? | 03 (épisodes 1 à 12) ou 04 (épisodes 13 à 25) | 02 pour les invités |
| Qui joue tel rôle ? Dans quel épisode apparaît tel acteur ? | 02 | 03, 04 |
| Biographie, prix et carrière d'un acteur | 02, section 5 | 09, section 9 |
| Dans quel épisode et par qui est dite telle réplique ? | 05 | 03, 04 ; contrôler dans 00 les lignes X19 à X40 |
| Gag récurrent, faux produit, fausse publicité, mot inventé | 05 | 07 |
| Qui a produit, réalisé, monté ? Où la série a-t-elle été tournée ? | 01 | 06 pour les lieux |
| Audiences, DVD, streaming, remakes, diffusion et doublage en France | 01 | 09 pour les audiences ; 08 pour la VF |
| Décor du sous-sol, objets, ordinateurs anciens, t-shirts de Roy | 06 | 07, 02 |
| Que parodie tel gag ? Quelle référence geek ou britannique ? | 07 | 05, 03, 04 |
| Accents, argot, traduction, procédés comiques, méthode de Linehan | 08 | 05 |
| Critiques, prix, classements, mèmes, postérité | 09 | 05 pour les répliques |
| Retrait de « The Speech », polémiques autour de Graham Linehan | 09, section 10 | 07, section 9.2 ; 01, section 10 |
| Générique d'ouverture | 10 (quand elle sera disponible) | 06, section 9 ; 07, section 7.2 |
| Ce fait est-il sûr ? | 00 | Étiquette de la ligne dans la fiche |

### Règles de restitution

- Reprendre l'étiquette avec le fait. Ne jamais présenter un `[PROBABLE]` ou un `[À VÉRIFIER]` comme établi.
- Pour tout fait `[VÉRIFIÉ]`, dire « selon telle source », pas « on voit dans l'épisode ».
- Citer une réplique en VO, une ligne au plus, en précisant que le mot à mot n'a pas été contrôlé à l'écoute.
- Les traductions françaises de la fiche 05 sont libres : ne pas les présenter comme le texte du doublage.
- Pour un titre français, donner le titre le mieux attesté et sa variante, et préciser qu'aucun n'est confirmé par un diffuseur.
- Les chiffres en ligne de la fiche 09 (notes, vues, abonnés) sont datés du 2026-10-10 : les redonner avec leur date.
- Si la base ne contient pas l'information, le dire et renvoyer à la lacune correspondante du fichier 00 (L01 à L20), qui indique comment la combler.

### Codes et conventions communs

| Élément | Convention |
|---|---|
| Épisode | `SxEy` ; « Spécial » ou `SP` pour l'épisode de 2013 ; `#n` ou « n° global » de 1 à 25 |
| Saison | Les fiches écrivent « saison » ou « série » (usage britannique) : même sens |
| Dates | En toutes lettres ou au format ISO (fiche 04) |
| Titres d'œuvres et noms propres | En anglais ; graphies de noms de personnages selon British Comedy Guide (Philip, Johann, Pippin, Jorg, Stephen Premel) |
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

## Découpages scène par scène (dossier `episodes/`)

- 24 épisodes sur 25 ont été regardés sur la chaîne YouTube officielle et découpés scène par scène : voir `episodes/README.md`.
- S3E4 « The Speech » n'est pas disponible en entier sur la chaîne officielle : non traité.
- Méthode et limites : `_methode/visionnage.md`. Visionnage par échantillonnage d'images et sous-titres automatiques ; le son n'a pas été écouté.
- **Les fiches 01 à 09 n'ont pas encore été corrigées d'après ce visionnage.** En cas de désaccord, `episodes/_CORRECTIONS-ISSUES-DU-VISIONNAGE.md` et les fiches d'épisodes font foi, car elles sont les seules à porter `[VU À L'IMAGE]`.
- Étiquette supplémentaire propre à ces fiches : `[SOUS-TITRES AUTO]` = lu dans les sous-titres automatiques de YouTube, non contrôlé à l'oreille.
