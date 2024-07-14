from flask import Flask,request, abort
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>我的第一個網站-修改目前網站</h1>"

@app.route("/pwd")
def pwd():
    return f'''
    <h2>{os.environ['CHANNEL_ACCESS_TOKEN']}</h2>
    <h2>{os.environ['CHANNEL_SECRET']}</h2>
    <h2>{os.environ['Gemini_API_KEY']}</h2>
    '''