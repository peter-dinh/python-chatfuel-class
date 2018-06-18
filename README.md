# class-chatfuel-python

## Descrpition: Python Wrapper for JSON API Chatfuel

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


## Usage


## Author: Peter Dinh
