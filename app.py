from email import message
from flask import Flask, redirect, render_template, request
from process import process
from time import sleep
from functions.get_country_code import get_country_code

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():

    if request.method=='POST':
        color = request.form['color']
        nft = request.form['nft']
        token_ID = request.form['token_ID']
        size = request.form['size']
        placement = request.form['placement']
        choice = request.form['submit_button']
        sleep(1)

        if(choice=="Get Mockup"):
            message = process(nft, token_ID, color, size,placement, choice, "")
            mockup_image = message[0]
            return render_template('index.html', mockup_image=mockup_image, choice=choice, color=color, size=size, placement=placement,token_ID=token_ID,nft=nft)

        elif(choice=="Place Order"):
            recipient = {
            "name": request.form['name'],
            "address1": request.form['address1'],
            "city": request.form['city'],
            "state": request.form['state'],
            "country_code": get_country_code(request.form['country_name']),
            "country_name": request.form['country_name'],
            "zip": request.form['zip']
            }

            message = process(nft, token_ID, color, size,placement, choice, recipient)
            return render_template('index.html', mockup_image=message[0], choice=choice, color=color, size=size, placement=placement,token_ID=token_ID,nft=nft,order_ID=message[1])

    else:
        choice = 'none'
        color=""
        token_ID=0
        placement=""
        size=""
        nft=""
        return render_template('index.html',message="none",choice=choice, color=color, size=size, placement=placement,token_ID=token_ID, nft=nft)

@app.route('/form',methods=['POST','GET'])
def get_form():
    return render_template('form.html')

if __name__ == "__main__":
    app.run(port=5000)
    app.run(debug=True)