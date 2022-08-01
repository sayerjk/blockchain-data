import json
from decimal import Decimal
import datetime
import psycopg2


class DecimalEncoder(json.JSONEncoder):
    """Converts Decimal() objects to string, allowing JSON storage"""
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def create_dictionary(labels, vals):
    results = {}
    for key, value in zip(labels, vals):
        results[key] = value
    return results


def query_near_testnet(sql_query: str) -> dict:
    """Query NEAR blockchain based on sql_query() string input"""
    # test NEAR Indexer database info
    conn = psycopg2.connect(host="35.184.214.98",
                            database="testnet_explorer",
                            user="public_readonly",
                            password="nearprotocol")
    cur = conn.cursor()
    cur.execute(sql_query)
    return cur.fetchall()


def export_json(data: list[dict]):
    now = datetime.datetime.now()
    timestamp = datetime.datetime.timestamp(now)
    with open(f'data/NEAR_{timestamp}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, cls=DecimalEncoder)
