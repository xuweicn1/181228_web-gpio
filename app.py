import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# 创建字典存储引脚号、引脚名称和状态

pins = {
   18 : {'name' : '信道1', 'state' : GPIO.LOW},
   23 : {'name' : '信道2', 'state' : GPIO.LOW},
   24 : {'name' : '信道3', 'state' : GPIO.LOW},
   25 : {'name' : '信道4', 'state' : GPIO.LOW}
   
   }


for pin in pins:
    '''设置每个引脚为输出,置低电平'''
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   '''读引脚状态发送到前端'''
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   templateData = {
      'pins' : pins
      }
   return render_template('home.html', **templateData)

@app.route("/<int:changePin>/<action>", methods=['GET', 'POST'])
def action(changePin, action):
    '''执行前端发来请求'''
    
    if action == "on":
        '''通电'''
        GPIO.output(changePin, GPIO.HIGH) 

    if action == "off": 
        '''断电'''
        GPIO.output(changePin, GPIO.LOW)

    for pin in pins:
        '''读引脚状态发送到网页'''
        pins[pin]['state'] = GPIO.input(pin)

    templateData = {
    'pins' : pins
    }

    return render_template('home.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)