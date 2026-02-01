import sys
import os
from dotenv import load_dotenv

print("🔍 DIAGNOSTIC MODE")
print("-------------------")

# 1. Test .env loading
load_dotenv()
key = os.getenv("OPENAI_API_KEY")
if key:
    print(f"✅ API Key Found: {key[:8]}... (Length: {len(key)})")
else:
    print("❌ API Key NOT Found. Please check .env file location.")

# 2. Test Person 2 Loading
print("\n🔍 Testing Intelligence Engine Import...")
try:
    from data_intelligence.tool_definitions import ALL_DEFINED_TOOLS
    print(f"✅ Success! Loaded {len(ALL_DEFINED_TOOLS)} tools from Person 2.")
except Exception as e:
    print(f"❌ FAILED to load Person 2. The error is:\n")
    print(e)
    print("\n💡 TIP: If it says 'No module named X', run 'pip install X'")