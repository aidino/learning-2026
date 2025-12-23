# Reflexion 

Reference: https://www.promptingguide.ai/techniques/reflexion


## 1. Định nghĩa cốt lõi: Reflexion là gì?

**Reflexion** không đơn thuần là một câu lệnh (prompt), mà là một **khung cấu trúc (framework)** cho phép LLM học hỏi từ những sai lầm của chính nó thông qua phản hồi ngôn ngữ.

Thay vì chỉ đưa ra câu trả lời một lần (Zero-shot) hoặc suy nghĩ từng bước (Chain-of-Thought), Reflexion thiết lập một vòng lặp: **Hành động -> Nhận xét lỗi -> Suy ngẫm -> Thử lại.**

> **Cốt lõi:** Nó chuyển đổi các phản hồi dạng "đúng/sai" thành các bài học bằng văn bản (linguistic feedback), giúp mô hình cập nhật "bộ nhớ ngắn hạn" để thực hiện tốt hơn trong lần thử kế tiếp.

---

## 2. Nguyên lý hoạt động (The Loop)

Reflexion hoạt động dựa trên sự phối hợp của 3 thành phần chính (thường được gọi là các Agent con):

1. **Actor (Người thực hiện):** Đưa ra phản hồi ban đầu hoặc thực hiện một nhiệm vụ (vô code, giải toán).
2. **Evaluator (Người đánh giá):** Kiểm tra kết quả của Actor (ví dụ: chạy thử code xem có lỗi không, hoặc so sánh với đáp án đúng).
3. **Self-Reflection (Người suy ngẫm):** Nếu kết quả sai, Agent này sẽ phân tích: *"Tại sao tôi sai? Lỗi nằm ở dòng nào? Tôi nên thay đổi chiến thuật gì?"*.

### Ví dụ thực tế: Viết Code Python

* **Bước 1 (Actor):** LLM viết một đoạn code để trích xuất dữ liệu web.
* **Bước 2 (Evaluator):** Hệ thống chạy code và báo lỗi `AttributeError: 'NoneType' object has no attribute 'find'`.
* **Bước 3 (Self-Reflection):** LLM nhìn vào lỗi và tự nhủ: *"À, tôi đã quên kiểm tra xem thẻ HTML có tồn tại hay không trước khi tìm nội dung bên trong. Lần tới tôi cần thêm câu lệnh if-else"*.
* **Bước 4 (Actor - Retry):** LLM viết lại code dựa trên bài học trên và thành công.

---

## 3. Ưu điểm và Nhược điểm

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Độ chính xác** | Cải thiện đáng kể trong các tác vụ phức tạp (Logic, Code, Toán). | Tốn kém hơn do phải thực hiện nhiều lượt gọi API (multi-turn). |
| **Tính linh hoạt** | Có thể học hỏi từ lỗi mà không cần huấn luyện lại (fine-tuning) mô hình. | Độ trễ (Latency) cao vì phải chờ vòng lặp suy ngẫm. |
| **Khả năng giải thích** | Chúng ta có thể đọc được quá trình "suy ngẫm" của AI để biết nó hiểu sai ở đâu. | Có nguy cơ bị "hallucination" (ảo giác) ngay trong chính bước suy ngẫm. |

---

## 4. Những quan niệm sai lầm phổ biến

* **Sai lầm 1: "Chỉ cần bảo AI 'Hãy tự kiểm tra lại' là xong."**
* *Thực tế:* Reflexion cần một cơ chế đánh giá (Evaluator) khách quan (như trình biên dịch code hoặc bộ kiểm tra logic). Nếu chỉ bảo AI tự xem lại mà không có dữ liệu phản hồi mới, nó thường sẽ lặp lại lỗi cũ một cách tự tin hơn.


* **Sai lầm 2: "Reflexion làm cho model thông minh hơn mãi mãi."**
* *Thực tế:* Các bài học trong Reflexion thường được lưu vào **Context (bộ nhớ ngắn hạn)**. Khi bạn bắt đầu một phiên làm việc mới, model sẽ "quên" những gì nó đã phản chiếu trừ khi bạn lưu các bài học đó vào một cơ sở dữ liệu (Long-term memory).


* **Sai lầm 3: "Model nào cũng làm được Reflexion."**
* *Thực tế:* Kỹ thuật này đòi hỏi model phải có khả năng lập luận (Reasoning) tốt. Các model nhỏ thường không đủ khả năng tự nhận ra lỗi logic của mình dù đã được chỉ ra.



---

## 5. Cập nhật mới nhất 2025

Đến năm 2025, khái niệm Reflexion đã tiến hóa vượt bậc so với các bài báo khoa học ban đầu:

1. **Internalized Reflexion (Suy ngẫm nội tại):** Các mô hình như **OpenAI o1, o3** hoặc **DeepSeek-R1** đã tích hợp sẵn vòng lặp "suy ngẫm" vào bên trong quá trình suy nghĩ (Hidden Chain of Thought). Bạn không còn cần phải thiết lập các Agent rời rạc; mô hình tự thực hiện hàng ngàn vòng lặp Reflexion siêu tốc trước khi đưa ra câu trả lời cuối cùng.
2. **Multi-Agent Reflexion:** Không chỉ một AI tự soi mình, mà một "Hội đồng AI" (Consensus) sẽ phản biện lẫn nhau. Agent A làm, Agent B chỉ lỗi, Agent C tổng hợp bài học.
3. **Học máy từ Reflexion:** Các bài học thu được từ quá trình suy ngẫm đang được dùng để tạo ra dữ liệu tổng hợp (Synthetic Data) chất lượng cao nhằm huấn luyện các mô hình nhỏ hơn (Distillation), giúp chúng có khả năng suy luận như mô hình lớn mà không tốn tài nguyên.

