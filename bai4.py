from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bai4')
def index():
        return render_template('bai4.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
