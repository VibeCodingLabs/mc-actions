import os
import aiosqlite
from dotenv import load_dotenv

load_dotenv(override=True)

SQLITE_PATH = os.getenv("SQLITE_PATH", "/var/lib/moonclaw/jobs.db")

CREATE_JOBS_TABLE = """
CREATE TABLE IF NOT EXISTS jobs (
    id          TEXT PRIMARY KEY,
    slug        TEXT NOT NULL,
    status      TEXT DEFAULT 'queued',
    payload     TEXT,
    result      TEXT,
    attempts    INTEGER DEFAULT 0,
    workflow    TEXT,
    project     TEXT,
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP
)
"""

async def get_db() -> aiosqlite.Connection:
    os.makedirs(os.path.dirname(SQLITE_PATH), exist_ok=True)
    db = await aiosqlite.connect(SQLITE_PATH)
    await db.execute("PRAGMA journal_mode=WAL")
    await db.execute("PRAGMA synchronous=NORMAL")
    await db.execute(CREATE_JOBS_TABLE)
    await db.commit()
    return db

async def upsert_job(db: aiosqlite.Connection, job_id: str, **fields) -> None:
    set_clause = ", ".join(f"{k}=?" for k in fields)
    values = list(fields.values()) + [job_id]
    await db.execute(
        f"UPDATE jobs SET {set_clause}, updated_at=CURRENT_TIMESTAMP WHERE id=?",
        values
    )
    await db.commit()
