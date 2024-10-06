import requests
import psycopg2
response=requests.get("https://reqres.in/api/users?page=2")
data=response.json()["data"]

with (psycopg2.connect(
    dbname="student_db",
    user="shreyasrao",
    password="1234",
    host="localhost",
    port="5432"
)) as conn:
    with conn.cursor() as cur:
        for i in data:
            query=f'''INSERT INTO public.myuser ( first_name,last_name,email,avatar) 
            values ('{i["first_name"]}','{i["last_name"]}','{i["email"]}','{i["avatar"]}')'''
            cur.execute(query)
        conn.commit()
