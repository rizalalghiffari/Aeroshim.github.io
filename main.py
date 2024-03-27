from flask import Flask, render_template, request

app = Flask(__name__)

def mm_to_inches(mm):
    return mm / 25.4

def calculate_clearance(x, t, u):
    p = 2.277 - (x - t + u)
    return p

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        x = float(request.form['x'])
        t = float(request.form['t'])
        u = float(request.form['u'])
        unit = request.form['unit']

        if unit == 'mm':
            x = mm_to_inches(x)
            t = mm_to_inches(t)
            u = mm_to_inches(u)

        p = calculate_clearance(x, t, u)
        return render_template('index.html', result=p)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
