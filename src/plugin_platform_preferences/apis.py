"""What Preferences attaches to (plugin API 2.2, liminal_libs.sources.apis; the user, 2026-11-11: "each plugin should
reflect the the API its attached to, and present links that provide documentation ... it should also expose more of
what the API is about"): Liminal's own UI preferences, the library's (liminal_libs.ui): one file for every app on this
machine, served by every app's frame at GET /api/ui and applied by its theme.js. It is local only: nothing is sent
anywhere. Its documentation is the library's own, on GitHub (pcxmac-dev/liminal-libs is public; its release/0.2.0 branch
holds the UI preferences since 1.23.0), read on 2026-11-11 (`VERIFIED`). The plugin keeps nothing of it between two
reads (api_facts: the contract's, {})."""
from __future__ import annotations

from liminal_libs import ui
from liminal_libs.sources.apis import Api, Area, Call, Link

VERIFIED = "2026-11-11"
LIBS = "https://github.com/pcxmac-dev/liminal-libs/"
BRANCH = LIBS + "blob/release/0.2.0/"
UI = BRANCH + "src/liminal_libs/ui/__init__.py"
APP = BRANCH + "src/liminal_libs/apps/app.py"
THEME_JS = BRANCH + "src/liminal_libs/ui/static/theme.js"
CSS = BRANCH + "src/liminal_libs/ui/static/liminal.css"

PREFERENCES = Api(
    name="Liminal's UI preferences",
    maker="Liminal (liminal-libs)",
    about=("The look of every Liminal app's page, kept in one file for this machine: the data folder's ui.json "
           f"({ui.UI_VAR} names another). The plugin writes it; every app's frame answers it at GET /api/ui, and the "
           "library's theme.js paints each page in it (the page's origin remembers it, so the next visit is painted at "
           "once). Its themes are liminal.css's: Dark, Midnight and Graphite on the dark base, Light and Paper on the light."),
    kind="file",
    base=f"the data folder's ui.json ({ui.UI_VAR} names another); GET /api/ui on every app's frame",
    version="liminal-libs' UI preferences (since 1.23.0): {\"theme\": <name>}",
    auth="none: a file of this machine's user; every app's own page reads it from its own frame",
    limits="",
    costs="",
    links=(
        Link("The UI preferences (liminal_libs.ui)", UI, "docs"),
        Link("GET /api/ui on every app's frame (liminal_libs.apps.app)", APP, "reference"),
        Link("theme.js: the page painted in the theme", THEME_JS, "reference"),
        Link("liminal.css: the themes", CSS, "reference"),
        Link("liminal-libs' changes", BRANCH + "CHANGELOG.md", "changelog"),
        Link("liminal-libs", LIBS + "tree/release/0.2.0", "source"),
    ),
    areas=(
        Area("The theme", "the one preference there is: Dark, Midnight, Graphite, Light or Paper", UI,
             covered="chosen on the platform's page (Preferences' Theme), kept for every app"),
        Area("The file", f"ui.json in the data folder, or the file {ui.UI_VAR} names", UI,
             covered="written whole (a part file moved into place); its place said on the page"),
        Area("The themes' colours", "each theme's base and its page, card, accent and text colours", CSS,
             covered="shown as each choice's swatch"),
        Area("GET /api/ui", "every app's frame answering the preferences as JSON", APP),
        Area("theme.js", "each page painted in the theme as it loads, the next visit painted at once", THEME_JS),
        Area("A theme in the page's address", "?theme=<name>: a page shown inside another app painted in that app's theme",
             THEME_JS),
        Area("The charts app's Preferences", "the charts app's own view offering the same themes"),
    ),
    calls=(
        Call("ui.preferences(path)", "the theme (the default when none is saved), its base, the themes there are", "The theme",
             used="the plugin's status: the theme and its choices", docs=UI),
        Call("ui.save_preferences(path, theme=<name>)", "the theme changed and kept (ValueError for an unknown one)", "The theme",
             used="the theme hook", docs=UI, writes=True),
        Call("ui.preferences_file(path)", "where the file is", "The file", used="the page's facts: the file", docs=UI),
        Call("GET /api/ui", "the preferences, as every app's frame answers them", "GET /api/ui", docs=APP),
        Call("LiminalTheme.apply(<name>) (theme.js)", "a page painted in a theme", "theme.js", docs=THEME_JS),
    ),
    verified=VERIFIED,
)

APIS = (PREFERENCES,)
