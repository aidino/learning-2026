# Active-Prompt 

Reference: https://www.promptingguide.ai/techniques/activeprompt

![](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Factive-prompt.f739657b.png&w=1200&q=75)

Image Source: Diao et al., (2023)


## 1. Định nghĩa cốt lõi (The Core Definition)

**Active-Prompt** là một phương pháp tối ưu hóa Prompt dựa trên việc xác định và ưu tiên giải quyết các câu hỏi mà mô hình AI đang "lúng túng" nhất.

Thay vì chọn ngẫu nhiên các ví dụ (few-shot examples) để đưa vào prompt, Active-Prompt sử dụng chính mô hình AI để tự đánh giá xem nó không chắc chắn ở đâu. Sau đó, con người (hoặc một mô hình mạnh hơn) sẽ can thiệp để hướng dẫn những phần đó, giúp mô hình học được nhiều nhất từ một lượng dữ liệu mẫu ít nhất.

---

## 2. Nguyên lý hoạt động và Ví dụ thực tế

Nguyên lý của Active-Prompt tuân theo một quy trình vòng lặp gồm 4 bước chính:

### Quy trình chi tiết:

1. **Trích xuất (Sampling):** Cho mô hình trả lời một tập hợp các câu hỏi đầu vào nhiều lần (ví dụ: 10-20 lần cho mỗi câu hỏi).
2. **Đo lường sự không chắc chắn (Uncertainty Estimation):** Tính toán độ biến thiên của các câu trả lời. Nếu 20 lần trả lời mà kết quả ra giống hệt nhau, mô hình "tự tin". Nếu kết quả ra 20 kiểu khác nhau, mô hình đang "bối rối".
* *Công thức:* Thường dùng độ lệch chuẩn hoặc entropy .


3. **Gán nhãn (Annotation):** Chọn ra top các câu hỏi có độ không chắc chắn cao nhất để con người viết lời giải mẫu (Chain-of-Thought).
4. **Suy luận (Inference):** Đưa các ví dụ "khó" đã được gán nhãn này vào Prompt chính thức để chạy các tác vụ thực tế.

### Ví dụ thực tế:

Giả sử bạn muốn AI giải các bài toán logic phức tạp.

* **Bước 1:** Bạn đưa 100 bài toán cho AI làm thử mỗi bài 5 lần.
* **Bước 2:** Bạn thấy bài toán số 45 có 5 kết quả khác nhau (Uncertainty cao).
* **Bước 3:** Bạn (con người) viết lời giải chi tiết từng bước cho bài số 45.
* **Bước 4:** Bạn dùng lời giải bài 45 đó làm ví dụ "Few-shot" trong Prompt. AI sẽ hiểu cách xử lý các tình huống lắt léo tương tự cực kỳ hiệu quả.

---

## 3. Ưu điểm và Nhược điểm

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Hiệu suất** | Vượt trội hơn hẳn so với Few-shot ngẫu nhiên hay Chain-of-Thought thông thường. | Tốn kém chi phí ban đầu do phải chạy thử nghiệm nhiều lần (Sampling). |
| **Dữ liệu** | Cần ít dữ liệu mẫu hơn nhưng chất lượng cực cao. | Quy trình thiết lập phức tạp, đòi hỏi kỹ năng lập trình/vận hành. |
| **Độ chính xác** | Giảm thiểu hiện tượng "ảo giác" (hallucination) ở những phần kiến thức khó. | Cần sự can thiệp của con người (Human-in-the-loop) để gán nhãn chính xác. |

---

## 4. Những quan niệm sai lầm phổ biến

* **Sai lầm 1: "Active-Prompt chỉ là viết Prompt một cách chủ động."** * *Thực tế:* Nó là một thuật toán/quy trình kỹ thuật, không phải là việc bạn "chăm chỉ" viết prompt hơn.
* **Sai lầm 2: "Càng nhiều ví dụ Few-shot càng tốt."** * *Thực tế:* Trong Active-Prompt, chất lượng của ví dụ (đánh đúng vào chỗ AI yếu) quan trọng hơn số lượng. 1-2 ví dụ "đúng bệnh" có giá trị hơn 10 ví dụ ngẫu nhiên.
* **Sai lầm 3: "Có thể áp dụng Active-Prompt bằng tay (manual) hoàn toàn."**
* *Thực tế:* Rất khó. Bạn cần dùng script/code để chạy lặp và tính toán độ không chắc chắn (uncertainty) một cách định lượng.



---

## 5. Cập nhật mới nhất 2025

Đến năm 2025, Active-Prompt đã tiến hóa vượt bậc nhờ sự ra đời của các mô hình có khả năng suy luận (Reasoning Models) như GPT-o1 hay Claude 3.5/4:

1. **Self-Active Prompting (Cơ chế tự trị):** Thay vì cần con người gán nhãn ở Bước 3, các mô hình mạnh (như GPT-o1) sẽ đóng vai trò là "Teacher" để giải các bài toán khó mà mô hình nhỏ hơn (Student) đang bối rối.
2. **Kỹ thuật "Batch Active Learning":** Cho phép lọc và gán nhãn hàng nghìn Prompt cùng lúc thông qua các Agent điều hướng, giúp tối ưu chi phí token.
3. **Tích hợp RAG động:** Active-Prompt hiện được dùng để xác định khi nào hệ thống RAG cần tìm thêm tài liệu mới (nếu Uncertainty của câu trả lời quá cao, Agent sẽ tự động đi tìm thêm dữ liệu thay vì trả lời bừa).

---

> **Lời khuyên cho bạn:** Nếu bạn đang xây dựng một ứng dụng AI đòi hỏi độ chính xác tuyệt đối (như phân tích tài chính, y tế), hãy đầu tư thời gian vào Active-Prompt. Nó giúp bạn "dạy" AI tập trung vào đúng những gì nó còn thiếu sót.
