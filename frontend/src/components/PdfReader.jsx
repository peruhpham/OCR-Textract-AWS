import React, { useState } from "react";
import * as pdfjsLib from "pdfjs-dist";
import "pdfjs-dist/build/pdf.worker.entry"; // quan trọng để PDF.js hoạt động

function PdfReader() {
  const [text, setText] = useState("");

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = async () => {
      const typedArray = new Uint8Array(reader.result);
      const pdf = await pdfjsLib.getDocument(typedArray).promise;
      let fullText = "";

      for (let i = 1; i <= pdf.numPages; i++) {
        const page = await pdf.getPage(i);
        const textContent = await page.getTextContent();
        const pageText = textContent.items.map((item) => item.str).join(" ");
        fullText += pageText + "\n";
      }

      setText(fullText);
    };
    reader.readAsArrayBuffer(file);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "2rem" }}>
      <h2>📄 Đọc và trích xuất nội dung PDF bằng PDF.js</h2>
      <input type="file" accept="application/pdf" onChange={handleFileChange} />
      <textarea
        value={text}
        readOnly
        placeholder="Nội dung PDF sẽ hiển thị ở đây..."
        style={{ width: "80%", height: "400px", marginTop: "1rem" }}
      />
    </div>
  );
}

export default PdfReader;