---

# Example 

Để áp dụng kỹ thuật **Reflexion** một cách hiệu quả, chúng ta không nên dùng một Prompt duy nhất mà nên sử dụng một **quy trình (workflow)** gồm các bước riêng biệt.

Dưới đây là một hệ thống Prompt Template giúp bạn thiết lập một "vòng lặp tự học" cho AI, áp dụng cho các tác vụ khó như: Lập trình, giải quyết vấn đề logic, hoặc viết lách chuyên sâu.


## Bước 1: The Actor Prompt (Khởi tạo)

Ở bước này, mục tiêu là yêu cầu AI thực hiện nhiệm vụ một cách tốt nhất có thể trong lần thử đầu tiên.

> **Prompt:**
> "Bạn là một chuyên gia trong lĩnh vực **[Lĩnh vực, ví dụ: Viết nội dung kỹ thuật]**. Nhiệm vụ của bạn là **[Nhiệm vụ cụ thể]**.
> **Yêu cầu:** > - Đối tượng độc giả: [Ví dụ: Người mới bắt đầu]
> * Giọng văn: [Ví dụ: Chuyên nghiệp, dễ hiểu]
> * Định dạng: [Ví dụ: Markdown]
> 
> 
> Hãy thực hiện nhiệm vụ này và liệt kê các giả định bạn đã sử dụng để đưa ra câu trả lời."

---

## Bước 2: The Evaluator Prompt (Đánh giá khách quan)

Sau khi AI đưa ra kết quả, bạn đừng vội dùng ngay. Hãy dùng Prompt này để AI đóng vai một "người kiểm định khắt khe".

> **Prompt (Dán kết quả bước 1 vào):**
> "Bây giờ, hãy đóng vai một **[Người kiểm định/Biên tập viên cấp cao]**. Hãy phê bình bản thảo trên dựa trên các tiêu chí sau:
> 1. **Độ chính xác:** Có lỗi sai nào về mặt kỹ thuật hoặc logic không?
> 2. **Sự rõ ràng:** Có đoạn nào khó hiểu đối với đối tượng độc giả mục tiêu không?
> 3. **Tính đầy đủ:** Có khía cạnh quan trọng nào bị bỏ sót không?
> 
> 
> Hãy liệt kê các điểm yếu một cách thẳng thắn và đánh giá thang điểm 1-10."

---

## Bước 3: The Reflection Prompt (Suy ngẫm kiến trúc)

Đây là "linh hồn" của Reflexion. AI phải tự phân tích **tại sao** nó lại mắc lỗi ở bước trên.

> **Prompt:**
> "Dựa trên những phê bình ở Bước 2, hãy thực hiện một phân tích tự soi chiếu (Self-reflection):
> * Tại sao phương pháp tiếp cận ban đầu của bạn dẫn đến những lỗi này?
> * Bạn đã hiểu sai yêu cầu ở đâu (nếu có)?
> * Bạn cần thay đổi chiến thuật gì để đạt điểm 10/10?
> 
> 
> **Lưu ý:** Chỉ đưa ra các bài học rút ra, chưa viết lại nội dung vội."

---

## Bước 4: The Final Actor Prompt (Hoàn thiện)

Sử dụng các bài học từ bước suy ngẫm để tạo ra kết quả cuối cùng.

> **Prompt:**
> "Bây giờ, hãy sử dụng tất cả các phản hồi từ người kiểm định và các bài học bạn vừa rút ra ở bước suy ngẫm. Hãy viết lại toàn bộ nội dung để khắc phục triệt để các vấn đề đã nêu.
> Đảm bảo rằng kết quả cuối cùng là phiên bản hoàn hảo nhất của bạn."

---

## 💡 Ví dụ áp dụng thực tế: Giải toán logic phức tạp

Nếu bạn dùng một model không có sẵn "Reasoning" mạnh như GPT-4o (không phải bản o1), bạn sẽ thấy sự khác biệt:

1. **Actor:** Giải bài toán đố về xác suất. (AI có thể sai do tính toán vội).
2. **Evaluator:** "Kiểm tra lại từng dòng tính toán, kiểm tra xem có vi phạm định luật xác suất nào không."
3. **Reflection:** "Tôi đã áp dụng sai công thức Bayes vì chưa tính đến biến số phụ. Tôi cần xác định lại không gian mẫu."
4. **Final:** Đưa ra đáp án hoàn chỉnh với logic đã được sửa đổi.

---

### Mẹo nhỏ cho năm 2025:

Nếu bạn đang sử dụng các mô hình như **GPT-4o, Claude 3.5 Sonnet**, bạn có thể gộp 4 bước này vào một **"Mega Prompt"** duy nhất bằng cách sử dụng các thẻ XML để cấu trúc tư duy:

```markdown
Hãy thực hiện nhiệm vụ sau theo quy trình Reflexion:
<thinking>
1. Thực hiện nhiệm vụ.
2. Tự phê bình lỗi logic/ngôn ngữ.
3. Rút ra bài học cụ thể.
</thinking>

<final_answer>
Dựa trên quá trình suy nghĩ trên, đưa ra kết quả cuối cùng hoàn thiện nhất.
</final_answer>

```
