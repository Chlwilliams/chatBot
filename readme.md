# Simple Chatbot using Llama3

## Description

This project demonstrates a simple chatbot powered by Llama3. Using a pre-trained Llama model, the chatbot generates responses for casual conversation, FAQs, or customer support. It uses **Streamlit** for the user interface, making it easy to interact with the bot.


## Getting Started

### Dependencies

To get started, ensure your system meets the following prerequisites:

- **Windows 10** 
- **Ollama3** - A platform to run Llama3 models, which can be downloaded from [Ollama.com](https://ollama.com/download).
- **Python** - Required to run the chatbot program and manage dependencies.
- Python libraries will be listed in `requirements.txt`, which will need to be installed via pip.

### Installing

1. **Download and Install Ollama3**: Visit the official [Ollama website](https://ollama.com/download) to download and install Ollama3.
2. **Create a Virtual Environment**:
   - Open a terminal and create a new virtual environment for the chatbot project by running:
     ```bash
     python -m venv chatbot
     ```
3. **Activate the Virtual Environment**:
   - On Windows, activate the environment by running:
     ```bash
     .\chatbot\Scripts\activate.ps1
     ```
   - After activation, your terminal should show the AI environment.
   ![example](./pictures/example.png)
4. **Install Required Libraries**:
   - With the virtual environment activated, install the necessary libraries by running:
     ```bash
     pip install -r requirements.txt
     ```

### Executing the Program

1. Ensure you are still in the AI virtual environment (indicated by the terminal).
2. To start the chatbot application, navigate to the project directory and run the following command:
   ```bash
   streamlit run main.py

   ## Authors

The chatbot project was developed by the following contributors:

- **Christian Williams** 

- **Christian Hernandez**  


Feel free to reach out to the authors for feedback or improvements!

