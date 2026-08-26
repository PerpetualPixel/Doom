# DOOM.html

A Doom-style FPS recreated in a single HTML file. No build step, no dependencies,
no bundled assets — every texture and sprite is generated in code at runtime.

**Play it:** open `index.html` in any modern browser. That's it.

## Levels

Three levels, grid homages of the *Knee-Deep in the Dead* openers (the real maps
aren't tile-based, so these recreate the layout beats, not the exact geometry):

1. **E1M1: Hangar** — three-room front block, side chambers, pillared exit hall
2. **E1M2: Nuclear Plant** — nested ring corridors around a computer core
3. **E1M3: Toxin Refinery** — four quadrants, a toxin pit, and a locked-away exit room

Find and press the **exit switch** in each level to advance. Health and ammo
carry over between levels; dying restarts the current level with a fresh pistol.

## Audio

The game looks for two optional local folders:

- `SFX/` — classic Doom sound effect WAVs (`dspistol.wav`, `dsdoropn.wav`, ...)
- `Doom OST/` — the soundtrack MP3s (each level plays its matching track,
  plus intermission and victory music)

If they exist, you get the real sounds and music. If not (as in this repo and
the hosted build — those files are id Software's copyrighted assets, so they are
git-ignored and not distributed here), the game falls back to fully synthesized
WebAudio sound effects and an original metal-style music loop.

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
