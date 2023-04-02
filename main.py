from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

menu = [{"title": "Main", "url": "/"},
        {"title": "Add", "url": "/add_post"}]

@app.route('/', methods=['GET', 'POST'])


def upload():
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_csv(file)
        df = df.head()
        return render_template('table.html', table=df.to_html())
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000, host="127.0.0.1")
