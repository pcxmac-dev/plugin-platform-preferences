# Changelog

## 0.2.0 (2026-11-11)

Its API on its page, plugin API 2.2 (the user: "each plugin should reflect the the API its attached to, and present
links that provide documentation, the plugin interface should more or less contain what it already has, BUT, it should
also expose more of what the API is about"). One card (`apis.py`): Liminal's own UI preferences, local only, linked to
the library's own pages on GitHub (pcxmac-dev/liminal-libs, public; the `release/0.2.0` branch): the UI preferences,
the frame's `GET /api/ui`, `theme.js`, `liminal.css`, the library's changes. Its parts the plugin uses (the theme, the
file, the themes' colours) first, then the rest; its calls (`ui.preferences`, `ui.save_preferences`,
`ui.preferences_file`) beside `GET /api/ui` and theme.js'. It keeps nothing between two reads: `api_facts()` stays the
contract's ({}). Tests: the card names the library calls the plugin makes; a link check runs with LIMINAL_VENDOR_PAGES=1.
Needs liminal-libs>=1.49.0.

## 0.1.0 (2026-11-07)

The first release: the UI's theme (Dark, Midnight, Graphite, Light, Paper) chosen on the platform for every
Liminal app's page, kept in the library's UI preferences (liminal-libs 1.23.0: the data folder's `ui.json`,
`GET /api/ui` on every app's frame, `theme.js`).
