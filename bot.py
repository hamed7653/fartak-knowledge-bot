import os
import glob
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print("Error: GEMINI_API_KEY not found in .env file.")
    exit(1)

# Initialize the new Client
client = genai.Client(api_key=API_KEY)

def load_knowledge_base(docs_path="docs/"):
    """Reads all text files in the docs directory and combines them into one context string."""
    context = "COMPANY KNOWLEDGE BASE:\n\n"
    for filepath in glob.glob(os.path.join(docs_path, "*.txt")):
        filename = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8") as f:
            context += f"--- Document: {filename} ---\n"
            context += f.read() + "\n\n"
    return context

def start_bot():
    print("Loading Fartak Knowledge Base...")
    company_context = load_knowledge_base()
    
    system_instruction = (
        "You are the Fartak Tech Internal Assistant. "
        "Answer the user's questions STRICTLY based on the provided COMPANY KNOWLEDGE BASE. "
        "If the answer is not in the knowledge base, say: 'I apologize, but I do not have that information in my current documents.' "
        "Be professional and concise."
    )
    
    # Create chat session with the new SDK
    # Create chat session with the new SDK
    chat = client.chats.create(
        model="gemini-2.5-flash", 
        config={"system_instruction": system_instruction}
    )
    
    print("\n✅ Bot is ready! (Type 'exit' to quit)")
    print("-" * 40)
    
    is_first_message = True
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Goodbye!")
            break
            
        # Inject the context silently with the first prompt
        if is_first_message:
            prompt = f"{company_context}\nUser Question: {user_input}"
            is_first_message = False
        else:
            prompt = user_input
            
        try:
            response = chat.send_message(prompt)
            print(f"Bot: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_bot()