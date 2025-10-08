import React, { useState } from "react";
import { uploadFile, getStatus, getResult } from "../services/api";
import PdfViewer from "../components/PdfViewer";

export default function OcrUpload({ onResult }) {
  const [file, setFile] = useState(null);
  const [jobId, setJobId] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Hãy chọn file trước!");

    setLoading(true);
    const data = await uploadFile(file);

    //debug
    if (!data.job_id) {
      alert("Upload thất bại! Kiểm tra lại backend.");
      setLoading(false);
      return;
    }
    // Luu jobId de hien thi
    setJobId(data.job_id);

    // Polling trang thai job, Polling để check status job
    const poll = setInterval(async () => {
      const s = await getStatus(data.job_id);
      if (s.status === "COMPLETED") {
        clearInterval(poll);
        const r = await getResult(data.job_id);
        onResult(r);
        setLoading(false);
      }
    }, 2000);
  };

  return (
    <div className="max-w-5xl mx-auto py-2">
      {/* <h1 className="text-3xl font-bold text-center mb-8">OCR Textract App</h1> */}
      <div className="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg">
        <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-4">
          Upload file OCR
        </h2>
        <input
          type="file"
          accept="image/*,application/pdf"
          onChange={(e) => setFile(e.target.files[0])}
          className="block w-full text-sm text-gray-500 mb-4
                     file:mr-4 file:py-2 file:px-4
                     file:rounded-full file:border-0
                     file:text-sm file:font-semibold
                     file:bg-indigo-50 file:text-indigo-700
                     hover:file:bg-indigo-100"
        />

        {/* Nếu là file PDF thì hiển thị preview */}
        {file && file.type === "application/pdf" && (
          <div className="my-4 border rounded-xl shadow bg-gray-50 dark:bg-gray-900 p-2">
            <PdfViewer file={file} />
          </div>
        )}

        <button
          onClick={handleUpload}
          disabled={loading}
          className="w-full bg-indigo-600 text-white py-2 rounded-lg 
                     hover:bg-indigo-700 disabled:opacity-50 mt-4"
        >
          {loading ? "Đang xử lý..." : "Upload & OCR"}
        </button>

        {jobId && (
          <p className="mt-3 text-sm text-gray-500">Job ID: {jobId}</p>
        )}
      </div>
    </div>
  );
}



