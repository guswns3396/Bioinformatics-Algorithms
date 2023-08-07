import importlib
import numpy as np
import pandas as pd


def runScript(mod_name: str, func_name: str, *args):
    mod = importlib.import_module('scripts.' + mod_name)
    func = getattr(mod, func_name)
    print(func)
    print(args)
    return func(*args)
