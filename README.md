# DOOM.html

A Doom-style FPS recreated in a single HTML file. No build step, no dependencies,
no assets — every texture, sprite, and sound effect is generated in code at runtime.

**Play it:** open `index.html` in any modern browser. That's it.

## Features

- Classic raycasting engine (DDA) with textured walls, floor, and ceiling casting
- Distance fog and side-shading for depth
- Sliding doors: press `E` to open them (with grind/thunk sounds); they auto-close
- Two demon types: **imps** (throw fireballs) and **pinkies** (fast, melee)
- Enemy AI: line-of-sight detection, sight screeches, chase growls, ranged/melee attacks, pain states
- Hitscan pistol with muzzle flash and view bobbing
- Health and ammo pickups
- Doom-style HUD: ammo / health / kills counters and a status face that reacts to damage
- Synthesized sound effects via WebAudio (gunshots, fireballs, demon deaths, doors)
- Original synthesized metal-style music loop (toggle with `N`) — the classic id
  Software tracks are copyrighted, so this is an original composition in the same spirit
- Minimap (toggle with `M`) — doors show in yellow (closed) / green (open)

## Controls

| Input | Action |
|---|---|
| Click | Lock mouse / fire |
| `WASD` | Move / strafe |
| Mouse or `←` `→` | Turn |
| `Shift` | Run |
| `Space` | Fire |
| `E` | Open / close doors |
| `N` | Toggle music |
| `M` | Toggle map |
| `R` | Restart (after death or victory) |

Kill all 10 demons to clear the level.
