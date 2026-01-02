PROMPT = """
Hãy phân tích bản ghi chép (Transcript) cuộc họp dưới đây. 

Nhiệm vụ của bạn là tách biệt "Substantive content" (nội dung trọng tâm) khỏi "Conversational noise" (nhiễu hội thoại).

- Substantive content bao gồm: các quyết định (decisions), cập nhật dự án (project updates), các vấn đề phát sinh (problems raised), và đề xuất chiến lược (strategic suggestions).
- Noise bao gồm: lời chào hỏi (greetings), xã giao (pleasantries), và các trao đổi ngoài lề không liên quan đến công việc (off-topic remarks).

Yêu cầu:
1. CHỈ trả về "Substantive content".
2. Loại bỏ hoàn toàn mọi lời dẫn giải hoặc kết luận của AI.
3. Trình bày dưới dạng danh sách các ý chính (bullet points) súc tích.
"""