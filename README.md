# WeChatGPT

## Install and run
```
git clone https://github.com/PengZiqiao/WeChatGPT.git

pip install openai wxpy pillow

cd ./WeChatGPT/

python main.py
```

## How to use
* 首先在添加环境变量OPENAI_API_KEY，填写你的openai api key
* 运行后，控制台会出现二维码。
* 用微信扫码登录后，只要有消息含小G小G，就会触发chatGPT自动回复

## TODO
* 实现多轮会话
* 只需在开始输入触发词，后续无再输入小G小G
* 解决重新登录后，重复回复之前消息的问题
