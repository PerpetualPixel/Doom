# Roadmap

The working plan for the post-1.0 feature notes. Batches run easiest → hardest;
each batch ships playable. Items marked **needs asset** have a procedural
placeholder in the meantime — drop the real art in and it takes over.

## Batch 1 — mechanics & feel (DONE)

- [x] **Armor system** — armor stat capped at 200, soaks 1/3 of every hit until it
  breaks. Pickups: helmet (+1), green armor (fills to 100), blue armor (fills
  to 200, rare). HUD shows ARMOR. *Placeholder sprites; needs asset: helmet +
  armor pickup art.*
- [x] **Weapon drops** — sergeants drop their shotgun (weapon if you lack it,
  shells either way); barons drop a rocket launcher + rockets; zombies keep
  dropping clips.
- [x] **Boss tuning** — faster movement, tighter shot group, faster fire rate.
  Sprite no longer pokes through the ceiling (interim clamp — the real fix is
  tall arena ceilings, Batch 3).
- [x] **Movement** — sprint removed; base speed is fast, and holding forward
  accelerates to a top speed. Slight speed-scaled view bob.
- [x] **Minigun** — chaingun reworked: spin-up before it fires, then a much
  faster stream.
- [x] **Hip fire vs ADS** — right mouse aims: tighter grouping and a slight
  zoom; hip fire is a wider spray.
- [x] **Bullet sparks & ricochet** — missed hitscan shots spark on the wall
  they hit, with an occasional ricochet ping.
- [x] **Muzzle light** — firing (and nearby fireballs) briefly lights the
  surroundings. Cheap radial version; true dynamic lights are Batch 3.
- [x] **Deeper liquid pits** — water/nukage sit lower still; walking out
  always works.
- [x] **Automap defaults** — smallest size, 50% opacity.
- [x] **Door open/close sounds** — synth grind + thunk fallback existed for
  nothing; now audible everywhere. *Needs asset: real door sfx if wanted.*
- [x] **Gun size** — first-person weapons scaled down ~15%.

## Batch 2 — systems (DONE)

- [x] **Save/load, 5 slots** — full mid-level snapshot (position, health,
  armor, arsenal, every monster, every door, thrown switches, automap fog).
  Save from the pause menu, load from the title or pause menu.
- [x] **Custom key binds** — controls menu records a new key per action
  (clashing keys swap); mouse sensitivity slider. Stored with the other prefs.
- [x] **Flashlight** — F toggles a cone of light around the view centre.
- [x] **Super shotgun** — double-barrel on key 9: 16 pellets, wide spread,
  two shells a pull, slow reload. One sergeant in four from E2 on drops it.
  *Placeholder art; needs asset: gun sprite/sheet.*
- [x] **Scroll wheel** — cycles the arsenal in slot order, skipping empty guns.
- [x] **Green wall switches** — V/Y map tiles: throwing the switch (it stays
  thrown) raises every switch door in the level, permanently. Switch vaults
  live on E1M1, E2M2, E3M3.
- [x] **Vertical aim** — mouse pitch via y-shear; walls stay vertical, the
  crosshair rides the horizon, the gun tracks.
- [x] **Wall monitors** — Mars on animated-static screens, dressed onto tech
  walls procedurally (hash-picked, so they never move). *Needs asset: real
  monitor imagery.*
- [x] **Brutal deaths** — blood spray on every hit; overkill gibs the monster
  into flying chunks and leaves a floor stain instead of a corpse, with a wet
  synth burst. *Needs asset: death/gib sheets + sounds for the full effect.*
- [x] **Exit door** — the exit is now a recessed doorway under a glowing red
  EXIT sign.

## Batch 3 — renderer (the hard ones)

- [ ] **Variable ceiling heights** — per-area ceiling levels; tall boss
  arenas (the real fix for the boss/roof clamp). The plan, per Pixel: every
  map distinct — some rooms with no ceiling at all, big rooms with open
  strips or one big hole, small corridors reading as tunnels, high perches
  with windows; variety in wall/ceiling dressing per area.
- [ ] **Open-sky areas** — zones with no ceiling showing a hell skybox, plus
  distance terrain on the horizon. *Needs asset: skybox art; procedural sky
  until then.*
- [ ] **Ceiling lights** — fixtures in white/red/blue by area, some
  flickering, lighting the cells beneath.
- [ ] **Slitted walls & windows** — partially see-through wall types you
  can't walk through.
- [ ] **Tall standing lights** and other solid props.
- [ ] **Stairs / slopes** — genuinely hard in a 2D-grid raycaster; needs a
  floor-height pass like the ceiling one. Feasibility after variable
  ceilings.
- [ ] **True dynamic lights** — fireballs/plasma lighting walls as they fly.

## Assets wanted (everything has a placeholder until provided)

| Asset | Used for |
|---|---|
| Helmet + green/blue armor pickup art | Batch 1 armor |
| Liquid animation sheets (water/nukage/lava) | animated pits & barrels |
| Gun firing animation sheets (per weapon) | weapon feel |
| Super shotgun sprite | Batch 2 weapon 9 |
| Wall/floor/ceiling texture images | texture pass (same pipeline as the doors: drop in `textures/`, add to the loader, rerun `tools/embed_assets.py`) |
| Monitor screen images (Mars) | wall monitors |
| Hell skybox + horizon terrain | open-sky areas |
| Death/gib sprite sheets + brutal sounds | Batch 2 deaths |
| Door open/close sounds | replaces synth fallback |
