import styled from "styled-components";

export default function AboutMe() {
  return <MainContainer>About me</MainContainer>;
}

const MainContainer = styled.div`
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
`;
