import psycopg2
from flask import Flask


app=Flask(__name__)

def get_db_connection():
    conn=psycopg2.connect(host="localhost",
        database="student_db",
        user="shreyasrao",
        password="1234")
    return conn

@app.route("/users/")
def get_users():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM public.myuser")
            col_name = [desc[0] for desc in cur.description]
            values=cur.fetchall()
            res=[]
            for val in values:
                d={col_name[0]:val[0],
                   col_name[1]:val[1],
                   col_name[2]:val[2],
                   col_name[3]:val[3],
                   col_name[4]:val[4]}
                res.append(d)
    return res

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)