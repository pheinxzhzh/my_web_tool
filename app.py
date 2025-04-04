from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
latest_data = {'a': '--', 'b': '--', 'c': '--'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(latest_data)

@app.route('/update', methods=['POST'])
def update_data():
    global latest_data
    latest_data = request.get_json()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
