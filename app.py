from flask import Flask, render_template, redirect, url_for, request
import mlab
import conversationV1
from models.collection import Message



app = Flask(__name__)

mlab.connect()


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "GET":
        all_message = Message.objects()
        return render_template('index.html',all_message=all_message)
    elif request.method == "POST":
        form = request.form
        user_input = form['user_input']
        conversationV1.bot_response(user_input=user_input)
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=False)
