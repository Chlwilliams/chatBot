import streamlit as st


def main():
#makes userHistory & botHistory (if they don't exist) 
    if 'userHistory' not in st.session_state:
        st.session_state.userHistory = []

    if 'botHistory' not in st.session_state:
        st.session_state.botHistory = []

    
    st.title("Chat Bot App")

# grabs userInput & adds to history (if its != None)
    userInput = st.chat_input()
    if userInput:
        st.session_state.userHistory.append(userInput)
        print(userInput)

        userInputLower = userInput.lower()

#simple testing of bot responses
        if 'how are you doing' in userInputLower:
            st.session_state.botHistory.append("Im good thanks!")
        else:
            st.session_state.botHistory.append("I don't really get what you're trying to say. Please try again.")

#wwrites out history will remove try/except later (had for debugging purposes)
    try:
        if userInput:
            with st.expander("History"):
                for i in range(len(st.session_state.userHistory)):
                    st.write('User: "',st.session_state.userHistory[i],'"')
                    st.write('Bot: "',st.session_state.botHistory[i],'"')
    except:
        print(st.error(st.session_state.userHistory))
        print(st.error(st.session_state.botHistory))
    


if __name__ == "__main__":
    main()