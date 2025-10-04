// src/pages/Home.jsx
import React, { useState } from "react";
import OcrUpload from "../components/OcrUpload";
import OcrResult from "../components/OcrResult";

export default function Home() {
  const [ocrResult, setOcrResult] = useState(null);

  return (
    <div className="max-w-3xl mx-auto py-10">
      <h1 className="text-3xl font-bold text-center mb-10">
        OCR Textract App
      </h1>
      <OcrUpload onResult={setOcrResult} />
      
      <OcrResult result={ocrResult} />
    </div>
  );
}




// // File: src/pages/Home.jsx
// import React, { useState } from "react";
// import OcrUpload from "../components/OcrUpload";
// import OcrResult from "../components/OcrResult";

// export default function Home() {
//   const [result, setResult] = useState(null);

//   return (
//     <div className="max-w-3xl mx-auto py-10">
//       <h1 className="text-3xl font-bold text-center mb-8">OCR Textract App</h1>
//       <OcrUpload onResult={setResult} />
//       <OcrResult result={result} />
//     </div>
//   );
// }
// // Compare this snippet from frontend/src/components/OcrUpload.jsx:
// // // File: src/components/OcrUpload.jsx
// // import React, { useState } from "react";