import gspread
from flask import Flask, request

 # 建立一個 Flask 伺服器的實體
app = Flask(__name__)
# 根據 credential (憑證) 檔案建立一個 google 服務帳號實體
sheet_account = gspread.service_account("./configs/sheet-api-credential.json")
# 使用 google 服務帳號實體打開試算表
work_book = sheet_account.open("2024專題資料庫")
# 使用 google 服務帳號實體打開試算表
sheet = work_book.worksheet("蝦趴")

@app.route('/', methods=['GET'])
def hello():
    return 'Hello'

# @app.route() 是 Flask 框架用來設定伺服器「路由 (route)」的修飾詞，是 Flask 框架規定的用法
# /sheet-test 代表 HTTP 請求打到這台伺服器後，如果指定的路徑是 "伺服器/sheet-test"
# 則這個請求會被分配到這個修飾詞下方的函式，也就是 sheet_test() 這個函式
# methods 參數指定了["GET", "POST"]，代表這個路由 (route) 接收 HTTP GET 與 POST 請求
@app.route("/sheet-test", methods=["GET", "POST"])
def sheet_test():
    # 請參考之前黑客松的程式碼，實作插入資料與讀取資料的功能
    # GET 請求照慣例是取得資料；POST 請求照慣例是新增資料，
    # 但是其實真正做什麼事還是伺服器的程式碼決定
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass

if __name__ == '__main__':
    app.run(debug=True)
