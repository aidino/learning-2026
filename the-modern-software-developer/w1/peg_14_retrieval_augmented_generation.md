# Retrieval Augmented Generation (RAG) 

Reference: https://www.promptingguide.ai/techniques/rag

## 1. Định nghĩa cốt lõi: RAG là gì?

**Retrieval-Augmented Generation (RAG)** là một kỹ thuật trong Prompt Engineering giúp tối ưu hóa đầu ra của Mô hình Ngôn ngữ Lớn (LLM) bằng cách **kết nối nó với các nguồn tri thức tin cậy bên ngoài** trước khi tạo câu trả lời.

Hãy tưởng tượng LLM như một vị giáo sư cực kỳ thông minh nhưng trí nhớ chỉ dừng lại ở kiến thức của 2 năm trước. RAG giống như việc đưa cho vị giáo sư đó một chiếc máy tính có kết nối Internet hoặc một thư viện sách chuyên ngành mới nhất để ông ấy tra cứu trước khi trả lời câu hỏi của bạn.

---

## 2. Nguyên lý hoạt động (The Mechanics)

RAG hoạt động dựa trên quy trình 3 bước chính: **Retrieval (Truy xuất)  Augmentation (Tăng cường)  Generation (Tạo sinh)**.

### Quy trình kỹ thuật:

1. **Dữ liệu bên ngoài (Knowledge Base):** Tài liệu của bạn (PDF, Doc, Database) được chia nhỏ (Chunking) và chuyển đổi thành các chuỗi số gọi là **Vector Embeddings**.
2. **Truy xuất (Retrieval):** Khi bạn đặt câu hỏi, hệ thống sẽ tìm kiếm trong "kho vector" những đoạn văn bản có ý nghĩa gần giống nhất với câu hỏi đó.
3. **Tăng cường & Tạo sinh (Augmentation & Generation):** Những đoạn thông tin tìm được sẽ được "nhồi" vào Prompt gửi cho LLM. Câu lệnh lúc này sẽ đại loại là: *"Dựa vào các thông tin sau: [Dữ liệu tìm được], hãy trả lời câu hỏi: [Câu hỏi của bạn]"*.

> **Ví dụ thực tế:** Một nhân viên ngân hàng muốn kiểm tra chính sách cho vay mới nhất vừa ban hành sáng nay.
> * **Không có RAG:** AI sẽ trả lời dựa trên dữ liệu cũ (có thể sai lệch).
> * **Có RAG:** Hệ thống tự động tra cứu file PDF "Chính sách 2025" trong ổ cứng nội bộ, trích xuất đoạn văn về lãi suất và yêu cầu AI tóm tắt cho nhân viên.
> 
> 

---

## 3. Ưu điểm và Nhược điểm

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Độ chính xác** | Giảm thiểu hiện tượng "ảo tưởng" (Hallucination) vì AI phải nói có sách, mách có chứng. | Phụ thuộc hoàn toàn vào chất lượng dữ liệu đầu vào (Garbage in, Garbage out). |
| **Tính cập nhật** | Cung cấp thông tin thời gian thực mà không cần huấn luyện lại (Retrain) mô hình. | Tăng độ trễ (Latency) vì phải thực hiện thêm bước tra cứu trước khi trả lời. |
| **Chi phí** | Rẻ hơn rất nhiều so với việc Fine-tuning (tinh chỉnh) mô hình định kỳ. | Cần chi phí duy trì cơ sở dữ liệu Vector và hệ thống truy xuất. |
| **Sự minh bạch** | Có thể trích dẫn nguồn (Citations), giúp người dùng kiểm chứng được thông tin. | Phức tạp trong việc thiết lập hệ thống (Chunking, Reranking). |

---

## 4. Những quan niệm sai lầm phổ biến

* **Sai lầm 1: "RAG thay thế hoàn toàn Fine-tuning":** Thực tế, RAG giúp AI có **kiến thức mới**, còn Fine-tuning giúp AI có **phong cách/kỹ năng chuyên biệt**. Chúng bổ trợ cho nhau.
* **Sai lầm 2: "Cứ ném file vào là RAG sẽ trả lời đúng":** Việc xử lý dữ liệu (Làm sạch, chia nhỏ đoạn văn đúng cách) chiếm 80% thành công. Nếu bạn chia nhỏ một bảng biểu thành các dòng rời rạc, AI sẽ không thể hiểu được mối liên hệ giữa chúng.
* **Sai lầm 3: "RAG là giải pháp bảo mật tuyệt đối":** Dữ liệu của bạn có thể bị lộ qua Prompt nếu hệ thống không được thiết kế các lớp lọc (Guards) cẩn thận.

---

## 5. Update mới nhất 2025: Kỷ nguyên của RAG thông minh

Năm 2025 đánh dấu bước chuyển mình từ RAG đơn giản sang các hệ thống có khả năng "tư duy".

### 1. GraphRAG (RAG dựa trên Đồ thị)

Thay vì chỉ tìm kiếm các đoạn văn bản tương tự, GraphRAG xây dựng một mạng lưới các mối quan hệ (thực thể, sự kiện). Điều này giúp AI trả lời được các câu hỏi mang tính tổng hợp cao như: *"Các chủ đề chính nổi bật trong 100 báo cáo tài chính gần đây là gì?"* mà RAG truyền thống thường bỏ lỡ.

### 2. Agentic RAG (RAG tác nhân)

AI không còn chỉ tra cứu một lần rồi trả lời. Nó hoạt động như một "Agent": Nếu lần tra cứu đầu tiên không đủ thông tin, nó sẽ tự quyết định tra cứu tiếp ở nguồn khác, hoặc tự đặt câu hỏi ngược lại cho người dùng để làm rõ ý định.

### 3. Long-Context vs. RAG

Với việc các mô hình như Gemini 1.5 hay Claude 3 có cửa sổ ngữ cảnh (Context Window) lên tới hàng triệu token, nhiều người tự hỏi liệu RAG có chết? Câu trả lời năm 2025 là: **Không**. RAG vẫn là cách hiệu quả nhất về chi phí và khả năng quản lý quyền truy cập dữ liệu ở quy mô lớn (hàng tỷ tài liệu).

### 4. Multimodal RAG (RAG đa phương thức)

RAG giờ đây không chỉ đọc văn bản mà còn có thể truy xuất thông tin từ hình ảnh, video và sơ đồ kỹ thuật để trả lời người dùng.

---