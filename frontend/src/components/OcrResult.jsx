// import React from "react";

// export default function OcrResult({ result }) {
//   if (!result) return null;

//   const lines = result.Blocks?.filter(b => b.BlockType === "LINE") || [];

//   return (
//     <div className="mt-6 bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-lg">
//       <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-200 mb-3">
//         Kết quả OCR
//       </h3>
//       {lines.length === 0 ? (
//         <p className="text-gray-500">Không có văn bản được nhận diện</p>
//       ) : (
//         <ul className="list-disc pl-6 space-y-1">
//           {lines.map((line, idx) => (
//             <li key={idx} className="text-gray-700 dark:text-gray-300">
//               {line.Text}{" "}
//               <span className="text-sm text-gray-400">
//                 ({Math.round(line.Confidence)}%)
//               </span>
//             </li>
//           ))}
//         </ul>
//       )}
//     </div>
//   );
// }



