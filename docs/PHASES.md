# Rewarding the phases in order (RQ-049)

The lead designer's target: a game moves through four phases, and each one
pays for its own play.

| # | phase | rounds | what should pay |
|---|---|---|---|
| 1 | Laning | 1-4 | last-hitting waves, jungle camps |
| 2 | Sieging and objectives | 5-8 | tier-1 towers, Dragon |
| 3 | Team fights and sieging | 9-12 | champion kills, tier-2 towers |
| 4 | Baron and ending | 13+ | Baron, then the Nexus |

## Why it does not happen today

Under rules 1.8.0 with tower 4 / Nexus 8 (RQ-048), the first tower falls in
round 4 and the sieger beats a laning opening 60-40 (RQ-048c). Every structure
is at its weakest from round 1, so a team that walks waves into towers skips
the early phases. A champion kill pays 3 AP, one early wave, and in a 16-game
smoke kills were 2-9% of earned AP in every window: fighting does not pay.

## First proposal: round gates (rejected)

Towers unlocked by round (tier 1 at 5, tier 2 at 9) and the Nexus locked behind
the Baron card or round 16. The smoke ordered the phases (median 17, first tower
round 6, Baron taken in 94%), but the designer rejected gating structure death
behind arbitrary round or monster conditions. The code was removed.

## Current proposal: structures decay, kills pay in waves

The designer's shape (config, off by default, `engine/config.py`):

| knob | meaning |
|---|---|
| `tower_hp`, `nexus_hp` | start high |
| `structure_decay` = 1 | at every Upkeep from round 2, each standing tower and Nexus loses 1 HP, never below `structure_decay_floor` (1) - decay alone never destroys a structure; a team still has to hit it |
| `kill_ap_waves` | a champion kill pays this many of the current minion waves (waves are 3 / 4 / 5 chips as they grow in rounds 7 and 13); 1 = one wave, 2 = two |

A tower that starts at T HP and takes about one hit a round falls near round
(T+1)/2, so a tower 10-12 start puts the first tower in rounds 5-6. Tier-2
towers, reached around round 9, have decayed to a few HP; the Nexus has
decayed most of the way by round 13-15. Early structures are walls, late ones
are glass: laning pays first because sieging is slow, and the game closes by
itself because every structure is getting weaker. Kills paying 1-2 waves makes
a fight worth what a round of farming is.

`SM_g3_phase` (`ai/policy_v1_4_0/machines/gen3.json`) plays the target order -
laner, then sieger/objective from round 5, brawler after a won fight from round
9, objective when the Baron is up from round 10, sieger once it holds Baron - so
the read shows whether playing the phases in order beats ignoring them.

## How it is judged

`tools/phase_read.py` reads the per-round trace every game carries:

1. **Where AP comes from in each window** (lane / jungle / objectives / towers
   / kills, as a share of earned AP). Pass: lane + jungle lead rounds 1-4,
   towers a material share in 5-8, kills a material share in 9-12.
2. **Does the phase leader win?** Win rate of the team ahead on farm at round
   4, on towers taken + Dragons at round 8, on kills in rounds 9-12, and of the
   Baron holder. Pass: every leader above 50% and none above ~80%.
3. **Firsts in order**: first kill, first tower, first Dragon, Baron.
4. **Pacing**: median 13-18, Nexus kills above 90%.
5. **Personality**: no single personality above 60%.

Baseline: `batch_0059` (today's rules, same field and seed). Nothing here goes
into the rulebook until the designer rules on it.

## Result (batches 0065-0068, 600 games each, paired with batch_0059)

Win rate of the team ahead in each phase:

| rules | farm r4 | towers+Dragons r8 | kills r9-12 | Baron holder | median | Nexus kills |
|---|---|---|---|---|---|---|
| today (tower 4 / Nexus 8) | 48.0 | 72.2 | 32.3 | 32.0 | 13 | 100% |
| decay T8/N14, kill 1 wave | 47.8 | 65.6 | 36.8 | 41.7 | 15 | 98.8% |
| decay T8/N14, kill 2 waves | 50.3 | 63.0 | 43.8 | 43.0 | 15 | 100% |
| decay T10/N18, kill 1 wave | 52.7 | 59.5 | 50.2 | 48.7 | 17 | 96.2% |
| **decay T10/N18, kill 2 waves** | **56.4** | **54.2** | **48.5** | **49.7** | 17 | 96.5% |

Recommended: towers start 10 (floor 4), Nexus 18 (floor 8), every structure
loses 1 HP every other round, a champion kill pays two current waves. Every
phase pays and none decides the game alone. Open item: 3.5% of games still
reach round 20; the proposed confirmation lowers the Nexus floor to 6.
