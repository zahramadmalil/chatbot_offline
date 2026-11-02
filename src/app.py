
import streamlit as st
import utils

# prompt = st.chat_input('Enter your prompt')
# if prompt:
#     st.write(f'prompt: {prompt}')

# st.chat_message('ai').write('How can I help you')
# st.chat_message('user').write('tell me about food')
# #role --> ai / user
# #content --> message

# st.write(st.session_state)
# if 'count' not in st.session_state:
#     st.session_state['count']=0

# #count = 0

# if st.button('ADD'):
#     st.session_state['count'] = st.session_state['count'] + 1 
#     st.write(f'count: {st.session_state['count']}')

# import time
# with st.spinner('Generating...'):
#     time.sleep(3)

st.title('STREAMLIT CHATBOT')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role':'ai', 'content':'How Can I Help You?'}]

for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

prompt = st.chat_input('Enter Your Question')
model = 'gemma3:1b'
if prompt:

    new_prompt = prompt + 'Describe your answer with detail and images'
    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role':'user', 'content':prompt})

    with st.spinner('Generating Response...'):
        response = utils.call_ollama_model(new_prompt, model)

    st.chat_message('ai').write(response)
    st.session_state['messages'].append({'role':'ai', 'content':response})

