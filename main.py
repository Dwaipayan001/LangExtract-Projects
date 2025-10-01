import langextract as lx
import os
from dotenv import load_dotenv

load_dotenv()

instructions = """
    Extract characters, emotions, and relationships in order of appearance.
    Use exact text for extractions. Do not paraphrase or overlap entities.
    Provide meaningful attributes for each entity to add context."""

examples = [
    lx.data.ExampleData(
        text="ROMEO. But soft! What light through yonder window breaks? It is the east, and Juliet is the sun.",
        extractions=[
            lx.data.Extraction(
                extraction_class="character",
                extraction_text="ROMEO",
                attributes={"emotional_state": "wonder"}
            ),
            lx.data.Extraction(
                extraction_class="emotion",
                extraction_text="But soft!",
                attributes={"feeling": "gentle awe"}
            ),
            lx.data.Extraction(
                extraction_class="relationship",
                extraction_text="Juliet is the sun",
                attributes={"type": "metaphor"}
            ),
        ]
    )
]

result = lx.extract(
    text_or_documents="Lady Juliet gazed longingly at the stars, her heart aching for Romeo",
    prompt_description=instructions,
    model_id="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    fence_output=True,
    use_schema_constraints=False,\
    examples=examples,
)

print(result)

# lx.io.save_annotated_documents([result], output_name="extraction_results.jsonl", output_dir=".")

# # Generate the visualization from the file
# html_content = lx.visualize("extraction_results.jsonl")
# with open("visualization.html", "w") as f:
#     f.write(html_content)

