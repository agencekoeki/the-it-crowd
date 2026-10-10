---
title: "Méthode de visionnage des épisodes"
scope: "Comment les fiches du dossier episodes/ ont été établies : source, procédé, limites. À lire avant de s'appuyer sur une étiquette [VU À L'IMAGE] ou [SOUS-TITRES AUTO]"
last_updated: 2026-10-11
---

# Méthode de visionnage

## Source

- Chaîne YouTube « The IT Crowd » (vérifiée, 156 k abonnés au 2026-10-10), vidéos titrées « The IT Crowd - <Titre> | Full Episode | Series X Episode Y ».
- L'identifiant de chaque vidéo figure dans le frontmatter de la fiche d'épisode (`source_video`) et dans `episodes/README.md`.
- 24 épisodes sur 25 y sont disponibles en entier. S3E4 « The Speech » n'y figure que par deux extraits : il n'a pas été traité, et aucune copie d'un autre compte n'a été utilisée.
- S3E6 a été regardé dans une compilation officielle (épisodes 5 et 6) : ses minutages sont ceux de la compilation.

## Procédé

1. **Fiche de la vidéo** : titre, durée, description et chapitres relevés sur la page.
2. **Sous-titres** : lecture intégrale des sous-titres automatiques de YouTube, avec leurs minutages.
3. **Image** : la vidéo est parcourue par sauts réguliers, et les images obtenues sont affichées côte à côte dans la page, sous forme de planche légendée du minutage. Le pas est de 3 à 10 secondes selon l'épisode, resserré à 1 ou 2 secondes sur les changements de scène, les gags visuels, les décors et les textes lisibles (affiches, t-shirts, écrans, génériques).
4. **Rédaction** : chaque scène est décrite avec les mots du rédacteur. Les dialogues ne sont pas retranscrits ; au plus une dizaine de répliques courtes par épisode sont citées.

Aucune image ni vidéo n'a été enregistrée : les planches n'existent que le temps de la lecture.

## Ce que valent les étiquettes

| Étiquette | Ce qu'elle atteste | Ce qu'elle n'atteste pas |
|---|---|---|
| `[VU À L'IMAGE]` + minutage | Le fait est visible sur une image regardée à ce minutage | Ce qui se passe entre deux images échantillonnées |
| `[SOUS-TITRES AUTO]` + minutage | Le texte figure dans les sous-titres automatiques | L'exactitude du mot à mot, ni l'identité du locuteur |
| `[INTERPRÉTATION]` | Lecture du rédacteur (locuteur déduit de l'image, sens d'un gag) | Un fait |

## Limites

- **Échantillonnage** : ce n'est pas un visionnage continu. Un geste très bref peut avoir échappé ; chaque fiche liste ceux qu'elle sait avoir manqués.
- **Son non écouté** : accents, intonations, rires du public, musique et bruitages ne sont pas observés. Les citations ne sont pas contrôlées à l'oreille.
- **Sous-titres automatiques** : pas de nom de locuteur, pas de ponctuation, des erreurs de reconnaissance (noms propres, jeux de mots).
- **Définition** : les petits textes (détail d'un t-shirt, plaque, écran) sont parfois illisibles.
- **Publicités** : elles ont interrompu certaines planches, refaites ensuite ; quelques images manquantes sont signalées dans les fiches concernées.
- **Version de la chaîne** : les durées varient de 21 à 25 minutes ; il n'est pas établi que chaque vidéo soit le montage diffusé à l'origine.

## Pour compléter

- Écouter les épisodes pour contrôler les citations, attribuer les répliques et documenter accents, musique et rires.
- Traiter S3E4 à partir d'une édition DVD.
- Recouper les textes illisibles sur une source en meilleure définition.
