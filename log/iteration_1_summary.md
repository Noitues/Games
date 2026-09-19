# Iteration 1 status (Facilitator → lead designer)

1. **Roster expanded to 25 on your instruction** (5 per role). All 15 new kits
   landed inside the 22 ± 2 budget on the first pass, use only Rules 6.3 icons,
   and needed no change to the 14.2 point table. 78 unit tests pass.
2. **`batch_0004`** (400 games, T1 vs T1, roster 1.1.0, seed 525252):
   **0 anomalies**, 98.8% [97.1, 99.5] of games end by Nexus kill.
3. **Pacing slipped out of band**: median 12 rounds [12, 12], against 15
   [14, 15] on the 10-champion roster. The new area and long-range kits close
   games faster; this is a pacing lever question, not a champion question.
4. **Economy is the top open problem.** Four champions exceed 1.5x the roster
   mean (2.16 AP/round): Quillan 5.07x, Sable 3.25x, Ashwyn 3.15x, Ossuar 2.12x.
   Every one of them is an area or multi-hit ability priced at 2 AP or less.
5. **Champion win rates**: Quillan 91.1% [85.8, 94.5] and Noctis 6.5%
   [3.7, 11.2] are the extremes; 8 FAIL and 17 INCONCLUSIVE of 25.
6. **Seat balance improved**: priority 47.5% [42.7, 52.4], against 59.0%
   [52.1, 65.6] on the small roster. The earlier flag looks composition-driven.
   Retest under T2 before spending a lever on it.
7. **Sampling cost of 25 champions** (RQ-028): each champion now plays 40% of
   games, so champion verdicts at the Rules 14.3 precision need roughly
   5,000-game batches. 400 games is a smoke read, not a balance read.
8. **Triage order unchanged**: AI competence first. T2_search and the exploit
   set come before any champion patch, because usage rates (47/58 abilities
   outside 40-70%) and the Quillan/Noctis spread may be T1's blind spots, not
   the kits'. Still waiting on you: RQ-001, RQ-002, RQ-016.
