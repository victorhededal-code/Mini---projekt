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


def load_characters(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.executemany(
                """
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
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                [
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
                ],
            )
        conn.commit()
    finally:
        conn.close()

    print("Characters imported successfully")



def export_character(json_path, character_id):
    conn = get_conn()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, class_name, class_resource
                    FROM public.class_info
                    WHERE id = %s
                """, (character_id,))

                row = cur.fetchone()

        if not row:
            print("Character not found")
            return

        char_id, name, features_text = row

        character = {
            "id": char_id,
            "Name": name,
            "Class Features": (
                features_text.strip().split("\n")
                if features_text else []
            )
        }

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(character, f, indent=4)

        print("Character exported successfully")

    finally:
        conn.close()


# Run import
load_characters("characters.json")