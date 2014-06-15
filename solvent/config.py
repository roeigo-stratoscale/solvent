import yaml

LOCAL_OSMOSIS = 'localhost:1010'
OFFICIAL_OSMOSIS = None
OFFICIAL_BUILD = False
WITH_OFFICIAL_OBJECT_STORE = True


def load(filename):
    with open(filename) as f:
        data = yaml.load(f.read())
    if data is None:
        raise Exception("Configuration file must not be empty")
    globals().update(data)
    if OFFICIAL_OSMOSIS is None:
        raise Exception("Configuration file must contain 'OFFICIAL_OSMOSIS' field")


def objectStoresOsmosisParameter():
    return LOCAL_OSMOSIS + "+" + OFFICIAL_OSMOSIS
