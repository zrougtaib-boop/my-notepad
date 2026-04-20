from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
data_store = {"note": "مرحباً بك في دفترك الرسمي يا الطيب!"}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>S-Class Notepad</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; background: #1a1a1a; color: white; text-align: center; padding: 20px; }
        textarea { width: 90%; height: 300px; background: #333; color: #00ff00; padding: 15px; border-radius: 10px; border: 2px solid #555; font-size: 16px; }
        input[type="submit"] { background: #ffcc00; color: black; padding: 15px 30px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; margin-top: 10px; font-size: 18px; }
    </style>
</head>
<body>
    <h2>🚀 دفتر ملاحضات الطيب الرسمي 🚀</h2>
    <form method="POST">
        <textarea name="my_note">{{ current_note }}</textarea><br>
        <input type="submit" value="حـفـظ فـي الـ سـحـاب">
    </form>
    <p style="color: #888;">هذا الموقع يشتغل 24 ساعة بفضل تعب الطيب</p>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data_store['note'] = request.form['my_note']
    return render_template_string(HTML, current_note=data_store['note'])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

