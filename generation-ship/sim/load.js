// Load game data from data/*.json (Node). The browser prototype will fetch the same files.
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const DATA = join(dirname(fileURLToPath(import.meta.url)), "..", "data");
const read = (f) => JSON.parse(readFileSync(join(DATA, f), "utf8"));

export function loadData() {
  const data = {
    people: read("people.json"), events: read("events.json"), discoveries: read("discoveries.json"),
    crisis: read("crisis.json"), boards: read("boards.json"), houses: read("houses.json"),
    destinations: read("destinations.json"),
  };
  data.cardById = Object.fromEntries(data.people.map((c) => [c.id, c]));
  data.eventById = Object.fromEntries([...data.events.cards, data.events.landfall].map((e) => [e.id, e]));
  data.discoveryById = Object.fromEntries(data.discoveries.map((d) => [d.id, d]));
  data.houseById = Object.fromEntries(data.houses.houses.map((h) => [h.id, h]));
  return data;
}
