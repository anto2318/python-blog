# import requests
# import json


# class WeChat:
#     def __init__(self):
#         self.APPID = "wx987a385b2456ae5d"
#         self.SECRET = "e332dbbf783906a52d12a96e4afcb005"
#         self.TOUSER = "anto2318859"

#     def get_access_token(self):
#         url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+self.APPID+"&secret="+self.SECRET
#         req = requests.get(url)
#         data = json.loads(req.text)
#         return data["access_token"]

#     def send_data(self, message):
#         access_token = self.get_access_token()
#         send_url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token="+access_token
#         send_values = {"touser":self.TOUSER,"msgtype":"text","text":{"content":message}}
#         send_msges=(bytes(json.dumps(send_values), "utf-8"))
#         response = requests.post(send_url, send_msges)
#         response = response.json()
#         print(response)
#         return response["errmsg"]


# if __name__ == "__main__":
#     wx = WeChat()
#     wx.send_data("This is the first message sent by the program!\n Python Program calling enterprise wechat API,Message sent to administrator from self built application alarm test application!")
#     wx.send_data("This is the second message sent by the program!")

from wxpy import *
bot = Bot(cache_path = True)
girl_friend = bot.search('Noah Wang')[0]

print(girl_friend)
@bot.register() 

# To receive a message from a designated friend, the sender is recv_msg.sender For designated friends girl_friend

def recv_send_msg(recv_msg):

    print('Message received:',recv_msg.text) # recv_msg.text Get text

    if recv_msg.sender == girl_friend:
        
        .forward(bot.file_helper,prefix='Wife message: ') #Keep a copy in the file transfer assistant to make it easier for you to check back when you are finished

    ms='My wife is the most beautiful. My love for my wife is like a flowing river'

    print('>>>Reply to my wife:', ms)

    return  ms#Give your wife one



embed()