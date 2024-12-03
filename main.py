from streamlit_chat import message

from langchain_ollama import OllamaLLM


def updateHistory(userHistory, botHistory):
    if userHistory:
        for i in range(len(userHistory)):
            message(userHistory[i], is_user=True)
            message(botHistory[i]) 
            

def main():
    if 'userHistory' not in st.session_state:
        st.session_state.userHistory = []
    if 'botHistory' not in st.session_state:
        st.session_state.botHistory = []
    botOutput = ""


     
    with st.form(key="chat"):
        model = OllamaLLM(model="llama3")

        st.title("Chatbot :)")
        message("""Welcome to (CHRISTIAN) Team Chat bot. To stop using
                 this AI chat bot type quit""")
        
        

        userInput = st.text_input(" ")
        submit = st.form_submit_button("Submit")
        if submit:
            st.session_state.userHistory.append(userInput)
            try:
                botOutput = model.invoke(input=userInput)
                st.session_state.botHistory.append(botOutput)
            except:
                botOutput = "Something is wrong with my brian. Try again when I am fixed."
                st.session_state.botHistory.append(botOutput)
                

            updateHistory(st.session_state.userHistory, st.session_state.botHistory)




if __name__ == "__main__":
    main()

