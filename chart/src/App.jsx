import React, { useState } from "react";
import Chart from "./components/Chart";
import Search from "./components/Search";
import Header from "./components/Header";
import News from "./components/News";
// import 'bootstrap/dist/css/bootstrap.min.css';
function App() {
  const [choice, setChoice] = useState("RELIANCE");

  return (
    <>
      <Header />
      <div className="main-container">
        <Search setChoice={setChoice} />
        <Chart choice={choice} />
        <News />
      </div>
    </>
  );
}

export default App;
