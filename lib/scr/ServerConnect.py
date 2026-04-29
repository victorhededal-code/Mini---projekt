import json
import psycopg2
import os

def get_conn():
    return psycopg2.connect(
        dbname="defaultdb",
        user="avnadmin",
        password=os.getenv("PG_PASSWORD"),
        host="pg-4a73aa4-itek-thostrup.i.aivencloud.com",
        port=18539,
    )

def sync_characters_to_db(json_path):
    if not os.path.exists(json_path):
        print("No JSON file found to sync.")
        return

    with open(json_path, "r") as f:
        data = json.load(f)

    conn = get_conn()
    cur = conn.cursor()

    # Clear the old database table completely
    cur.execute("TRUNCATE TABLE public.class_info;")

    if isinstance(data, dict):
        data = [data]

    for character in data:
        name = character.get("Name")
        features = character.get("Class Features", [])
        features_text = "\n".join(features)

        cur.execute("""
            INSERT INTO public.class_info (class_name, class_resource)
            VALUES (%s, %s)
        """, (name, features_text))

    conn.commit()
    cur.close()
    conn.close()
    print("Database synced and old data replaced successfully.")

if __name__ == "__main__":
    sync_characters_to_db("characters.json")