

import os
import sys

project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), '..'))
sys.path.insert(0, project_path)

base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, base_path)


# Test chat availability

from backend.chat.langchain import generate_text

def test_generate_text():
    prompt = "Hello, world!"
    response = generate_text(prompt)
    print(response)
    assert isinstance(response, str), "The response should be a string"
    assert len(response) > 0, "The response should not be empty"

if __name__ == "__main__":
    test_generate_text()