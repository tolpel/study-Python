from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User値を設定:' + session['user']


@app.route('/getuser')
def getuser() -> str:
    return 'ログインしていません。' + session['user']


if __name__ == '__main__':
    app.run(debug=True)
