// Every tunable value and rule toggle (see GDD.md). Override per run.
export const DEFAULT_CONFIG = {
  players: 2,
  houses: ["galvan", "keel"],
  eventPairing: "offset",        // "offset" | "direct"
  decayPerPlayer: 3, decayBase: 1,
  crisisRefillPerPlayer: 1,
  purposePerPlayer: 4,
  discoveriesPerTier: 3,
  stageCounts: { 1: 3, 2: 4, 3: 5 },
  startCredits: 0,
  crewHealth: 2, crewDamage: 2,
  tierConditions: "shifted",    // "shifted": I no threat+no Decay, II no threat, III no Faults/Failures | "classic": I no threat, II no Faults/Failures, III no Failures
  seedGlitches: 1,              // Glitches added per seeded section
  decayThreshold: 2,             // section damage that places Decay
  purposeFault: 1, purposeFailure: 2,
  nomineeFree: true,             // nominee costs 0 credits
  remarkablePerGeneration: 1,    // max Remarkable draw substitutions
  destination: null,            // id from data/destinations.json
  destinationLevel: 0,
  landfallCard: false,          // Landfall card win variant
  maxGenerations: 40,            // safety stop
};
