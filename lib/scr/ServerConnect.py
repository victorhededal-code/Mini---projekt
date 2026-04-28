import json
import psycopg2
import os

def get_conn():
    return psycopg2.connect(
        dbname="defaultdb",
        user="avnadmin",
        password=os.getenv("AVNS_OS7k6IhujLNj9O7-AeD"),
        host="pg-4a73aa4-itek-thostrup.i.aivencloud.com",
        port=18539,
    )

def load_characters(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)

    conn = get_conn()
    cur = conn.cursor()

    # NOTE: your JSON is a single object, not a list
    if isinstance(data, dict):
        data = [data]

    for character in data:
        name = character.get("Name")
        features = character.get("Class Features", [])

        # convert list → string (safe for TEXT column)
        features_text = "\n".join(features)

        cur.execute("""
            INSERT INTO public.class_info (class_name, class_resource)
            VALUES (%s, %s)
        """, (name, features_text))

    conn.commit()
    cur.close()
    conn.close()

    print("Character imported successfully")