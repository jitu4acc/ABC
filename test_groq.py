#!/usr/bin/env python3
"""
Test script to verify Groq API setup
"""

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Test Groq API key
groq_api_key = os.environ.get("GROQ_API_KEY")

if not groq_api_key:
    print("❌ GROQ_API_KEY not found in environment variables")
    print("Please check your .env file")
    exit(1)

print(f"✅ GROQ_API_KEY found: {groq_api_key[:10]}...")

# Test Groq connection
try:
    from langchain_groq import ChatGroq
    from langchain_core.messages import HumanMessage
    
    print("✅ LangChain Groq imports successful")
    
    # Test Groq API
    llm = ChatGroq(model="llama3-70b-8192", api_key=groq_api_key)
    response = llm.invoke([HumanMessage(content="Hello, just testing!")])
    
    print("✅ Groq API test successful!")
    print(f"Response: {response.content}")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install required packages:")
    print("pip install langchain-groq langchain-core")
    
except Exception as e:
    print(f"❌ Groq API error: {e}")
    print("Please check your Groq API key at https://console.groq.com/keys")

print("\n=== Test Complete ===")
