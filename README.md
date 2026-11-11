# plugin-platform-preferences

UI preferences for Liminal: the theme of every Liminal app's page, chosen on the platform for this machine.

The user's words (2026-11-07): "yes add a preferences plugin for the 'UI' and add the different themes".

## What it does

A machine plugin of the platform (`liminal_libs.machines.MachinePlugin`, plugin API 2.2, its icon the sliders):

- The theme, one of the library's (`liminal_libs.ui.THEMES`, the themes of `liminal.css`): Dark, Midnight and
  Graphite on the dark base, Light and Paper on the light one.
- Kept in one file for every app on this machine: the library's UI preferences, the data folder's `ui.json`
  (`LIMINAL_UI_FILE` names another).
- Every app's frame answers it at `GET /api/ui`, and the library's `theme.js` paints each page in it (the page's
  own origin remembers it, so the next visit is painted at once).

The platform's page shows the themes with their colours; choosing one applies it there at once, and every other
app's page on its next load.

## Its hooks

`present` (always), `status` (the summary, the facts, `options`: the theme and its choices), `theme(name)`.

## Its API

The user's words (2026-11-11): "each plugin should reflect the the API its attached to, and present links that provide
documentation, the plugin interface should more or less contain what it already has, BUT, it should also expose more of
what the API is about". Since 0.2.0 (plugin API 2.2) the plugin declares what it attaches to (`apis.py`), and the
platform's page draws its card: Liminal's own UI preferences, local only (nothing is sent anywhere), linked to the
library's own pages on GitHub (pcxmac-dev/liminal-libs is public; its `release/0.2.0` branch holds the UI preferences
since 1.23.0):

- [the UI preferences (`liminal_libs.ui`)](https://github.com/pcxmac-dev/liminal-libs/blob/release/0.2.0/src/liminal_libs/ui/__init__.py),
- [`GET /api/ui` on every app's frame](https://github.com/pcxmac-dev/liminal-libs/blob/release/0.2.0/src/liminal_libs/apps/app.py),
- [`theme.js`](https://github.com/pcxmac-dev/liminal-libs/blob/release/0.2.0/src/liminal_libs/ui/static/theme.js) and
  [`liminal.css`](https://github.com/pcxmac-dev/liminal-libs/blob/release/0.2.0/src/liminal_libs/ui/static/liminal.css),
- [the library's changes](https://github.com/pcxmac-dev/liminal-libs/blob/release/0.2.0/CHANGELOG.md).

Its parts: the theme and the file (the plugin's), the themes' colours, `GET /api/ui`, `theme.js`, a theme in a page's
address, the charts app's own Preferences. The plugin keeps nothing between two reads, so `api_facts()` is the
contract's: nothing to say. The test `test_the_cards_pages_answer` asks each address again when `LIMINAL_VENDOR_PAGES=1`
is set (it is skipped otherwise).

## From the command line

```
python -m plugin_platform_preferences status
python -m plugin_platform_preferences theme
python -m plugin_platform_preferences theme midnight
```
