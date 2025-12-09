import os
from dotenv import load_dotenv
from crewai import LLM
from langchain_community.chat_models import FakeListChatModel
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# to avoid errors in init as crewai sometimes tries to access openai even if not used
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = "NA"

def get_llm(choice=None):
    
    #GROQ
    if choice == "1":
        print("🚀 Using GROQ (Llama 3.1 8B):")
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            api_key = input("Enter Groq API Key (gsk_...): ")
            os.environ["GROQ_API_KEY"] = api_key
            
        return LLM(
            model="groq/llama-3.1-8b-instant",
            api_key=api_key,
            temperature=0.2
        )
    
    #GOOGLE GEMINI
    elif choice == "2":
        print("Using GOOGLE GEMINI...")
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

    #OLLAMA
    elif choice == "3":
        ollama_base_url = os.getenv("OLLAMA_BASE_URL")
        ollama_model_name = os.getenv("OLLAMA_MODEL_NAME")

        print("Using OLLAMA (Local LLM)...")

        if not ollama_base_url or not ollama_model_name:
            print("ERROR: OLLAMA_BASE_URL and OLLAMA_MODEL_NAME must be set in your .env file.")
            ollama_base_url = "http://localhost:11434"
            ollama_model_name = "ollama/llama3"
            print(f"   Falling back to default: {ollama_model_name} @ {ollama_base_url}")
        
        return LLM(
            model=ollama_model_name,
            base_url=ollama_base_url,
            api_key='ollama_is_local', 
            temperature=0.3
        )

    #MOCK LLM
    elif choice == "4":
        print("Using MOCK LLM (Testing Mode)...")
        responses = [
            "Data Extraction: Loaded data successfully.",
            "Model Training: Accuracy 0.95.",
            "MRM: Approved."
        ]
        return FakeListChatModel(responses=responses)
        
    
    else:
        print("ERROR: Invalid choice received. Using MOCK LLM as fallback.")
        responses = ["Fallback: Mock Output"]
        return FakeListChatModel(responses=responses)