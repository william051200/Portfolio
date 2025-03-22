import { useState } from "react";
import { ChevronRight, ChevronLeft } from "@mui/icons-material";
import { Button, MenuItem, Select, TextField } from "@mui/material";
import styled from "styled-components";
import { ConversionType, ConversionTypeList } from "./enums";

export default function BinaryConverter() {
  const numberOfRows = 16;
  const [convertFrom, setconvertFrom] = useState(ConversionType.TEXT);
  const [convertTo, setconvertTo] = useState(ConversionType.TEXT);
  const [inputValue, setInputValue] = useState("");
  const [outputValue, setOutputValue] = useState("");
  const [convertLeftToRight, setConvertLeftToRight] = useState(true);

  const convertTextToBinary = (text) => {
    return text
      .split("")
      .map((char) => {
        return char.charCodeAt(0).toString(2).padStart(8, "0");
      })
      .join(" ");
  };

  const convertBinaryToText = (binary) => {
    // Remove spaces and split into 8-bit chunks
    const bytes = binary.replace(/\s/g, "").match(/.{1,8}/g) || [];

    // Convert each 8-bit binary to character
    return bytes
      .map((byte) => {
        const charCode = parseInt(byte, 2);
        return String.fromCharCode(charCode);
      })
      .join("");
  };

  const convertTextToDecimal = (text) => {
    return text
      .split("")
      .map((char) => char.charCodeAt(0))
      .join(" ");
  };

  const convertDecimalToText = (decimal) => {
    return decimal
      .split(" ")
      .map((num) => String.fromCharCode(num))
      .join("");
  };

  const convertTextToHex = (text) => {
    return text
      .split("")
      .map((char) => char.charCodeAt(0).toString(16))
      .join(" ");
  };

  const convertHexToText = (hex) => {
    return hex
      .split(" ")
      .map((num) => String.fromCharCode(parseInt(num, 16)))
      .join("");
  };

  const convertTextToOctal = (text) => {
    return text
      .split("")
      .map((char) => char.charCodeAt(0).toString(8))
      .join(" ");
  };

  const convertOctalToText = (octal) => {
    return octal
      .split(" ")
      .map((num) => String.fromCharCode(parseInt(num, 8)))
      .join("");
  };

  const convertValue = () => {
    let result = convertLeftToRight ? inputValue : outputValue;

    if (convertFrom === convertTo) {
      if (convertLeftToRight) setOutputValue(result);
      else setInputValue(result);
      return;
    }

    let from = convertLeftToRight ? convertFrom : convertTo;
    let to = convertLeftToRight ? convertTo : convertFrom;

    switch (from) {
      case ConversionType.BINARY:
        result = convertBinaryToText(result);
        break;
      case ConversionType.DECIMAL:
        result = convertDecimalToText(result);
        break;
      case ConversionType.HEXADECIMAL:
        result = convertHexToText(result);
        break;
      case ConversionType.OCTAL:
        result = convertOctalToText(result);
        break;
      default:
        break;
    }

    switch (to) {
      case ConversionType.BINARY:
        result = convertTextToBinary(result);
        break;
      case ConversionType.DECIMAL:
        result = convertTextToDecimal(result);
        break;
      case ConversionType.HEXADECIMAL:
        result = convertTextToHex(result);
        break;
      case ConversionType.OCTAL:
        result = convertTextToOctal(result);
        break;
      default:
        break;
    }

    if (convertLeftToRight) setOutputValue(result);
    else setInputValue(result);
  };

  const switchConversion = () => {
    setConvertLeftToRight(!convertLeftToRight);
  };

  const renderSelection = (value = "", onChangeHandler) => {
    return (
      <TypeSelectorContainer>
        <TypeSelector value={value} onChange={(e) => onChangeHandler(e.target.value)}>
          {ConversionTypeList.map((option) => (
            <MenuItem key={option} value={option}>
              {option}
            </MenuItem>
          ))}
        </TypeSelector>
      </TypeSelectorContainer>
    );
  };

  const renderSection = (
    textFieldValue = "",
    onTextFieldChangeHandler,
    textFieldLabel = "",
    typeValue = "",
    onTypeChangeHandler
  ) => {
    return (
      <SubContainer>
        <FunctionContainer>{renderSelection(typeValue, onTypeChangeHandler)}</FunctionContainer>

        <BottomContainer>
          <StyledTextField
            value={textFieldValue}
            onChange={(e) => onTextFieldChangeHandler(e.target.value)}
            multiline
            fullWidth
            rows={numberOfRows}
            placeholder={textFieldLabel}
          />
        </BottomContainer>
      </SubContainer>
    );
  };

  const renderConvert = () => {
    return (
      <MidContainer>
        <FunctionContainer>
          <Button variant="contained" onClick={convertValue}>
            Convert
          </Button>
        </FunctionContainer>

        <BottomContainer>
          <Button variant="contained" onClick={switchConversion}>
            {convertLeftToRight ? <ChevronRight /> : <ChevronLeft />}
          </Button>
        </BottomContainer>
      </MidContainer>
    );
  };

  return (
    <MainContainer>
      {renderSection(inputValue, setInputValue, "Write your value here...", convertFrom, setconvertFrom)}
      {renderConvert()}
      {renderSection(outputValue, setOutputValue, "Your result output here...", convertTo, setconvertTo)}
    </MainContainer>
  );
}

const MainContainer = styled.div`
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
`;

const SubContainer = styled.div`
  width: calc(100% - 200px);
  height: 500px;
  margin: 20px 50px 20px 50px;
`;

const MidContainer = styled.div`
  width: 200px;
  height: 500px;
  display: flex;
  flex-direction: column;
`;

const FunctionContainer = styled.div`
  height: 80px;
`;

const BottomContainer = styled.div`
  height: 420px;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const TypeSelector = styled(Select)`
  background-color: #ffffff3b;
  width: 300px;
`;

const TypeSelectorContainer = styled.div`
  display: flex;
  justify-content: center;
  width: 100%;
`;

const StyledTextField = styled(TextField)`
  background-color: #ffffff3b;
  border-radius: 10px;
`;
