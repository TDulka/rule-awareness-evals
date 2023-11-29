# rule-awareness-evals
Exploring how language models understand simple rules from context. Contrasting their ability to follow patterns in context with explicit reasoning about the rule.

The code needs an OpenAI API key to run, which is expected to be located in `keys.json` in the format `{ "openai": "YOUR_CODE_HERE" }`

The notebook `exploration.ipynb` tries out different tasks to examine their classification accuracy and rule articulation. The articulations are in `data/articulation`.

The notebook `faithfulness.ipynb` looks at post-hoc reasoning, flipping the order in which exploration was done by first prompting LLM to reason and then making it classify inputs with access to either full or truncated reasoning.

Data for tasks is located in `data/examples.jsonl`.
