# Smart Movie Picker

An offline Tkinter desktop app that suggests five movies or series to match your filters, your mood and a request in plain English, and explains why it picked each one.

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GUI: Tkinter](https://img.shields.io/badge/GUI-Tkinter%20%2F%20ttk-2B5B84)](https://docs.python.org/3/library/tkinter.html)
[![Dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen)](requirements.txt)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

![Smart Movie Picker main window. The Preferences dropdowns are set to Series, Korean, Business and Motivational, and the status line reads "2 exact match(es) found". Below it are the first three of the five recommendation cards (Start-Up and Itaewon Class at 100%, Business Proposal at 76%), each with a rating, a Preference Match percentage and a "Why recommended" explanation. The other two cards are cut off by the window height.](docs/screenshot.png)

> **Learning project.** This repo is part of my Python learning log. It is a working desktop app, written as a single script while I practised Tkinter, text processing and rule-based scoring. The sections below cover [what the project covers](#what-this-project-covers), its [known limitations](#known-limitations) and a [roadmap](#roadmap) for turning it into a structured, tested package.

## Why I built this

Picking something to watch usually means scrolling through long lists that don't know your mood, and that rarely say why a title was suggested. This app answers a narrower question: given the type, industry/language, genre and mood I want, plus a short description in my own words, which five titles fit best, and why? It runs fully offline on the Python standard library alone, so there is nothing extra to install and your viewing history stays on your machine.

## Features

- **Four filters.** Type (Movie / Series), Industry / Language (Hollywood, Bollywood, Punjabi, Korean), Genre (10 options) and Mood (7 options). Each one defaults to "Anything".
- **Smart Request box.** Type something like *"Korean series about startups and technology"*. The request is lowercased, aliases are normalized (`kdrama` → `korean`, `hindi` → `bollywood`, `films` → `movie`, `sci fi` → `sci-fi`), filler words such as "I want something to watch tonight" are dropped, and the remaining words are matched against each title's metadata.
- **Typo tolerance.** Words that don't match exactly can still match through fuzzy matching with `difflib` (for example, `tecnology` matches `technology`).
- **Explainable, weighted scoring.** Each card shows a **Preference Match** percentage and a **"Why recommended"** line, for example `Series, Korean, related to Business: Drama, similar mood: Serious`.
- **Partial credit.** Related genres (for example Tech → Sci-Fi, Business, Thriller) and related moods (for example Serious → Dark, Emotional) still count, so near-misses rank above unrelated titles.
- **Built-in catalog of 53 titles.** 21 Hollywood (13 movies, 8 series), 10 Bollywood (7 movies, 3 series), 8 Punjabi movies and 14 Korean (4 movies, 10 series). Each title is tagged with genres, moods, keywords and an approximate rating out of 10.
- **Sensible fallbacks.** With no filters and no request you get 5 random "discovery" picks. If nothing scores at all, the search widens to 5 random alternatives.
- **Surprise Me** gives 5 random picks, and **Reset** clears all filters and results.
- **Watched tracking.** Mark any card as watched. **Hide watched** (on by default) leaves watched titles out of results.
- **Add your own titles** in a dialog with title, type, industry, genre, mood, an optional rating (checked to be between 0 and 10) and comma-separated keywords. Custom titles appear in every search from then on.
- **Local persistence.** The watched list and custom titles are saved to a small JSON file next to the script.
- **Keyboard shortcut.** Press **Enter** anywhere in the main window to run the search.

## Tech stack

| Area | What is used |
| --- | --- |
| Language | Python 3 (standard library only, no third-party packages) |
| GUI | `tkinter` / `ttk` with the `clam` theme: `Combobox`, `LabelFrame`, `Checkbutton`, a `Toplevel` dialog and `messagebox` |
| Matching | `re` for text cleanup, `difflib.get_close_matches` for fuzzy matching |
| Ranking | Hand-weighted rule-based scoring, with `random` for tie-breaking and discovery picks |
| Storage | `json` file stored next to the script (path built with `os.path`) |

## Getting started

### Prerequisites

- **Python 3.8 or newer** with Tkinter. The app has been run with Python 3.12 (Tk 8.6) on Windows. The code uses no newer syntax than Python 3.6, so other Python 3.8+ builds that include Tkinter should work too.
  - The python.org installers for Windows and macOS include Tkinter.
  - Debian/Ubuntu: `sudo apt install python3-tk`
  - Fedora: `sudo dnf install python3-tkinter`
  - macOS with Homebrew Python: `brew install python-tk`
  - To check your setup, run `python -m tkinter`. It should open a small test window.

### Install and run

```bash
git clone https://github.com/uzairsynth/smart-movie-picker.git
cd smart-movie-picker

python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Windows (cmd.exe)
.venv\Scripts\activate.bat
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt   # installs nothing: the app uses only the standard library
python app.py
```

On macOS and Linux you may need `python3` instead of `python` before the virtual environment is active.

## Usage walkthrough

1. **Launch the app.** Run `python app.py`. The window shows a **Preferences** panel with four dropdowns, a **Smart Request** box and a row of buttons.
2. **Filter.** For example, set *Type = Series*, *Industry = Korean*, *Genre = Business* and *Mood = Motivational*, then click **Find Best 5** (or press **Enter**). On a fresh install with no watched titles:
   - *Start-Up* and *Itaewon Class* match every filter: **100%**.
   - *Business Proposal* matches type, industry and genre but not the mood: **76%**.
   - *Halt and Catch Fire* and *TVF Pitchers* match everything except the industry: **70%**.
   - The status line reads *"2 exact match(es) found. Other results are the closest alternatives."*
3. **Describe what you want.** Type a request such as `korean series about startups and technology` in the Smart Request box. You can use it on its own or together with the dropdowns. Matching words show up in the card's reason, for example `request: korean, series, startup, technology` on *Start-Up*. (A request on its own currently always gets the "No exact combination found" status. See [Known limitations](#known-limitations).)
4. **Read each card.** A card shows the rank and title, the rating, `Type | Industry | Genres`, the moods, the Preference Match percentage (or *Discovery Pick* for random picks) and up to four reasons.
5. **Pick Again** re-runs the same search. Titles with equal scores are tie-broken at random, so you may get a different mix of equally good options. **Surprise Me** ignores the filters and the request and shows 5 random titles (watched titles stay hidden while **Hide watched** is on). **Reset** clears everything.
6. **Mark Watched** saves the title to your watched list. With **Hide watched** on, the search re-runs without that title. With it off, you get a confirmation pop-up instead. Toggling the checkbox takes effect on the next search.
7. **Add My Own Title** opens a form. Saved titles go into `movie_picker_data.json` and are scored like the built-in ones.

## How the scoring works

Only the criteria you actually set count toward the maximum score:

| Criterion | Exact match | Partial credit |
| --- | --- | --- |
| Type | +18 | none |
| Industry / Language | +30 | none |
| Genre | +28 | +10 if the title has a genre related to the selected one |
| Mood | +24 | +8 if the title has a mood related to the selected one |
| Smart Request | up to +30 | +6 per word that matches a title term exactly, +3 per fuzzy match (cutoff 0.80) |

**Preference Match** = `score / maximum possible for the active criteria × 100`, rounded and capped at 100%.

Example: with Series + Korean + Business + Motivational the maximum is 100. *Squid Game* scores 18 (Series) + 30 (Korean) + 10 (Drama is related to Business) + 8 (Serious is related to Motivational) = **66%**.

Results are sorted by score, and ties are broken at random. The status line reports how many titles matched **every** active dropdown filter: 5 or more gives "Strong matches found", 1 to 4 gives "N exact match(es) found", and 0 gives "No exact combination found".

## What this project covers

This is a single-script project, so the table maps each concept I practised to the place in `app.py` where it appears:

| Concept | Where it appears in `app.py` |
| --- | --- |
| Tkinter layout with `pack` and `grid`, `ttk` themes (with a `TclError` fallback), readonly `Combobox`, `LabelFrame` | Main window, filter panel |
| Event handling: button commands, `root.bind("<Return>", ...)` | Buttons and Enter-key binding |
| Capturing a loop variable in a callback with `lambda name=item["name"]: ...` | `render_results` (Mark Watched button) |
| Building widgets dynamically and clearing them with `winfo_children()` / `destroy()` | `render_results`, `clear_results` |
| A secondary window with `Toplevel`, a nested function (closure) that reads the dialog's widgets, and input validation with `try` / `except ValueError` | `open_add_title_window`, `save_new_title` |
| Text normalization: lowercasing, alias maps, regex cleanup, stop words | `normalize_text`, `text_match_score` |
| Fuzzy string matching with `difflib.get_close_matches` | `text_match_score` |
| Weighted, explainable scoring with partial credit from lookup maps of sets | `score_item`, `RELATED_GENRES`, `RELATED_MOODS` |
| Ranking with a tuple sort key and random tie-breaking, `random.sample` fallbacks | `find_recommendations`, `surprise_me` |
| JSON persistence with paths relative to the script | `load_data`, `save_data` |
| Modelling data with lists of dicts and sets | `BUILTIN_TITLES`, `RATINGS`, `watched` |

## Known limitations

These are real issues in the current version. They are listed here on purpose, because fixing them is the next stage of this project:

- **Results can be cut off.** The results area has no scrollbar. With five cards the layout needs about 1,350 px of height, so in the default 1000×850 window the lower cards are hidden. Maximizing the window helps on tall screens.
- **Alias replacement is substring-based.** Aliases are replaced inside words, not on whole words, so `dark drama` becomes `darkorean` and word order can change the results.
- **Small stop-word list.** Common words such as `and` are not filtered out, so they can match title names (for example, `and` matches *Halt and Catch Fire*).
- **Misleading status for text-only searches.** A search that uses only the Smart Request box always reports "No exact combination found", even when the matches are strong.
- **Reason text can vary between runs.** When a title has more than one related genre or mood, the one named in "Why recommended" is picked from a set, so it can differ from one launch to the next.
- **Corrupt data is silently replaced.** If `movie_picker_data.json` can't be read, the app starts empty and the next save overwrites the file. Writes are not atomic.
- **Missing UI actions and a thin data model.** You can't un-mark a watched title or edit or delete custom titles in the app, and the add-title form accepts only one genre and one mood. Watched titles are stored by name, and duplicate custom titles are allowed.
- **GUI and logic are mixed.** Everything runs at module level (there is no `if __name__ == "__main__":` guard), and the scoring reads Tk variables directly. That means the engine can't be imported or unit-tested without opening a window, and there are **no automated tests yet**.
- **Windows-centric styling.** The `Segoe UI` font is Windows-specific; other systems fall back to a default font.
- **Static ratings.** Ratings are hand-entered snapshots and will go out of date.

## Project structure

```text
smart-movie-picker/
├── app.py              # Whole app: catalog, text matching, scoring engine, Tkinter GUI
├── docs/
│   └── screenshot.png  # Screenshot used in this README
├── requirements.txt    # No third-party packages (standard library only)
├── .gitignore
├── LICENSE
└── README.md
```

The app creates `movie_picker_data.json` next to `app.py` the first time you mark a title as watched or add a title. It holds your personal viewing data, so it is listed in `.gitignore`.

## Roadmap

Each item below is the next learning goal for this project:

- [x] README, MIT license and `.gitignore`
- [ ] Fix the visible bugs: whole-word alias matching (`re.sub(rf"\b{re.escape(old)}\b", new, text)`) and a scrollable results area
- [ ] Format with `ruff format`, lint with `ruff check`, and add type hints and docstrings
- [ ] Split into a package: `models.py` (`Title` and `Preferences` dataclasses), `engine.py` (pure functions, no Tk), `storage.py`, `gui.py` and `__main__.py` with a `main()` entry point
- [ ] Move the catalog and ratings into one `data/catalog.json` with a stable id per title, validated on load, and store watched and custom titles by id instead of by name
- [ ] Make storage safe: atomic writes (temp file + `os.replace`), a `.bak` backup and a warning on corrupt files, and the data file kept in the user data directory (for example with `platformdirs`)
- [ ] Add a `pytest` suite for the engine and storage: alias regressions (`dark drama`, `Indiana`), weights and Preference Match, partial credit, hide-watched filtering, and a storage round-trip and corrupt-file test
- [ ] Fix the UX gaps: correct status for text-only searches, refresh results when *Hide watched* changes, un-mark watched titles, edit and delete custom titles, allow several genres and moods in the add form, merge *Find Best 5* and *Pick Again*, and make the reason text deterministic
- [ ] Add a `pyproject.toml` with a `movie-picker` console-script entry point
- [ ] Add GitHub Actions CI that runs ruff, mypy and pytest on Ubuntu and Windows
- [ ] Add one differentiator: a Streamlit web front end that reuses the engine, optional TMDB integration (API key from an environment variable, attribution shown), or a TF-IDF ranker compared against the hand-tuned weights
- [ ] Publish a Windows `.exe` built with PyInstaller as a GitHub Release, with semantic versioning and a CHANGELOG

## Data, privacy and responsible use

- **Offline by design.** The app makes no network calls, scrapes nothing and needs no account.
- **Your data stays local.** `movie_picker_data.json` stores your watched list and custom titles in plain text next to `app.py`. It is git-ignored so your viewing history isn't published by accident. Delete the file to start fresh.
- **Ratings are approximate.** The built-in ratings are hand-entered approximations out of 10 for convenience. They don't come from any ratings service, aren't endorsed by one and aren't kept up to date, so please don't present them as official scores.
- **Extending with live data.** If you add a movie-database API (for example TMDB or OMDb), follow its terms of use and attribution requirements, and load API keys from environment variables rather than source code.

## License

Released under the [MIT License](LICENSE). Copyright (c) 2026 Muhammad Uzair.

## Author

Built by **Muhammad Uzair** ([@uzairsynth](https://github.com/uzairsynth)) as part of a Python learning log.
