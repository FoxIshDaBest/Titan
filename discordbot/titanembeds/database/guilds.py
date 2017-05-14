from titanembeds.database import db, Base

class Guilds(Base):
    __tablename__ = "guilds"
    id = db.Column(db.Integer, primary_key=True)    # Auto incremented id
    guild_id = db.Column(db.String(255))            # Discord guild id
    name = db.Column(db.String(255))                # Name
    unauth_users = db.Column(db.Boolean())          # If allowed unauth users
    chat_links = db.Column(db.Boolean())            # If users can post links
    bracket_links = db.Column(db.Boolean())         # If appending brackets to links to prevent embed
    mentions_limit = db.Column(db.Integer)          # If there is a limit on the number of mentions in a msg
    roles = db.Column(db.Text())                    # Guild Roles
    channels = db.Column(db.Text())                 # Guild channels
    owner_id = db.Column(db.String(255))            # Snowflake of the owner
    icon = db.Column(db.String(255))                # The icon string, null if none

    def __init__(self, guild_id, name, roles, channels, owner_id, icon):
        self.guild_id = guild_id
        self.name = name
        self.unauth_users = True # defaults to true
        self.chat_links = True
        self.bracket_links = True
        self.mentions_limit = -1 # -1 = unlimited mentions
        self.roles = roles
        self.channels = channels
        self.owner_id = owner_id
        self.icon = icon

    def __repr__(self):
        return '<Guilds {0} {1}>'.format(self.id, self.guild_id)