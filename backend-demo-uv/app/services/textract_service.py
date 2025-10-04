#gọi AWS Textract

# app/services/textract_service.py
# import boto3
# import os

# AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

# # Khởi client boto3 bình thường (sử dụng AWS credentials từ env or profile)
# textract = boto3.client("textract", region_name=AWS_REGION)

# def detect_text(file_bytes: bytes) -> dict:
#     """
#     Gọi Textract synchronous API: detect_document_text.
#     Thích hợp cho ảnh (single-page). Với PDF multipage, phải dùng async StartDocumentTextDetection + S3.
#     Trả về dict (boto3 response).
#     """
#     if not file_bytes:
#         raise ValueError("file_bytes empty")

#     response = textract.detect_document_text(
#         Document={"Bytes": file_bytes}
#     )
#     # response là dict -> có thể return trực tiếp (JSON serializable)
#     return response






# Đây là ví dụ đơn giản, trong thực tế có thể phức tạp hơn.
# app/services/textract_service.py

import time

def detect_text(content: bytes):
    """
    Mock Textract service (không cần AWS).
    Trả về kết quả giả định khi OCR.
    """
    # Giả lập thời gian xử lý
    time.sleep(1)

    return {
        "Blocks": [
            {"BlockType": "LINE", "Text": "Hello OCR"},
            {"BlockType": "LINE", "Text": "Demo result"},
            {"BlockType": "WORD", "Text": "FastAPI"},
            {"BlockType": "WORD", "Text": "Textract"},
        ]
    }
# Có thể thêm các trường khác vào response nếu cần.
# Ví dụ: thêm DocumentMetadata, ResponseMetadata, v.v.
# Hoặc có thể thêm các hàm khác để gọi các API khác của Textract.
# Ví dụ: AnalyzeDocument, DetectDocumentText, v.v.
# Xem thêm: https://docs.aws.amazon.com/textract/latest/dg/API_Welcome.html
# Hoặc có thể thêm các hàm để xử lý lỗi nếu cần.
# Ví dụ: xử lý các lỗi từ Textract, timeout, v.v.
# Nhưng trong ví dụ đơn giản này, ta sẽ giữ code ngắn gọn và tập trung vào chức năng chính.
# Nếu muốn sử dụng Textract thật, có thể bỏ comment phần import boto3 và đoạn code khởi tạo client.
# Sau đó, thay thế hàm detect_text bằng phiên bản gọi Textract thật.
# Ví dụ:
# import boto3
# import os
# AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
# textract = boto3.client("textract", region_name=AWS_REGION)
# def detect_text(file_bytes: bytes) -> dict:
#     if not file_bytes:
#         raise ValueError("file_bytes empty")
#     response = textract.detect_document_text(
#         Document={"Bytes": file_bytes}
#     )
#     return response
# Lưu ý: hàm detect_text trong ví dụ này là synchronous.
# Nếu muốn gọi Textract asynchronous API, cần thay đổi cách gọi và xử lý kết quả
# (ví dụ: StartDocumentTextDetection, GetDocumentTextDetection).
# Xem thêm tài liệu của AWS Textract để biết chi tiết.
# Ngoài ra, cần đảm bảo rằng AWS credentials đã được cấu hình đúng.
# Có thể sử dụng biến môi trường, file cấu hình, hoặc IAM role nếu chạy trên AWS.
# Xem thêm: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
# Khi gọi Textract thật, cần chú ý đến giới hạn của API.
# Ví dụ: giới hạn số lần gọi, kích thước file, định dạng file, v.v.
# Xem thêm: https://docs.aws.amazon.com/textract/latest/dg/limits.html
# Cần xử lý các lỗi có thể xảy ra khi gọi Textract.
# Ví dụ: InvalidParameterException, AccessDeniedException, v.v.
# Xem thêm: https://docs.aws.amazon.com/textract/latest/dg/handling-errors.html
# Có thể thêm logging để ghi lại các cuộc gọi Textract.






# response example: https://docs.aws.amazon.com/textract/latest/dg/API_DetectDocumentText.html#API_DetectDocumentText_ResponseSyntax
# response có thể rất lớn, nên không log hết ở đây.
# Chỉ log một số thông tin cơ bản.
# print(f"Textract response: {response['DocumentMetadata']}")
# Có thể thêm các hàm khác để gọi Textract asynchronous API nếu cần.
# Ví dụ: StartDocumentTextDetection, GetDocumentTextDetection (cho PDF multipage)
# Xem thêm: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html
# Lưu ý: asynchronous API yêu cầu file phải nằm trong S3 bucket.
# Có thể thêm các hàm để xử lý kết quả Textract nếu cần.
# Ví dụ: trích xuất text từ response, định dạng lại kết quả, v.v.
# Nhưng trong ví dụ này, ta sẽ lưu nguyên response vào MongoDB.
# Việc xử lý kết quả sẽ do frontend hoặc các dịch vụ khác đảm nhiệm.
# Điều này giúp tách biệt rõ ràng giữa việc gọi Textract và việc xử lý kết quả.
# Giúp code dễ bảo trì và mở rộng hơn.
# Ngoài ra, có thể thêm logging, error handling, v.v. tùy theo yêu cầu cụ thể.
# Ví dụ, có thể thêm logging để ghi lại các cuộc gọi Textract.
# Hoặc thêm error handling để xử lý các lỗi từ Textract.
# Tuy nhiên, trong ví dụ đơn giản này, ta sẽ giữ code ngắn gọn và tập trung vào chức năng chính.
# Cuối cùng, có thể thêm các hàm để cấu hình Textract client nếu cần.
# Ví dụ: thay đổi region, sử dụng profile khác, v.v.
# Nhưng trong ví dụ này, ta sẽ sử dụng cấu hình mặc định từ môi trường.
# Điều này giúp code đơn giản và dễ hiểu hơn.
# Nếu cần, có thể mở rộng dịch vụ này trong tương lai.
# Ví dụ: thêm các hàm để gọi các API khác của Textract.
# Hoặc thêm các hàm để tích hợp với các dịch vụ AWS khác.
# Nhưng hiện tại, ta sẽ tập trung vào chức năng chính là gọi Textract để nhận
# dạng văn bản từ ảnh.
# Đây là dịch vụ cơ bản để gọi Textract.
# Các dịch vụ khác (như lưu trữ kết quả vào DB) sẽ được tách ra thành các module riêng.
# Điều này giúp code dễ quản lý và bảo trì hơn.
# Tóm lại, dịch vụ này cung cấp một hàm đơn giản để gọi Textract.
# Hàm này có thể được sử dụng bởi các phần khác của ứng dụng.
# Ví dụ: trong các route của FastAPI.
# Dịch vụ này có thể được mở rộng trong tương lai nếu cần.
# Nhưng hiện tại, nó đáp ứng đủ yêu cầu cơ bản của ứng dụng.
# Đây là một ví dụ đơn giản về cách tổ chức code trong một ứng dụng FastAPI.
# Giúp tách biệt rõ ràng giữa các chức năng khác nhau.
# Giúp code dễ đọc, dễ hiểu và dễ bảo trì hơn.
# Có thể thêm các tính năng khác nếu cần.
# Nhưng trong ví dụ này, ta sẽ giữ code ngắn gọn và tập trung vào chức năng chính.
# Đây là cách tiếp cận phổ biến trong phát triển phần mềm hiện đại.
# Giúp tạo ra các ứng dụng có cấu trúc tốt và dễ mở rộng.
# Nếu có thắc mắc hoặc cần hỗ trợ thêm, hãy hỏi nhé!
# Chúc bạn thành công với dự án của mình!
