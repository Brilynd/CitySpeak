import React from "react";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend);

export const data = (cleanData) => {
  return ({
  labels: ["Culture", "Economic", "Health", "Social"],
  datasets: [
    {
      label: "# of Votes",
      data: cleanData,
      backgroundColor: [
        "rgba(255, 99, 132, 0.2)",
        "rgba(54, 162, 235, 0.2)",
        "rgba(255, 206, 86, 0.2)",
        "rgba(75, 192, 192, 0.2)"
      ],
      borderColor: [
        "rgba(255, 99, 132, 1)",
        "rgba(54, 162, 235, 1)",
        "rgba(255, 206, 86, 1)",
        "rgba(75, 192, 192, 1)"
      ],
      borderWidth: 1,
    },
  ],
})
};

export function PieChart(props) {


  const analytics = props.data.analytics;
  let cleanData = [0,0,0,0];
  if (analytics != undefined) {
    const sum = Object.values(analytics).reduce((a, b) => a + b, 0)
    cleanData = [
      analytics.culture / sum,
      analytics.economic / sum,
      analytics.health / sum,
      analytics.social / sum
    ]
  }
  

  return <Pie data={data(cleanData)}  />;
}
