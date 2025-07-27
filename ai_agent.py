# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

#Step1: Setup API Keys for Groq only
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

# Validate Groq API key
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is required")

#Step2: Setup LLM & Tools (Groq only)
try:
    from langchain_groq import ChatGroq
    from langchain_core.messages import SystemMessage, HumanMessage
    
    # Only initialize Groq LLM
    groq_llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
    
except ImportError as e:
    print(f"Import error: {e}")
    print("Please install required packages: pip install langchain-groq langchain-core")
    raise

#Step3: Simplified AI Agent (Groq only, no search)
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    """
    Simplified agent that only uses Groq API
    """
    try:
        # Only support Groq provider
        if provider != "Groq":
            raise ValueError("Only Groq provider is supported")
        
        # Create Groq LLM with specified model
        llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY)
        
        # Prepare messages
        messages = [SystemMessage(content=system_prompt)]
        
        # Add query messages
        if isinstance(query, list):
            for msg in query:
                messages.append(HumanMessage(content=str(msg)))
        else:
            messages.append(HumanMessage(content=str(query)))
        
        # Get response from Groq
        response = llm.invoke(messages)
        
        return response.content
        
    except Exception as e:
        print(f"Error in AI agent: {e}")
        return f"Sorry, I encountered an error: {str(e)}"