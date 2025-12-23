# Multimodal CoT Prompting

Reference: https://www.promptingguide.ai/techniques/multimodalcot

![](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmultimodal-cot.a84f6cc1.png&w=1080&q=75)

## 1. Định nghĩa cốt lõi

**Multimodal CoT Prompting** là một kỹ thuật kỹ nghệ gợi ý (Prompt Engineering) yêu cầu mô hình AI đa phương thức (ví dụ: GPT-4o, Gemini 2.0/3, Claude 3.5/4.5) thực hiện các bước **suy luận trung gian** (intermediate reasoning steps) dựa trên nhiều loại dữ liệu đầu vào khác nhau (văn bản, hình ảnh, âm thanh, video) trước khi đưa ra câu trả lời cuối cùng.

Thay vì đi thẳng từ `[Hình ảnh + Câu hỏi]`  `[Câu trả lời]`, Multimodal CoT buộc mô hình phải đi qua lộ trình:
`[Dữ liệu đa phương thức]`  `[Trích xuất đặc điểm]`  `[Lập luận từng bước]`  `[Kết luận]`.

---

## 2. Nguyên lý hoạt động & Ví dụ thực tế

### Nguyên lý hoạt động

Nguyên lý của nó thường dựa trên khung sườn **Hai giai đoạn (Two-stage framework)**:

1. **Giai đoạn Rationale (Cơ sở lý luận):** AI phân tích các thành phần trong hình ảnh/video và diễn giải chúng thành các bằng chứng logic.
2. **Giai đoạn Answer (Trả lời):** AI kết hợp các bằng chứng vừa trích xuất với kiến thức nền của nó để đưa ra lời giải.

### Ví dụ thực tế

**Bối cảnh:** Bạn cung cấp một bức ảnh chụp bảng điều khiển xe hơi bị lỗi và hỏi: *"Xe tôi bị làm sao và tôi nên làm gì?"*

* **Nếu không có CoT:** AI có thể chỉ nói: "Xe bạn bị lỗi động cơ, hãy đi sửa." (Dễ sai hoặc quá chung chung).
* **Với Multimodal CoT Prompting:**
* **Bước 1 (Phân tích thị giác):** "Tôi quan sát thấy biểu tượng 'Check Engine' màu vàng đang sáng. Kim đồng hồ nhiệt độ đang chỉ gần vạch đỏ."
* **Bước 2 (Suy luận logic):** "Biểu tượng Check Engine kết hợp với nhiệt độ cao thường chỉ ra vấn đề về hệ thống làm mát hoặc quá nhiệt động cơ."
* **Bước 3 (Kết luận & Hành động):** "Bạn nên tấp xe vào lề ngay lập tức, tắt máy và kiểm tra nước làm mát sau khi máy nguội. Đừng tiếp tục lái để tránh hỏng máy hoàn toàn."



---

## 3. Ưu điểm và Nhược điểm

| Đặc điểm | Chi tiết |
| --- | --- |
| **Ưu điểm** | - **Độ chính xác cao:** Đặc biệt với các bài toán logic phức tạp, khoa học hoặc y tế.<br>

<br>- **Tính minh bạch:** Bạn biết tại sao AI đưa ra kết quả đó (có thể kiểm chứng lỗi sai ở bước nào).<br>

<br>- **Tận dụng tối đa dữ liệu:** AI không bỏ sót các chi tiết nhỏ trong hình ảnh/video. |
| **Nhược điểm** | - **Độ trễ (Latency):** Việc suy luận từng bước tốn thời gian hơn.<br>

<br>- **Chi phí (Cost):** Sử dụng nhiều token hơn cho phần "suy nghĩ".<br>

<br>- **Ảo giác logic:** Đôi khi AI trích xuất hình ảnh đúng nhưng lại suy luận sai (Hallucination trong bước trung gian). |

---

## 4. Những quan niệm sai lầm phổ biến

1. **"Nó chỉ là Image-to-Text rồi dùng CoT":** * *Sự thật:* Ở các mô hình "Native Multimodal" năm 2025 (như Gemini 3), AI xử lý hình ảnh và văn bản đồng thời trong cùng một không gian vector (shared latent space). Nó không cần chuyển ảnh thành mô tả văn bản trước rồi mới suy nghĩ.
2. **"Càng nhiều bước suy luận càng tốt":** * *Sự thật:* Suy luận quá dài có thể dẫn đến hiện tượng "trệch hướng logic" (drift), khiến AI đi lạc khỏi câu hỏi ban đầu.
3. **"Mô hình nào cũng làm được":** * *Sự thật:* Các mô hình nhỏ (Small Models) thường gặp khó khăn với Multimodal CoT nếu không được tinh chỉnh (Fine-tuning) kỹ lưỡng. Chỉ các mô hình Frontier mới thực sự làm tốt việc này một cách tự nhiên.

---

## 5. Cập nhật mới nhất 2025 (Update 2025)

Trong năm 2025, Multimodal CoT đã có những bước tiến vượt bậc:

* **Sự trỗi dậy của "Thinking Mode" bản địa:** Các dòng mô hình như OpenAI o1-multimodal hay GPT-5.1 đã tích hợp sẵn cơ chế "Hidden CoT". Bạn không cần viết "Let's think step by step" nữa; mô hình tự động dành thêm tài nguyên tính toán để suy luận đa phương thức trước khi phản hồi.
* **Layered CoT (CoT phân lớp):** AI bắt đầu thực hiện các vòng lặp kiểm chứng. Ví dụ: Sau khi đưa ra bước suy luận 1, nó tự "nhìn" lại hình ảnh để xác nhận xem bước đó có khớp với thực tế không trước khi sang bước 2.
* **Long-context Video CoT:** Khả năng suy luận CoT trên video dài (hàng giờ). AI có thể kết nối một chi tiết ở phút thứ 5 với một hành động ở phút thứ 50 để giải thích nguyên nhân-kết quả.
* **Trace-of-Thought cho Robot:** Ứng dụng mạnh mẽ trong điều khiển robot (Embodied AI), nơi robot nhìn môi trường và tự lập lộ trình suy luận: "Tôi thấy cái cốc -> Nó ở quá xa -> Tôi cần di chuyển lại gần -> Tránh vật cản là con mèo".

