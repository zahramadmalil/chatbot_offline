import streamlit as st
import utils

st.set_page_config(page_title="Chatbot Offline", page_icon="🤖")
st.title('🤖 STREAMLIT CHATBOT (Offline with Ollama)')

MODEL = 'gemma3:1b'

# ---------- مقداردهی اولیه session_state ----------

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {'role': 'ai', 'content': 'How Can I Help You?'}
    ]

# پرچم توقف مدل
if 'stop_requested' not in st.session_state:
    st.session_state['stop_requested'] = False

# ---------- دکمه‌های کنترل (قسمت اول تمرین) ----------
col1, col2 = st.columns(2)

with col1:
    if st.button('⏹️ توقف مدل', use_container_width=True):
        st.session_state['stop_requested'] = True
        st.warning('درخواست توقف ثبت شد. اگر مدل در حال تولید پاسخ است، پس از پایان این نوبت متوقف می‌شود.')

with col2:
    if st.button('🗑️ پاک کردن تاریخچه', use_container_width=True):
        st.session_state['messages'] = [
            {'role': 'ai', 'content': 'How Can I Help You?'}
        ]
        st.session_state['stop_requested'] = False
        st.success('تاریخچه چت پاک شد.')
        st.rerun()

st.divider()

# ---------- نمایش چت ----------
for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

# ---------- ورودی کاربر ----------
prompt = st.chat_input('Enter Your Question')

if prompt:
    # اگر کاربر دکمه توقف را زده بود، از ادامه جلوگیری کن
    if st.session_state['stop_requested']:
        st.info('مدل متوقف شده است. برای ادامه، دکمه توقف را ریست کنید یا صفحه را رفرش کنید.')
        st.session_state['stop_requested'] = False
    else:
        new_prompt = prompt + ' Describe your answer with detail and images'
        st.chat_message('user').write(prompt)
        st.session_state['messages'].append({'role': 'user', 'content': prompt})

        with st.spinner('Generating Response...'):
            response = utils.call_ollama_model(new_prompt, MODEL)

        st.chat_message('ai').write(response)
        st.session_state['messages'].append({'role': 'ai', 'content': response})

st.divider()

# ---------- بخش ذخیره و خلاصه‌سازی (قسمت دوم تمرین) ----------
st.subheader('💾 ذخیره و خلاصه‌سازی چت')

col_a, col_b = st.columns(2)

with col_a:
    if st.button('📥 ذخیره کل چت در فایل', use_container_width=True):
        if len(st.session_state['messages']) <= 1:
            st.warning('چت خالی است! اول چند پیام بفرستید.')
        else:
            path = utils.save_chat_to_file(st.session_state['messages'])
            with open(path, 'rb') as f:
                st.download_button(
                    label='⬇️ دانلود فایل چت',
                    data=f,
                    file_name=path,
                    mime='text/plain',
                    use_container_width=True
                )
            st.success(f'چت در فایل «{path}» ذخیره شد.')

with col_b:
    if st.button('📝 خلاصه‌سازی چت با AI', use_container_width=True):
        if len(st.session_state['messages']) <= 1:
            st.warning('چت خالی است! اول چند پیام بفرستید.')
        else:
            with st.spinner('در حال خلاصه‌سازی توسط مدل...'):
                summary = utils.summarize_chat(st.session_state['messages'], MODEL)
                path = utils.save_summary_to_file(summary)

            st.success(f'خلاصه در فایل «{path}» ذخیره شد.')
            st.text_area('📋 خلاصه تولید شده:', summary, height=250)

            with open(path, 'rb') as f:
                st.download_button(
                    label='⬇️ دانلود فایل خلاصه',
                    data=f,
                    file_name=path,
                    mime='text/plain',
                    use_container_width=True
                )

# ---------- نمایش وضعیت در Sidebar ----------
with st.sidebar:
    st.header('ℹ️ وضعیت')
    st.write(f'**مدل:** `{MODEL}`')
    st.write(f'**تعداد پیام‌ها:** {len(st.session_state["messages"])}')
    st.write(f'**وضعیت توقف:** {"متوقف" if st.session_state["stop_requested"] else "آماده"}')