// The 15-day programme. Shared by index.html (day map) and day.html (lesson viewer).
window.P2P_DAYS = [
  { day: 1,  level: 1, title: "What's actually on the other side" },
  { day: 2,  level: 1, title: "The anatomy of a good prompt" },
  { day: 3,  level: 1, title: "Be specific, then iterate" },
  { day: 4,  level: 2, title: "Show, don't tell" },
  { day: 5,  level: 2, title: "Let it think" },
  { day: 6,  level: 2, title: "Output that computers can read" },
  { day: 7,  level: 2, title: "System prompts and personas" },
  { day: 8,  level: 2, title: "Prompt chains" },
  { day: 9,  level: 3, title: "Prompting through an API" },
  { day: 10, level: 3, title: "Give it your documents (RAG)" },
  { day: 11, level: 3, title: "Tools, agents and testing" },
  { day: 12, level: 4, title: "Direct prompt injection" },
  { day: 13, level: 4, title: "Indirect prompt injection" },
  { day: 14, level: 4, title: "Defence in depth" },
  { day: 15, level: 4, title: "Build it, break it, fix it" }
];

window.P2P_LEVELS = {
  1: "Foundations",
  2: "Techniques",
  3: "Real systems",
  4: "Security"
};

// Progress is stored per browser: { "3": [true, false, ...] } = to-do ticks for day 3.
window.P2P_PROGRESS = {
  key: "p2p-day-todos",
  load: function () {
    try { return JSON.parse(localStorage.getItem(this.key) || "{}") || {}; } catch (e) { return {}; }
  },
  save: function (state) {
    try { localStorage.setItem(this.key, JSON.stringify(state)); } catch (e) {}
  },
  // Returns 0-100 for one day, based on its ticked to-do items.
  percent: function (state, day) {
    var ticks = state[String(day)];
    if (!ticks || !ticks.length) return 0;
    var done = ticks.filter(Boolean).length;
    return Math.round(done / ticks.length * 100);
  }
};
