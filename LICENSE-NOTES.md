# Notes de licence et de droits

Statut : le dépôt est public. Les licences décrites en section 6 sont **une proposition appliquée par défaut** dans le fichier [`LICENSE`](LICENSE), pour que le dépôt ne reste pas sans licence. Kōeki peut les changer : la marche à suivre est en section 6. Ce document n'est pas un avis juridique. Il fixe une ligne de conduite prudente ; les points marqués « à trancher » demandent une décision, et au besoin un conseil.

## 1. Le principe

Le dépôt public ne contient que ce que le projet a écrit ou dessiné lui-même, plus des liens. Tout ce qui sort de la série reste hors du dépôt.

## 2. Ce qui est dans le dépôt public

| Contenu | Pourquoi | Condition |
|---|---|---|
| Les fiches de `kb/` | Texte original : des faits, reformulés et sourcés | Pas de copie de passages entiers d'une source |
| Les découpages de `kb/episodes/` | Texte original : l'action racontée scène par scène | Voir section 3 |
| Les liens vers les sources et vers les vidéos officielles | Un lien n'est pas une copie | Vers des pages légitimes ; aucun lien vers une copie pirate d'un épisode |
| Titres d'épisodes, dates, noms, crédits | Des faits | Aucune |
| Répliques en VO | Courte citation, à l'appui d'un commentaire | Une ligne au plus, attribuée (personnage, épisode), jamais un dialogue ni une scène |
| Traductions libres des répliques | Écrites par le projet | Dire que ce n'est pas le texte du doublage |
| Le pixel art de `assets/` et de `docs/` | Création originale | Aucun portrait ressemblant, aucun décalque d'une image de la série |
| Le code de `tools/` et de `docs/` | Écrit pour le projet | Aucune dépendance embarquée |

## 3. Les découpages scène par scène

Les fichiers de `kb/episodes/` décrivent chaque épisode regardé. Ce qui les rend publiables :

- **Ce sont des textes originaux.** Le rédacteur raconte ce qu'il voit : le lieu, qui est là, ce qui se passe, ce qu'il y a au mur. Aucun scénario, aucune description officielle n'est recopié.
- **Les dialogues ne sont pas retranscrits.** L'action est résumée. Chaque découpage ne cite qu'une poignée de répliques, courtes, d'une ligne, pour situer un gag.
- **Ces répliques viennent des sous-titres automatiques de YouTube.** Elles portent l'étiquette `[SOUS-TITRES AUTO]` : non contrôlées à l'oreille, sans nom de locuteur, avec les erreurs de la machine. Ce n'est ni le texte du scénario, ni celui des sous-titres officiels.
- **Le découpage renvoie à la vidéo, il ne la remplace pas.** Chaque fichier donne l'identifiant de la vidéo sur la chaîne YouTube officielle ; le site et le README en font un lien. Rien n'est copié, intégré ni téléchargé : pas de vidéo, pas de son, pas d'image, pas de fichier de sous-titres.
- **Aucune source illicite.** Un épisode absent de la chaîne officielle n'est pas regardé ailleurs. C'est pourquoi S3E4 n'a pas de découpage.
- **Le visionnage n'a rien laissé derrière lui.** Les images ont été affichées dans un navigateur le temps de les décrire, sans capture enregistrée (voir `kb/_methode/visionnage.md`).

Règle pour la suite : si un découpage grossit au point de pouvoir se lire à la place de l'épisode, répliques comprises, il est allé trop loin. On raccourcit les citations, pas le lien.

Point à trancher par Kōeki : un résumé détaillé de chaque scène reste une œuvre dérivée d'un genre toléré (guides d'épisodes, wikis de fans), mais vingt-quatre épisodes décrits en entier, c'est beaucoup de détail. La parade retenue ici est la sobriété des citations et le renvoi systématique à la source officielle. En cas de demande d'un ayant droit, voir section 8.

## 4. Ce qui reste hors du dépôt

