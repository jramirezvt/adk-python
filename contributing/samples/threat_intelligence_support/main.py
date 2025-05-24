# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Standard library imports
import sys
import os

# Ensure the sample directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
kit_dir = os.path.abspath(os.path.join(current_dir, "..", "..", ".."))
sys.path.insert(0, kit_dir)

# Import ADK framework and agent classes
# It's good practice to initialize the framework if it provides central setup,
# error handling, or logging, even for simple scripts.
from contributing.samples.threat_intelligence_support.classifier_agent import ClassifierAgent
from contributing.samples.threat_intelligence_support.responder_agent import ResponderAgent

def main():
    """
    Runs a demonstration of the Classifier and Responder agents.
    """
    # 1. Define a sample user input
    # sample_user_input = "USER: I think my computer has been infected with malware. Can you help?"
    # Let's try another input to test a different category
    sample_user_input = "USER: I received a suspicious email asking for my password. I think it's a phishing attempt."


    print(f"Sample User Input: \"{sample_user_input}\"\n")

    # 2. Instantiate ClassifierAgent
    # For this example, we are not passing a real LLM instance.
    # The agents have placeholder logic.
    classifier = ClassifierAgent(llm_instance=None)

    # 3. Invoke the ClassifierAgent to get a category
    print("Invoking ClassifierAgent...")
    category = classifier.invoke(user_input=sample_user_input)
    print(f"ClassifierAgent - Determined Category: \"{category}\"\n")

    # 4. Instantiate ResponderAgent
    responder = ResponderAgent(llm_instance=None)

    # 5. Invoke the ResponderAgent with the original input and the determined category
    print("Invoking ResponderAgent...")
    final_response = responder.invoke(user_input=sample_user_input, category=category)

    # 6. Print the final response
    print(f"ResponderAgent - Final Response: \"{final_response}\"")

if __name__ == "__main__":
    main()
