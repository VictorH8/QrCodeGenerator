from flask import Flask, render_template, request
import qrcode
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    img_path = None
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    
    if request.method == 'POST':
        texto = request.form['qrcodetext']
        img = qrcode.make(texto)

        img_path = f"qrcodes/qrcode.png"
        img.save(f"static/{img_path}")

    return render_template("index.html", img_path=img_path)

if __name__ == "__main__":
    app.run(debug=True)
