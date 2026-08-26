# DOOM.html

A Doom-style FPS recreated in a single HTML file. No build step, no dependencies,
no bundled assets — every texture and sprite is generated in code at runtime.

**Play it:** open `index.html` in any modern browser. That's it.

## Levels

The full *Knee-Deep in the Dead* episode as grid adaptations (the real maps
aren't tile-based, so these recreate each level's layout beats, themes, and
progression — not the exact geometry):

1. **E1M1: Hangar** · 2. **E1M2: Nuclear Plant** · 3. **E1M3: Toxin Refinery**
   (hides a **secret exit** to E1M9) · 4. **E1M4: Command Control** ·
   5. **E1M5: Phobos Lab** · 6. **E1M6: Central Processing** ·
   7. **E1M7: Computer Station** · 8. **E1M8: Phobos Anomaly** (episode boss:
   twin **Barons of Hell**) · 9. **E1M9: Military Base** (secret level, exits to E1M4)

Find and press the **exit switch** in each level to advance. Colored **keycards**
open matching locked doors, **teleporter pads** whisk you across the map,
and some walls hide **secret doors** (press `E` on suspicious walls). Health
and ammo carry over between levels; dying restarts the current level.

## Optional local assets

The game looks for optional local folders and auto-detects what's present:

- `SFX/` — classic Doom sound effect WAVs (`dspistol.wav`, `dsdoropn.wav`, ...)
- `Doom OST/` — the soundtrack MP3s (each level plays its matching track,
  plus intermission and victory music)
- `sprites/` — monster sprite sheets (`Imp.png`, `Demon.png`, `Baron Of Hell.png`),
  auto-sliced at runtime (requires serving over http, e.g. `python -m http.server`;
  browsers block pixel access to local images on `file://`)

Whatever is missing falls back to fully synthesized WebAudio sound, an original
metal-style music loop, and procedural sprite art. These folders are
git-ignored and not distributed with the repo — they are id Software's
copyrighted assets.

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
