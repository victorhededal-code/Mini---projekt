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

    # Ensure consistent structure
    if isinstance(data, dict):
        data = [data]
    elif not isinstance(data, list):
        raise ValueError("Invalid JSON format: expected dict or list")

    conn = get_conn()

    with conn:
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO public.class_info2 (class_name, class_resource)
                VALUES (%s, %s)
                """,
                [
                    (character.get("Name"), "TEST")
                    for character in data
                ],
            )

    print("Character imported successfully")


def export_characters(json_path):
    conn = get_conn()

    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT class_name, class_resource
                FROM public.class_info
            """)

            rows = cur.fetchall()

    data = []

    for name, features_text in rows:
        character = {
            "Name": name,
            "Class Features": features_text.split("\n") if features_text else []
        }
        data.append(character)

    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)

    print("Characters exported successfully")


# Run import
load_characters("characters.json")