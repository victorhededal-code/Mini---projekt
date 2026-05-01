import json
import psycopg2
import os


def get_conn():
    return psycopg2.connect(
        dbname="defaultdb",
        user="avnadmin",
        password="AVNS_OS7k6IhujLNj9O7-AeD",
        host="pg-4a73aa4-itek-thostrup.i.aivencloud.com",
        port=18539,
    )

def ensure_json_file(path):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f)
        return

    # If file exists but is empty or broken, fix it
    with open(path, "r+", encoding="utf-8") as f:
        content = f.read().strip()

        if not content:
            f.seek(0)
            json.dump([], f)
            f.truncate()
            return

        try:
            json.loads(content)  # validate JSON
        except json.JSONDecodeError:
            f.seek(0)
            json.dump([], f)
            f.truncate()

def load_characters(json_path):

    ensure_json_file(json_path)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    sql = """
        INSERT INTO public.class_info2
        (
            pc_name,
            class_name,
            class_level,
            pc_race,
            pc_background,
            str,
            dex,
            con,
            intelligence,
            wis,
            cha,
            pc_code
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = [
        (
            c.get("Name"),
            c.get("Class"),
            c.get("Level"),
            c.get("Race"),
            c.get("Background"),
            c.get("Stats", {}).get("STR"),
            c.get("Stats", {}).get("DEX"),
            c.get("Stats", {}).get("CON"),
            c.get("Stats", {}).get("INT"),
            c.get("Stats", {}).get("WIS"),
            c.get("Stats", {}).get("CHA"),
            c.get("id"),
        )
        for c in data
    ]


    conn = get_conn()

    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany(sql, values)

        print("Characters imported successfully")

    finally:
        conn.close()


def export_character(json_path, character_id):
    conn = get_conn()

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT *
                    FROM public.class_info2
                    WHERE pc_code = %s
                """, (character_id,))

                row = cur.fetchone()

                if not row:
                    print("Character not found")
                    return

                # Get column names
                columns = [desc[0] for desc in cur.description]

                # Build dictionary dynamically
                character = dict(zip(columns, row))

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(character, f, indent=4, default=str)

        print("Character exported successfully")

    finally:
        conn.close()

if __name__ == "__main__":
    export_character(
        "upload_pc.json",
        "acd65821ce7f3494c080e3213d36dcf0a989086c"
    )