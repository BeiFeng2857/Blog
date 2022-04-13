import json

from flask import Flask, request
from flask import render_template
import pymysql

db_mysql = pymysql.connect(host='43.132.250.79', port=3306, user='root', password='8888', database='KOL')
cursor = db_mysql.cursor()
app = Flask(__name__)


@app.route('/index', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/kol', methods=["GET"])
def kol():
    return render_template('kol.html')


@app.route('/items', methods=['POST'])
def kol_items():
    # print(request.form)
    # print(request.data)
    search_key = request.data.decode()
    sql = 'select user_name, user_country, user_language, user_url, user_fans, user_view_mean,' \
          ' user_email from ytb_kol where search_key=%s limit 25'
    cursor.execute(sql, search_key)
    # cursor.execute(sql, 'game')
    items = cursor.fetchall()
    kol_list = []
    for item in items:
        dic = {
            'user_name': item[0],
            'user_country': item[1],
            'user_language': item[2],
            'channel_url': item[3],
            'fans': item[4],
            'view_mean': item[5],
            'email': item[6]
        }
        kol_list.append(dic)
    return json.dumps(kol_list)

if __name__ == '__main__':
    # kol_items()
    # app.run(host='0.0.0.0', port=51786, debug=True)
    app.run(host='127.0.0.1', port=51786, debug=True)
