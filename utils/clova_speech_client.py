import requests
import json
import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

class ClovaSpeechClient:

    secret = os.getenv("CLOVASPEECH_API_KEY")
    if not secret:
        print("Error: CLOVASPEECH_API_KEY is not set in environment variables.")

    invoke_url = os.getenv("CLOVASPEECH_INVOKE_URL")
    if not invoke_url:
        print("Error: CLOVASPEECH_INVOKE_URL is not set in environment variables.")

    def req_url(self, url, completion, callback=None, userdata=None, \
    	forbiddens=None, boostings=None, wordAlignment=True, \
        	fullText=True, diarization=None, sed=None):
        request_body = {
            'url': url,
            'language': 'ko-KR',
            'completion': completion,
            'callback': callback,
            'userdata': userdata,
            'wordAlignment': wordAlignment,
            'fullText': fullText,
            'forbiddens': forbiddens,
            'boostings': boostings,
            'diarization': diarization,
            'sed': sed,
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'Content-Type': 'application/json;UTF-8',
            'X-CLOVASPEECH-API-KEY': self.secret
        }
        return requests.post(headers=headers,
                             url=self.invoke_url + '/recognizer/url',
                             data=json.dumps(request_body).encode('UTF-8'))

    def req_object_storage(self, data_key, completion, callback=None, \
    	userdata=None, forbiddens=None, boostings=None,wordAlignment=True, \
        	fullText=True, diarization=None, sed=None):
        request_body = {
            'dataKey': data_key,
            'language': 'ko-KR',
            'completion': completion,
            'callback': callback,
            'userdata': userdata,
            'wordAlignment': wordAlignment,
            'fullText': fullText,
            'forbiddens': forbiddens,
            'boostings': boostings,
            'diarization': diarization,
            'sed': sed,
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'Content-Type': 'application/json;UTF-8',
            'X-CLOVASPEECH-API-KEY': self.secret
        }
        return requests.post(headers=headers,
                             url=self.invoke_url + '/recognizer/object-storage',
                             data=json.dumps(request_body).encode('UTF-8'))

    def req_upload(self, input_audio_path, completion, callback=None, userdata=None, 
    	forbiddens=None, boostings=None, wordAlignment=True,
        	fullText=True, diarization={'enable':False}, sed=None):
        request_body = {
            'language': 'ko-KR',
            'completion': completion,
            'callback': callback,
            'userdata': userdata,
            'wordAlignment': wordAlignment,
            'fullText': fullText,
            'forbiddens': forbiddens,
            'boostings': boostings,
            'diarization': diarization,
            'sed': sed,
        }
        headers = {
            'Accept': 'application/json;UTF-8',
            'X-CLOVASPEECH-API-KEY': self.secret
        }
        print(json.dumps(request_body, ensure_ascii=False).encode('UTF-8'))
        files = {
            'media': open(input_audio_path, 'rb'),
            'params': (None, json.dumps(request_body, \
            			ensure_ascii=False).encode('UTF-8'), \
                        		'application/json')
        }
        response = requests.post(headers=headers, url=self.invoke_url \
        			+ '/recognizer/upload', files=files)
        return response
