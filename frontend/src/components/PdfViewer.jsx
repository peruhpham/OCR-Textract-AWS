import React, { useState } from "react";
import { Document, Page, pdfjs } from "react-pdf";
import "react-pdf/dist/Page/AnnotationLayer.css";

// Khai báo worker
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.min.js`;

export default function PdfViewer({ file }) {
  const [numPages, setNumPages] = useState(null);
  const [pageNumber, setPageNumber] = useState(1);

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
    setPageNumber(1);
  }

  const goToPrevPage = () => setPageNumber((p) => Math.max(p - 1, 1));
  const goToNextPage = () => setPageNumber((p) => Math.min(p + 1, numPages));

  return (
    <div className="pdf-viewer bg-white dark:bg-gray-800 p-4 rounded-xl shadow">
      <Document
        file={file}
        onLoadSuccess={onDocumentLoadSuccess}
        onLoadError={(err) => console.error("PDF load error:", err)}
        loading="Đang tải PDF..."
      >
        <Page pageNumber={pageNumber} />
      </Document>
      {numPages && (
        <div className="flex items-center justify-center gap-4 mt-4">
          <button
            onClick={goToPrevPage}
            disabled={pageNumber <= 1}
            className="px-3 py-1 bg-indigo-500 text-white rounded disabled:opacity-50"
          >
            Prev
          </button>
          <span>
            Trang {pageNumber} / {numPages}
          </span>
          <button
            onClick={goToNextPage}
            disabled={pageNumber >= numPages}
            className="px-3 py-1 bg-indigo-500 text-white rounded disabled:opacity-50"
          >
            Next
          </button>
        </div>
      )}
    </div>
  );
}
