# Basic of Prompting 

Nội dung được dịch từ: https://www.promptingguide.ai/introduction/basics

## Prompting an LLM

Bạn có thể đạt được nhiều kết quả chỉ với những lời nhắc đơn giản, nhưng chất lượng đầu ra phụ thuộc vào lượng thông tin bạn cung cấp cho mô hình và mức độ tinh tế trong việc xây dựng lời nhắc. Một lời nhắc có thể bao gồm các thông tin như hướng dẫn hoặc câu hỏi bạn truyền vào mô hình, đồng thời cũng có thể chứa các chi tiết khác như ngữ cảnh, dữ liệu đầu vào hoặc các ví dụ minh họa. Bạn có thể sử dụng những yếu tố này để hướng dẫn mô hình một cách hiệu quả hơn nhằm nâng cao chất lượng kết quả.

Hãy bắt đầu bằng cách xem xét một ví dụ cơ bản về một lời nhắc đơn giản:

Prompt

```
The sky is

```

Output

```
blue.

```

Điều cần lưu ý là khi sử dụng các mô hình trò chuyện của OpenAI như `gpt-3.5-turbo` hoặc `gpt-4` , bạn có thể cấu trúc lời nhắc (prompt) của mình bằng ba vai trò khác nhau: `system` , `user` và `assistant` . Thông điệp hệ thống (system message) không bắt buộc, nhưng giúp thiết lập hành vi tổng thể của trợ lý. Ví dụ ở trên chỉ bao gồm một thông điệp người dùng (user message), bạn có thể sử dụng thông điệp này để kích hoạt trực tiếp mô hình. Vì lý do đơn giản hóa, tất cả các ví dụ trong tài liệu này—trừ khi được nêu rõ ràng—sẽ chỉ sử dụng thông điệp user để kích hoạt mô hình `gpt-3.5-turbo` . Thông điệp `assistant` trong ví dụ trên tương ứng với phản hồi của mô hình. Bạn cũng có thể xác định một thông điệp trợ lý (assistant message) để cung cấp các ví dụ minh họa cho hành vi mong muốn. 

Bạn có thể quan sát từ ví dụ lời nhắc ở trên rằng mô hình ngôn ngữ trả lời bằng một chuỗi các token hợp lý trong bối cảnh đã cho `"The sky is"` . Tuy nhiên, đầu ra có thể bất ngờ hoặc lệch xa mục tiêu mà bạn muốn đạt được. Thực tế, ví dụ cơ bản này làm nổi bật nhu cầu phải cung cấp thêm bối cảnh hoặc hướng dẫn cụ thể hơn về những gì bạn thực sự muốn hệ thống thực hiện. Đây chính là bản chất cốt lõi của Prompt Engineering.

Hãy thử cải thiện ví dụ này một chút:

Prompt

```
Complete the sentence: 
The sky is
```

Output

```
blue during the day and dark at night.
```

Điều đó có tốt hơn không? À, với lời nhắc ở trên, bạn đang hướng dẫn mô hình hoàn thành câu, do đó kết quả trông tốt hơn nhiều vì nó tuân theo chính xác những gì bạn yêu cầu (“hoàn thành câu”). Cách tiếp cận thiết kế các lời nhắc hiệu quả nhằm hướng dẫn mô hình thực hiện một nhiệm vụ mong muốn như vậy được gọi là *Prompt Engineering* trong hướng dẫn này.

Ví dụ trên đây là minh họa cơ bản về những khả năng mà các LLMs hiện nay có thể thực hiện. Các LLMs ngày nay có khả năng thực hiện nhiều loại nhiệm vụ nâng cao, từ *Summarization* văn bản đến suy luận toán học và tạo mã.

## Prompt Formatting

Bạn đã thử một lời nhắc rất đơn giản ở trên. Một lời nhắc tiêu chuẩn có định dạng như sau:

```
<Question>?
```

or 

```
<Instruction>
```

Bạn có thể định dạng điều này theo dạng hỏi–đáp (QA), vốn là chuẩn trong nhiều tập dữ liệu hỏi–đáp, như sau:

```
Q: <Question>?
A: 
```

Khi đưa ra lời nhắc (prompt) theo cách trên, phương pháp này còn được gọi là “lời nhắc không mẫu” (zero-shot prompting), tức là bạn trực tiếp yêu cầu mô hình đưa ra câu trả lời mà không cung cấp bất kỳ ví dụ hay minh họa nào về nhiệm vụ mà bạn muốn mô hình thực hiện. Một số mô hình ngôn ngữ lớn có khả năng thực hiện lời nhắc không mẫu, tuy nhiên khả năng này phụ thuộc vào mức độ phức tạp và yêu cầu kiến thức của nhiệm vụ cụ thể cũng như các nhiệm vụ mà mô hình đã được huấn luyện để thực hiện tốt.

Một ví dụ cụ thể về lời nhắc như sau:

```
Q: What is prompt engineering?
```

Với một số mô hình mới hơn, bạn có thể bỏ qua phần “Q:” vì mô hình đã ngầm hiểu đây là một nhiệm vụ trả lời câu hỏi dựa trên cách chuỗi được cấu thành. Nói cách khác, lời nhắc có thể được đơn giản hóa như sau:

```
What is prompt engineering?
```

Với định dạng tiêu chuẩn nêu trên, một kỹ thuật đưa ra yêu cầu (prompting) phổ biến và hiệu quả là “few-shot prompting”, trong đó người dùng cung cấp các ví dụ minh họa (tức là các minh chứng). Bạn có thể định dạng các yêu cầu theo kiểu few-shot như sau:

```
<Question>?
<Answer>

<Question>?
<Answer>

<Question>?
<Answer>

<Question>?

```

Phiên bản ở định dạng hỏi–đáp (QA) sẽ có dạng như sau:

```
Q: <Question>?
A: <Answer>

Q: <Question>?
A: <Answer>

Q: <Question>?
A: <Answer>

Q: <Question>?
A:
```

Lưu ý rằng việc sử dụng định dạng hỏi–đáp (QA) là không bắt buộc. Định dạng lời nhắc (prompt) phụ thuộc vào từng nhiệm vụ cụ thể. Chẳng hạn, bạn có thể thực hiện một tác vụ phân loại đơn giản và cung cấp các ví dụ minh họa cho nhiệm vụ đó như sau:

```
This is awesome! // Positive
This is bad! // Negative
Wow that movie was rad! // Positive
What a horrible show! //
```

Output:

```
Negative
```

Các lời nhắc few-shot cho phép học trong bối cảnh (in-context learning), tức là khả năng của các mô hình ngôn ngữ trong việc học các tác vụ dựa trên một vài minh họa. Chúng tôi sẽ trình bày chi tiết hơn về lời nhắc zero-shot và lời nhắc few-shot trong các phần tiếp theo.

