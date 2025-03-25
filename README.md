# Patent Text Summarization Script

This script is designed to process patent information from an Excel file, summarize specific text fields using the Azure OpenAI API, and save the summarized data back to an Excel file. It combines the Title, Abstract, Claims, and First Claim fields for each entry before summarization.

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or above
- pip (Python package manager)
- Access to the Azure OpenAI API

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/chitrakumarsai-inv/3rd-party-patent-genai-summarization.git
   cd https://github.com/chitrakumarsai-inv/3rd-party-patent-genai-summarization.git
   ```

2. **Install Required Python Packages**:
   Install the dependencies using the following command:
   ```bash
   pip install -r requirements.txt
   ```
   Ensure the `requirements.txt` file includes:
   ```
   openai
   pandas
   openpyxl
   python-dotenv
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory of the project.
   - Add the following variables to your `.env` file:
     ```
     OPENAI_KEY=<Your OpenAI API Key>
     OPENAI_DEPLOYMENT_NAME=<Your GPT-4 Deployment Name>
     OPENAI_ENDPOINT=<Your Azure OpenAI Endpoint>
     ```

## Usage

To execute the script, run:
```bash
python summarize.py
```
Replace `summarize.py` with the actual filename if different.

## Configuration

The script uses environment variables for configuration. Ensure your `.env` file is correctly set up with your Azure OpenAI API credentials:
- `OPENAI_KEY`: Your API key for Azure OpenAI.
- `OPENAI_DEPLOYMENT_NAME`: The name of your GPT-4 deployment in Azure.
- `OPENAI_ENDPOINT`: The endpoint URL for accessing Azure OpenAI services.

## Output

- **Input File**: Reads from `./data/raw_data/Intermediates ADN Alert - NLP-ML Experiment Feed_2025-03-23.xlsx`.
- **Output File**: Saves the summarized data to `summarized_output_adn.xlsx`.
- **Content**: The output file contains the original data with an additional column `Summarized_Text` for the summarized content.

---

By following these instructions, you should be able to run the script and obtain summarized patent information efficiently. For any issues or questions, please contact the script maintainer.
