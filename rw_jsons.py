import json
from collections import OrderedDict
from undef_behaviour_catcher import undef_behaviour_catcher


@undef_behaviour_catcher
def read_json(json_file):
    with open(json_file) as f:
        return json.load(f)


@undef_behaviour_catcher
def write_json(data, json_outfile):
    with open(json_outfile, 'w') as f:
        json.dump(data, f, indent=2)
        print(file=f)


@undef_behaviour_catcher
def read_ordered_json(json_file):
    """
    for the right ordering of filters
    """
    with open(json_file) as f:
        return json.load(f, object_pairs_hook=OrderedDict)

