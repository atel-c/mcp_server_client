# MCP Server-Client Demo

Un projet démontrant l'interaction entre :
- **`temp_convert_server/`** : un serveur MCP qui convertit des températures,
- **`tcs_mcp_client/`** : un agent Python qui communique avec ce serveur via le protocole MCP.

## Structure

- `temp_convert_server/` : contient le serveur MCP, voir son propre `README.md` pour les détails.
- `tcs_mcp_client/` : le client qui utilise `praisonaiagents` pour interagir avec le serveur MCP.

## Lancement rapide

Tout est automatisé. Depuis `tcs_mcp_client`, exécutez simplement :

```bash
python app.py
```

## Prérequis
Avant de commencer, assurez-vous d'avoir installé les dépendances nécessaires pour faire fonctionner l'application :

Python 3.7+

uv : Outil pour la gestion de l'environnement Python

Gradio : Outil pour la création d'interfaces web

praisonaiagents : Bibliothèque pour l'intégration avec le protocole MCP



## Exemple de format du fichier JSON d'entrée

```json
{
  "Paris": {
    "scale": "celsius",
    "values": [12.5, 15.0, 18.3]
  },
  "New York": {
    "scale": "fahrenheit",
    "values": [59.0, 68.0, 72.5]
  }
}
```

### Exemple de format du fichier JSON de sortie

```json
{
  "Paris": [
    {
      "Celsius": 12.5,
      "Fahrenheit": 54.5
    },
    {
      "Celsius": 15,
      "Fahrenheit": 59
    },
    {
      "Celsius": 18.3,
      "Fahrenheit": 64.94
    }
  ],
  "New York": [
    {
      "Fahrenheit": 59,
      "Celsius": 15
    },
    {
      "Fahrenheit": 68,
      "Celsius": 20
    },
    {
      "Fahrenheit": 72.5,
      "Celsius": 22.5
    }
  ]
}
```
