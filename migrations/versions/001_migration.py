"""
Autogenerated migration file.

Revision: 1
Message: Migration
"""
from asyncqlio import Session

revision = "1"
message = "Migration"


async def upgrade(session: Session):
    """
    Performs an upgrade. Put your upgrading SQL here.
    """
    await session.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        guild_id BIGINT,
        channel_id BIGINT,
        message_id BIGINT PRIMARY KEY,
        author BIGINT,
        content TEXT,
        timestamp TIMESTAMP
    );
    
    CREATE INDEX messages_guild_id_idx ON messages (guild_id);
    CREATE INDEX messages_channel_id_idx ON messages (channel_id);
    CREATE INDEX messages_author_idx ON messages (author);
    
    CREATE TABLE IF NOT EXISTS dynamic_rules (
        guild_id BIGINT PRIMARY KEY,
        attrs TEXT
    );
    
    CREATE INDEX dynamic_rules_guild_id_idx ON dynamic_rules (guild_id);
    
    CREATE TABLE IF NOT EXISTS schedule(
        id BIGSERIAL NOT NULL PRIMARY KEY,
        expires TIMESTAMP,
        event TEXT,
        extras TEXT
    );
    
    CREATE INDEX schedule_id_idx ON schedule (id);
    
    CREATE TABLE IF NOT EXISTS ignored(
        object_id BIGINT PRIMARY KEY,
        reason TEXT DEFAULT NULL,
        type TEXT
    );
    
    CREATE INDEX ignored_type_idx on ignored (type);
    ''')


async def downgrade(session: Session):
    """
    Performs a downgrade. Put your downgrading SQL here.
    """
    await session.execute('''
        DROP TABLE IF EXISTS messages;
        DROP TABLE IF EXISTS dynamic_rules;
        DROP TABLE IF EXISTS schedule;
        DROP TABLE IF EXISTS ignored;
    ''')
