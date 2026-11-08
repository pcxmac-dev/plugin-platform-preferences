# plugin-platform-preferences

UI preferences for Liminal: the theme of every Liminal app's page, chosen on the platform for this machine.

The user's words (2026-11-07): "yes add a preferences plugin for the 'UI' and add the different themes".

## What it does

A machine plugin of the platform (`liminal_libs.machines.MachinePlugin`, plugin API 2.1, its icon the sliders):

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

## From the command line

```
python -m plugin_platform_preferences status
python -m plugin_platform_preferences theme
python -m plugin_platform_preferences theme midnight
```
