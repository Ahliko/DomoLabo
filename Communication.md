
### Structure de la requête
[![Format JSON](https://img.shields.io/badge/Format-JSON-red.svg)]()
```json
<identity>,
<content>
```

<br>

**\<identity>** :

| | Balise | Contenu |
| -- | :--------------- | -----:|
| ![String](https://img.shields.io/badge/String-green.svg) | ***\<name>*** | Contient le nom de l'objet. |
| ![String](https://img.shields.io/badge/String-green.svg) | ***\<mac>*** |  Contient l'adresse mac de l'objet. |

```json
"identity":{
    "name":"<name>",
    "mac":"<adress_mac>"
}
 ```

<br>

**\<content>** :

| | Balise | Contenu |
| -- | :--------------- | -----:|
| ![String](https://img.shields.io/badge/String-green.svg) | [***\<type>***](#type) | Contient le type de requête. |
| ![String](https://img.shields.io/badge/String-green.svg) | [***\<what>***](#what) |  Contient le type de requête à laquelle on réponds. |
| ![String](https://img.shields.io/badge/String-green.svg) | ***\<topic>*** |  Contient le topic de communication de l'objet à ajouter. |
| ![String](https://img.shields.io/badge/String-green.svg) | [***\<status>***](#status) |  Contient le status de la réponse à la requête. |
| ![Json](https://img.shields.io/badge/JSON-red.svg) | [***\<data>***](#data) |  Contient les données transmisent. |

 ```json
"content":{
    "type":"<type>",
    "what":"<subject>",
    "topic":"<topic>",
    "response":"<status>",
    "data": "<data>"
}
 ```
<br>

 #### **\<data>** :



<br>

#### **\<type>** :

| Valeur | Cas d'utilisation | Nécessite |
| :--------------- | -----:| -- |
| ***response*** | Utilisé lors que l'on envoie une réponse. | [***\<what>***](#what) |
| ***data*** |  Utilisé pour envoyer une donnée. | [***\<data>***](#data) |
| ***connection*** |  Utilisé lors d'une demande de connexion. | - |
| ***add*** |  Utilisé lors de l'ajoute d'un objet. | ***\<topic>*** |

<br>

#### **\<what>** :

| Valeur | Cas d'utilisation | Nécessite |
| :--------------- | -----:| -- |
| ***connection*** |  Utilisé lors d'une demande de connexion. | - |
| ***add*** |  Utilisé lors de l'ajoute d'un objet. | - |

<br>

#### **\<status>** :

| Valeur | Cas d'utilisation | Nécessite |
| :--------------- | -----:| -- |
| ***disponible*** | Informe de la disponibilité d'une appareil. | - |
| ***ok*** |  Utilisé à chaque réponse valide. | - |
| ***erreur*** |  Utilisé lors d'une erreur de traitement de la requête. | - |