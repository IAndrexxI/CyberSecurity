from flask import Flask, render_template, make_response, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        resp = make_response(render_template('index.html'))
        resp.set_cookie('credits', '10')
        return resp
    elif request.method == 'POST':
        cookie = request.cookies.get('credits')
        try:
            credits = int(cookie)
            game_choice = request.form.get('game', 'classic')

            if game_choice == 'premium':
                if credits >= 100:
                    resp = make_response(render_template('flag.html'))
                else:
                    print(f'[!] Insufficient credits = {credits}')
                    resp = make_response(render_template('insufficient.html', credits=credits))
            else:
                # Play classic game (always available)
                resp = make_response(render_template('classic.html'))

            return resp
        except (ValueError, TypeError):
            resp = make_response(render_template('error.html'))
            return resp


@app.route('/flag/')
def flag():
    return render_template('flag.html')


@app.route('/insufficient/')
def insufficient():
    cookie = request.cookies.get('credits', '0')
    try:
        credits = int(cookie)
    except (ValueError, TypeError):
        credits = 0
    return render_template('insufficient.html', credits=credits)


@app.route('/classic/')
def classic():
    return render_template('classic.html')
