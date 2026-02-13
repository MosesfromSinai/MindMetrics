import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "MindMetrics",
  description: "Emotional insight platform for tracking mood and attachment-related behaviors",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
