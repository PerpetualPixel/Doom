# DOOM.html

A Doom-style FPS recreated in a single HTML file. No build step, no dependencies,
no assets — every texture, sprite, and sound effect is generated in code at runtime.

**Play it:** open `index.html` in any modern browser. That's it.

## Features

- Classic raycasting engine (DDA) with textured walls, floor, and ceiling casting
- Distance fog and side-shading for depth
- Two demon types: **imps** (throw fireballs) and **pinkies** (fast, melee)
- Enemy AI: line-of-sight detection, chase, ranged/melee attacks, pain states
- Hitscan pistol with muzzle flash and view bobbing
- Health and ammo pickups
- Doom-style HUD: ammo / health / kills counters and a status face that reacts to damage
- Synthesized sound effects via WebAudio (gunshots, fireballs, demon deaths)
- Minimap (toggle with `M`)

## Controls

| Input | Action |
|---|---|
| Click | Lock mouse / fire |
| `WASD` | Move / strafe |
| Mouse or `←` `→` | Turn |
| `Shift` | Run |
| `Space` | Fire |
| `M` | Toggle map |
| `R` | Restart (after death or victory) |

Kill all 10 demons to clear the level.
