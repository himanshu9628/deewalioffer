
import requests,json

import sqlite3
def get_data(*li):
    da = {}
    data = requests.get('https://appsdetails.herokuapp.com/appdata')
    tmp = json.loads(data.text)

    for i in li[0]:
        try:
            da[i] = tmp.get(i).get('category')
        except:
            da[i] = "Not Available"

    return da 



def get_db_connection():
    conn = sqlite3.connect('working.db')
    # conn.row_factory = sqlite3.Row
    conn.execute("create table IF NOT EXISTS packageId (PackageId TEXT PRIMARY KEY)")
    conn.execute("create table IF NOT EXISTS checkedid (PackageId TEXT PRIMARY KEY, status TEXT)")
    conn.execute("create table IF NOT EXISTS Issue (PackageId TEXT PRIMARY KEY, Issue TEXT)")

    return conn



def get_issue_data(*li):
    db = get_db_data()
    d2 = {}
    for i in li[0]:
        if db.get(i):
            d2[i] = db.get(i)
        else:
            d2[i] = "No Issue"

    return d2





def get_db_data():
    con = get_db_connection()
    # con.execute("create table IF NOT EXISTS Issue (PackageId TEXT PRIMARY KEY, Issue TEXT)")
    query = "SELECT * FROM Issue"
    print(query)
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    dic = {}
    for  row in rows:
        dic[row[0]] = row[1]
    return dic

# li=['862390640','com.mosaicwellness.manmatters','com.squats.fittr','1078997450','com.carshering']

# print(get_issue_data(li))
