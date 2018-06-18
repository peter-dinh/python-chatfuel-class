import json
from flask import Flask
from class_chatfuel import Chatfuel
app = Flask(__name__)


@app.route('/')
def hello():
    return "Welcome to My Github!"


@app.route('/sendText/<text>')
def sendText(text):
    chatfuel = Chatfuel()
    chatfuel.sendText(text)
    return chatfuel.get_response()


@app.route('/sendImage/')
def sendImage():
    chatfuel = Chatfuel()
    url_image = ''
    chatfuel.sendImage(url_image)
    return chatfuel.get_response()


@app.route('/sendAudio/')
def sendAudio():
    chatfuel = Chatfuel()
    url_audio = ''
    chatfuel.sendAudio(url_audio)
    return chatfuel.get_response()


@app.route('/sendVideo/')
def sendVideo():
    chatfuel = Chatfuel()
    url_video = ''
    chatfuel.sendVideo(url_video)
    return chatfuel.get_response()


@app.route('/sendTextCard/ButtonToBlock')
def createButtonToBlock():
    chatfuel = Chatfuel()
    ButtonToBlock = chatfuel.createButtonToBlock(
        'Button To Block',
        ['#block_1', '#block_2'],
        {'setAttribute_1': 'value_1'}
    )
    chatfuel.sendTextCard('Clicking the button below!', [ButtonToBlock])
    return chatfuel.get_response()


@app.route('/sendTextCard/ButtonToURL')
def ButtonToURL():
    chatfuel = Chatfuel()
    ButtonToURL = chatfuel.createButtonToURL(
        'Button To URL',
        'url_website',
    )
    chatfuel.sendTextCard('Clicking the button below!', [ButtonToURL])
    return chatfuel.get_response()


@app.route('/sendTextCard/PostBackButton')
def PostBackButton():
    chatfuel = Chatfuel()
    PostBackButton = chatfuel.createPostBackButton(
        'Post Back Button',
        'url_plugin',
    )
    chatfuel.sendTextCard('Clicking the button below!', [PostBackButton])
    return chatfuel.get_response()


@app.route('/sendTextCard/CallButton')
def CallButton():
    chatfuel = Chatfuel()
    CallButton = chatfuel.createCallButton(
        'Call Button',
        'Phone_number', #example; +84919666666
    )
    chatfuel.sendTextCard('Clicking the button below!', [CallButton])
    return chatfuel.get_response()


@app.route('/sendGallery/')
def sendGallery():
    chatfuel = Chatfuel()
    elements = []
    #maximum 3 button
    button_access_url = chatfuel.createButtonToURL('Access Website', 'https://www.google.com.vn')
    button_call = chatfuel.createCallButton('+84919666666')
    button_share = chatfuel.createShareButton()
    title = 'Send Gallery'
    image_url = ''
    subTitle = 'subTitle Item'
    for i in range(5):
        elements.append(chatfuel.createElement(title, image_url, subTitle, [button_access_url, button_call, button_share]))
    chatfuel.sendGallery(elements)
    return chatfuel.get_response()


@app.route('/sendList/')
def sendList():
    #minimum 2 items in one List (Elements)
    #maximum 4 items in one List (Elements)
    chatfuel = Chatfuel()
    elements = []
    button_access_url = chatfuel.createButtonToURL('Access Website', 'https://www.google.com.vn')
    title = 'Send List'
    image_url = ''
    subTitle = 'subTitle Item'
    for i in range(2):
        elements.append(chatfuel.createElement(title, image_url, subTitle, [button_access_url]))
    chatfuel.sendList(elements)
    return chatfuel.get_response()


@app.route('/sendQuickReply/')
def sendQuickReply():
    chatfuel = Chatfuel()
    button_quick_replies_attributes = chatfuel.createButtonToBlock(
        'Send Quick Reply',
        ['#block_1'],
        {'setAttributes_1': 'value_1'},
    )
    button_quick_replies = chatfuel.createButtonToBlock('Title', ['#block_1'])
    chatfuel.sendQuickReply('Text', [button_quick_replies_attributes, button_quick_replies])
    return chatfuel.get_response()


@app.route('/redirectBlock/')
def redirectBlock():
    return json.dumps({"redirect_to_blocks": ["Welcome message", "Default answer"]})


if __name__ == '__main__':
    app.run()
