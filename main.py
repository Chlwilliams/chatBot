import streamlit as st

from streamlit_chat import message
from langchain_ollama import OllamaLLM


def updateHistory(userHistory, botHistory):
    if userHistory:
        for i in range(len(userHistory)):
            message(userHistory[i], is_user=True)
            message(botHistory[i]) 
            

def main():
    # Establishes storages if they do not already exist
    if 'userHistory' not in st.session_state:
        st.session_state.userHistory = []
    if 'botHistory' not in st.session_state:
        st.session_state.botHistory = []
    if 'botMemory'  not in st.session_state:
        st.session_state.botMemory = {"Memory of UserInput" : "Memory of botOutput"}
    


    # form / model name
    with st.form(key="chat"):
        model = OllamaLLM(model="llama3")
    # intial prompt to user
        st.title("Chatbot :)")
        message("Welcome! You've reached our friendly AI Chatbot! I'm thrilled to assist you with any questions, or with some fun conversations. What brings you hear today?")

    # user input
        userInput = st.text_input(" ")
        submit = st.form_submit_button("Submit")
    # memory prompt
        memories = ""
        for x, y in st.session_state.botMemory.items():  
            memories += f"{x}: {y}\n"  
            
        prompt = f"""The bot should only respond to message after 'New Message:'
        Everything before that will be for the bot's memory, memory will be stored like 'userinput:botinput'
        Do not mention memory.
        Memory: {memories}
        New Message: {userInput} """

        # st.write(prompt)- for memory testing

    # submits input : updates memory / chat history
        if submit:
            st.session_state.userHistory.append(userInput)
            
            try:
                botOutput = model.invoke(input=prompt)
                st.session_state.botHistory.append(botOutput)

            except:
                botOutput = "Something is wrong with my brian. Try again when I am fixed."
                st.session_state.botHistory.append(botOutput)
            
            st.session_state.botMemory[userInput] = botOutput
                

            updateHistory(st.session_state.userHistory, st.session_state.botHistory)


if __name__ == "__main__":
    main()

