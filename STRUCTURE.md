# Structure du dépôt

Ce document décrit ce que le dépôt contient vraiment, les conventions de nommage, et ce qui reste à faire. La première partie est un état des lieux ; la feuille de route est à la fin, à part. Les chiffres entre repères `<!--n:...-->` sont recalculés par `tools/build_svg.py --sync-docs`.

## 1. Arborescence réelle

```text
the-it-crowd/
├── README.md                    Vitrine GitHub : SVG animés, sommaire, installation, contribution.
├── STRUCTURE.md                 Ce fichier.
├── LICENSE                      Les trois licences et leur périmètre (MIT, CC BY-SA 4.0, CC BY 4.0).
├── LICENSE-NOTES.md             Ce qui peut être publié et pourquoi ; licences appliquées par défaut.
├── .gitignore                   Écarte les médias tirés de la série, les captures de contrôle, les caches.
│
├── kb/                          La base de connaissances : la source de vérité.
│   ├── README.md                Conventions, table de référence des 25 épisodes, mode d'emploi IA.
│   ├── 00-CONTRADICTIONS-ET-LACUNES.md
│   ├── 01-production-diffusion.md
│   ├── 02-personnages-casting.md
│   ├── 03-episodes-saisons-1-2.md
│   ├── 04-episodes-saisons-3-4-special.md
│   ├── 05-repliques-gimmicks-running-gags.md
│   ├── 06-decors-lieux-accessoires.md
│   ├── 07-references-geek-tech-pop-culture.md
│   ├── 08-accents-langue-humour.md
│   ├── 09-reception-memes-heritage.md
│   ├── 10-generique.md          Le générique image par image.
│   ├── _methode/
│   │   └── visionnage.md        Comment les épisodes ont été regardés ; limites de la méthode.
│   └── episodes/                Un découpage scène par scène par épisode regardé.
│       ├── README.md            Index des découpages.
│       ├── S1E1-yesterdays-jam.md
│       ├── …                    Un fichier par épisode, de S1E1 à S4E6.
│       ├── SP-the-internet-is-coming.md
│       ├── S3E4-the-speech-NON-TRAITE.md      Constat : épisode absent de la chaîne officielle.
│       └── _CORRECTIONS-ISSUES-DU-VISIONNAGE.md   Ce que le visionnage corrige dans les fiches 01 à 09.
│
├── assets/                      Générés par tools/build_svg.py : ne pas modifier à la main.
│   ├── hero.svg                 Bannière : boot, titre, kernel panic, extinction, redémarrage.
│   ├── crew.svg                 Les cinq personnages, le trou, la porte rouge.
│   ├── emergency-number.svg     Le numéro d'urgence qui défile.
│   ├── fire.svg                 Le feu et le courriel.
│   ├── the-internet.svg         La boîte noire et sa diode.
│   ├── answerphone.svg          Le répondeur à bandes.
│   ├── counter.svg              Jours sans incident : 0.
│   ├── loading.svg              La barre de chargement.
│   ├── tnetennba.svg            Les neuf tuiles.
│   ├── divider-tape.svg         Séparateur : bandes de chargement.
│   ├── divider-cable.svg        Séparateur : la prise.
│   ├── badge-*.svg              Cinq badges animés ; deux comptent ce qu'il y a dans kb/.
│   └── social-preview.png       Image de partage, 1280 × 640 (à téléverser dans les réglages du dépôt).
│
├── docs/                        Site GitHub Pages.
│   ├── index.html               Page autonome : un fichier, aucune dépendance. Lit les fiches dans kb/.
│   ├── 404.html                 Page d'erreur autonome. Générée.
│   ├── social-preview.png       Copie de l'image de partage, servie par le site. Générée.
│   └── .nojekyll                Sert le dossier tel quel.
│
└── tools/                       Fabrication.
    ├── pixel.json               Police 5 × 7 et personnages : source unique du graphisme.
    └── build_svg.py             Génère assets/ ; avec --sync-docs, met aussi à jour docs/ et les compteurs.
```

