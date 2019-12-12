import yaml
from collections import OrderedDict

yaml.add_representer(OrderedDict,
                     lambda dumper, data: dumper.represent_mapping('tag:yaml.org,2002:map', data.items()))


class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


def raw_read_yaml(file):
    with open(file) as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            raise


def read_yaml(yaml_file):
    with open(yaml_file) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            raise


def write_yaml(data, yaml_outfile):
    with open(yaml_outfile, 'w') as outfile:
        if isinstance(data, dict):
            data = OrderedDict(data)
        yaml.dump(data, outfile, Dumper=MyDumper, default_flow_style=False)
