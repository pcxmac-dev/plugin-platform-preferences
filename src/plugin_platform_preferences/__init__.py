"""UI preferences for Liminal (the user, 2026-11-07: "yes add a preferences plugin for the 'UI' and add the different
themes"): the look of every Liminal app's page, kept in one file for this machine (the library's UI preferences, the
data folder's ui.json), chosen on the platform's page and applied by every app's page (the library's theme.js). The
theme is one of liminal.css's: Dark, Midnight and Graphite on the dark base, Light and Paper on the light one.

What it attaches to (0.2.0, plugin API 2.2; the user, 2026-11-11: "each plugin should reflect the the API its attached
to, and present links that provide documentation"): Liminal's own UI preferences, the library's (apis.py), linked to the
library's own pages on GitHub; local only, nothing is sent anywhere. It keeps nothing between two reads (api_facts: the
contract's, {}).

    python -m plugin_platform_preferences status | theme [NAME]
"""
from __future__ import annotations

from pathlib import Path

from liminal_libs import ui
from liminal_libs.machines.plugin import MachinePlugin

from .apis import APIS

__version__ = "0.2.0"


class PreferencesPlugin(MachinePlugin):
    """The UI's preferences: present wherever the platform runs; `theme(name)` sets the theme."""

    name = "preferences"
    title = "Preferences"
    about = "The UI of every Liminal app's page: its theme (Dark, Midnight, Graphite, Light or Paper), chosen here for this machine"
    api = "2.2"
    apis = APIS  # what it attaches to: Liminal's own UI preferences (apis.py)
    order = 740
    ICON = "sliders"
    HOOKS = (*MachinePlugin.HOOKS, "theme")

    def __init__(self, path: Path | None = None):
        self._path = path  # the preferences' file; the library's (the data folder's ui.json) unless given

    def present(self) -> bool:
        return True

    def theme(self, name: str) -> dict:
        """The UI's theme set (one of the library's ui.THEMES; ValueError otherwise): every app's page follows."""
        ui.save_preferences(self._path, theme=name)
        return self.status()

    def status(self) -> dict:
        p = ui.preferences(self._path)
        current = ui.THEMES[p["theme"]]
        return {"present": True, "summary": f"theme: {current['title']}", "theme": current["title"],
                "base": f"{current['base']}-based", "file": str(ui.preferences_file(self._path)),
                "options": [{"key": "theme", "title": "Theme", "hook": "theme", "value": p["theme"],
                             "choices": [{"value": t["name"], "title": t["title"], "note": f"{t['base']}-based", "swatch": t["swatch"]}
                                         for t in p["themes"]]}]}


MACHINE = PreferencesPlugin()
