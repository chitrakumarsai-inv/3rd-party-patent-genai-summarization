import openai
import pandas as pd
import os
import dotenv

dotenv.load_dotenv()
# Azure OpenAI setup
api_key = os.getenv("OPENAI_KEY")
deployment_name = os.getenv("OPENAI_DEPLOYMENT_NAME")  # Replace with your GPT-4 deployment name
azure_endpoint = os.getenv("OPENAI_ENDPOINT")  # Your Azure OpenAI endpoint

client = openai.AzureOpenAI(
    api_key=api_key,
    api_version="2023-12-01-preview",
    azure_endpoint=azure_endpoint,
)

def summarize_text(text, max_tokens=300):
    """ Function to summarize combined Title, Abstract, and Claims using Azure OpenAI """
    if not text or pd.isna(text) or text.strip() == "":
        return ""  # Handle empty text cases
    
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are an AI that summarizes text concisely. Do not introduce new information or assumptions."},
            {"role": "user", "content": f"Summarize the following combined patent information while keeping all key points:\n{text}"}
        ],
        max_tokens=max_tokens,
        temperature=0,   # Reduces hallucination
        top_p=0.1        # Ensures deterministic results
    )
    
    return response.choices[0].message.content.strip()

# Load dataset
df = pd.read_excel("./data/raw_data/Intermediates ADN Alert - NLP-ML Experiment Feed_2025-03-23.xlsx", engine="openpyxl", skiprows=1)  # Change to your actual file

# Summarize each column while keeping ID unchanged
# Combine Title, Abstract, and Claims
df["Combined_Text"] = df.apply(lambda row: f"Title: {row['Title (English)']}\nAbstract: {row['Abstract (English)']}\nClaims: {row['Claims (English)']}\nFirstClaims: {row['First Claim (English)']}", axis=1)
# Summarize combined text
df["Summarized_Text"] = df["Combined_Text"].apply(lambda x: summarize_text(x, max_tokens=300))

# # Keep only necessary columns
# df_summarized = df[["ID", "Summarized_Title", "Summarized_Abstract", "Summarized_Claims", "Target"]]

# Save the summarized dataset
df.to_excel("summarized_output_adn.xlsx", index=False)

print("Summarization completed and saved to summarized_output.csv")
