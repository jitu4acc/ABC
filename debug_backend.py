#!/usr/bin/env python3
"""
Simplified backend for debugging
"""

import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=== AI Chatbot Backend Debug ===")
print()

# Check environment variables
groq_key = os.environ.get("GROQ_API_KEY")
if not groq_key:
    print("❌ GROQ_API_KEY not found!")
    sys.exit(1)

print(f"✅ GROQ_API_KEY found: {groq_key[:20]}...")

# Test imports
try:
    print("Testing imports...")
    from fastapi import FastAPI
    print("✅ FastAPI imported")
    
    from langchain_groq import ChatGroq
    print("✅ LangChain Groq imported")
    
    from database import db
    print("✅ Database module imported")
    
    from ai_agent import get_response_from_ai_agent
    print("✅ AI agent imported")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please install missing packages:")
    print("pip install fastapi langchain-groq python-dotenv")
    sys.exit(1)

# Test Groq API
try:
    print("Testing Groq API...")
    llm = ChatGroq(model="llama3-70b-8192", api_key=groq_key)
    from langchain_core.messages import HumanMessage
    response = llm.invoke([HumanMessage(content="Hello!")])
    print("✅ Groq API working!")
    print(f"Response: {response.content[:50]}...")
    
except Exception as e:
    print(f"❌ Groq API error: {e}")
    print("Please check your API key at https://console.groq.com/keys")
    sys.exit(1)

# Start FastAPI server
try:
    print("Starting FastAPI server...")
    
    app = FastAPI(title="AI Chatbot Backend")
    
    @app.get("/")
    async def root():
        return {"message": "AI Chatbot Backend is running!"}
    
    @app.get("/health")
    async def health():
        return {"status": "healthy", "groq_api": "connected"}
    
    print("✅ All checks passed!")
    print("Starting server on http://127.0.0.1:9999")
    
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
    
except Exception as e:
    print(f"❌ Server startup error: {e}")
    sys.exit(1)
