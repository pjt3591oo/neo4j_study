import os
from dotenv import load_dotenv
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, db)
import copy


load_dotenv()
config.DATABASE_URL = os.environ["NEO4J_BOLT_URL"]
config.ENCRYPTED_CONNECTION = False

