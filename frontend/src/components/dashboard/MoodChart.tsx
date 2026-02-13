"use client";

import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const placeholderData = {
  labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
  datasets: [
    {
      label: "Mood",
      data: [6, 7, 5, 8, 6, 7, 9],
      borderColor: "#6366f1",
      backgroundColor: "rgba(99, 102, 241, 0.1)",
      tension: 0.3,
    },
    {
      label: "Energy",
      data: [5, 6, 4, 7, 5, 8, 7],
      borderColor: "#22c55e",
      backgroundColor: "rgba(34, 197, 94, 0.1)",
      tension: 0.3,
    },
    {
      label: "Anxiety",
      data: [4, 3, 6, 2, 4, 2, 1],
      borderColor: "#ef4444",
      backgroundColor: "rgba(239, 68, 68, 0.1)",
      tension: 0.3,
    },
  ],
};

const options = {
  responsive: true,
  plugins: {
    legend: {
      labels: { color: "#ededed" },
    },
  },
  scales: {
    x: {
      ticks: { color: "#888" },
      grid: { color: "#262626" },
    },
    y: {
      min: 0,
      max: 10,
      ticks: { color: "#888" },
      grid: { color: "#262626" },
    },
  },
};

export default function MoodChart() {
  return <Line data={placeholderData} options={options} />;
}
