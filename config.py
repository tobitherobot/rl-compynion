import os


# MySQL Connection
DATABASE_URL = '192.168.178.222'
USERNAME = 'root'
PASSWORD = 'external'
DATABASE = 'rl_compynion'

# File Storage Directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\'


RESOURCES_DIR = os.path.join(ROOT_DIR + 'resources\\')
REPLAYS_DIR = os.path.join(RESOURCES_DIR + 'replays\\')
JSON_DIR = os.path.join(RESOURCES_DIR + 'json\\')
