from server import mcp


# Ici on place les outils mcp
import tools.cities_temp_converter_tool

print("Lancement du serveur")
# Point d'entrée pour lancer le serveur

if __name__ == '__main__':
    mcp.run()