Deux dossiers peuvent exister sur une machine sans jamais être versionnés : `_previews/` (captures de contrôle de la page et des SVG) et `media-local/` (captures et extraits de travail tirés de la série). Le `.gitignore` les écarte.

## 2. Ce qui est fait

| Élément | État |
|---|---|
| Fiches thématiques | <!--n:fiches-->11<!--/n-->, de 00 à <!--n:derniere-->10<!--/n-->, <!--n:fiches_poids-->939 Ko<!--/n--> |
| Découpages scène par scène | <!--n:vus-->24<!--/n--> épisodes sur <!--n:eps-->25<!--/n-->, <!--n:scenes-->652<!--/n--> scènes, <!--n:decoupages_poids-->769 Ko<!--/n--> |
| Méthode de visionnage, index, fichier de corrections | Écrits |
| Base entière | <!--n:kb_fichiers-->40<!--/n--> fichiers Markdown, <!--n:kb_poids-->1,8 Mo<!--/n--> |
| README animé | <!--n:svg-->16<!--/n--> SVG générés, sans script ni ressource externe |
| Site | Terminal, lecteur de fiches et de découpages, grille des épisodes, page d'erreur, balises de partage |
| Licences | Appliquées par défaut dans `LICENSE` ; Kōeki peut en changer (voir `LICENSE-NOTES.md`) |
| Compteurs | Tous calculés par `tools/build_svg.py --sync-docs` à partir de `kb/` |

## 3. Conventions de nommage

| Objet | Règle | Exemple |
|---|---|---|
| Fiche | `NN-sujet-en-minuscules.md`, deux chiffres, tirets, sans accent | `06-decors-lieux-accessoires.md` |
| Fichier transversal de la base | Majuscules ; tiret bas en tête dans `episodes/` | `00-CONTRADICTIONS-ET-LACUNES.md` |
| Découpage | `CODE-titre-en-minuscules.md` | `S2E1-the-work-outing.md`, `SP-the-internet-is-coming.md` |
| Épisode, dans le texte | `SxEy` ; `SP` pour le spécial ; numéro global de 1 à 25 | `S2E1`, `SP`, n° 7 |
| Réplique, gag, faux produit, mot | Identifiants de la fiche 05, stables | `R15`, `G04`, `P07`, `M01` |
| Contradiction, lacune | `Xnn` et `Lnn` dans la fiche 00 ; `Cn`, `Ln` dans une fiche | `X19`, `L04` |
| Source | Clé courte entre crochets | `[BCG-S1E2]`, `[W-LIST]` |
| Étiquette de preuve | Entre crochets, en majuscules, avec accents. Cinq dans les fiches, deux de plus dans les découpages | `[À VÉRIFIER]`, `[SOUS-TITRES AUTO]` |
| Minutage | `m:ss` de la vidéo officielle, après l'étiquette | `[VU À L'IMAGE 4:25]` |
| Correction de relecture | Marque `RC`, le texte d'origine reste | `RC : relu le 2026-10-10` |
| Date | ISO dans les données, en toutes lettres dans la prose | `2006-02-03` |
| SVG | Minuscules, tirets, nom de ce qu'on voit | `the-internet.svg` |
| Titres d'œuvres, noms propres | En anglais, graphie de British Comedy Guide pour les personnages | *Calamity Jen* |
| Langue | Fiches et documentation en français ; répliques en VO | |

Frontmatter YAML d'une fiche thématique : `title`, `scope`, `last_updated`, `language`, `fiche`, plus la clé des étiquettes (nommée de plusieurs façons selon les fiches).

Frontmatter d'un découpage : `title`, `scope`, `episode` (le code), `numero_global`, `source_video` (l'identifiant YouTube de onze caractères, ou `null`), `duree`, `last_updated`. C'est ce que lit le script pour construire l'index : un fichier de `kb/episodes/` sans champ `episode` est ignoré, un fichier dont `source_video` vaut `null` ou qui porte `statut: non_traite` compte comme non traité. Le nombre de scènes n'est pas déclaré : le script compte les titres numérotés (`### 12. …` ou `### Scène 12 — …`) de la section « Découpage scène par scène ».

