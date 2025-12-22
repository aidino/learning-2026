# Prompt Chaining 

Reference: https://www.promptingguide.ai/techniques/prompt_chaining

### 1. Định nghĩa cốt lõi của Prompt Chaining

**Prompt Chaining** là kỹ thuật chia nhỏ một nhiệm vụ phức tạp thành một chuỗi các bước (prompt) kế tiếp nhau. Thay vì yêu cầu AI làm mọi thứ trong một câu lệnh duy nhất (Mega-prompt), bạn yêu cầu nó hoàn thành từng phần nhỏ.

Kết quả đầu ra (output) của bước trước sẽ được sử dụng làm đầu vào (input) hoặc một phần bối cảnh cho bước tiếp theo.

> **Tư duy cốt lõi:** "Chia để trị" (Divide and Conquer). AI sẽ hoạt động tốt nhất khi nó tập trung toàn bộ "sức mạnh xử lý" vào một khía cạnh cụ thể tại một thời điểm.

---

### 2. Nguyên lý hoạt động và Ví dụ thực tế

#### Nguyên lý hoạt động

Quy trình này hoạt động như một dây chuyền sản xuất trong nhà máy. Mỗi "trạm" (một prompt) chỉ thực hiện một nhiệm vụ chuyên biệt trước khi chuyển sản phẩm sang trạm kế tiếp.

#### Ví dụ thực tế: Viết một bài blog chuẩn SEO

Thay vì viết: *"Hãy viết cho tôi một bài blog về lợi ích của cà phê"*, một chuỗi Prompt Chaining sẽ trông như sau:

* **Bước 1 (Nghiên cứu):** "Hãy liệt kê 5 lợi ích sức khỏe hàng đầu của cà phê dựa trên các nghiên cứu khoa học gần đây."
* **Bước 2 (Lập dàn ý):** "Dựa trên 5 lợi ích trên [Output bước 1], hãy lập một dàn ý chi tiết cho bài blog dài 1000 chữ."
* **Bước 3 (Viết nội dung):** "Dựa trên dàn ý này [Output bước 2], hãy viết phần mở đầu sao cho thật thu hút và khơi gợi sự tò mò."
* **Bước 4 (Kiểm tra & Tối ưu):** "Hãy đọc lại phần mở đầu [Output bước 3] và kiểm tra xem nó có chứa từ khóa 'lợi ích của cà phê' chưa, nếu chưa hãy chèn vào một cách tự nhiên."

---

### 3. Ưu điểm và Nhược điểm

Dưới đây là bảng so sánh để bạn dễ dàng hình dung:

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Độ chính xác** | Giảm thiểu hiện tượng "ảo giác" (hallucination) vì AI tập trung vào phạm vi hẹp. | **Độ trễ (Latency):** Mất nhiều thời gian hơn vì phải chờ từng bước phản hồi. |
| **Kiểm soát** | Bạn có thể can thiệp, chỉnh sửa ở giữa quy trình nếu một bước nào đó chưa ưng ý. | **Chi phí:** Tốn nhiều Token hơn do phải lặp lại bối cảnh ở mỗi bước. |
| **Độ phức tạp** | Xử lý được những yêu cầu mà một prompt đơn lẻ không bao giờ làm nổi. | **Quản lý:** Khó thiết lập và duy trì nếu chuỗi quá dài (dễ bị "tam sao thất bản"). |

---

### 4. Những quan niệm sai lầm phổ biến

#### Sai lầm 1: Prompt Chaining giống hệt Chain of Thought (CoT)

Nhiều người nhầm lẫn hai khái niệm này.

* **Chain of Thought:** Là yêu cầu AI "suy nghĩ từng bước một" **ngay trong một câu trả lời duy nhất**.
* **Prompt Chaining:** Là việc **tách biệt hoàn toàn** các bước thành các lượt tương tác khác nhau (hoặc các lời gọi API khác nhau).

#### Sai lầm 2: Càng nhiều bước càng tốt

Việc chia quá nhỏ đôi khi làm mất đi "mối liên kết ngữ cảnh" tổng thể. Nếu bước 1 hơi lệch hướng, bước 5 sẽ trở thành một thảm họa. Bạn chỉ nên chia nhỏ khi nhiệm vụ đó thực sự đa tầng.

#### Sai lầm 3: Chỉ dùng được khi biết lập trình

Dù Prompt Chaining rất mạnh khi dùng với công cụ tự động hóa (như LangChain hay Make), bạn hoàn toàn có thể thực hiện nó **thủ công** bằng cách copy-paste kết quả của câu trả lời trước vào câu hỏi tiếp theo trong ChatGPT hay Claude.

---
