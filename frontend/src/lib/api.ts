const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "";

export async function fetchMoods() {
  const res = await fetch(`${API_BASE}/api/v1/moods/`);
  if (!res.ok) throw new Error("Failed to fetch moods");
  return res.json();
}

export async function createMood(data: {
  mood_score: number;
  energy_level: number;
  anxiety_level: number;
  attachment_score?: number;
  label?: string;
}) {
  const res = await fetch(`${API_BASE}/api/v1/moods/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to create mood");
  return res.json();
}

export async function fetchJournals() {
  const res = await fetch(`${API_BASE}/api/v1/journals/`);
  if (!res.ok) throw new Error("Failed to fetch journals");
  return res.json();
}

export async function createJournal(data: {
  title: string;
  content: string;
  mood_tag?: string;
}) {
  const res = await fetch(`${API_BASE}/api/v1/journals/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to create journal");
  return res.json();
}
