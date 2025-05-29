from helpers.agent_scaffold_bare import agentscaffold

class first_layer_abstraction:
    def __init__(self, query: str, llm):
        self.query = query
        self.llm = llm

    def entrypoint_rewrite(self,query: str) -> str:
        output = agentscaffold(query, self.llm).rewrite_query(query)
        return output
    