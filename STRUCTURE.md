# Structure du dépôt

Ce document décrit l'arborescence visée, les conventions de nommage et la feuille de route. « Existe » : présent dans cette livraison. « Prévu » : proposé, pas encore créé.

## 1. Arborescence

```text
it-crowd/
├── README.md                    Existe. Vitrine GitHub : SVG animés, sommaire, installation, contribution.
├── STRUCTURE.md                 Existe. Ce fichier.
├── LICENSE-NOTES.md             Existe. Ce qui peut être publié, licences proposées (à valider).
├── LICENSE                      Prévu. Code : MIT (à valider).
├── LICENSE-CONTENT              Prévu. Texte : CC BY-SA 4.0 ; graphisme : CC BY 4.0 (à valider).
├── CONTRIBUTING.md              Prévu. Version longue de la section « Contribuer » du README.
├── .gitignore                   Prévu. Ignore media-local/ et les fichiers vidéo.
│
├── kb/                          Existe. La base de connaissances : la source de vérité.
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
│   └── 10-generique.md          Prévu. Analyse image par image ; première fiche à porter [VU À L'IMAGE].
│
├── data/                        Prévu. Données structurées, dérivées de kb/, jamais l'inverse.
│   ├── episodes/
│   │   ├── s1e1.json            Un fichier par épisode (25 fichiers), plus sp.json pour le spécial.
│   │   └── …
│   ├── episodes.json            Index : la table de référence du README de la base.
│   ├── characters.json          Personnages, interprètes, épisodes de présence.
│   ├── quotes.json              Répliques (identifiants R01 à R102 de la fiche 05).
│   ├── gags.json                Gags récurrents (G01 à G28) et faux produits (P01…).
│   ├── sources.json             Clés de sources unifiées (elles diffèrent d'une fiche à l'autre).
│   └── schema/
│       ├── episode.schema.json  Schémas JSON ; chaque valeur porte son étiquette de preuve.
│       └── …
│
├── assets/                      Existe. SVG animés du README : générés, ne pas modifier à la main.
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
│   └── badge-*.svg              Cinq badges animés.
│
├── docs/                        Existe. Site GitHub Pages.
│   ├── index.html               Page autonome : un fichier, aucune dépendance.
│   └── .nojekyll                Sert le dossier tel quel.
│
├── tools/                       Existe. Fabrication.
│   ├── pixel.json               Police 5 × 7 et personnages : source unique du graphisme.
│   ├── build_svg.py             Génère assets/*.svg ; --sync-docs met à jour les données de docs/index.html.
│   ├── build_data.py            Prévu. Extrait data/*.json des fiches.
│   └── check_kb.py              Prévu. Contrôles : étiquettes, clés de sources, table des épisodes.
│
├── links/                       Prévu. Liens externes, classés.
│   ├── sources.md               Toutes les sources citées, dédoublonnées, avec date de consultation.
│   ├── ou-regarder.md           Offres légales, datées (elles changent).
│   └── communautes.md           Forums, wikis, comptes de fans.
│
├── media-local/                 Jamais versionné. Captures et extraits de travail, sur chaque machine.
│
└── _previews/                   Existe. Captures de contrôle des SVG et de la page (à retirer ou à ignorer avant publication).
```

## 2. Conventions de nommage

