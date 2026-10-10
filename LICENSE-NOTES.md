# Notes de licence et de droits

Statut : proposition, à valider par Kōeki avant toute publication. Ce document n'est pas un avis juridique. Il fixe une ligne de conduite prudente pour un dépôt public ; les points marqués « à trancher » demandent une décision, et au besoin un conseil.

## 1. Le principe

Le dépôt public ne contient que ce que le projet a écrit ou dessiné lui-même, plus des liens. Tout ce qui sort de la série reste hors du dépôt.

## 2. Ce qui peut aller dans le dépôt public

| Contenu | Pourquoi | Condition |
|---|---|---|
| Les fiches de `kb/` | Texte original : des faits, reformulés et sourcés | Pas de copie de passages entiers d'une source (voir section 5) |
| Les liens vers les sources | Un lien n'est pas une copie | Vers des pages légitimes ; aucun lien vers une copie pirate d'un épisode |
| Titres d'épisodes, dates, noms, crédits | Des faits | Aucune |
| Répliques en VO | Courte citation, à l'appui d'un commentaire | Une ligne au plus, attribuée (personnage, épisode), jamais un dialogue ni une scène |
| Traductions libres des répliques | Écrites par le projet | Dire que ce n'est pas le texte du doublage |
| Le pixel art de `assets/` et de `docs/` | Création originale | Aucun portrait ressemblant, aucun décalque d'une image de la série |
| Le code de `tools/` et de `docs/` | Écrit pour le projet | Aucune dépendance embarquée |
| Données structurées (`data/`, à venir) | Faits extraits des fiches | Mêmes règles que les fiches |

## 3. Ce qui reste hors du dépôt

| Contenu | Où le garder |
|---|---|
| Captures d'écran, photogrammes, images de plateau, visuels de presse, jaquettes | En local, dans `media-local/` (ignoré par git) |
| Extraits audio ou vidéo, génériques, musique, jingles | En local |
| Logo de la série, logo de Channel 4, typographie du titre reproduite | Nulle part dans le dépôt |
| Scénarios, transcriptions, sous-titres, dialogues retranscrits | En local |
| Paroles complètes de chansons de la série | En local |
| GIF et mèmes tirés d'images de la série | Lien vers la page qui les documente, pas le fichier |
| Portraits des acteurs, y compris dessinés de façon ressemblante | Nulle part dans le dépôt (droit à l'image) |
| Copies d'articles de presse ou de pages de wiki | Lien et résumé, pas la copie |

Le travail d'analyse image par image (fiche 10) s'appuie sur des captures : elles servent à l'analyse et restent sur la machine de la personne qui analyse. La fiche publiée décrit ce qui est à l'écran, avec le minutage ; elle ne montre pas l'image.

Fichier `.gitignore` recommandé :

```gitignore
media-local/
*.mp4
*.mkv
*.srt
```

## 4. Les personnages en pixels

Les cinq personnages sont des archétypes de bureau : un technicien, un génie à lunettes, une cheffe, un patron, un gothique. Chacun est dessiné en une seule couleur vive sur une grille de 12 pixels de large, à la manière des micro-ordinateurs 8 bits. À cette taille et dans ces couleurs, aucun n'est le portrait de quelqu'un. Règle pour la suite : ne pas chercher la ressemblance, ne pas reprendre un t-shirt, une affiche ou un accessoire copié d'une image de la série.

Deux points de vigilance, à trancher par Kōeki :

- Le titre « The IT Crowd » apparaît en toutes lettres dans la bannière, dessiné dans la police du projet. C'est le nom du sujet, pas le logo. Si la prudence l'emporte, le remplacer par « L'encyclopédie du sous-sol » ne casse rien.
- Les noms inventés par la série (Reynholm Industries, Friendface, etc.) sont cités dans les fiches comme des faits. Dans le graphisme, ils servent de clin d'œil (« Reynholm 48K »). Même remarque : faciles à retirer.

## 5. Licences proposées

| Partie | Licence proposée | Raison |
|---|---|---|
| Texte des fiches (`kb/`), README, documentation | CC BY-SA 4.0 | Une partie des faits vient de Wikipedia et de wikis de fans, eux-mêmes sous CC BY-SA. Les faits ne sont pas protégés, mais si une formulation est restée proche de la source, cette licence est la seule compatible. Elle garantit aussi que les reprises restent ouvertes. |
| Code (`tools/`, JavaScript et CSS de `docs/`) | MIT | Simple, permissive, habituelle |
| Graphisme original (`assets/*.svg`, `tools/pixel.json`) | CC BY 4.0 | Réutilisable par les fans, avec crédit. Choisir CC BY-SA 4.0 si Kōeki veut que les dérivés restent ouverts. |

Aucune de ces licences ne couvre la série elle-même : elles ne portent que sur ce que le projet a produit. Le fichier `LICENSE` devra le dire en toutes lettres.

À faire avant publication :

1. Kōeki choisit les trois licences et crée `LICENSE` (texte MIT) et `LICENSE-CONTENT` (CC BY-SA 4.0 et CC BY 4.0, avec le périmètre de chacune).
2. Relire les fiches à la recherche de passages recopiés d'une source plutôt que reformulés, en commençant par les synopsis des fiches 03 et 04 et les biographies de la fiche 02.
3. Vérifier que chaque réplique citée tient en une ligne.
4. Décider du sort du titre et des noms de fiction dans le graphisme (section 4).

## 6. Mention à afficher

Elle figure déjà au pied du README et de la page `docs/index.html` :

> Projet de fans, non officiel. Aucun lien avec Channel 4, Talkback Thames, Graham Linehan ni aucun ayant droit de *The IT Crowd*. Aucune image, aucun logo, aucun son, aucun extrait de la série.

## 7. En cas de demande de retrait

Retirer d'abord, discuter ensuite. Une adresse de contact ou un modèle de ticket « retrait » est à prévoir dans le dépôt public.
