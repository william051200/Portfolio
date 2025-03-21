import { useState } from "react";
import "../assets/App.css";
import AboutMe from "./about_me";
import Tool1 from "./tool_1";
import Tool2 from "./tool_2";
import Skills from "./skills";
import Contact from "./contact";
import styled from "styled-components";

export default function App() {
  // const [count, setCount] = useState(0);

  return (
    <>
      <MainContainer>
        <AboutMe />
        <Tool1 />
        <Tool2 />
        <Skills />
        <Contact />
      </MainContainer>
      {/* <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>count is {count}</button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">Click on the Vite and React logos to learn more</p> */}
    </>
  );
}

const MainContainer = styled.div`
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
`;
