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
            cha,
            pc_code
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
            character.get("id"),
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
                    SELECT
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
                    FROM public.class_info2
                    WHERE id = %s
                """, (character_id,))

                row = cur.fetchone()

        if not row:
            print("Character not found")
            return

        (
            name,
            class_name,
            level,
            race,
            background,
            str_val,
            dex,
            con,
            intelligence,
            wis,
            cha,
            pc_code
        ) = row

        character = {
            "Name": name or "",
            "Class": class_name,
            "Level": level,
            "Race": race,
            "Background": background or "None",
            "Stats": {
                "STR": str_val,
                "DEX": dex,
                "CON": con,
                "INT": intelligence,
                "WIS": wis,
                "CHA": cha
            },
            "id": pc_code
        }

        with open("upload_pc", "w", encoding="utf-8") as f:
            json.dump([character], f, indent=4)

        print("Character exported successfully")

    finally:
        conn.close()


# Run import
if __name__ == "__main__":
    load_characters("characters.json")