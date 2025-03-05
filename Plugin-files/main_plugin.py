import importlib
import os

def load_student_plugins():
    plugins = {}
    plugin_dir = "student_plugins"
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            module = importlib.import_module(f"{plugin_dir}.{module_name}")
            for attr in dir(module):
                if attr.endswith("Command"):
                    plugins[module_name] = getattr(module, attr)
    return plugins

student_plugins = load_student_plugins()
print("Loaded student plugins:", student_plugins)
