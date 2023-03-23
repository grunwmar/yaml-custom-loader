import yaml
from yaml import SafeLoader
from yaml import load


class CustomLoader(SafeLoader):

    @classmethod
    def constructor(cls, klass):
        def inner(loader, node):
            if isinstance(node, yaml.nodes.MappingNode):
                return klass(kwargs=loader.construct_mapping(node))
            elif isinstance(node, yaml.nodes.SequenceNode):
                node_list = list(loader.construct_yaml_seq(node))
                if len(node_list) > 0:
                    node_list = node_list[0]
                return klass(args=node_list)
            elif isinstance(node, yaml.nodes.ScalarNode):
                return klass(args=[node.value])
        return inner


    @classmethod
    def set_constructor(cls, klass, alias=None):
        klass_name = klass.__name__ if alias is None else alias
        cls.add_constructor("!"+klass_name, cls.constructor(klass))


    @classmethod
    def load_file(cls, filename):
        with open(filename, "r") as f:
            jd = load(f, cls)
            return jd

    
    @classmethod
    def set(cls, alias=None):
        def inner(klass):
            cls.set_constructor(klass, alias=alias)
        return inner

