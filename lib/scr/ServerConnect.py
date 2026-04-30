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
    # Load JSOl
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Ensure list format
    if isinstance(data, dict):
        data = [data]

    # Prepare SQL (11 columns → 11 placeholders)
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
            cha
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Build values correctly (MUST match placeholders exactly)
    values = [
        (
            character.get("Name"),
            character.get("Class"),
            character.get("Level"),
            character.get("Race"),
            character.get("Background"),
            character.get("Stats", {}).get("STR"),
            character.get("Stats", {}).get("DEX"),
            character.get("Stats", {}).get("CON"),
            character.get("Stats", {}).get("INT"),
            character.get("Stats", {}).get("WIS"),
            character.get("Stats", {}).get("CHA"),
        )
        for character in data
    ]

    # DB connection (safe)
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