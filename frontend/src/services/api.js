// File: src/services/api.js
const BASE_URL = "http://localhost:8000"; // // backend FastAPI chạy ở port 8000

export async function uploadFile(file) {
  const form = new FormData();
  form.append("file", file);
  const res = await fetch(`${BASE_URL}/api/upload`, { method: "POST", body: form });
  return res.json();
}

export async function getStatus(jobId) {
  const res = await fetch(`${BASE_URL}/api/status/${jobId}`);
  return res.json();
}

export async function getResult(jobId) {
  const res = await fetch(`${BASE_URL}/api/result/${jobId}`);
  return res.json();
}
// Compare this snippet from frontend/src/components/OcrResult.jsx: