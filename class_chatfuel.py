import json
#import request

class Chatfuel:
    CONST_VERSION = '1.0.0.1'
    
    response = []
    
    def __init__(self, debug = False):
        self.response = []
            
    def __del__(self,):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

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
        if self.isURL(url_image):
            self.sendAttachment('image', {'url': url_image})
        else:
            self.sendText('Error: Invalid URL!')
    
    def sendVideo(self, url):
        if self.isURL(url):
            self.sendAttachment('video', {'url': url})
        else:
            self.sendText('Error: Invalid URL!')
            
    def sendAudio(self, url):
        if self.isURL(url):
            self.sendAttachment('audio', {'url': url})
        else:
            self.sendText('Error: Invalid URL!')
    
    def sendTextCard(self, text, buttons):
        if isinstance(buttons, list):
            self.sendAttachment('template', {
                'template_type' : 'button',
                'text'          : text,
                'buttons'       : buttons
            })
            return True
        return False

    def sendGallery(self, elements):
        if isinstance(elements, list):
            self.sendAttachment('template', {
                'template_type' : 'generic',
                "image_aspect_ratio": "square",
                'elements'      :  elements
            })
            return True
        return False


    def sendList(self, elements):
        if isinstance(elements, list):
            self.sendAttachment('template', {
                'template_type' : 'list',
                'top_element_style' : 'large',
                'elements'      :  elements
            })
            return True
        return False


    def createElement(self, title, image, subTitle, buttons):
        if self.isURL(image) and isinstance(buttons, list):
            return {
                'title'     : title,
                'image_url' : image,
                'subtitle'  : subTitle,
                'buttons'   : buttons
                }
        return False
    
    
    def createButtonToBlock(self, title, block, setAttributes = None):
        button = {}
        button['type'] = 'show_block'
        button['title'] = title

        if isinstance(block, list):
            button['block_names'] = block
        else:
            button['block_name'] = block

        if not setAttributes and isinstance(setAttributes, list):
            button['set_attributes'] = setAttributes
        return button

    def createButtonToURL(self, title, url, setAttributes = None):
        if self.isURL(url):
            button = {}
            button['type'] = 'web_url'
            button['url'] = url
            button['title'] = title

            if isinstance(setAttributes, list) and not setAttributes:
                button['set_attributes'] = setAttributes
            return button
        return False


    def createPostBackButton(self, title, url):
        if self.isURL(url):
            return {
                    'url'   : url,
                    'type'  : 'json_plugin_url',
                    'title' : title
                }
        return False


    def createCallButton(self, phoneNumber, title = 'Call'):
        return {
                'type'         : 'phone_number',
                'phone_number' : phoneNumber,
                'title'        : title,
            }

    def createShareButton(self):
        return {
                'type' : 'element_share'
            }

    def sendQuickReply(self, text, quickReplies):
        if isinstance(quickReplies, list):
            self.response.append({
                'text': text,
                'quick_replies': quickReplies
            })
            
    def createButtonQuickReplysetAttributes(self, title, block, attribute):
        if isinstance(block, list) and isinstance(attribute, dict):
            return {
                  "set_attributes": attribute,
                  "block_names": block,
                  "type": "show_block",
                  "title": title
                }
        
        
    def createQuickReplyButton(self, title, block):
        button = {}
        button['title'] = title

        if isinstance(block, list):
            button['block_names'] = block
        
        return button
        

    def sendAttachment(self, _type, payload):
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


    def isURL(self, url):
        return 1