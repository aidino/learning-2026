# Automatic Reasoning and Tool-use (ART) 

Reference: https://www.promptingguide.ai/techniques/art


## 1. Định nghĩa cốt lõi của ART

**Automatic Reasoning and Tool-use (ART)** là một khung công tác (framework) cho phép mô hình ngôn ngữ lớn (LLM) tự động hóa quy trình suy luận đa bước và sử dụng các công cụ bên ngoài (như máy tính, bộ máy tìm kiếm, hoặc API) để giải quyết các tác vụ phức tạp.

Thay vì yêu cầu con người phải viết các câu lệnh mồi (prompts) chi tiết cho từng bước (Chain-of-Thought thủ công), ART **tự động lựa chọn** các ví dụ minh họa phù hợp từ một thư viện tác vụ và **điều phối** các công cụ để đưa ra câu trả lời chính xác nhất.

---

## 2. Nguyên lý hoạt động và Ví dụ thực tế

### Nguyên lý hoạt động

ART hoạt động dựa trên cơ chế **"Truy xuất và Phối hợp"**:

1. **Phân rã tác vụ (Decomposition):** Khi nhận câu hỏi, ART chia nhỏ nó thành các bước logic.
2. **Lấy mẫu ví dụ (Retrieval):** Nó tìm kiếm trong thư viện các ví dụ (demos) có cấu trúc tương tự để học cách giải quyết.
3. **Tích hợp công cụ (Tool Integration):** Khi gặp các bước cần dữ liệu thực tế hoặc tính toán chính xác, nó sẽ gọi công cụ (ví dụ: Google Search, Python code).
4. **Dừng và Chỉnh sửa:** Mô hình biết khi nào nên dừng suy luận và đưa ra kết quả cuối cùng.

### Ví dụ thực tế

**Câu hỏi:** *"Dân số của thủ đô nước Pháp vào năm 2024 tăng bao nhiêu phần trăm so với năm 2010?"*

* **Bước 1 (Suy luận):** Xác định thủ đô nước Pháp là Paris.
* **Bước 2 (Dùng công cụ):** Gọi Search API để tìm dân số Paris năm 2010 và 2024.
* **Bước 3 (Dùng công cụ):** Gọi máy tính (Calculator) để thực hiện phép tính: `((Dân số 2024 - Dân số 2010) / Dân số 2010) * 100`.
* **Bước 4 (Kết luận):** Tổng hợp dữ liệu và trả lời người dùng.

---

## 3. Ưu điểm và Nhược điểm

### Ưu điểm

* **Độ chính xác cao:** Giảm thiểu hiện tượng "ảo giác" (hallucination) vì kết quả dựa trên dữ liệu thực và tính toán logic của công cụ.
* **Khả năng mở rộng (Scalability):** Bạn không cần viết prompt mới cho mỗi câu hỏi; chỉ cần bổ sung thư viện ví dụ.
* **Tính minh bạch:** Người dùng có thể thấy từng bước suy luận và các công cụ mà AI đã sử dụng.

### Nhược điểm

* **Độ trễ (Latency):** Việc gọi API bên ngoài và suy luận nhiều bước tốn nhiều thời gian hơn trả lời trực tiếp.
* **Chi phí:** Sử dụng nhiều token hơn cho việc truy xuất ví dụ và gọi công cụ.
* **Phụ thuộc vào thư viện:** Nếu thư viện ví dụ (demos) nghèo nàn, ART sẽ gặp khó khăn với các tác vụ lạ.

---

## 4. Những quan niệm sai lầm phổ biến

* **"ART giống hệt như Chain-of-Thought (CoT)":** * *Sự thật:* CoT yêu cầu con người viết mẫu suy luận. ART **tự động hóa** việc tìm và áp dụng mẫu đó, đồng thời kết hợp thêm công cụ ngoại vi.
* **"Chỉ có các model lớn (như GPT-4) mới dùng được ART":** * *Sự thật:* ART được thiết kế để giúp các model nhỏ hơn hoạt động hiệu quả như model lớn bằng cách cung cấp cho chúng "quy trình" và "công cụ".
* **"ART là một loại phần mềm":**
* *Sự thật:* ART là một **chiến lược Prompt Engineering** (framework), không phải là một phần mềm độc lập.



---

## 5. Cập nhật mới nhất năm 2025

Đến năm 2025, ART đã tiến hóa vượt xa các nghiên cứu ban đầu của năm 2023-2024:

1. **Self-Evolving Libraries (Thư viện tự tiến hóa):** Các hệ thống ART hiện nay có khả năng tự đánh giá kết quả của mình. Nếu một suy luận thành công, nó tự thêm vào thư viện làm ví dụ mẫu cho các tác vụ sau mà không cần con người can thiệp.
2. **Multi-modal Tool-use:** ART không chỉ dùng text. Nó có thể gọi các công cụ xử lý hình ảnh, âm thanh hoặc chạy giả lập môi trường 3D để kiểm chứng logic.
3. **Agentic RAG Integration:** ART được tích hợp sâu vào RAG (Retrieval-Augmented Generation), nơi nó không chỉ tìm văn bản mà còn tìm "cách giải quyết" trong các kho dữ liệu doanh nghiệp.
4. **Local Execution (Chạy cục bộ):** Nhờ sự tối ưu, ART đã có thể chạy trên các SLM (Small Language Models) ngay trên thiết bị cá nhân, giảm bớt lo ngại về bảo mật dữ liệu khi gọi API bên thứ ba.

---

> **Ghi chú quan trọng:** ART hiện là nền tảng cốt lõi cho các "AI Agents" (Tác nhân AI) mà bạn thấy trên thị trường hiện nay.
