"""Database functions"""

sql_schema = '''
CREATE TABLE IF NOT EXISTS logs (
    time TIMEASAMP,
    level VARCHAR(16),
    message TEXT
);

CREATE INDEX IF NOT EXISTS logs_time ON logs(time);
CREATE INDEX IF NOT EXISTS logs_level ON logs(level);
'''


def create_schema(conn):
    """Create logs schema in database"""
    cur = conn.cursor()
    try:
        cur.executescript(sql_schema)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
