# Iteration 0 status (Facilitator → lead designer)

1. **Phase 0 exit met.** 76/76 engine unit tests pass; `batch_0002` (200 games,
   T1 vs T1, seed 424242) ran with **0 anomalies** and no illegal states.
2. **Pacing already passes.** Median game length 15 rounds [14, 15]; 99.5%
   [97.2, 99.9] of games end by Nexus kill before round 20.
3. **Champion balance fails, hard.** Ashwyn 88.0% WR [82.8, 91.8]; Vellum 12.0%
   [8.2, 17.2]. Nothing else is decided (8 of 10 inconclusive at n=200).
4. **Economy outlier.** Ashwyn earns 7.80 AP/round = 4.07x the roster mean
   (1.92); its W (AREA 1 at range 2 for 1 AP) is the driver.
5. **Ability usage is not trustworthy yet** (20/26 AP-cost abilities outside
   40-70%): T2 does not exist, so this is AI competence, not kit design.
6. **Seat balance flagged**: priority 59.0% [52.1, 65.6] under T1, 68.3% under
   T0. Retest under T2 before touching any lever.
7. **AI acceptance**: T1 beat T0 in 100/100 games (target >=90%). T2_search and
   the exploit set are Phase 1.
8. **Needs your decision**: RQ-001/RQ-002 (can units and towers inside a hidden
   tile be reached at tile range?) and RQ-016 (engine ends movement on a flip).
   Everything else is ruled and logged.

Next: Phase 1 (T2 + exploit policies), then triage in category order - AI
competence before pacing, economy before champion win rates.
