import React, { useState, useEffect } from "react";
import { Document, Page, pdfjs } from "react-pdf";
// import "react-pdf/dist/Page/AnnotationLayer.css";

pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.min.js`;

export default function PdfViewer({ file }) {
  const [fileURL, setFileURL] = useState(null);
  const [numPages, setNumPages] = useState(null);
  const [pageNumber, setPageNumber] = useState(1);
  const [scale, setScale] = useState(1.0);

  useEffect(() => {
    if (file) {
      setFileURL(URL.createObjectURL(file));
      setPageNumber(1);
      setNumPages(null);
    }
    return () => fileURL && URL.revokeObjectURL(fileURL);
  }, [file]);

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
  }

  return (
    <div className="flex flex-col items-center">
      <div className="flex gap-2 mb-2">
        <button
          disabled={pageNumber <= 1}
          onClick={() => setPageNumber((p) => p - 1)}
          className="px-3 py-1 bg-indigo-500 text-white rounded disabled:opacity-50"
        >
          Prev
        </button>
        <span className="px-2 py-1 bg-gray-200 rounded">
          Trang {pageNumber} / {numPages ?? "—"}
        </span>
        <button
          disabled={numPages && pageNumber >= numPages}
          onClick={() => setPageNumber((p) => p + 1)}
          className="px-3 py-1 bg-indigo-500 text-white rounded disabled:opacity-50"
        >
          Next
        </button>
        <button
          onClick={() => setScale((s) => Math.max(0.5, s - 0.1))}
          className="px-2 py-1 bg-gray-300 rounded ml-2"
        >
          Zoom -
        </button>
        <button
          onClick={() => setScale((s) => Math.min(3, s + 0.1))}
          className="px-2 py-1 bg-gray-300 rounded"
        >
          Zoom +
        </button>
      </div>
      <div className="border rounded shadow bg-white p-2">
        <Document file={fileURL} onLoadSuccess={onDocumentLoadSuccess}>
          <Page pageNumber={pageNumber} width={700} scale={scale} />
        </Document>
      </div>
    </div>
  );
}



