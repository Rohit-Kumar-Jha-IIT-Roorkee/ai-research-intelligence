# test_backend.py
import sys
import os
from dotenv import load_dotenv
load_dotenv()

# Ensure python can find your folders
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agent_reasoning.brain import AgentBrain

def run_test():
    print("🧠 Initializing Agent Brain...")
    try:
        # Initialize the Brain (Person 1)
        brain = AgentBrain()
        print("✅ Brain Initialized.")
    except Exception as e:
        print(f"❌ Brain Initialization Failed: {e}")
        return

    # Simulate a User Input
    user_input = "I want to launch a new subscription coffee service for remote workers."
    print(f"\n🗣️  User Input: '{user_input}'")
    print("--------------------------------------------------")

    # Run the Processing Loop
    try:
        response = brain.process_turn(user_input)
        print("\n🤖 Agent Response:")
        print(response)
        print("\n--------------------------------------------------")
        print("✅ TEST PASSED: The Agent successfully processed the intent.")
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_test()