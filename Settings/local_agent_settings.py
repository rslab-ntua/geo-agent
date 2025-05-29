from llama_index.core.tools import ToolMetadata

choices_2_experts = [
            ToolMetadata(description="Water expert, ", name="choice_1"),
            ToolMetadata(description="Land expert", name="choice_2"),
        ]


choices_4_experts = [
            ToolMetadata(description="Water expert, ", name="choice_1"),
            ToolMetadata(description="Water expert", name="choice_2"),
            ToolMetadata(description="Water expert, ", name="choice_1"),
            ToolMetadata(description="Water expert", name="choice_2"),
        ]