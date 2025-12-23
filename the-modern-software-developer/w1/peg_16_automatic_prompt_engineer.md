# Automatic Prompt Engineer (APE) 

Reference: https://www.promptingguide.ai/techniques/ape

![](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FAPE.3f0e01c2.png&w=828&q=75)

Image Source: Zhou et al., (2022)


## 1. Định nghĩa cốt lõi: APE là gì?

**Automatic Prompt Engineer (APE)** là một phương pháp sử dụng chính các mô hình ngôn ngữ lớn (LLM) để tự động hóa việc tạo, đánh giá và tối ưu hóa các câu lệnh (prompts).

Thay vì con người ngồi viết: *"Hãy tóm tắt văn bản này sao cho hay"*, rồi sửa đi sửa lại, APE coi "prompt" là một **biến số cần tối ưu hóa**. Hệ thống sẽ tự tạo ra hàng chục biến thể của prompt đó, chạy thử, chấm điểm và chọn ra phiên bản mang lại kết quả tốt nhất.

> **Hiểu đơn giản:** APE là "AI viết prompt cho AI".

---

## 2. Nguyên lý hoạt động và Ví dụ thực tế

APE hoạt động dựa trên một vòng lặp phản hồi (Feedback Loop) gồm 3 bước chính:

### Các bước thực hiện:

1. **Generation (Khởi tạo):** LLM (đóng vai trò "Generator") tạo ra nhiều ứng viên prompt khác nhau dựa trên một tập dữ liệu mẫu nhỏ.
2. **Evaluation (Đánh giá):** Các prompt này được chạy thử. Một LLM khác (đóng vai trò "Evaluator") hoặc một bộ quy tắc sẽ chấm điểm kết quả dựa trên độ chính xác, phong cách hoặc yêu cầu cụ thể.
3. **Selection (Lựa chọn):** Hệ thống chọn ra prompt có điểm cao nhất để sử dụng hoặc tiếp tục tinh chỉnh.

### Ví dụ thực tế:

Bạn muốn AI viết tiêu đề email quảng cáo sao cho tỷ lệ click cao.

* **Cách làm cũ:** Bạn tự viết 5 tiêu đề và thử từng cái.
* **Cách APE:**
* **Input:** "Tôi có sản phẩm giày chạy bộ mới, hãy viết tiêu đề email."
* **APE Generator:** Tạo ra 20 câu lệnh khác nhau (ví dụ: "Viết kiểu hài hước", "Viết kiểu khẩn cấp", "Viết tập trung vào lợi ích sức khỏe"...).
* **APE Evaluator:** Chạy thử các câu lệnh này trên dữ liệu khách hàng cũ và nhận thấy câu lệnh "Viết theo phong cách kể chuyện tâm tình" mang lại phản hồi tốt nhất.
* **Kết quả:** Hệ thống tự động đề xuất câu lệnh tối ưu nhất mà bạn có thể chưa bao giờ nghĩ tới.



---

## 3. Ưu điểm và Nhược điểm

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Hiệu suất** | Vượt xa trực giác của con người. AI thường tìm ra những từ ngữ "kỳ lạ" nhưng lại kích hoạt mô hình hiệu quả hơn. | **Chi phí:** Tốn kém tài nguyên (Tokens) vì phải chạy rất nhiều biến thể prompt cùng lúc. |
| **Quy mô** | Có thể tối ưu hóa hàng nghìn prompt cho các tác vụ khác nhau trong tích tắc. | **Phụ thuộc dữ liệu:** Nếu dữ liệu mẫu để đánh giá bị sai lệch, prompt tạo ra cũng sẽ kém chất lượng. |
| **Tính khách quan** | Loại bỏ định kiến cá nhân của người viết prompt. | **Rủi ro Overfitting:** Prompt quá tối ưu cho một tập dữ liệu nhỏ nhưng lại hoạt động kém khi gặp dữ liệu thực tế mới. |

---

## 4. Những quan niệm sai lầm phổ biến

* **Sai lầm 1: "APE sẽ làm nghề Prompt Engineer biến mất."**
* *Sự thật:* APE thay đổi vai trò của con người. Thay vì viết từng chữ, bạn trở thành người **thiết kế hệ thống đánh giá** và **giám sát mục tiêu**. Bạn điều khiển "cỗ máy tạo prompt" thay vì tự mình gõ prompt.


* **Sai lầm 2: "Cứ dùng AI tạo prompt là sẽ có kết quả hoàn hảo."**
* *Sự thật:* APE chỉ giỏi khi bạn có tiêu chí đánh giá (metrics) rõ ràng. Nếu bạn không biết mình muốn gì, AI cũng sẽ tạo ra những prompt "vô thưởng vô phạt".


* **Sai lầm 3: "APE chỉ là dùng ChatGPT để 'viết lại' câu lệnh."**
* *Sự thật:* APE thực thụ là một quy trình toán học/thuật toán có chấm điểm và chọn lọc, không đơn thuần là yêu cầu AI "viết lại cho hay hơn".



---

## 5. Cập nhật mới nhất năm 2025

Bước sang năm 2025, APE không còn chỉ là một kỹ thuật rời rạc mà đã tiến hóa lên tầm cao mới:

1. **Sự trỗi dậy của DSPy (Declarative Self-Improving Language Programs):** Đây là xu hướng "hot" nhất hiện nay. Thay vì viết prompt, lập trình viên viết code logic, và DSPy sẽ tự động tính toán các prompt tối ưu nhất cho từng bước trong luồng công việc.
2. **Multi-Agent APE:** Không chỉ một AI tạo prompt, mà là một nhóm các Agent chuyên biệt (một đứa chuyên tạo, một đứa chuyên phản biện, một đứa chuyên kiểm tra lỗi logic) cùng nhau hội ý để ra được prompt cuối cùng.
3. **Context-Aware Optimization:** Các hệ thống APE năm 2025 có khả năng tự thay đổi prompt theo thời gian thực dựa trên tâm trạng hoặc phản hồi vừa nhận được từ người dùng cuối.
4. **Tích hợp sâu vào mô hình Reasoning (như dòng o1 của OpenAI):** Các mô hình có khả năng suy nghĩ sâu giúp việc tự đánh giá prompt trở nên cực kỳ chính xác, giảm thiểu hiện tượng "hallucination" (ảo giác) ngay từ khâu thiết kế câu lệnh.

---
