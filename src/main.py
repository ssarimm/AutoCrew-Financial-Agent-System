import sys
import os
from src.config import get_llm
from src.modeling_crew import ModelingCrew
from src.mrm_crew import MRMCrew

def main():
    print("==========================================")
    print("🤖 FINANCIAL AGENT SYSTEM (CrewAI + LLMs)")
    print("==========================================")

   
    print("\nSelect LLM Provider:")
    print("1. Groq (Llama 3.1 8B)")
    print("2. Google Gemini 1.5 Flash")
    print("3. Ollama (Local LLM)")
    print("4. MOCK LLM")
    llm_choice = input("Choice (1-4): ") 
    
    
    if llm_choice not in ['1', '2', '3', '4']: 
        print("Invalid LLM choice. Exiting.")
        sys.exit()
        
    llm = get_llm(llm_choice)

    print("\nSelect Task:")
    print("1. Credit Card Approval (UCI)")
    print("2. Fraud Detection (Kaggle)")
    print("3. Portfolio Credit Risk (Give Me Some Credit)")
    task_choice = input("Choice (1-3): ")
    
    if task_choice == "1":
        dataset = "data/credit_card_approval.csv"
        task_desc = "Predict credit approval (Binary Classification)."
    elif task_choice == "2":
        dataset = "data/creditcard_2023.csv"
        task_desc = "Detect Fraud (Imbalanced Data)."
    elif task_choice == "3":
        dataset = "data/cs-training.csv"
        task_desc = "Predict probability of financial distress (Credit Scoring)."
    else:
        print("Invalid task choice. Exiting.")
        sys.exit()

   
    if llm_choice != '4' and not os.path.exists(dataset):
        print(f"\nERROR: Dataset not found: {dataset}")
        print(f"Please download it and save it to the 'data/' folder.")
        sys.exit()

    # running modeling crew
    print(f"\nStarting Modeling Phase for: {task_desc} using LLM choice: {llm_choice}")
    model_crew = ModelingCrew(llm)
    modeling_output = model_crew.run(dataset, task_desc)
    
    print("\nModeling Output:")
    print(modeling_output)

    # human intervention
    print("\n" + "="*40)
    print("HUMAN INTERVENTION (MRM Audit Gate)")
    proceed = input("Proceed to Audit? (y/n): ")
    if proceed.lower() != 'y':
        sys.exit()

    # running mrm crew
    print("\nStarting MRM Audit Phase...")
    mrm_crew = MRMCrew(llm)
    final_verdict = mrm_crew.run(modeling_output)
    
    print("\n" + "="*40)
    print(f"FINAL VERDICT:\n{final_verdict}")

if __name__ == "__main__":
    main()