# Tree of Thoughts (ToT) 

Reference: https://www.promptingguide.ai/techniques/tot


## 1. Định nghĩa cốt lõi (Core Definition)

**Tree of Thoughts (ToT)** là một khung công việc (framework) giải quyết vấn đề bằng cách cho phép mô hình ngôn ngữ lớn (LLM) khám phá nhiều con đường suy luận khác nhau dưới dạng các "nhánh" của một cái cây.

Thay vì chỉ đưa ra một câu trả lời duy nhất từ đầu đến cuối, ToT chia nhỏ vấn đề thành các đơn vị suy nghĩ (thoughts). Tại mỗi bước, AI sẽ tạo ra nhiều phương án, tự đánh giá chúng và quyết định xem nên tiếp tục phát triển nhánh nào, hoặc dừng lại để thử một hướng khác.

---

## 2. Nguyên lý hoạt động

ToT hoạt động dựa trên sự kết hợp giữa khả năng ngôn ngữ của AI và các thuật toán tìm kiếm cổ điển trong khoa học máy tính.

Cấu trúc của ToT gồm 4 thành phần chính:

1. **Phân rã suy nghĩ (Thought Decomposition):** Chia bài toán lớn thành các bước nhỏ (ví dụ: một dòng lập luận, một bước giải toán).
2. **Tạo suy nghĩ (Thought Generator):** Tại mỗi bước, AI tạo ra  phương án khả thi thay vì chỉ một.
3. **Đánh giá trạng thái (State Evaluator):** AI tự đóng vai "giám khảo" để chấm điểm các phương án (ví dụ: "chắc chắn đúng", "có khả năng", hoặc "loại bỏ").
4. **Thuật toán tìm kiếm (Search Algorithm):** Sử dụng các thuật toán như **BFS** (Tìm kiếm theo chiều rộng) hoặc **DFS** (Tìm kiếm theo chiều sâu) để điều hướng cây suy luận.

### Ví dụ thực tế: Trò chơi "Game of 24"

Giả sử bạn có 4 số: **4, 9, 10, 13**. Mục tiêu là dùng các phép tính (+, -, *, /) để ra kết quả 24.

* **Cách tiếp cận thông thường:** AI có thể thử  rồi bị rối.
* **Cách tiếp cận ToT:**
* **Bước 1:** Tạo ra các nhánh:  hoặc  hoặc 
* **Bước 2:** Đánh giá: Nhánh  có vẻ hứa hẹn vì gần 24. Nhánh  quá lớn, loại bỏ ngay.
* **Bước 3:** Tiếp tục phát triển nhánh hứa hẹn nhất cho đến khi tìm thấy đáp án.



---

## 3. Ưu điểm và Nhược điểm

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Độ chính xác** | Vượt trội trong các bài toán logic, toán học và lập kế hoạch phức tạp. | Tốn kém chi phí (Token) vì phải tạo nhiều phương án trung gian. |
| **Khả năng tự sửa lỗi** | Có thể quay lại (backtrack) nếu nhận ra nhánh hiện tại không khả thi. | Độ trễ (Latency) cao do phải thực hiện nhiều lượt truy vấn AI. |
| **Tính minh bạch** | Con người có thể theo dõi được lộ trình suy luận qua từng nút của cây. | Cần thiết lập hệ thống điều khiển phức tạp (không chỉ là một câu prompt đơn giản). |

---

## 4. Những quan niệm sai lầm phổ biến

Khi nói về ToT, rất nhiều người (kể cả những người làm kỹ thuật) thường mắc phải các lỗi sau:

* **Lầm tưởng 1: "ToT chỉ là một câu Prompt dài"**
> **Thực tế:** ToT không phải là một "siêu Prompt". Nó là một **quy trình (pipeline)** hoặc một framework yêu cầu code bên ngoài (như Python) để điều hướng các bước suy luận, lưu trữ trạng thái cây và gọi API nhiều lần.


* **Lầm tưởng 2: "Cứ dùng ToT là kết quả sẽ tốt hơn"**
> **Thực tế:** Với các tác vụ sáng tạo đơn giản (viết thư, tóm tắt), ToT chỉ làm lãng phí tài nguyên. Nó chỉ thực sự phát huy sức mạnh khi bài toán có không gian lời giải lớn và cần sự chính xác tuyệt đối.


* **Lầm tưởng 3: "ToT là một tính năng có sẵn trong ChatGPT"**
> **Thực tế:** Mặc dù các mô hình như GPT-4o hay Claude 3.5 có thể mô phỏng một phần ToT nếu được yêu cầu, nhưng một hệ thống ToT thực thụ cần một cấu trúc lặp (loop) và đánh giá khách quan mà giao diện chat thông thường khó đáp ứng hoàn hảo.



---

## 5. Kết luận

Tree of Thoughts đưa AI từ một "người nói nhanh nhưng đôi khi ẩu" trở thành một "người giải quyết vấn đề cẩn trọng", biết cân nhắc mọi khả năng trước khi đưa ra quyết định cuối cùng. Đây là bước tiến quan trọng hướng tới Hệ thống trí tuệ tổng quát (AGI).


--- 

Code reference: 
- https://github.com/princeton-nlp/tree-of-thought-llm - 5.7k stars
- https://github.com/kyegomez/tree-of-thoughts - 4.6k stars