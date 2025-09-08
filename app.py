from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# حالة التحكم (تشغيل/إيقاف)
bot_status = {'active': False}

@app.route('/')
def index():
    return render_template('index.html', status=bot_status['active'])

@app.route('/toggle', methods=['POST'])
def toggle():
    bot_status['active'] = not bot_status['active']
    return jsonify({'status': bot_status['active']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