## 4. Règles de flux

1. `kb/` est la source. Tout le reste en dérive, jamais l'inverse.
2. `tools/pixel.json` est la source du graphisme. `assets/`, l'icône et le pixel art des pages en dérivent.
3. Après toute modification de `kb/` ou de `tools/pixel.json` : `python3 tools/build_svg.py --sync-docs`. Le script récrit `assets/`, les blocs de données et les compteurs de `docs/index.html`, `docs/404.html`, l'image de partage, et les chiffres de `README.md` et de ce fichier. Le relancer sans rien avoir changé ne modifie aucun fichier.
4. Rien de ce qui sort de la série n'entre dans le dépôt. Voir `LICENSE-NOTES.md`.

## 5. Feuille de route : ce qui reste

Rien de ce qui suit n'existe dans le dépôt.

| Chantier | Contenu | État |
|---|---|---|
| Le son | Les découpages ont été faits son coupé. Restent à contrôler à l'oreille : le mot à mot des répliques, les accents, la musique, les rires, et tout ce que la fiche 08 affirme sur les voix | À faire |
| S3E4, *The Speech* | Découpage à partir d'une source licite (DVD, plateforme), ou à défaut des deux extraits officiels. Le fichier `S3E4-the-speech-NON-TRAITE.md` cède alors la place à un découpage normal ; la phrase du README sur le vingt-cinquième épisode est à récrire à la main | À faire |
| Report des corrections | Reporter dans les fiches 01 à 09 ce que consigne `_CORRECTIONS-ISSUES-DU-VISIONNAGE.md`, puis lever les contradictions et lacunes de la fiche 00 que le visionnage tranche | En cours |
| Version française | Les découpages décrivent la VO. Titres français, doublage et sous-titres officiels restent `[À VÉRIFIER]` faute de source de diffuseur | À faire |
| Données par épisode | Un JSON par épisode, dérivé de `kb/` par script (forme proposée ci-dessous), puis personnages, répliques, gags | À faire |
| Contrôles automatiques | Étiquettes valides, clés de sources connues, table des épisodes intacte, nombre de scènes de l'index conforme aux fichiers | À faire |
| Liens | Sources dédoublonnées avec date de consultation ; offres légales, datées | À faire |
| Recherche | Recherche plein texte dans la page | À faire |
| Version anglaise | README et page en anglais | À décider |
| Harmonisation | Une seule clé de frontmatter pour les étiquettes ; un seul format de titre de scène dans les découpages | À faire |

### Forme proposée pour un fichier de données d'épisode

Proposition, pas encore appliquée. Chaque valeur porterait son étiquette et sa source, comme dans les fiches.

```json
{
  "code": "S1E2",
  "number": 2,
  "title": { "value": "Calamity Jen", "label": "VÉRIFIÉ", "sources": ["W-LIST", "BCG", "TVMAZE"] },
  "first_aired": { "value": "2006-02-03", "channel": "Channel 4", "label": "VÉRIFIÉ", "sources": ["W-LIST", "BCG", "TVMAZE"] },
  "title_fr": { "value": "Aïe mes pieds !", "variant": "Calamity Jen !", "label": "À VÉRIFIER" },
  "official_video": "Z0dvAy1puIE",
  "quotes": ["R15", "R16", "R17", "R18", "R19", "R20"],
  "gags": ["G02", "G03", "G24"],
  "kb": ["kb/03-episodes-saisons-1-2.md", "kb/episodes/S1E2-calamity-jen.md"]
}
```
