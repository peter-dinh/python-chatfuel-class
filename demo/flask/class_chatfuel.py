from urllib.parse import urlparse
import json

class Chatfuel:
    CONST_VERSION = '2.0.1'

    response = []

    def __init__(self, debug = False):
        self.response = []


    def __del__(self,):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")


    def get_response(self):
        if len(self.response) > 0:
            try:
                print(json.dumps({'messages' : self.response}))
                return json.dumps({'messages' : self.response})
            except:
                raise


    def sendText(self, messages = None):
        if messages is None:
            raise ValueError('Invalid input message is null!')
        if isinstance(messages, str) or isinstance(messages, unicode):
            self.response.append({'text': messages})
        elif isinstance(messages, list):
            for message in messages:
                self.response.append({'text': messages})
        else:
            self.response.append({'text': 'Error!'})


    def sendImage(self, url_image):
        if self._isURL(url_image):
            self.createAttachment('image', {'url': url_image})
        else:
            self.sendText('Error: Invalid URL!')


    def sendVideo(self, url):
        if self._isURL(url):
            self.createAttachment('video', {'url': url})
        else:
            self.sendText('Error: Invalid URL!')


    def sendAudio(self, url):
        if self._isURL(url):
            self.createAttachment('audio', {'url': url})
        else:
            self.sendText('Error: Invalid URL!')


    def sendTextCard(self, text, buttons):
        for item in buttons:
            if item['type'] == 'element_share':
                raise ValueError("Text Card don't support Button Share!")
            self.createAttachment('template', {
                'template_type' : 'button',
                'text'          : text,
                'buttons'       : buttons
            })
            return True
        return False


    def sendGallery(self, elements):
        if isinstance(elements, list):
            self.createAttachment('template', {
                'template_type' : 'generic',
                "image_aspect_ratio": "square",
                'elements'      :  elements
            })
            return True
        return False


    def sendList(self, elements):
        if len(elements) > 4:
            raise ValueError('Maximum 4 items in Elements for List!')
        if len(elements) < 2:
            raise ValueError('Minimum 2 items in Elements for List!')
        if isinstance(elements, list):
            self.createAttachment('template', {
                'template_type' : 'list',
                'top_element_style' : 'large',
                'elements'      :  elements
            })
            return True
        return False


    def sendQuickReply(self, text, quickReplies):
        if isinstance(quickReplies, list):
            self.response.append({
                'text': text,
                'quick_replies': quickReplies
            })


    def createElement(self, title, image, subTitle, buttons):
        if self._isURL(image) and isinstance(buttons, list):
            return {
                'title'     : title,
                'image_url' : image,
                'subtitle'  : subTitle,
                'buttons'   : buttons
                }
        else:
            raise ValueError('Buttons are not List!')
        return False


    def createButtonToBlock(self, title, block, setAttributes = None):
        button = {}
        button['type'] = 'show_block'
        button['title'] = title
        if isinstance(block, list):
            button['block_names'] = block
        else:
            button['block_name'] = block
        if not isinstance(setAttributes, dict):
            raise ValueError('Attributes are not Dict!')
        if setAttributes and isinstance(setAttributes, dict):
            button['set_attributes'] = setAttributes
        return button


    def createButtonToURL(self, title, url):
        if self._isURL(url):
            button = {}
            button['type'] = 'web_url'
            button['url'] = url
            button['title'] = title
            return button
        return False


    def createPostBackButton(self, title, url_plugin):
        if self._isURL(url_plugin):
            return {
                    'url'   : url_plugin,
                    'type'  : 'json_plugin_url',
                    'title' : title
                }
        return False


    def createCallButton(self, title, phoneNumber):
        return {
                'type'         : 'phone_number',
                'phone_number' : phoneNumber,
                'title'        : title,
            }


    def _createShareButton(self):
        return {
                'type' : 'element_share'
            }


    def createAttachment(self, _type, payload):
        _type = _type.lower()
        list_type = ['image', 'video', 'audio', 'template']
        if _type in list_type:
            self.response.append({
                "attachment": {
                        "type"      : _type,
                        "payload"   : payload
                    }
                })
        else:
            self.response.append({'text':'Error: Invalid type!'})


    def _isURL(self, url):
        try:
            if not url:
                raise ValueError ('Not found url!')
            req = urlparse(url)
            if req.scheme == 'https' or req.scheme == 'http':
                return 1
            else:
                raise ValueError( url + ' Not url or url die!')
        except:
            raise
