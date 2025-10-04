# #lưu/lấy document vào MongoDB

# # app/services/ocr_store.py
# from app.models.database import db
# from typing import Dict, Any

# COLNAME = "ocr_results"

# async def save_ocr_result(job_id: str, result: Dict[str, Any]):
#     """
#     Lưu document:
#       {
#         _id: job_id,
#         status: "COMPLETED",
#         result: <raw textract json>,
#         created_at: <iso>
#       }
#     """
#     doc = {
#         "_id": job_id,
#         "status": "COMPLETED",
#         "result": result
#     }
#     await db[COLNAME].insert_one(doc)

# async def get_status(job_id: str):
#     doc = await db[COLNAME].find_one({"_id": job_id}, {"status": 1})
#     if not doc:
#         return {"status": "NOT_FOUND"}
#     return {"status": doc.get("status", "UNKNOWN")}

# async def get_result(job_id: str):
#     doc = await db[COLNAME].find_one({"_id": job_id}, {"result": 1})
#     if not doc:
#         return {"error": "Job not found"}
#     return doc.get("result", {})
# # Có thể thêm các hàm khác để cập nhật status, xóa document, v.v. nếu cần.
# # Nhưng trong ví dụ đơn giản này, ta chỉ cần các hàm cơ bản trên.






# app/services/ocr_store.py

# app/services/ocr_store.py
from app.models.database import ocr_collection

async def save_ocr_result(job_id, result):
    await ocr_collection.insert_one({
        "job_id": job_id,
        "status": "COMPLETED",
        "result": result,
    })

async def get_status(job_id):
    doc = await ocr_collection.find_one({"job_id": job_id}, {"status": 1})
    if not doc:
        return {"status": "NOT_FOUND"}
    return {"status": doc["status"]}

async def get_result(job_id):
    doc = await ocr_collection.find_one({"job_id": job_id}, {"result": 1})
    if not doc:
        return {"error": "Not found"}
    return doc["result"]


