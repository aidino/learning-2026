previous_summary = "Trong cuộc họp trước, chúng ta đã thống nhất các mục tiêu cho Dự án Phoenix, đồng thời phân công phần việc backend cho Tom và front-end cho Maria."

PROMPT = f"""
Context: Tóm tắt của cuộc họp trước là: 

{previous_summary}

Task: Phân tích nội dung trọng tâm (substantive content) từ cuộc họp mới dưới đây. Hãy đối chiếu và CHỈ xác định, tóm tắt những diễn biến mới, các vấn đề phát sinh, hoặc các quyết định vừa được đưa ra kể từ cuộc họp trước. Tuyệt đối không lặp lại các thông tin đã có trong bản tóm tắt cũ.

New Meeting Content:
---
{{substantive_content}}
---
"""