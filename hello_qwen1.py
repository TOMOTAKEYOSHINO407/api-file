import os
from openai import OpenAI


client = OpenAI(
    api_key="sk-6267c004c2ac41d69c098628660f41d0",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


def detect_end_conversation(user_input):
    end_phrases = ["结束", "再见", "拜拜", "谢谢", "不聊了"]
    return any(phrase in user_input for phrase in end_phrases)


def chat():
    conversation_history = [{'role': 'system', 'content': 'You are a helpful assistant.'}]

    while True:
        user_input = input("用户：")


        if detect_end_conversation(user_input):
            print("助理：感谢您的咨询，再见")
            break  # 检测到结束意图后自动退出


        conversation_history.append({'role': 'user', 'content': user_input})


        try:
            completion = client.chat.completions.create(
                model="qwen-plus",
                messages=conversation_history
            )
            assistant_reply = completion.choices[0].message.content
            print(f"助理：{assistant_reply}")


            conversation_history.append({'role': 'assistant', 'content': assistant_reply})

        except Exception as e:
            print(f"错误信息：{e}")
            print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")
            break
# 启动对话
chat()