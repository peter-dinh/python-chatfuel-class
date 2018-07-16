# python-chatfuel-class

## Descrpition: Python Wrapper for JSON API Chatfuel
##### This project was inspired by [php-chatfuel-class](https://github.com/J2TEAM/php-chatfuel-class)

## Functions List:
* Send Text:
```python
def sendText(self, messages = None)
```
* Send Image
```python
def sendImage(self, url_image)
```
* Send Audio
```python
def sendAudio(self, url):
```
* Send Video
```python
def sendVideo(self, url)
```
* Send Text Card
```python
def sendTextCard(self, text, buttons)
```
* Send Gallery
```python
def sendGallery(self, elements)
```
* Send List
```python
def sendList(self, elements)
```
* Send Quick Reply
```python
def sendQuickReply(self, text, quickReplies)
```
* Create Element
```python
def createElement(self, title, image, subTitle, buttons)
```

* Create Button To Block
```python
def createButtonToBlock(self, title, block, setAttributes = None)
```
* Create Button To URL
```python
def createButtonToURL(self, title, url)
```
* Create PostBack Button
```python
def createPostBackButton(self, title, url_plugin)
```
* Create Call Button
```python
def createCallButton(self, title, phoneNumber)
```
* Create Share Button
```python
def _createShareButton(self)
```
* Create Attachment
```python
def createAttachment(self, _type, payload)
```

### You can see the code at here [class_chatfuel.py](class-chatfuel-python/class-cchatfuel.py)

## Installation

##### For python 2x
```shell
pip install python_chatfuel_class
```

##### For python 3x
```shell
pip3 install python_chatfuel_class
```

## Usage
* Send Text:
```python
@app.route('/sendText/<text>')
def sendText(text):
    chatfuel = Chatfuel()
    chatfuel.sendText(text)
    return chatfuel.get_response()
```
![send-text](https://peter-dinh.github.io/python-chatfuel-class/img/sendText.png)

* Send Image:
```python
@app.route('/sendImage/')
def sendImage():
    chatfuel = Chatfuel()
    url_image = ''
    chatfuel.sendImage(url_image)
    return chatfuel.get_response()
```
![send-Image](https://peter-dinh.github.io/python-chatfuel-class/img/sendImage.png)

* Send Audio:
```python
@app.route('/sendAudio/')
def sendAudio():
    chatfuel = Chatfuel()
    url_audio = ''
    chatfuel.sendAudio(url_audio)
    return chatfuel.get_response()
```
![send-Audio](https://peter-dinh.github.io/python-chatfuel-class/img/sendAudio.png)

* Send Video:
```python
@app.route('/sendVideo/')
def sendVideo():
    chatfuel = Chatfuel()
    url_video = ''
    chatfuel.sendVideo(url_video)
    return chatfuel.get_response()
```
![send-Video](https://peter-dinh.github.io/python-chatfuel-class/img/sendVideo.png)

* Send Button to Block:
```python
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
```
![Button to Block](https://peter-dinh.github.io/python-chatfuel-class/img/buttontoBlock.png)

* Send Button to URL:
```python
@app.route('/sendTextCard/ButtonToURL')
def ButtonToURL():
    chatfuel = Chatfuel()
    ButtonToURL = chatfuel.createButtonToURL(
        'Button To URL',
        'url_website',
    )
    chatfuel.sendTextCard('Clicking the button below!', [ButtonToURL])
    return chatfuel.get_response()
```
![Button To URL](https://peter-dinh.github.io/python-chatfuel-class/img/buttontoURL.png)

* Send Button Post Back:
```python
@app.route('/sendTextCard/PostBackButton')
def PostBackButton():
    chatfuel = Chatfuel()
    PostBackButton = chatfuel.createPostBackButton(
        'Post Back Button',
        'url_plugin',
    )
    chatfuel.sendTextCard('Clicking the button below!', [PostBackButton])
    return chatfuel.get_response()
```
![PostBack Button](https://peter-dinh.github.io/python-chatfuel-class/img/buttontopostback.png)

* Send Button Call:
```python
@app.route('/sendTextCard/CallButton')
def CallButton():
    chatfuel = Chatfuel()
    CallButton = chatfuel.createCallButton(
        'Call Button',
        'Phone_number', #example; +84919666666
    )
    chatfuel.sendTextCard('Clicking the button below!', [CallButton])
    return chatfuel.get_response()
```
![Call Button](https://peter-dinh.github.io/python-chatfuel-class/img/buttoncall.png)

* Send Gallery:
```python
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
```
![send-Gallery](https://peter-dinh.github.io/python-chatfuel-class/img/gallery.png)

* Send List:
```python
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

```
![send-List](https://peter-dinh.github.io/python-chatfuel-class/img/sendList.png)

* Send Quick Reply:
```python
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
```
![send-Quick-Reply](https://peter-dinh.github.io/python-chatfuel-class/img/quickreply.png)

* Redirect Block
```python
@app.route('/redirectBlock/')
def redirectBlock():
    return json.dumps({"redirect_to_blocks": ["Welcome message", "Default answer"]})
```
![Redirect Block](https://peter-dinh.github.io/python-chatfuel-class/img/redirectblock.png)


## Demo:
* [BotChat VietNam](https://m.me/2059865890937967)

* [Peter Dinh](https://m.me/bot.peter.com.vn)

## Author: Peter Dinh
