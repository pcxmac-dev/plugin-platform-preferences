"""What Preferences attaches to (plugin API 2.2): its card is sound and links the library's own pages on GitHub; it
names the library calls the plugin makes and the frame's GET /api/ui as the library serves it; it keeps nothing to say
(api_facts {}); and the card's pages answer (LIMINAL_VENDOR_PAGES=1 only, the one test that reaches the network)."""
from __future__ import annotations

import inspect
import os
import re

import pytest

import plugin_platform_preferences as module
from liminal_libs import ui
from liminal_libs.apps import app as frame
from liminal_libs.sources.apis import dead_links, problems
from plugin_platform_preferences import MACHINE, PreferencesPlugin
from plugin_platform_preferences import apis as cards


def test_the_card_is_sound_and_links_the_librarys_own_pages():
    assert problems(MACHINE.apis) == [] and MACHINE.apis == cards.APIS == (cards.PREFERENCES,)
    api = cards.PREFERENCES
    assert api.kind == "file" and api.verified == "2026-11-11" and api.costs == "" and not api.limits
    assert all(x.url.startswith("https://github.com/pcxmac-dev/liminal-libs/") for x in api.links)
    assert api.docs.endswith("/src/liminal_libs/ui/__init__.py") and api.used and len(api.areas) > len(api.covered)
    assert ui.UI_VAR in api.base and all(t["title"] in api.about for t in ui.THEMES.values())


def test_the_card_names_the_library_calls_the_plugin_makes(tmp_path):
    src = inspect.getsource(module)
    made = set(re.findall(r"\bui\.(\w+)\(", src))
    assert made == {c.name.split("(")[0].removeprefix("ui.") for c in cards.PREFERENCES.used}
    assert all(callable(getattr(ui, name)) for name in made)
    assert 'path == "/api/ui"' in inspect.getsource(frame)  # every app's frame answers it
    p = PreferencesPlugin(path=tmp_path / "ui.json")
    assert p.theme("paper")["theme"] == "Paper" and p.api_facts() == {}  # nothing kept between two reads


@pytest.mark.skipif(os.environ.get("LIMINAL_VENDOR_PAGES") != "1", reason="reaches the library's pages: LIMINAL_VENDOR_PAGES=1")
def test_the_cards_pages_answer():
    assert dead_links(MACHINE.apis) == []
