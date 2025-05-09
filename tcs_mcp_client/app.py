from praisonaiagents import Agent, MCP
import gradio as gr
import threading
import queue
import time
import io
import sys
from contextlib import redirect_stdout

log_queue = queue.Queue()

def agent_with_logs(query):
    buffer = io.StringIO()

    with redirect_stdout(buffer):
        agent = Agent(
            instructions="""
            Vous êtes un assistant IA qui utilise des outils externes via MCP
            pour répondre aux questions. Utilisez les outils disponibles pour fournir des réponses précises.
            """,
            llm="ollama/qwen3:8b",
            tools=MCP(
                command="uv",
                args=["run", "C:/Users/Public/Documents/Tutoriels/mcp_server_client/temp_convert_server/main.py"]
            )
        )
        result = agent.start(query, stream=False)
        print("\n---\nRéponse finale:\n", result)

    # Met tout dans la file
    for line in buffer.getvalue().splitlines():
        log_queue.put(line)

def run_agent(query):
    log_display = ""

    thread = threading.Thread(target=agent_with_logs, args=(query,))
    thread.start()

    while thread.is_alive() or not log_queue.empty():
        while not log_queue.empty():
            log_display += log_queue.get() + "\n"
            yield log_display
        time.sleep(0.2)

    yield log_display

# Gradio Blocks UI
with gr.Blocks() as demo:
    gr.Markdown("""# Conversion des Températures (C° ↔ F°)
Entrez une commande pour convertir les températures d'une ville. Le raisonnement complet de l'IA s'affichera ci-dessous.
""")
    query = gr.Textbox(label="Commande", placeholder="convert_city_temp temperatures.json")
    output = gr.Textbox(label="Raisonnement de l'IA", lines=25)
    run_btn = gr.Button("Lancer")

    run_btn.click(fn=run_agent, inputs=query, outputs=output)

if __name__ == "__main__":
    demo.launch()