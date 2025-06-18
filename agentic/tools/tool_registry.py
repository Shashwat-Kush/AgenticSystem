class ToolRegistry:
    def __init__(self, settings):
        # you can inspect settings to decide which tools to load
        self._tools = {}

    def get(self, name: str):
        if name not in self._tools:
            raise KeyError(f"No tool named {name}")
        return self._tools[name]