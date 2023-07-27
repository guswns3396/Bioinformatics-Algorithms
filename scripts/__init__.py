import importlib


def runScript(mod_name: str, func_name: str, *args):
    mod = importlib.import_module('scripts.' + mod_name)
    func = getattr(mod, func_name)
    print(func)
    print(args)
    return func(*args)
