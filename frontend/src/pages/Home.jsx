import React, { useState } from "react";
import  OcrUpload  from "../components/OcrUpload";
import OcrResult from "../components/OcrResult";
// import { OcrResult } from "../components/OcrResult";

// import PdfReader from "./components/PdfReader";
// import PdfViewer from "../components/PdfViewer";

export default function Home() {
  const [ocrResult, setOcrResult] = useState(null);

  return (
    <div className="max-w-5xl mx-auto py-10">
      <h1 className="text-5xl font-bold text-center mb-10 text-blue-600">
        OCR TEXTRACT APP
      </h1>

      <OcrUpload onResult = {setOcrResult} />
      {/* <PdfReader /> */}
      <OcrResult result={ocrResult} />
    </div>
  );
}




