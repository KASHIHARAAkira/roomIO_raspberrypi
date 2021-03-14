import RPi.GPIO as gpio
import time
import requests, json

pathURL = 'urlWebhook.txt'

with open(pathURL) as f:
    WEB_HOOK_URL = f.read()

BUTTON1_PIN = 17
BUTTON2_PIN = 4

def main():
    gpio.setmode(gpio.BCM)
    gpio.setup(BUTTON1_PIN, gpio.IN)
    gpio.setup(BUTTON2_PIN, gpio.IN)
    gpio.add_event_detect(BUTTON1_PIN, gpio.FALLING, callback=inRoom, bouncetime=300)
    gpio.add_event_detect(BUTTON2_PIN, gpio.FALLING, callback=outRoom, bouncetime=300)

    try:
        while(True):
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        gpio.cleanup()

def inRoom(channel):
    print("Button pushed is %s"%channel)
    requests.post(WEB_HOOK_URL, data = json.dumps({
        'text': u'Akira entered to LAB',
        'username': u'roomIO',
        'icon_emoji': u':penguin:',
        'link_names': 1,
    }))

def outRoom(channel):
    print("Button pushed is %s"%channel)
    requests.post(WEB_HOOK_URL, data = json.dumps({
        'text': u'Akira left from LAB',
        'username': u'roomIO',
        'icon_emoji': u':penguin:',
        'link_names': 1,
    }))

if __name__ == "__main__":
    main()
