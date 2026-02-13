import MoodChart from "@/components/dashboard/MoodChart";

export default function Home() {
  return (
    <main style={{ maxWidth: "1200px", margin: "0 auto", padding: "2rem" }}>
      <h1 style={{ fontSize: "2rem", marginBottom: "0.5rem" }}>MindMetrics</h1>
      <p style={{ color: "#888", marginBottom: "2rem" }}>
        Track your emotional patterns and attachment-related behaviors
      </p>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
          gap: "1.5rem",
        }}
      >
        <div
          style={{
            background: "var(--card-bg)",
            border: "1px solid var(--border)",
            borderRadius: "12px",
            padding: "1.5rem",
          }}
        >
          <h2 style={{ fontSize: "1.25rem", marginBottom: "1rem" }}>Mood Trends</h2>
          <MoodChart />
        </div>

        <div
          style={{
            background: "var(--card-bg)",
            border: "1px solid var(--border)",
            borderRadius: "12px",
            padding: "1.5rem",
          }}
        >
          <h2 style={{ fontSize: "1.25rem", marginBottom: "1rem" }}>Journal</h2>
          <p style={{ color: "#888" }}>Your recent journal entries will appear here.</p>
        </div>
      </div>
    </main>
  );
}
