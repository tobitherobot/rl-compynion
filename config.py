import os


# MySQL Connection
DATABASE_URL = '127.0.0.1'
USERNAME = 'root'
PASSWORD = 'admin'
DATABASE = 'rl_compynion'

# File Storage Directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\'


RESOURCES_DIR = os.path.join(ROOT_DIR + 'resources\\')
REPLAYS_DIR = os.path.join(RESOURCES_DIR + 'replays\\')
JSON_DIR = os.path.join(RESOURCES_DIR + 'json\\')
