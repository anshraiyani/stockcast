import { blue } from "@mui/material/colors";
import React from "react";
import { useState, useEffect } from "react";
import ReactApexChart from "react-apexcharts";
import ReactLoading from "react-loading"

export default function Chart({ choice }) {
  const [data, setData] = useState(null);
  const [loading,setLoading] = useState(false)

  const fetchData = (choice) => {
    fetch(`candlestick/${choice.split(".")[0]}.json`)
      .then((response) => response.json())
      .then((jsonData) => {
        setData(jsonData);
        setLoading(false)
        console.log("data set");
      })
      .catch((error) => {
        console.error("Error loading data:", error);
      });
  };

  useEffect(() => {
      setData(null)
      // setLoading(true)
      fetchData(choice);
  }, [choice]);

  const series = [
    {
      name: "candle",
      data: data,
    },
  ];

  const options = {
    chart: {
      type: "candlestick",
      height: 350,
      zoom: {
        enabled: true,
        type: "x",
        autoScaleYaxis: false,
        zoomedArea: {
          fill: {
            color: "#90CAF9",
            opacity: 0.4,
          },
          stroke: {
            color: "#0D47A1",
            opacity: 0.4,
            width: 1,
          },
        },
      },
    },
    title: {
      text: choice,
      align: "left",
    },
    xaxis: {
      type: "category",
    },
    yaxis: {
      tooltip: {
        enabled: true,
      },
    },
    annotations: {
      xaxis: [
        {
          x: data ? data[data.length - 4]["x"] : 123,
          borderColor: "#00E396",
          label: {
            borderColor: "#00E396",
            style: {
              fontSize: "12px",
              color: "#fff",
              background: "#00E396",
            },
            orientation: "horizontal",
            offsetY: 7,
            text: "Prediction",
          },
        },
      ],
    },
  };

  return (
    <div className="chart-container">
      {data ? (
        <ReactApexChart
          series={series}
          options={options}
          type="candlestick"
          height={600}
          width={850}
        />
      ) : <ReactLoading type={"spin"} color={blue} height={80} width={80}  />}
      {
        // data &&
        // <p>{data[data.length - 4]["x"]}</p>
        // console.log(data)
      }
    </div>
  );
}
