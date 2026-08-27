# DOOM.html

A Doom-style FPS recreated in a single HTML file. No build step, no dependencies,
no bundled assets — every texture and sprite is generated in code at runtime.

**Play it now:** [perpetualpixel.github.io/Doom](https://perpetualpixel.github.io/Doom/)

Or run it locally: open `index.html` in any modern browser. That's it.

## Levels

All three original episodes — 27 levels — as grid adaptations (the real maps
aren't tile-based, so these recreate each level's layout beats, themes, and
progression — not the exact geometry). Pick your episode from the main menu:

- **Episode 1: Knee-Deep in the Dead** — E1M1 Hangar through E1M8 Phobos
  Anomaly (twin **Barons of Hell**). E1M3 hides a secret exit to E1M9
  Military Base, which exits back to E1M4.
- **Episode 2: The Shores of Hell** — E2M1 Deimos Anomaly through E2M8 Tower
  of Babel (**Cyberdemon**). E2M5 hides a secret exit to E2M9 Fortress of
  Mystery, which exits back to E2M6.
- **Episode 3: Inferno** — E3M1 Hell Keep through E3M8 Dis (**Spider
  Mastermind**). E3M6 hides a secret exit to E3M9 Warrens, which exits back
  to E3M7.

The bestiary: zombies, imps, demons, lost souls, cacodemons, Barons of Hell,
the Cyberdemon, and the Spider Mastermind.

## Arsenal

Seven weapons on keys `1`–`7`: fist, pistol, shotgun (7-pellet spread with
pump-action sound), chaingun, rocket launcher (splash damage — careful up
close), plasma rifle, and the BFG9000. Four ammo types (bullets, shells,
rockets, cells) with pickups placed through the levels; the HUD ARMS panel
shows what you own. You start with the pistol; find the rest — the BFG is
hidden in the Fortress of Mystery and guarded in Dis. Dying resets you to
a pistol start.

Find and press the **exit switch** in each level to advance. Colored **keycards**
open matching locked doors, **teleporter pads** whisk you across the map,
and some walls hide **secret doors** (press `E` on suspicious walls). Health
and ammo carry over between levels; dying restarts the current level.

## Menus

A classic-styled main menu (episode select, music toggle, help) with skull
cursor and clickable buttons, and a pause menu on `Esc` (resume, restart
level, music, end game).

## Soundtrack

The shipped soundtrack is royalty-free metal from Pixabay Music — tracks by
**Alec Koff**, **NickPanek**, **Emmraan**, and **The_Mountain** (`Music/`).
The title screen, the three boss levels, and the victory screen each have
dedicated tracks; other levels rotate through the rest. When the optional
local `Doom OST/` folder is present it serves as a fallback, and a
synthesized loop backs everything as a last resort.

## Assets

The custom monster sheets (`sprites/`) and weapon art (`Guns/`) ship with the
repo and are also inlined as data URIs in `assets.js`, so the real art loads
even when `index.html` is opened straight from the files — no local server
needed. After changing anything in `sprites/` or `Guns/`, regenerate with:

    python3 tools/embed_assets.py

The game also looks for optional local folders and auto-detects what's present:

- `SFX/` — sound effect files (the shipped MP3s, plus classic `ds*.wav`
  names if you drop them in)
- `Doom OST/` — soundtrack MP3s (each level plays its matching track,
  plus intermission and victory music); git-ignored, not distributed

Whatever is missing falls back to fully synthesized WebAudio sound and an
original metal-style music loop.

## Features

- Classic raycasting engine (DDA) with textured walls, floor, and ceiling casting
- Distance fog and side-shading for depth
- Sliding doors: press `E` to open them (with grind/thunk sounds); they auto-close
- Exit switches, per-level intermission screens, and a victory screen
- Two demon types: **imps** (throw fireballs) and **pinkies** (fast, melee)
- Enemy AI: line-of-sight detection, sight screeches, chase growls, ranged/melee attacks, pain states
- Distance-attenuated sound: far demons sound far away
- Hitscan pistol with muzzle flash and view bobbing
- Health and ammo pickups
- Doom-style HUD: ammo / health / kills / level and a status face that reacts to damage
- Minimap (toggle with `M`) — doors show yellow (closed) / green (open), exit in red

## Controls

| Input | Action |
|---|---|
| Click | Lock mouse / fire |
| `WASD` | Move / strafe |
| Mouse or `←` `→` | Turn |
| `Shift` | Run |
| `Space` | Fire (or continue, on intermission) |
| `E` | Use doors and exit switches |
| `N` | Toggle music |
| `M` | Toggle map |
| `R` | Restart level (after death) / new game (after victory) |
