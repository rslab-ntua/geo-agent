class agentscaffold:
    def __init__(self, query: str, llm):
        self.query = query
        self.llm = llm  # Store the LLM instance

    def rewrite_query(self, query, prompt_file = "system_prompts/initial_rewrite.txt") -> str:
        with open(prompt_file) as f:
            q = f.read() + "\n" + str(query)
        return self.llm.complete(q).text

    
    # something to just chat for future use
    def get_llm_response(self,query: str) -> str:
        return self.llm.complete(query).text