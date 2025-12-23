# ReAct Prompting 

Reference: https://www.promptingguide.ai/techniques/react

ReAct (viết tắt của **Reason** + **Act**) là một bước tiến đột phá trong kỹ thuật Prompt Engineering, giúp mô hình ngôn ngữ lớn (LLM) không chỉ "suy nghĩ" mà còn biết "hành động" để giải quyết các tác vụ phức tạp.

Dưới đây là cái nhìn chi tiết và cập nhật nhất về ReAct tính đến năm 2025.

---

## 1. Định nghĩa cốt lõi

**ReAct Prompting** là một kỹ thuật hướng dẫn AI kết hợp đồng thời hai khả năng: **Suy luận logic (Reasoning)** và **Thực hiện hành động (Acting)**.

Thay vì chỉ đưa ra câu trả lời dựa trên dữ liệu cũ có sẵn trong "não bộ", AI sẽ:

1. Viết ra các bước tư duy (Thought).
2. Tự chọn và sử dụng công cụ bên ngoài như Google Search, máy tính, hoặc API (Action).
3. Quan sát kết quả từ công cụ đó (Observation).
4. Lặp lại quá trình này cho đến khi có câu trả lời cuối cùng.

---

## 2. Nguyên lý hoạt động (Vòng lặp ReAct)

ReAct hoạt động theo một vòng lặp khép kín được gọi là **Thought-Action-Observation**.

### Ví dụ thực tế:

**Câu hỏi:** "Vợ của đạo diễn vừa thắng giải Oscar 2024 hiện đang tham gia dự án phim nào?"

* **Thought 1 (Tư duy):** Đầu tiên, tôi cần tìm xem ai là người thắng giải Đạo diễn xuất sắc nhất tại Oscar 2024.
* **Action 1 (Hành động):** `Search[Oscar 2024 Best Director winner]`
* **Observation 1 (Quan sát):** Kết quả: Christopher Nolan (phim Oppenheimer).
* **Thought 2 (Tư duy):** Bây giờ tôi cần tìm vợ của Christopher Nolan là ai.
* **Action 2 (Hành động):** `Search[Who is Christopher Nolan's wife?]`
* **Observation 2 (Quan sát):** Kết quả: Emma Thomas.
* **Thought 3 (Tư duy):** Cuối cùng, tôi cần tìm các dự án phim hiện tại mà Emma Thomas đang tham gia.
* **Action 3 (Hành động):** `Search[Emma Thomas current movie projects 2025]`
* **Observation 3 (Quan sát):** Kết quả: Cô đang sản xuất bộ phim mới của Nolan dự kiến ra mắt năm 2026.
* **Final Answer:** Vợ của Christopher Nolan là Emma Thomas, bà đang tham gia sản xuất dự án phim bí mật tiếp theo của chồng dự kiến ra mắt vào năm 2026.

---

## 3. Ưu điểm và Nhược điểm

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Độ chính xác** | Giảm thiểu hiện tượng "ảo giác" (hallucination) nhờ tra cứu thông tin thực tế. | Phụ thuộc hoàn toàn vào chất lượng công cụ (ví dụ: Google Search trả về kết quả sai). |
| **Tính minh bạch** | Người dùng có thể theo dõi từng bước tư duy của AI (Traceability). | Tốn nhiều Token hơn vì AI phải viết ra cả quá trình suy nghĩ. |
| **Khả năng** | Giải quyết được các tác vụ cần thông tin thời gian thực hoặc tính toán phức tạp. | Độ trễ (Latency) cao do phải đợi kết quả từ các Action bên ngoài. |

---

## 4. Những quan niệm sai lầm phổ biến

1. **"ReAct chỉ là Chain-of-Thought (CoT)":** * *Sự thật:* CoT chỉ là "suy nghĩ nội tâm" của AI. ReAct là CoT **cộng thêm** khả năng tương tác với thế giới thực. CoT có thể sai nếu AI không biết kiến thức đó, còn ReAct sẽ đi tìm kiến thức đó.
2. **"Cứ dùng ReAct là AI sẽ thông minh hơn":** * *Sự thật:* Với các câu hỏi đơn giản (như "1+1 bằng mấy"), ReAct là sự lãng phí tài nguyên (overkill) và làm chậm tốc độ phản hồi không cần thiết.
3. **"ReAct chỉ dùng để tìm kiếm Google":** * *Sự thật:* "Action" trong ReAct có thể là bất cứ thứ gì: truy vấn SQL, gọi API ngân hàng, điều khiển cánh tay robot, hoặc chạy code Python.

---

## 5. Cập nhật mới nhất 2025

Năm 2025, ReAct không còn đứng độc lập mà đã tiến hóa thành các hệ thống **Agentic Workflows**:

* **Giao thức MCP (Model Context Protocol):** Đây là tiêu chuẩn mới giúp các mô hình (như Claude hay GPT) kết nối với các công cụ (Google Drive, Slack, Database) một cách liền mạch hơn, giúp vòng lặp ReAct trở nên cực kỳ nhanh và chuẩn xác.
* **Multi-modal ReAct:** AI hiện nay có thể thực hiện Action là "Nhìn" (Vision). Ví dụ: "Hãy xem ảnh chụp màn hình trang web này và chỉ cho tôi bước tiếp theo để thanh toán". AI sẽ Thought -> Action (phân tích ảnh) -> Observation.
* **Small Models ReAct:** Các mô hình nhỏ (như Phi-3.5 hoặc các bản Distilled) đã được tinh chỉnh (fine-tuned) để có khả năng ReAct tốt mà không cần đến các mô hình khổng lồ như GPT-4, giúp giảm chi phí vận hành.
* **Self-Correction:** Các Framework như LangGraph cho phép ReAct tự sửa lỗi. Nếu Action trả về lỗi, AI sẽ tự Thought để đổi chiến thuật Action khác thay vì bị kẹt trong vòng lặp vô tận.

