import requests
import json
import re


def call_ollama_model(prompt, model, stream=False):
    """
    ارسال پرامپت به مدل Ollama و دریافت پاسخ.
    """
    url = 'http://localhost:11434/api/generate'

    params = {
        'prompt': prompt,
        'model': model,
        'stream': stream
    }
    payload = json.dumps(params)

    try:
        response = requests.post(
            url,
            data=payload,
            headers={'Content-Type': 'application/json'},
            timeout=900  # برای مدل‌های کند، تایم‌اوت بیشتر
        )
    except requests.exceptions.ConnectionError:
        return "❌ خطا: نمی‌توان به Ollama متصل شد. مطمئن شوید Ollama اجرا می‌شود (ollama serve)."

    if response.status_code != 200:
        return f'❌ خطا ({response.status_code}): {response.text}'
    else:
        return response.json()['response']


def save_chat_to_file(messages, filepath='chat_history.txt'):
    """
    ذخیره کامل چت در یک فایل متنی.
    هر پیام به صورت:  [ROLE] content
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("تاریخچه کامل چت\n")
        f.write("=" * 60 + "\n\n")
        for msg in messages:
            role = msg['role'].upper()
            content = msg['content']
            f.write(f"[{role}]\n{content}\n")
            f.write("-" * 60 + "\n")
    return filepath


def summarize_chat(messages, model):
    """
    خلاصه‌سازی کل چت با یک پرامپت بهینه.
    """
    # ساخت متن یکپارچه از کل مکالمه
    conversation_text = ""
    for msg in messages:
        role = "کاربر" if msg['role'] == 'user' else "دستیار"
        conversation_text += f"{role}: {msg['content']}\n\n"

    # پرامپت بهینه برای خلاصه‌سازی
    summary_prompt = f"""You are an expert at summarizing conversations.

Please read the following conversation between a user and an AI assistant, and write a clear, concise summary in Persian (فارسی).

Rules:
- Summarize the main topics discussed.
- Mention the key questions asked by the user.
- Mention the key answers/information provided by the assistant.
- Use bullet points for readability.
- Do NOT add information that is not in the conversation.
- Keep it under 300 words.

Conversation:
----------------------
{conversation_text}
----------------------

Summary (in Persian):"""

    return call_ollama_model(summary_prompt, model)


def save_summary_to_file(summary_text, filepath='chat_summary.txt'):
    """
    ذخیره خلاصه در فایل جدید.
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("خلاصه چت (تولید شده توسط هوش مصنوعی)\n")
        f.write("=" * 60 + "\n\n")
        f.write(summary_text)
    return filepath


######################################
if __name__ == '__main__':
    model = 'gemma3:1b'
    prompt = input('Enter your Question: ')
    response = call_ollama_model(prompt, model)
    print(f'result:\n{response}')