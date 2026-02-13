export interface MoodEntry {
  id: number;
  mood_score: number;
  energy_level: number;
  anxiety_level: number;
  attachment_score: number | null;
  label: string | null;
  created_at: string;
}

export interface JournalEntry {
  id: number;
  title: string;
  content: string;
  mood_tag: string | null;
  created_at: string;
}
