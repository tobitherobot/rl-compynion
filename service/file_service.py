import config
import carball
import json


def decompile(filename):
    file = carball.decompile_replay(config.REPLAYS_DIR + filename + '.replay',
                                    output_path = config.JSON_DIR + filename + '.json',
                                    overwrite = True)
    return file


def load_json(filename):
    with open(config.JSON_DIR + filename + '.json', 'r') as file:
        data = json.load(file)
    return data
