// src/components/OcrUpload.jsx
import React, { useState } from "react";
import { uploadFile, getStatus, getResult } from "../services/api";
import PdfViewer from "./PdfViewer";

export default function OcrUpload({ onResult }) {
  const [file, setFile] = useState(null);
  const [jobId, setJobId] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Hãy chọn file trước!");

    setLoading(true);
    const data = await uploadFile(file);
    // debug
    if (!data.job_id) {
      alert("Upload thất bại! Kiểm tra lại backend.");
      setLoading(false);
      return;
    }
    // Lưu jobId để hiển thị
    setJobId(data.job_id);

    // Polling để check status job
    const poll = setInterval(async () => {
      const s = await getStatus(data.job_id);
      if (s.status === "COMPLETED") {
        clearInterval(poll);
        const r = await getResult(data.job_id);
        onResult(r);     // gửi kết quả cho Home
        setLoading(false);
      }
    }, 2000);
  };

  return (
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

    {/* Hiển thị PDF Viewer nếu là file PDF */}
        {file && file.type === "application/pdf" && (
  <div className="my-4 border rounded-xl shadow bg-gray-50 dark:bg-gray-900 p-2">
    <PdfViewer file={file} />
  </div>
)}

      <button
        onClick={handleUpload}
        disabled={loading}
        className="w-full bg-indigo-600 text-white py-2 rounded-lg 
                   hover:bg-indigo-700 disabled:opacity-50"
      >

        {loading ? "Đang xử lý..." : "Upload & OCR"}
      </button>

      {jobId && (
        <p className="mt-3 text-sm text-gray-500">Job ID: {jobId}</p>
      )}
    </div>
  );
}




// // File: src/components/OcrUpload.jsx

// import React, { useState } from "react";

// export default function OcrUpload() {
//   const [file, setFile] = useState(null);
//   const [jobId, setJobId] = useState(null);
//   const [result, setResult] = useState(null);
//   const [loading, setLoading] = useState(false);

//   const upload = async () => {
//     if (!file) return alert("Chọn file trước");
//     setLoading(true);
//     const form = new FormData();
//     form.append("file", file);

//     const res = await fetch("/api/upload", { method: "POST", body: form });
//     const data = await res.json();
//     setJobId(data.job_id);

//     const poll = setInterval(async () => {
//       const r = await fetch(`/api/status/${data.job_id}`);
//       const s = await r.json();
//       if (s.status === "COMPLETED") {
//         clearInterval(poll);
//         const rr = await fetch(`/api/result/${data.job_id}`);
//         setResult(await rr.json());
//         setLoading(false);
//       }
//     }, 2000);
//   };

//   return (
//     <div className="max-w-xl mx-auto bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg mt-8">
//       <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
//         OCR - Nhận diện văn bản
//       </h2>

//       <label className="block mb-4">
//         <span className="sr-only">Chọn file</span>
//         <input
//           type="file"
//           accept="image/*,application/pdf"
//           className="block w-full text-sm text-gray-500
//                      file:mr-4 file:py-2 file:px-4
//                      file:rounded-full file:border-0
//                      file:text-sm file:font-semibold
//                      file:bg-indigo-50 file:text-indigo-700
//                      hover:file:bg-indigo-100"
//           onChange={(e) => setFile(e.target.files[0])}
//         />
//       </label>

//       <button
//         onClick={upload}
//         disabled={loading}
//         className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg 
//                    hover:bg-indigo-700 disabled:opacity-50 transition-colors"
//       >
//         {loading ? "Đang xử lý..." : "Upload & OCR"}
//       </button>

//       {jobId && (
//         <p className="mt-4 text-sm text-gray-600 dark:text-gray-300">
//           Job ID: {jobId}
//         </p>
//       )}

//       {result && (
//         <div className="mt-6">
//           <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-2">
//             Kết quả OCR
//           </h3>
//           <pre className="bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-200 p-3 rounded-lg overflow-x-auto whitespace-pre-wrap text-sm">
//             {JSON.stringify(result, null, 2)}
//           </pre>
//         </div>
//       )}
//     </div>
//   );
// }
// // File: src/App.jsx

