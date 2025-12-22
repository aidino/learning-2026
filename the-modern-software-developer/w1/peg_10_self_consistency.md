# Self-Consistency 

Reference: https://www.promptingguide.ai/techniques/consistency

### 1. Định nghĩa cốt lõi

**Self-Consistency** là một kỹ thuật Prompt Engineering nâng cao, hoạt động như một cơ chế "bỏ phiếu đa số" (majority voting).

Thay vì chỉ yêu cầu AI đưa ra một lời giải duy nhất theo trình tự suy nghĩ (**Chain-of-Thought - CoT**), chúng ta yêu cầu mô hình tạo ra **nhiều con đường suy luận khác nhau** cho cùng một câu hỏi. Sau đó, kết quả nào xuất hiện nhiều nhất trong các lần thử đó sẽ được chọn làm câu trả lời cuối cùng.

> **Hiểu đơn giản:** Thay vì tin lời một người, bạn hỏi 10 người thông minh cùng một câu hỏi. Nếu 7 người đưa ra cùng một kết quả (dù cách giải thích có thể hơi khác nhau), bạn sẽ tin vào kết quả đó hơn.

---

### 2. Nguyên lý hoạt động và Ví dụ thực tế

Self-Consistency hoạt động dựa trên giả định rằng: **Một bài toán khó có thể có nhiều cách giải, nhưng các cách giải đúng thường hội tụ về một đáp án duy nhất.**

#### Quy trình 3 bước:

1. **Prompting:** Sử dụng Chain-of-Thought (CoT) để kích thích AI suy luận.
2. **Sampling:** Yêu cầu AI sinh ra nhiều phản hồi (ví dụ: 5, 10 hoặc 20 mẫu) bằng cách điều chỉnh tham số `temperature > 0`.
3. **Aggregation:** Thống kê các đáp án cuối cùng và chọn đáp án có số lần xuất hiện cao nhất.

#### Ví dụ thực tế:

**Câu hỏi:** *"Lan có 3 quả táo. Cô ấy mua thêm 2 túi táo, mỗi túi có 5 quả. Sau đó cô ấy cho bạn 4 quả. Hỏi Lan còn lại bao nhiêu quả?"*

* **Lần suy luận 1:** Lan có 3 quả. Thêm 2 x 5 = 10 quả. Tổng là 13. Cho đi 4 còn **9**.
* **Lần suy luận 2:** 2 túi là 10 quả, cộng 3 quả ban đầu là 13 quả. Trừ 4 quả cho bạn là còn **9**.
* **Lần suy luận 3:** Lan có 3 quả, cho đi 4 quả (thiếu 1), mua thêm 10 quả, vậy còn **9**.
* **Lần suy luận 4 (Lỗi):** Lan có 3 quả, thêm 2 túi là 5 quả. Tổng 8 quả. Cho 4 còn **4**.

**Kết quả:** Đáp án **9** xuất hiện 3 lần, đáp án **4** xuất hiện 1 lần. Hệ thống chọn **9**.

---

### 3. Ưu điểm và Nhược điểm

| Đặc điểm | Ưu điểm | Nhược điểm |
| --- | --- | --- |
| **Độ chính xác** | Cải thiện đáng kể kết quả trong các bài toán toán học, logic và lập trình. | Không cải thiện nhiều cho các tác vụ sáng tạo hoặc yêu cầu kiến thức phổ thông. |
| **Độ tin cậy** | Giảm thiểu tình trạng "ảo tưởng" (hallucination) ngẫu nhiên của AI. | **Chi phí cao:** Tốn nhiều token hơn vì phải chạy nhiều lần cho một câu hỏi. |
| **Tính ứng dụng** | Không yêu cầu huấn luyện lại mô hình (Fine-tuning), chỉ cần thay đổi cách Prompt. | **Độ trễ (Latency):** Mất nhiều thời gian chờ đợi hơn để nhận được kết quả cuối cùng. |

---

### 4. Những quan niệm sai lầm phổ biến

#### Sai lầm 1: "Self-Consistency là một loại Prompt khác với Chain-of-Thought"

Thực tế, Self-Consistency là một **lớp bổ trợ (layer)** nằm trên CoT. Bạn không thể dùng Self-Consistency hiệu quả nếu không có CoT để mô hình trình bày các bước suy luận. CoT tạo ra "đường đi", Self-Consistency chọn "con đường phổ biến nhất".

#### Sai lầm 2: "Cứ hỏi nhiều lần là sẽ ra đáp án đúng"

Nếu mô hình hoàn toàn không hiểu kiến thức đó (ví dụ: một hằng số vật lý sai), thì dù bạn có hỏi 100 lần, nó vẫn sẽ đồng thanh đưa ra một đáp án sai một cách "nhất quán". Self-Consistency chỉ giải quyết được các lỗi logic ngẫu nhiên trong quá trình suy luận.

