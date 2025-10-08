#kết nối MongoDB bằng motor

from motor.motor_asyncio import AsyncIOMotorClient
import os

# MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")
# MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB", "ocrdb")

client = AsyncIOMotorClient(MONGO_URL)
db = client[MONGO_DB]


#test
# Tạo collection
ocr_collection = db["ocr_results"]

# Đảm bảo có index cho job_id
async def init_db():
    await ocr_collection.create_index([("job_id", ASCENDING)], unique=True)
    
# db là đối tượng database, có thể dùng để truy cập các collection
# Ví dụ: db.ocr_results để truy cập collection ocr_results