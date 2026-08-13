from flask import Flask,render_template,request
import random
import secrets
import string

app=Flask(__name__,template_folder="Web",static_folder="Web")

def random_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    return "".join(random.choice(characters) for c in range(length))

def secure_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    return "".join(secrets.choice(characters) for c in range(length))

@app.route("/",methods=["GET","POST"])
def home():
    random_key=""
    secure_key=""
    length=10
    if request.method=="POST":

        length = int(request.form["length"])
        random_key=random_password(length)
        secure_key=secure_password(length)
    return render_template(("index.html"),random_key=random_key,secure_key=secure_key,length=length)

if __name__=="__main__":
    app.run(debug=True)
