import inspect


class Introspection:

    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        type_obj = type(self.obj).__name__
        attributes_obj = dir(self.obj)
        methods_obj = [method for method in attributes_obj if callable(getattr(self.obj, method))]
        module_obj = getattr(self.obj, '__module__', None)
        doc_obj = inspect.getdoc(self.obj)
        info = {
            'type': type_obj,
            'attributes': attributes_obj,
            'methods': methods_obj,
            'module': module_obj,
            'docstring': doc_obj
        }
        return info


obj = Introspection(42)
number_info = obj.introspection_info()
print(number_info)
