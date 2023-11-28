import json
import math
import os
import random
from typing import Dict, List, Tuple


def load_examples() -> List[Dict[str, str]]:
    examples: List[Dict[str, str]] = []

    with open('./data/examples.jsonl', 'r') as file:
        for line in file:
            examples.append(json.loads(line))

    return examples


def get_keys():
    with open("keys.json", "r") as f:
        keys = json.load(f)
        os.environ['OPENAI_API_KEY'] = keys['openai']


def create_text_example(example: Dict[str, str]) -> str:
    return f"Input: '{example['input']}' Label: {example['label']}"


def create_context(examples: List[Dict[str, str]]) -> str:
    return '\n'.join([create_text_example(example) for example in examples])


def get_train_test_split(task: str, examples: List[Dict[str, str]], train_share=0.5) -> Tuple[List[Dict[str, str]]]:
    task_examples = [
        example for example in examples if example["task"] == task]
    # Try to break any repeating pattern in the examples
    random.shuffle(task_examples)

    context_cutoff = math.floor(len(task_examples) * train_share)
    train_examples = task_examples[:context_cutoff]
    test_examples = task_examples[context_cutoff:]

    return train_examples, test_examples
