# Temperature Conversion Server (MCP)

Un serveur MCP (Message Control Protocol) qui traite des fichiers JSON contenant des listes de températures par ville et convertit automatiquement chaque valeur dans l'unité opposée (Celsius ↔ Fahrenheit).

## Fonctionnalités

- Accepte des fichiers JSON contenant des listes de températures par ville
- Détecte automatiquement l'échelle de température utilisée (celsius ou fahrenheit)
- Convertit chaque valeur de température dans l'unité opposée
- Restructure les données pour inclure les deux unités pour chaque mesure
- Retourne le fichier JSON transformé avec toutes les conversions

## Installation

### Cloner le dépôt

```bash
git clone https://github.com/atel-c/temp_convert_server.git
cd temp_convert_server
```

### Installer les dépendances

Avec pip :
```bash
pip install -e .
```

Avec uv (recommandé) :
```bash
uv install -e .
```

L'option `-e` installe le projet en mode développement, ce qui permet de modifier le code sans avoir à réinstaller le package.

## Utilisation

### Démarrer le serveur

```bash
python main.py
```
ou
```bash
uv run main.py
```



### Format du fichier JSON d'entrée

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

### Format du fichier JSON de sortie

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

### Tester avec MCP Inspector

Pour tester le serveur MCP et vérifier son fonctionnement, vous pouvez utiliser MCP Inspector :

```bash
mcp dev main.py
```

Cette commande lancera un serveur de développement accessible à l'adresse http://127.0.0.1:6274/. Vous pourrez y visualiser et tester les outils MCP en temps réel.
