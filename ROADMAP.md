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

## Batch 3 — renderer (DONE)

- [x] **Variable ceiling heights** — every cell now has one, derived from
  the level's own shape: squeezed corridors press down into tunnels, big
  rooms rise to 2.2, boss arenas higher still. Walls stand as tall as the
  room they face (textures tile up), and every ceiling step shows a real
  upper face. Each level rolls one of three habits — holes, strips, or
  closed-and-tall — so no two maps read alike.
- [x] **Open-sky areas** — rooms with no ceiling show a procedural skybox
  (Mars dusk for the installations, a blood sky for hell) with silhouetted
  distance terrain, stars, a sick sun, and embers on the crags. The sky
  pans with the view and shears with mouselook. *Still happy to take real
  skybox art.*
- [x] **Ceiling lights** — fixtures set into normal and tunnel ceilings
  (white/blue on Mars, red in hell), pooling light on the floor beneath;
  roughly one in four guns its ballast and flickers, and anything standing
  in the pool is lit too.
- [x] **Slitted walls & windows** — window walls with a see-through slit:
  sight and hitscan pass, bodies and fireballs don't. Placed on
  single-thickness walls between open areas; that geometry is rare in the
  current maps, so they're sparse — density grows when maps gain authored
  perches.
- [x] **Tall standing lights** — pole lamps ring the big and open-air rooms
  (where there's no ceiling to hang a fixture from), glowing and guttering
  in step with the light they cast.
- [x] **Stairs & raised floors** (the floor-height batch) — per-cell floor
  heights: knee-high daises out on the big floors (walk straight up from
  any side), waist-high perches against the walls, each with its step
  cell and a prize on top — most of them under a window, so a perch with
  a view actually happens. A walker climbs at most a step's height per
  stride and drops any distance freely; monsters obey the same rule.
  Melee and pickups respect height, platform tops cast on their own
  planes, risers draw as real faces, walls start at the platform behind
  them, and everything standing on a platform rides it. True slopes
  remain out of scope for a grid raycaster.
- [x] **True dynamic lights** — every flying shot projects to the screen
  and lights the walls, doors and sprites near its column, strongest at
  its own depth. Rockets and BFG bursts light rooms as they cross them.

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
