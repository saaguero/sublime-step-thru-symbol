import sublime_plugin


class StepSymbol(sublime_plugin.TextCommand):

    def _show_symbol(self, symbol):
        self.view.sel().clear()
        self.view.sel().add(symbol)
        self.view.show(symbol)


class StepSymbolUpCommand(StepSymbol):

    def run(self, edit):
        current_region = self.view.sel()
        match = next((s for s in reversed(self.view.symbols())
                      if s[0].a < current_region[0].a), current_region)
        self._show_symbol(match[0])


class StepSymbolDownCommand(StepSymbol):

    def run(self, edit):
        current_region = self.view.sel()
        match = next((s for s in self.view.symbols()
                      if s[0].a > current_region[0].a), current_region)
        self._show_symbol(match[0])
