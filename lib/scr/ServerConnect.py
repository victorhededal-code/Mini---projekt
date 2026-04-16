import psycopg2

SQL = "INSERT INTO public.class_info (class_id, class_name, class_resource) VALUES (%s,%s,%s);"

def get_conn():
    return psycopg2.connect(
        dbname="defaultdb",
        user="", #Brug individuelt brugernavn
        password="", #Brug individuelt password, skrevet i Discord
        host="pg-4a73aa4-itek-thostrup.i.aivencloud.com",
        port=18539,
    )
class_id = 1 #skal ændres til at opdatere/tælle op automatisk
class_name = "" #Måske ændres til at trække fra vores Dictionary?
class_resource = "" #Måske ændres til at trække fra vores Dictionary?
conn = get_conn()
curr = conn.cursor()
curr.execute(SQL, (class_id, class_name, class_resource))
conn.commit()
curr.close()
conn.close()