| Objet | Règle | Exemple |
|---|---|---|
| Fiche | `NN-sujet-en-minuscules.md`, deux chiffres, tirets, sans accent | `06-decors-lieux-accessoires.md` |
| Fichier transversal de la base | Majuscules | `00-CONTRADICTIONS-ET-LACUNES.md` |
| Épisode, dans le texte | `SxEy` ; `SP` pour le spécial ; numéro global de 1 à 25 | `S2E1`, `SP`, n° 7 |
| Épisode, nom de fichier | Minuscules | `data/episodes/s2e1.json`, `sp.json` |
| Réplique, gag, faux produit, mot | Identifiants de la fiche 05, stables | `R15`, `G04`, `P07`, `M01` |
| Contradiction, lacune | `Xnn` et `Lnn` dans la fiche 00 ; `Cn`, `Ln` dans une fiche | `X19`, `L04` |
| Source | Clé courte entre crochets ; à unifier dans `data/sources.json` | `[BCG-S1E2]`, `[W-LIST]` |
| Étiquette de preuve | Exactement l'une des cinq, entre crochets, en majuscules, avec accents | `[À VÉRIFIER]` |
| Correction de relecture | Marque `RC`, le texte d'origine reste | `RC : relu le 2026-10-10` |
| Date | ISO dans les données, en toutes lettres dans la prose | `2006-02-03` |
| SVG | Minuscules, tirets, nom de ce qu'on voit | `the-internet.svg` |
| Titres d'œuvres, noms propres | En anglais, graphie de British Comedy Guide pour les personnages | *Calamity Jen* |
| Langue | Fiches et documentation en français ; répliques en VO | |

Frontmatter YAML de chaque fiche : `title`, `scope`, `last_updated`, `language`, `fiche`, plus la clé des étiquettes. Les neuf fiches nomment cette clé de quatre façons différentes ; l'harmoniser en `evidence_labels` est au programme (étape 2).

## 3. Forme d'un fichier d'épisode (proposition)

Chaque valeur porte son étiquette et sa source, comme dans les fiches.

```json
{
  "code": "S1E2",
  "number": 2,
  "title": { "value": "Calamity Jen", "label": "VÉRIFIÉ", "sources": ["W-LIST", "BCG", "TVMAZE"] },
  "first_aired": { "value": "2006-02-03", "channel": "Channel 4", "label": "VÉRIFIÉ", "sources": ["W-LIST", "BCG", "TVMAZE"] },
  "title_fr": { "value": "Aïe mes pieds !", "variant": "Calamity Jen !", "label": "À VÉRIFIER" },
  "quotes": ["R15", "R16", "R17", "R18", "R19", "R20"],
  "gags": ["G02", "G03", "G24"],
  "kb": "kb/03-episodes-saisons-1-2.md#s1e2--calamity-jen"
}
```

## 4. Règles de flux

1. `kb/` est la source. `data/` en est dérivé par script. On ne corrige jamais un JSON à la main.
2. `tools/pixel.json` est la source du graphisme. `assets/` et le bloc de données de `docs/index.html` en sont dérivés.
3. Rien de ce qui sort de la série n'entre dans le dépôt. Voir `LICENSE-NOTES.md`.

## 5. Feuille de route

| Étape | Contenu | État |
|---|---|---|
| 0 | Dix fiches, relecture croisée, journal des contradictions | Fait |
| 1 | Vitrine : README animé, page GitHub Pages, structure, notes de licence | Fait (cette livraison) |
| 2 | Validation des licences par Kōeki ; `LICENSE`, `LICENSE-CONTENT`, `CONTRIBUTING.md`, `.gitignore` ; harmonisation du frontmatter | À faire |
| 3 | Fiche 10, le générique image par image : premières étiquettes `[VU À L'IMAGE]` | En cours, hors dépôt |
| 4 | Visionnage de contrôle : lever les 33 contradictions ouvertes et les 20 lacunes de la fiche 00, en commençant par les cartons-titres et le mot à mot des répliques | À faire |
| 5 | `data/` : un JSON par épisode, puis personnages, répliques, gags ; `tools/build_data.py` et `tools/check_kb.py` | À faire |
| 6 | Contrôle automatique à chaque contribution (étiquettes valides, clés de sources connues, table des épisodes intacte) | À faire |
| 7 | `links/` : sources dédoublonnées, offres légales datées | À faire |
| 8 | Page : recherche dans les fiches, fiche par épisode alimentée par `data/` | À faire |
| 9 | Version anglaise du README et de la page | À décider |
