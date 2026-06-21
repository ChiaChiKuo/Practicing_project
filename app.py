# 匯入 Flask 套件
from flask import Flask, render_template

# 建立 Flask 應用程式
app = Flask(__name__)

# 當使用者進入首頁("/")時，執行這個函式
@app.route('/')
def index():
    return render_template('index.html')
# 啟動伺服器
if __name__ == "__main__":
    # debug=True 代表開發模式
    # 程式修改後會自動重新啟動
    app.run(debug=True)