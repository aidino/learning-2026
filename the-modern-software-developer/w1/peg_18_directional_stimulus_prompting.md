# Directional Stimulus Prompting

Reference: https://www.promptingguide.ai/techniques/dsp

![](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdsp.27a0005f.jpeg&w=1080&q=75)

Image Source: Li et al., (2023)


## 1. Định nghĩa cốt lõi của Directional Stimulus Prompting

**Directional Stimulus Prompting (DSP)** là kỹ thuật sử dụng một "tín hiệu điều hướng" (hint/cue) — thường là một đoạn văn bản ngắn, từ khóa hoặc tóm tắt — để hướng dẫn mô hình ngôn ngữ lớn (LLM) tập trung vào những khía cạnh cụ thể khi tạo ra câu trả lời.

Trong cấu trúc truyền thống của DSP, chúng ta thường thấy sự xuất hiện của hai thành phần:

* **Mô hình chính (LLM):** Ví dụ như GPT-4, Claude 3.5...
* **Mô hình điều hướng (Policy Model):** Thường là một mô hình nhỏ hơn (như T5 hoặc Llama-3-8B) được huấn luyện để tạo ra các "gợi ý" tối ưu từ đầu vào để dẫn dắt mô hình chính.

---

## 2. Nguyên lý hoạt động và Ví dụ thực tế

### Nguyên lý hoạt động

DSP hoạt động dựa trên việc thu hẹp không gian xác suất của mô hình. Khi có thêm một "kích thích" (stimulus), mô hình không còn phải tự đoán xem người dùng muốn nhấn mạnh điều gì, mà nó sẽ bám sát vào gợi ý đó để triển khai ý tưởng.

### Ví dụ thực tế

Giả sử bạn muốn tóm tắt một bài báo dài về tình hình kinh doanh của Apple.

* **Prompt thông thường:** *"Hãy tóm tắt bài báo này."*
* *Kết quả:* Có thể quá dài, quá ngắn hoặc tập trung vào những thứ bạn không quan tâm (ví dụ: các hoạt động từ thiện của Apple thay vì doanh thu).


* **DSP (với gợi ý điều hướng):**
* **Đầu vào:** [Nội dung bài báo]
* **Gợi ý (Stimulus):** *"Tập trung vào doanh thu iPhone 16 và dự báo tài chính quý 4."*
* **Prompt hoàn chỉnh:** *"Dựa trên bài báo và các từ khóa: [Doanh thu iPhone 16, Dự báo quý 4], hãy viết một bản tóm tắt súc tích."*



**Sự khác biệt:** Kết quả của DSP sẽ có độ chính xác và tính phù hợp (relevance) cao hơn hẳn vì mô hình đã được "nhắc bài" trước khi làm.

---

## 3. Ưu điểm và Nhược điểm

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Độ chính xác** | Cải thiện đáng kể khả năng tập trung vào chi tiết quan trọng. | Cần đầu tư thời gian để thiết kế gợi ý (hoặc huấn luyện mô hình gợi ý). |
| **Tính linh hoạt** | Có thể áp dụng cho các mô hình "hộp đen" (Black-box) mà không cần can thiệp vào trọng số (weights). | Nếu gợi ý sai lệch, kết quả đầu ra của LLM sẽ bị sai lệch theo (bias). |
| **Chi phí** | Hiệu quả hơn so với việc Fine-tuning (tinh chỉnh) toàn bộ mô hình lớn. | Làm tăng độ dài của Prompt (Token usage) một chút. |

---

## 4. Những quan niệm sai lầm phổ biến

1. **"DSP chỉ là thêm từ khóa vào Prompt":**
Thực tế, DSP theo đúng định nghĩa nghiên cứu là một hệ thống tự động, nơi một mô hình nhỏ được tối ưu hóa bằng học tăng cường (Reinforcement Learning) để tạo ra các gợi ý tốt nhất cho mô hình lớn. Việc bạn tự tay thêm từ khóa chỉ là dạng "thủ công" của DSP.
2. **"Càng nhiều gợi ý càng tốt":**
Sai. Quá nhiều gợi ý gây nhiễu và khiến mô hình bị quá tải (over-constrained), dẫn đến câu trả lời máy móc hoặc bỏ sót thông tin quan trọng không nằm trong gợi ý.
3. **"DSP thay thế hoàn toàn cho Few-shot Prompting":**
Không phải. DSP cung cấp *hướng đi* cho một trường hợp cụ thể, trong khi Few-shot cung cấp *định dạng và phong cách* dựa trên các ví dụ mẫu. Chúng thường được dùng kết hợp với nhau.

---

## 5. Update mới nhất 2025: Kỷ nguyên của Agentic DSP

Vào cuối năm 2024 và đầu 2025, khái niệm DSP đã tiến hóa vượt bậc nhờ sự trỗi dậy của các **AI Agents**:

* **Self-Correcting Stimulus:** Các hệ thống hiện nay không chỉ đưa ra gợi ý một lần. Agent sẽ tạo ra gợi ý -> LLM phản hồi -> Agent đánh giá phản hồi đó và tự sửa lại gợi ý để LLM trả lời tốt hơn ở lần 2 (vòng lặp phản hồi).
* **Sự hỗ trợ từ mô hình nhỏ (Small Language Models - SLM):** Với sự ra đời của các mô hình cực mạnh nhưng nhỏ gọn như **Llama 3.2 (1B/3B)** hay **Phi-3.5**, việc triển khai một "Policy Model" để tạo gợi ý điều hướng trở nên rẻ và nhanh hơn bao giờ hết. Bạn có thể chạy mô hình điều hướng ngay trên trình duyệt hoặc điện thoại để tối ưu cho mô hình lớn chạy trên Cloud.
* **RAG-Enhanced DSP:** Gợi ý điều hướng không còn chỉ lấy từ văn bản đầu vào, mà được trích xuất từ các cơ sở dữ liệu khổng lồ thông qua RAG (Retrieval-Augmented Generation) để đưa ra chỉ dẫn mang tính thực tế và thời sự cao hơn.

---
