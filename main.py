import openai
import os
from wxpy import Bot, TEXT, embed


# 定义一个Chat类，用于封装openai的ChatCompletion接口
class Chat:
  def __init__(self):
    # 设置openai的api密钥，从环境变量中获取
    openai.api_key = os.environ['OPENAI_API_KEY']

  def __call__(self, prompt):
    # 调用openai的ChatCompletion接口，传入用户的输入作为消息
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{
                                              "role": "user",
                                              "content": prompt
                                            }])
    # 获取返回结果中的回复内容
    content = response['choices'][0]['message']['content']
    # 在回复内容前加上【chatGPT】标识，并返回
    return '【chatGPT】' + content


chat = Chat()

# 创建一个Bot对象，用于登录微信并获取消息，
bot = Bot(cache_path=True, console_qr=True)


# 定义一个回复消息的函数，并注册处理接收的消息
@bot.register(msg_types=TEXT, except_self=False)
def reply_message(msg):
    # 判断消息中包含“小G小G”这个关键词
    if '小G小G' in msg.text:
        # 调用封装的Chat对象的生成回复，传入去掉“小G”的消息文本，得到回复文本并发送
        reply_text = chat(msg.text.replace('小G', ''))
        msg.reply(reply_text)


# 调用embed函数，进入交互式命令行界面
# embed()
bot.join()