| Contenu | Où le garder |
|---|---|
| Captures d'écran, photogrammes, images de plateau, visuels de presse, jaquettes | En local, dans `media-local/` (ignoré par git), ou nulle part |
| Extraits audio ou vidéo, génériques, musique, jingles | En local |
| Logo de la série, logo de Channel 4, typographie du titre reproduite | Nulle part dans le dépôt |
| Scénarios, transcriptions, fichiers de sous-titres, dialogues retranscrits | En local |
| Paroles complètes de chansons de la série | En local |
| GIF et mèmes tirés d'images de la série | Lien vers la page qui les documente, pas le fichier |
| Portraits des acteurs, y compris dessinés de façon ressemblante | Nulle part dans le dépôt (droit à l'image) |
| Copies d'articles de presse ou de pages de wiki | Lien et résumé, pas la copie |

Le fichier `.gitignore` du dépôt écarte `media-local/` et les formats vidéo, audio et sous-titres courants, pour qu'un fichier de travail ne parte pas par accident.

## 5. Les personnages en pixels

Les cinq personnages sont des archétypes de bureau : un technicien, un génie à lunettes, une cheffe, un patron, un gothique. Chacun est dessiné en une seule couleur vive sur une grille de 12 pixels de large, à la manière des micro-ordinateurs 8 bits. À cette taille et dans ces couleurs, aucun n'est le portrait de quelqu'un. Règle pour la suite : ne pas chercher la ressemblance, ne pas reprendre un t-shirt, une affiche ou un accessoire copié d'une image de la série. L'image de partage, l'icône du site et la page d'erreur sont faites des mêmes pixels.

Deux points de vigilance, à trancher par Kōeki :

- Le titre « The IT Crowd » apparaît en toutes lettres dans la bannière et dans l'image de partage, dessiné dans la police du projet. C'est le nom du sujet, pas le logo. Si la prudence l'emporte, le remplacer par « L'encyclopédie du sous-sol » ne casse rien.
- Les noms inventés par la série (Reynholm Industries, Friendface, etc.) sont cités dans les fiches comme des faits. Dans le graphisme, ils servent de clin d'œil (« Reynholm 48K »). Même remarque : faciles à retirer.

## 6. Licences : une proposition, appliquée par défaut

| Partie | Licence | Raison |
|---|---|---|
| Code (`tools/`, JavaScript et CSS de `docs/`) | MIT | Simple, permissive, habituelle |
| Textes (`kb/`, README, documentation) | CC BY-SA 4.0 | Une partie des faits vient de Wikipedia et de wikis de fans, eux-mêmes sous CC BY-SA. Les faits ne sont pas protégés, mais si une formulation est restée proche de la source, cette licence est la seule compatible. Elle garantit aussi que les reprises restent ouvertes. |
| Graphisme original (`assets/`, `tools/pixel.json`, pixel art de `docs/`) | CC BY 4.0 | Réutilisable par les fans, avec crédit |

Le fichier [`LICENSE`](LICENSE) applique ces trois licences et dit en toutes lettres qu'aucune ne couvre la série elle-même.

**Ce choix n'a pas été validé par Kōeki : il a été posé par défaut au moment de finir la vitrine.** Pour en changer :

1. modifier le fichier `LICENSE` (le périmètre de chaque licence est en tête) ;
2. modifier le tableau ci-dessus, la ligne de licences au pied de `docs/index.html` et la phrase de la section « Contribuer » du README ;
3. noter que ce qui a déjà été diffusé sous une licence ouverte le reste pour qui l'a reçu : on change la licence des versions à venir, pas celle des copies déjà parties.

Variantes raisonnables : CC BY-SA 4.0 aussi pour le graphisme, si Kōeki veut que les dérivés restent ouverts ; CC BY-NC-SA pour les textes, si l'usage commercial doit être exclu (au prix d'une incompatibilité avec Wikipedia).

## 7. Ce qui reste à trancher ou à contrôler

1. Valider ou changer les trois licences (section 6).
2. Relire les fiches à la recherche de passages recopiés d'une source plutôt que reformulés, en commençant par les synopsis des fiches 03 et 04 et les biographies de la fiche 02.
3. Vérifier que chaque réplique citée tient en une ligne, découpages compris.
4. Décider du sort du titre et des noms de fiction dans le graphisme (section 5).
5. Décider du niveau de détail acceptable pour les découpages (section 3).

## 8. Mention affichée, et demandes de retrait

La mention figure au pied du README, de la page `docs/index.html` et de la page d'erreur :

> Projet de fans, non officiel. Aucun lien avec Channel 4, Talkback Thames, Graham Linehan ni aucun ayant droit de *The IT Crowd*. Aucune image, aucun logo, aucun son, aucun extrait de la série.

En cas de demande de retrait : retirer d'abord, discuter ensuite. Le README invite les ayants droit à ouvrir un ticket sur le dépôt ; une adresse de contact reste à ajouter si Kōeki préfère un canal privé.
