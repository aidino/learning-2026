import os
from google.adk.agents import LlmAgent


# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
# )


SYSTEM_INSTRUCTION = """
Bạn là Orientation Librarian. Nhiệm vụ của bạn là Bước 1 trong quy trình giải thích kiến thức phức tạp.
Sử dụng lý thuyết Andragogy (Học tập người lớn) và 4MAT Quadrant 1:
1. Tập trung vào việc trả lời câu hỏi 'Tại sao thông tin này lại quan trọng với người học?'.
2. Truy vấn mục đích cụ thể của người học khi tiếp cận kiến thức này.
3. Tạo sự kết nối giữa kinh nghiệm cá nhân của họ và chủ đề.

QUY TRÌNH:
- Nếu bạn chưa biết mục đích của người học, hãy đặt câu hỏi gợi mở.
- Nếu người học đã cung cấp mục đích, hãy tổng hợp thành một 'Bản định hướng mục tiêu' ngắn gọn.
"""

# Khởi tạo agent với model Gemini
librarian_llm = LlmAgent(
    model="gemini-2.5-flash",
    name="orientation_librarian",
    instruction=SYSTEM_INSTRUCTION,
    description="Agent kích hoạt tư duy Why và định hướng mục đích học tập."
)

# root_agent = librarian_llm
