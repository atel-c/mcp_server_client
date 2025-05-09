# remplacé par app.py
from praisonaiagents import Agent, MCP
 
def convert(query):
    agent = Agent(
        instructions="""
                      Vous êtes un assistant IA qui utilise des outils externes via MCP     
                      pour répondre aux questions.
                      Utilisez les outils disponibles pour fournir des réponses précises.
                     """,
        llm="ollama/qwen3:8b",
        tools=MCP(
            command="uv",
            args=["run", "../temperature_convert_server/main.py"]
        )
    )
    result = agent.start(query)
    return f"## Résultat obtenu :\n\n{result}"
 
if __name__ == "__main__":
    output = convert("convert_city_temperatures temperatures.json")
    print(output)
