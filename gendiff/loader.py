import json
import yaml


def load_files(path1, path2):
    loaders = {
        'json': json.load,
        'yml': yaml.safe_load,
    }

    format = path1.split('.')[-1]
    return loaders[format](open(path1)), loaders[format](open(path2))
