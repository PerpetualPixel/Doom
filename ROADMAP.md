# Roadmap

The working plan for the post-1.0 feature notes. Batches run easiest → hardest;
each batch ships playable. Items marked **needs asset** have a procedural
placeholder in the meantime — drop the real art in and it takes over.

## Batch 1 — mechanics & feel (IN PROGRESS)

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

## Batch 2 — systems (code-only, no assets required)

- [ ] **Save/load, 5 slots** — snapshot of level, skill, player stats,
  progress; save/load screens in the menu. Open question: checkpoint-at-level
  vs full mid-level snapshot.
- [ ] **Custom key binds** — menu that records keys/mouse buttons per action;
  mouse sensitivity slider.
- [ ] **Flashlight** — toggleable cone of light in the view.
- [ ] **Super shotgun** — double-barrel on key 9: huge burst, wide spread,
  slow reload. *Needs asset: gun sprite/sheet; placeholder art until then.*
- [ ] **Green wall switches** — switch tiles that open a linked door
  elsewhere. Map format gains a switch→door pairing.
- [ ] **Vertical aim** — mouse pitch via y-shear (Doom-style look up/down);
  the gun visually tracks.
- [ ] **Wall monitors** — still screens as wall tiles. *Needs asset: Mars
  imagery for the screens; procedural static until then.*
- [ ] **Brutal deaths** — procedural blood spray, gib chunks on overkill,
  harder death sounds. *Needs asset: death/gib sprite sheets + sounds for the
  full effect.*
- [ ] **Exit door** — the iconic exit-sign doorway as a distinct texture/prop.
  *Needs asset or procedural.*

## Batch 3 — renderer (the hard ones)

- [ ] **Variable ceiling heights** — per-area ceiling levels; tall boss
  arenas (the real fix for the boss/roof clamp).
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