#### Sai lầm 3: "Chỉ cần dùng Temperature = 0 là đủ"

Nhiều người nghĩ đặt `temperature = 0` (để AI trả lời ổn định nhất) là tốt. Nhưng với Self-Consistency, bạn **cần** `temperature > 0` (thường là 0.5 - 0.7) để tạo ra sự đa dạng trong các hướng tiếp cận bài toán. Nếu tất cả các mẫu đều giống hệt nhau, việc bỏ phiếu sẽ trở nên vô nghĩa.

#### Sai lầm 4: "Nó chỉ dành cho toán học"

Mặc dù toán học là ví dụ điển hình, nhưng nó cực kỳ hiệu quả trong việc kiểm tra mã nguồn (coding) hoặc phân tích các tình huống pháp lý phức tạp, nơi một bước suy luận sai có thể dẫn đến kết luận sai hoàn toàn.


--- 

Có lẽ một trong những kỹ thuật tiên tiến nhất hiện nay trong lĩnh vực Prompt Engineering là tính nhất quán bản thân. Kỹ thuật này do Wang và cộng sự (2022) đề xuất, nhằm “thay thế phương pháp giải mã tham lam (greedy decoding) sơ khai vốn được sử dụng trong kỹ thuật gợi mở chuỗi lập luận (chain-of-thought prompting)”. Ý tưởng cốt lõi là lấy mẫu nhiều đường suy luận khác nhau thông qua kỹ thuật gợi mở chuỗi lập luận với số lượng mẫu hạn chế (few-shot CoT), sau đó sử dụng các kết quả sinh ra để chọn ra đáp án có mức độ nhất quán cao nhất. Phương pháp này giúp nâng cao hiệu năng của kỹ thuật gợi mở chuỗi lập luận trong các nhiệm vụ đòi hỏi suy luận số học và suy luận thường thức.

Hãy thử ví dụ sau đây cho bài toán suy luận số học:

```
When I was 6 my sister was half my age. Now
I’m 70 how old is my sister?
```


Output:

```
35
```

Kết quả đầu ra là sai! Chúng ta có thể cải thiện điều này bằng cách áp dụng tính nhất quán bản thân như thế nào? Hãy cùng thực hiện. Chúng ta sẽ sử dụng các ví dụ minh họa trong tài liệu few-shot của Wang và cộng sự (2022) (Bảng 17):


Prompt: 

```
Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done,
there will be 21 trees. How many trees did the grove workers plant today?
A: We start with 15 trees. Later we have 21 trees. The difference must be the number of trees they planted.
So, they must have planted 21 - 15 = 6 trees. The answer is 6.

Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
A: There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. The answer is 5.

Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
A: Leah had 32 chocolates and Leah’s sister had 42. That means there were originally 32 + 42 = 74
chocolates. 35 have been eaten. So in total they still have 74 - 35 = 39 chocolates. The answer is 39.

Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops
did Jason give to Denny?
A: Jason had 20 lollipops. Since he only has 12 now, he must have given the rest to Denny. The number of
lollipops he has given to Denny must have been 20 - 12 = 8 lollipops. The answer is 8.

Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does
he have now?
A: He has 5 toys. He got 2 from mom, so after that he has 5 + 2 = 7 toys. Then he got 2 more from dad, so
in total he has 7 + 2 = 9 toys. The answer is 9.

Q: There were nine computers in the server room. Five more computers were installed each day, from
monday to thursday. How many computers are now in the server room?
A: There are 4 days from monday to thursday. 5 computers were added each day. That means in total 4 * 5 =
20 computers were added. There were 9 computers in the beginning, so now there are 9 + 20 = 29 computers.
The answer is 29.

Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many
golf balls did he have at the end of wednesday?
A: Michael initially had 58 balls. He lost 23 on Tuesday, so after that he has 58 - 23 = 35 balls. On
Wednesday he lost 2 more so now he has 35 - 2 = 33 balls. The answer is 33.

Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
A: She bought 5 bagels for $3 each. This means she spent $15. She has $8 left.

Q: When I was 6 my sister was half my age. Now I’m 70 how old is my sister?
A:
```

Output 1: 

```
When I was 6 my sister was half my age, so she was 3. Now I am 70, so she is 70 - 3 = 67. The answer is 67.
```

Output 2: 

```
When the narrator was 6, his sister was half his age, which is 3. Now that the narrator is 70, his sister would be 70 - 3 = 67 years old. The answer is 67.
``` 

Output 3: 

```
When I was 6 my sister was half my age, so she was 3. Now I am 70, so she is 70/2 = 35. The answer is 35.
``` 

Việc tính toán để thu được đáp án cuối cùng bao gồm một vài bước (chi tiết xem trong bài báo), tuy nhiên vì mục đích đơn giản hóa, ta có thể thấy rằng đã xuất hiện một đáp án chiếm đa số, và đáp án này về cơ bản sẽ trở thành đáp án cuối cùng.

