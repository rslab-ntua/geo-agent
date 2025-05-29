from llama_index.llms.ollama import Ollama
from llama_index.core.selectors import LLMSingleSelector
from llama_index.core.settings import Settings
from Settings.local_agent_settings import choices_2_experts, choices_4_experts
from helpers.agent_scaffold_bare import agentscaffold
from First_layer.first_layer_abstract import first_layer_abstraction

llm = Ollama(
    model="qwen2.5:14b",  # qwen2.5:7b or gemma3:12b
    request_timeout=220.0,
    base_url="http://ollama-container:11434",
    temperature=0.0, 
)
Settings.llm = llm

def main():
    while True:
        query = input("Enter your query (or type 'exit'): ")
        if query.lower() == "exit":
            break
        if not query.strip():
            continue

        output = first_layer_abstraction(query, llm).entrypoint_rewrite(query)
        print("-----Response after rewrite:", output)


        selector = LLMSingleSelector.from_defaults()
        selector_result = selector.select(
            choices_2_experts, query=output
        )
        routing_decision_index = selector_result.selections[0].index
        print("-----Routing Decision index:", routing_decision_index)
        print("-----Routing Decision Description:", choices_2_experts[routing_decision_index].description)
        

if __name__ == "__main__":
    main()



