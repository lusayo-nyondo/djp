import djp

@djp.hookimpl
def loaders():
    return [
        'from_plugin.loaders.MyPluginLoader'
    ]