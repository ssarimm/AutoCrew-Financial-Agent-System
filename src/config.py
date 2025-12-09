import os
from dotenv import load_dotenv
from crewai import LLM
from langchain_community.chat_models import FakeListChatModel
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

#to avoid errors in init as crewai sometimes tries to access openai even if not used
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = "NA"

def get_llm(choice=None):
    
    
    # GROQ
    if choice == "1":
        print("🚀 Using GROQ (Llama 3.1 8B - Fast & Free)...")
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            api_key = input("Enter Groq API Key (gsk_...): ")
            os.environ["GROQ_API_KEY"] = api_key
            
        return LLM(
            # "Instant" is the lite model 
            model="groq/llama-3.1-8b-instant",
            api_key=api_key,
            temperature=0.2
        )
    
    # GOOGLE GEMINI
    elif choice == "2":
        print("✨ Using GOOGLE GEMINI...")
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            api_key = input("Enter Gemini API Key: ")
        
        # langchain is stable wrapper
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            verbose=True,
            temperature=0.2,
            google_api_key=api_key
        )

    # 3. MOCK for testing
    else:
        print("🍌 Using MOCK LLM...")
        responses = [
            "Data Extraction: Loaded data successfully.",
            "Model Training: Accuracy 0.95.",
            "MRM: Approved."
        ]
        return FakeListChatModel(responses=responses) 