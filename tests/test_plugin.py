"""Preferences: the UI's theme read and set in a file of the test's own (never this machine's), offered as the
platform's page draws it, asked by name, refused when unknown, and from the command line."""
from __future__ import annotations

import json

import pytest

import plugin_platform_preferences.__main__ as cli
from liminal_libs import ui
from plugin_platform_preferences import PreferencesPlugin


def test_the_theme_is_read_offered_and_set(tmp_path):
    f = tmp_path / "ui.json"
    p = PreferencesPlugin(path=f)
    s = p.status()
    assert p.present() and s["summary"] == "theme: Dark" and s["theme"] == "Dark" and s["base"] == "dark-based" and s["file"] == str(f)
    (option,) = s["options"]
    assert (option["hook"], option["value"], option["title"]) == ("theme", "dark", "Theme")
    assert [c["value"] for c in option["choices"]] == ["dark", "midnight", "graphite", "light", "paper"] == list(ui.THEMES)
    assert option["choices"][4] == {"value": "paper", "title": "Paper", "note": "light-based", "swatch": list(ui.THEMES["paper"]["swatch"])}
    assert p.theme("midnight")["summary"] == "theme: Midnight" and json.loads(f.read_text(encoding="utf-8")) == {"theme": "midnight"}
    assert ui.preferences(f)["theme"] == "midnight" and ui.preferences(f)["base"] == "dark"  # what every app's page applies
    with pytest.raises(ValueError):
        p.theme("neon")
    assert ui.preferences(f)["theme"] == "midnight"  # a refused theme changes nothing


def test_the_platform_asks_it_by_name(tmp_path):
    p = PreferencesPlugin(path=tmp_path / "ui.json")
    assert {"present", "status", "theme"} <= set(p.interface()["hooks"])
    assert p.ask("theme", "paper")["theme"] == "Paper" and p.ask("status")["options"][0]["value"] == "paper"


def test_the_command_line(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(cli, "MACHINE", PreferencesPlugin(path=tmp_path / "ui.json"))
    assert cli.main(["theme"]) == 0 and capsys.readouterr().out == "Dark\n"
    assert cli.main(["theme", "graphite"]) == 0 and capsys.readouterr().out == "theme: Graphite\n"
    assert cli.main(["status"]) == 0 and json.loads(capsys.readouterr().out)["theme"] == "Graphite"
    assert cli.main(["theme", "neon"]) == 2 and "no theme named 'neon'" in capsys.readouterr().err
    assert cli.main(["colours"]) == 2 and "theme [dark|midnight|graphite|light|paper]" in capsys.readouterr().err
