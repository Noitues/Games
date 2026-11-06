// Seeded RNG (mulberry32). State lives in the game state so clones stay deterministic.
export function nextRandom(st) {
  st.rng = (st.rng + 0x6D2B79F5) | 0;
  let t = st.rng;
  t = Math.imul(t ^ (t >>> 15), t | 1);
  t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
  return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
}
export const randInt = (st, n) => Math.floor(nextRandom(st) * n);
export const pick = (st, arr) => arr[randInt(st, arr.length)];
export function shuffle(st, arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = randInt(st, i + 1);
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}