---

Để tạo ra một Prompt ReAct hiệu quả, bạn cần thiết lập một cấu trúc nghiêm ngặt để mô hình không bị "lạc đề". Dưới đây là mẫu (Template) chuẩn nhất, được tối ưu hóa cho các mô hình mạnh như GPT-4o, Claude 3.5/4 hoặc các mô hình nội bộ năm 2025.

---

## Template ReAct Prompt "Vạn năng"

Bạn hãy copy đoạn dưới đây vào khung chat (thay thế phần trong ngoặc vuông bằng nhu cầu của bạn):

```text
# VAI TRÒ
Bạn là một trợ lý thông minh có khả năng suy luận logic và sử dụng công cụ để giải quyết vấn đề phức tạp.

# CÔNG CỤ CỦA BẠN
Bạn có quyền truy cập vào các công cụ sau. Bạn PHẢI sử dụng chúng nếu cần thông tin chính xác hoặc thực hiện tính toán:
1. Google_Search: Dùng để tìm kiếm thông tin thực tế, tin tức mới nhất hoặc dữ liệu chưa biết.
2. Calculator: Dùng để thực hiện các phép tính số học phức tạp.
3. Python_Interpreter: Dùng để viết mã, phân tích dữ liệu hoặc xử lý logic logic học.

# QUY TRÌNH LÀM VIỆC (ReAct)
Bạn phải phản hồi theo định dạng sau cho từng bước. Đừng đưa ra câu trả lời ngay lập tức nếu chưa có đủ dữ liệu.

- Thought: Suy nghĩ của bạn về những gì cần làm tiếp theo. Bạn đang thiếu thông tin gì? Bạn định dùng công cụ nào?
- Action: Tên công cụ bạn chọn (phải thuộc danh sách trên).
- Action Input: Tham số hoặc câu lệnh cụ thể cho công cụ đó.
- Observation: (Tôi sẽ cung cấp kết quả từ công cụ cho bạn sau bước này).
... (Lặp lại Thought/Action/Observation nếu cần)
- Final Answer: Câu trả lời cuối cùng sau khi đã có đủ thông tin.

# VÍ DỤ MẪU
User: "Giá cổ phiếu của Apple hôm nay tăng bao nhiêu % so với đầu năm 2024?"
Thought: Tôi cần tìm giá cổ phiếu Apple hiện tại (cuối năm 2025) và giá tại thời điểm đầu năm 2024, sau đó tính tỷ lệ phần trăm.
Action: Google_Search
Action Input: "Apple stock price Jan 1 2024 vs Dec 2025"
Observation: [Dữ liệu trả về: Jan 1 2024 là $185, Dec 2025 là $250]
Thought: Đã có đủ dữ liệu. Tôi sẽ tính toán: (250 - 185) / 185 * 100.
Action: Calculator
Action Input: "(250 - 185) / 185 * 100"
Observation: 35.13
Final Answer: Giá cổ phiếu Apple đã tăng khoảng 35.13% kể từ đầu năm 2024.

# BẮT ĐẦU TÁC VỤ
Yêu cầu của người dùng: [NHẬP CÂU HỎI CỦA BẠN TẠI ĐÂY]

```

---

## Giải thích các thành phần quan trọng

1. **Định nghĩa Công cụ (Tools):** Đây là phần quan trọng nhất. AI cần biết nó có "vũ khí" gì trong tay. Nếu bạn đang dùng ChatGPT hay Claude bản Web, chúng đã tích hợp sẵn Browser/Analysis, bạn chỉ cần nhắc AI "Hãy sử dụng công cụ có sẵn".
2. **Cấu trúc Thought -> Action -> Observation:**
* **Thought:** Buộc AI phải "dừng lại một nhịp" để lập kế hoạch (Reasoning). Điều này ngăn AI đoán mò.
* **Action/Action Input:** Đây là định dạng để AI gọi API hoặc yêu cầu hệ thống bên ngoài can thiệp.
* **Observation:** Đây là "thông tin phản hồi" từ thế giới thực. Trong môi trường lập trình (như LangChain), phần này sẽ tự động điền vào. Nếu bạn chat thủ công, bạn sẽ đóng vai trò là người cung cấp kết quả tìm kiếm.


3. **Few-shot Prompting (Ví dụ mẫu):** Cung cấp 1-2 ví dụ giúp AI hiểu định dạng đầu ra (Output format) mà bạn mong muốn, tránh việc nó viết tràn lan không đúng cấu trúc.

---

## Lưu ý để Prompt hoạt động tốt hơn trong năm 2025

* **Sử dụng dấu phân tách:** Dùng các ký hiệu như `###` hoặc `---` để AI dễ dàng phân biệt giữa hướng dẫn hệ thống và dữ liệu người dùng.
* **Yêu cầu sự ngắn gọn:** Thêm câu lệnh *"Hãy viết suy nghĩ (Thought) ngắn gọn, tập trung vào hành động tiếp theo"* để tiết kiệm Token và tăng tốc độ phản hồi.
* **Kết hợp với JSON (Nếu dùng API):** Nếu bạn là lập trình viên, hãy yêu cầu AI trả về phần Action dưới dạng JSON để code của bạn dễ dàng bóc tách thông tin.

