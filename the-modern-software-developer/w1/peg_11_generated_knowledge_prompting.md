# Generated Knowledge Prompting 

Reference: https://www.promptingguide.ai/techniques/knowledge

### 1. Định nghĩa cốt lõi

**Generated Knowledge Prompting (GKP)** là một kỹ thuật yêu cầu AI **tự tạo ra các kiến thức, sự thật hoặc bối cảnh liên quan** trước khi bắt đầu thực hiện nhiệm vụ chính (trả lời câu hỏi hoặc giải quyết vấn đề).

Thay vì yêu cầu AI trả lời trực tiếp ngay lập tức, chúng ta chia quá trình thành hai bước:

1. **Bước 1 (Knowledge Generation):** Yêu cầu AI viết ra những gì nó biết về các khái niệm có trong câu hỏi.
2. **Bước 2 (Knowledge Integration):** Sử dụng chính những kiến thức vừa tạo ra đó làm bối cảnh (context) để đưa ra câu trả lời cuối cùng.

---

### 2. Nguyên lý hoạt động và Ví dụ thực tế

Nguyên lý của GKP dựa trên việc "khởi động" các vùng tri thức liên quan trong mạng thần kinh của AI. Điều này giúp giảm thiểu việc AI trả lời dựa trên xác suất từ ngữ thông thường và thay vào đó là dựa trên các dữ kiện logic.

#### Ví dụ thực tế:

Giả sử bạn hỏi một câu hỏi đòi hỏi sự hiểu biết về vật lý và đời sống:

> **Câu hỏi:** "Nếu tôi để một khối nước đá lên một miếng xốp (styrofoam) trong phòng kín 30°C, khối đá sẽ tan nhanh hơn hay chậm hơn so với việc đặt trực tiếp trên mặt bàn gỗ?"

**Nếu không dùng GKP:** AI có thể trả lời chung chung dựa trên dữ liệu văn bản nó có.

**Khi dùng GKP (2 bước):**

* **Bước 1 (Tạo kiến thức):** * *Prompt:* "Hãy liệt kê các đặc tính dẫn nhiệt của xốp (styrofoam) và gỗ. Cái nào cách nhiệt tốt hơn?"
* *AI trả lời:* "Xốp là chất cách nhiệt cực tốt vì nó chứa các túi khí nhỏ. Gỗ cũng là chất cách nhiệt nhưng khả năng dẫn nhiệt của gỗ cao hơn xốp..."


* **Bước 2 (Tích hợp kiến thức):**
* *Prompt:* "Dựa trên các đặc tính về dẫn nhiệt nêu trên, hãy trả lời câu hỏi: Khối đá trên xốp tan nhanh hơn hay chậm hơn trên bàn gỗ?"
* *AI trả lời:* "Khối đá trên xốp sẽ tan **chậm hơn**. Vì xốp cách nhiệt tốt hơn gỗ, nó ngăn cản nhiệt lượng từ môi trường và mặt bàn truyền vào khối đá hiệu quả hơn gỗ."



---

### 3. Ưu điểm và Nhược điểm

Dưới đây là bảng so sánh để bạn dễ dàng hình dung:

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Độ chính xác** | Giảm thiểu hiện tượng "ảo giác" (hallucination) đáng kể bằng cách buộc AI phải hệ thống hóa kiến thức trước. | Nếu kiến thức AI tạo ra ở bước 1 sai (Garbage In), kết quả cuối cùng cũng sẽ sai (Garbage Out). |
| **Lý luận** | Cải thiện khả năng suy luận trong các nhiệm vụ phức tạp, đặc biệt là các vấn đề khoa học hoặc logic. | Tăng độ trễ (latency) vì phải thực hiện hai hoặc nhiều lần gọi API/Prompt. |
| **Tính linh hoạt** | Không cần cơ sở dữ liệu bên ngoài (như RAG), tận dụng tối đa "trí nhớ" nội tại của mô hình. | Tốn kém hơn về chi phí (token) do phải sinh thêm văn bản trung gian. |

---

### 4. Những quan niệm sai lầm phổ biến

Khi tiếp cận GKP, người học thường dễ nhầm lẫn với các kỹ thuật khác. Dưới đây là 3 sai lầm điển hình:

* **Lầm tưởng 1: GKP giống hệt RAG (Retrieval-Augmented Generation).**
* *Sự thật:* RAG lấy kiến thức từ **nguồn bên ngoài** (PDF, Internet, Database). GKP lấy kiến thức từ **chính bên trong mô hình**. GKP dùng khi bạn tin rằng AI "biết" nhưng cần được gợi nhắc để hệ thống lại.


* **Lầm tưởng 2: GKP chỉ là Chain of Thought (CoT).**
* *Sự thật:* CoT (Chuỗi suy nghĩ) tập trung vào các **bước giải quyết vấn đề** (Step-by-step). GKP tập trung vào việc **cung cấp các dữ kiện nền tảng** trước khi bắt đầu giải quyết.


* **Lầm tưởng 3: Càng nhiều kiến thức tạo ra càng tốt.**
* *Sự thật:* Nếu yêu cầu AI tạo ra quá nhiều kiến thức không liên quan, nó sẽ làm loãng bối cảnh (context) và khiến AI bị lạc đề hoặc quá tải thông tin (Lost in the middle).


--- 

![](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgen-knowledge.055b8d37.png&w=828&q=75)

Nguồn ảnh: Liu et al., 2022