# Đây là phiên bản đơn giản, lưu tạm trong dict.
# Trong thực tế, ta sẽ lưu vào MongoDB như trong đoạn code bị comment ở trên.
# Nếu muốn sử dụng MongoDB, chỉ cần thay thế các hàm trên bằng phiên bản
# sử dụng db từ app.models.database.py.
# Ví dụ:
# from app.models.database import db
# await db[COLNAME].insert_one(doc)
# doc = await db[COLNAME].find_one({"_id": job_id}, {"status": 1})
# v.v.
# Lưu ý: các hàm trong ocr_store.py là async, vì vậy khi gọi từ routes/ocr.py
# cần dùng await.
# Điều này giúp tránh blocking event loop của FastAPI.
# Ngoài ra, trong thực tế có thể cần thêm xử lý lỗi, logging, v.v.
# Nhưng trong ví dụ đơn giản này, ta giữ code ngắn gọn và tập trung vào chức năng chính.
# Nếu muốn mở rộng, có thể thêm các hàm để cập nhật status (ví dụ: PROCESSING),
# xóa document, v.v. nếu cần.
# Xem thêm tài liệu của Motor (async MongoDB driver) để biết chi tiết.
# https://motor.readthedocs.io/en/stable/
# Xem thêm tài liệu của FastAPI để biết cách làm việc với async.
# https://fastapi.tiangolo.com/async/
# Xem thêm tài liệu của MongoDB để biết cách thiết kế schema nếu cần.
# https://www.mongodb.com/docs/manual/core/data-modeling-introduction/
# Hoặc có thể thêm các hàm để tìm kiếm, lọc kết quả nếu cần
# (ví dụ: tìm theo ngày tạo, trạng thái, v.v.).
# Nhưng trong ví dụ đơn giản này, ta sẽ giữ code ngắn gọn và tập trung vào chức năng chính.
# Nếu muốn sử dụng MongoDB thật, có thể bỏ comment phần code ở trên.
# Sau đó, thay thế các hàm trong ocr_store.py bằng phiên bản sử dụng MongoDB.
# Ví dụ:
# async def save_ocr_result(job_id: str, result: Dict[str, Any]):
#     doc = {
#         "_id": job_id,
#         "status": "COMPLETED",
#         "result": result
#     }
#     await db[COLNAME].insert_one(doc)
# async def get_status(job_id: str):
#     doc = await db[COLNAME].find_one({"_id": job_id}, {"status": 1})
#     if not doc:
#         return {"status": "NOT_FOUND"}
#     return {"status": doc.get("status", "UNKNOWN")}
# async def get_result(job_id: str):
#     doc = await db[COLNAME].find_one({"_id": job_id}, {"result": 1})
#     if not doc:
#         return {"error": "Job not found"}
#     return doc.get("result", {})
# Lưu ý: khi sử dụng MongoDB, cần đảm bảo rằng MongoDB server đang chạy
# và có thể kết nối được từ ứng dụng FastAPI.
# Nếu sử dụng Docker, có thể cấu hình trong docker-compose.yml để khởi động MongoDB cùng với ứng dụng.
# Xem thêm tài liệu của FastAPI để biết cách làm việc với async.
# https://fastapi.tiangolo.com/async/
# Xem thêm tài liệu của Motor (async MongoDB driver) để biết chi tiết.
# https://motor.readthedocs.io/en/stable/
# Xem thêm tài liệu của MongoDB để biết cách thiết kế schema nếu cần.
# https://www.mongodb.com/docs/manual/core/data-modeling-introduction/
# Hoặc có thể thêm các hàm để tìm kiếm, lọc kết quả nếu cần
# (ví dụ: tìm theo ngày tạo, trạng thái, v.v.).
# Nhưng trong ví dụ đơn giản này, ta sẽ giữ code ngắn gọn và tập trung vào chức năng chính.
# Nếu muốn sử dụng MongoDB thật, có thể bỏ comment phần code ở trên.
# Sau đó, thay thế các hàm trong ocr_store.py bằng phiên bản sử dụng MongoDB.
# Ví dụ:
# async def save_ocr_result(job_id: str, result: Dict[str, Any]):
#     doc = {
#         "_id": job_id,
#         "status": "COMPLETED",
#         "result": result
#     }
#     await db[COLNAME].insert_one(doc)
# async def get_status(job_id: str):
#     doc = await db[COLNAME].find_one({"_id": job_id}, {"status": 1})
#     if not doc:
#         return {"status": "NOT_FOUND"}
#     return {"status": doc.get("status", "UNKNOWN")}
# async def get_result(job_id: str):
#     doc = await db[COLNAME].find_one({"_id": job_id}, {"result": 1})
#     if not doc:
#         return {"error": "Job not found"}
#     return doc.get("result", {})
# Lưu ý: khi sử dụng MongoDB, cần đảm bảo rằng MongoDB server đang chạy
# và có thể kết nối được từ ứng dụng FastAPI.
# Nếu sử dụng Docker, có thể cấu hình trong docker-compose.yml để khởi động MongoDB cùng với ứng dụng.
# Xem thêm tài liệu của FastAPI để biết cách làm việc với async.
# https://fastapi.tiangolo.com/async/
# Xem thêm tài liệu của Motor (async MongoDB driver) để biết chi tiết.
# https://motor.readthedocs.io/en/stable/
# Xem thêm tài liệu của MongoDB để biết cách thiết kế schema nếu cần.
# https://www.mongodb.com/docs/manual/core/data-modeling-introduction/
# Hoặc có thể thêm các hàm để tìm kiếm, lọc kết quả nếu cần
# (ví dụ: tìm theo ngày tạo, trạng thái, v.v.).
# Nhưng trong ví dụ đơn giản này, ta sẽ giữ code ngắn gọn và tập trung vào chức năng chính.
# Nếu muốn sử dụng MongoDB thật, có thể bỏ comment phần code ở trên.
# Sau đó, thay thế các hàm trong ocr_store.py bằng phiên bản sử dụng MongoDB.
# Ví dụ:
# async def save_ocr_result(job_id: str, result: Dict[str, Any]):
#     doc = {
#         "_id": job_id,
#         "status": "COMPLETED",
#         "result": result
#     }
#     await db[COLNAME].insert_one(doc)
# async def get_status(job_id: str):
#     doc = await db[COLNAME].find_one({"_id": job_id}, {"status": 1})
#     if not doc:
#         return {"status": "NOT_FOUND"}
#     return {"status": doc.get("status", "UNKNOWN")}
# async def get_result(job_id: str):
#     doc = await db[COLNAME].find_one({"_id": job_id}, {"result": 1})
#     if not doc:
#         return {"error": "Job not found"}
#     return doc.get("result", {})
# Lưu ý: khi sử dụng MongoDB, cần đảm bảo rằng MongoDB server đang chạy
# và có thể kết nối được từ ứng dụng FastAPI.
# Nếu sử dụng Docker, có thể cấu hình trong docker-compose.yml để khởi động MongoDB cùng với ứng dụng.
# Xem thêm tài liệu của FastAPI để biết cách làm việc với async.
# https://fastapi.tiangolo.com/async/
# Xem thêm tài liệu của Motor (async MongoDB driver) để biết chi tiết.
# https://motor.readthedocs.io/en/stable/
# Xem thêm tài liệu của MongoDB để biết cách thiết kế schema nếu cần.
# https://www.mongodb.com/docs/manual/core/data-modeling-introduction/
# Hoặc có thể thêm các hàm để tìm kiếm, lọc kết quả nếu cần
# (ví dụ: tìm theo ngày tạo, trạng thái, v.v.).
# Nhưng trong ví dụ đơn giản này, ta sẽ giữ code ngắn gọn và tập trung vào chức năng chính.
# Nếu muốn sử dụng MongoDB thật, có thể bỏ comment phần code ở trên.
# Sau đó, thay thế các hàm trong ocr_store.py bằng phiên bản sử dụng MongoDB.
# Ví dụ:
# async def save_ocr_result(job_id: str, result: Dict[str, Any]):
#     doc = {