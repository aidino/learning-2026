# PAL (Program-Aided Language Models) 

Reference: https://www.promptingguide.ai/techniques/pal

## 1. Định nghĩa cốt lõi của PAL là gì?

**PAL (Program-Aided Language Models)** là một phương pháp Prompting mà trong đó, thay vì yêu cầu LLM đưa ra câu trả lời trực tiếp bằng ngôn ngữ tự nhiên (như Chain-of-Thought - CoT), chúng ta yêu cầu mô hình **viết ra một đoạn mã lập trình** (thường là Python) để giải quyết vấn đề.

Sau đó, đoạn mã này được gửi đến một **trình thông dịch bên ngoài** (External Interpreter) để thực thi và trả về kết quả cuối cùng.

> **Tóm tắt bằng công thức:** > `PAL = LLM (Lập luận & Viết code) + Interpreter (Tính toán chính xác)`

---

## 2. Nguyên lý hoạt động và Ví dụ thực tế

### Nguyên lý hoạt động

PAL hoạt động dựa trên sự phân tách giữa **Lập luận (Reasoning)** và **Tính toán (Computation)**:

1. **Bước 1:** LLM đọc bài toán và chia nhỏ thành các bước logic dưới dạng comment code hoặc biến số.
2. **Bước 2:** LLM viết mã lệnh để thực hiện các bước đó.
3. **Bước 3:** Hệ thống tự động chạy đoạn mã này trong môi trường Python.
4. **Bước 4:** Kết quả từ Python được trả về cho người dùng hoặc được LLM dùng để viết câu trả lời cuối cùng.

### Ví dụ thực tế

**Bài toán:** "Mẹ cho An 50k. An mua 3 quyển vở, mỗi quyển 7k, và 2 cây bút, mỗi cây 4k. Hỏi An còn lại bao nhiêu tiền?"

* **Với CoT truyền thống:** LLM có thể tính nhẩm sai:  (đôi khi nhầm thành 21 hoặc 23).
* **Với PAL:** Prompt sẽ yêu cầu mô hình giải bằng Python.

**Output của LLM:**

```python
# Tiền mẹ cho
initial_money = 50
# Mua vở
notebook_price = 7
notebook_count = 3
total_notebooks = notebook_price * notebook_count
# Mua bút
pen_price = 4
pen_count = 2
total_pens = pen_price * pen_count
# Tiền còn lại
money_left = initial_money - (total_notebooks + total_pens)
print(money_left)

```

**Kết quả từ Interpreter:** `21`. (Độ chính xác là tuyệt đối vì do máy tính thực hiện phép tính).

---

## 3. Ưu điểm và Nhược điểm

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Độ chính xác** | Cực cao trong toán học, tài chính và logic phức tạp. | Phụ thuộc vào khả năng viết code của mô hình. |
| **Tính minh bạch** | Bạn có thể kiểm tra logic thông qua các dòng code. | Khó gỡ lỗi (debug) nếu mô hình viết code sai cú pháp. |
| **Khả năng xử lý** | Giải được các bài toán có vòng lặp (loops) hoặc đệ quy mà LLM thường "bó tay". | Cần môi trường thực thi code (Sandbox) an toàn. |
| **Hiệu suất** | Giảm thiểu hiện tượng "hallucination" (ảo giác) về con số. | Tăng độ trễ (latency) vì phải qua bước chạy code. |

---

## 4. Những quan niệm sai lầm phổ biến

* **Sai lầm 1: PAL giống hệt Chain-of-Thought (CoT).** * *Sự thật:* CoT dùng ngôn ngữ tự nhiên để suy nghĩ ("Đầu tiên ta lấy 50 trừ..."). PAL dùng code. CoT vẫn tự tính nhẩm (dễ sai), còn PAL để máy tính tính.
* **Sai lầm 2: PAL chỉ dùng cho toán học.**
* *Sự thật:* PAL cực mạnh trong việc xử lý dữ liệu (Data manipulation), lập kế hoạch (Planning), và giải quyết các câu đố logic về lịch trình hoặc vị trí.


* **Sai lầm 3: Chỉ những mô hình cực lớn mới dùng được PAL.**
* *Sự thật:* Năm 2025, ngay cả các mô hình nhỏ (Small Language Models - SLM) nếu được tinh chỉnh tốt về code cũng có thể thực hiện PAL hiệu quả hơn là bắt chúng "tính nhẩm".



---

## 5. Cập nhật mới nhất 2025

Trong năm 2025, PAL đã tiến hóa vượt bậc với các xu hướng sau:

1. **Sự trỗi dậy của PoT (Program of Thoughts):** Một biến thể nâng cao của PAL, nơi mô hình không chỉ viết code mà còn tự lặp lại (Iterative) để sửa lỗi code nếu lần chạy đầu tiên thất bại.
2. **Tích hợp Agentic Workflows:** PAL hiện nay là kỹ năng "phải có" của các AI Agent. Ví dụ, khi bạn hỏi về báo cáo tài chính, Agent tự động viết script Python để truy vấn database và vẽ biểu đồ ngay lập tức.
3. **Giao thức MCP (Model Context Protocol):** Các mô hình đời mới (như Claude 3.7 hay GPT-5 sắp tới) sử dụng MCP để kết nối an toàn với máy tính cá nhân hoặc server, giúp việc thực thi PAL trở nên liền mạch và bảo mật hơn, tránh rò rỉ dữ liệu.
4. **Hỗ trợ đa ngôn ngữ lập trình:** Không còn bó hẹp ở Python, PAL 2025 đã hỗ trợ tốt SQL, JavaScript và thậm chí là các ngôn ngữ đặc tả logic như Lean cho toán học chuyên sâu.

