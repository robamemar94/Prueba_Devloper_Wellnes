from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_caching import Cache
from app.config.default import CacheConfig
ma = Marshmallow()
migrate = Migrate()

cache = Cache(config=CacheConfig)