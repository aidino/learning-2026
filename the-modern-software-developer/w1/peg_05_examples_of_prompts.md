# Examples of Prompts 

Nội dung được dịch từ:  https://www.promptingguide.ai/introduction/examples

Phần trước đã giới thiệu một ví dụ cơ bản về cách xây dựng lời nhắc cho các mô hình ngôn ngữ lớn (LLMs).

Phần này sẽ cung cấp thêm nhiều ví dụ về cách sử dụng lời nhắc để thực hiện các nhiệm vụ khác nhau, đồng thời giới thiệu các khái niệm then chốt trong quá trình đó. Thông thường, cách hiệu quả nhất để học các khái niệm là thông qua việc phân tích các ví dụ. Một số ví dụ dưới đây minh họa cách bạn có thể sử dụng các lời nhắc được thiết kế kỹ lưỡng để thực hiện các loại nhiệm vụ khác nhau.

## Text Summarization

Một trong những nhiệm vụ tiêu chuẩn trong lĩnh vực tạo ngôn ngữ tự nhiên là tóm tắt văn bản. Tóm tắt văn bản có thể bao gồm nhiều phong cách và lĩnh vực khác nhau. Thực tế, một trong những ứng dụng hứa hẹn nhất của các mô hình ngôn ngữ chính là khả năng tóm tắt các bài báo và khái niệm thành những đoạn tóm tắt ngắn gọn, dễ đọc. Hãy cùng thử một tác vụ tóm tắt cơ bản bằng cách sử dụng lời nhắc (prompt).

Giả sử bạn muốn tìm hiểu về kháng sinh, bạn có thể thử một lời nhắc như sau:

```
Explain antibiotics
A:
```

Output:

```
Antibiotics are a type of medication used to treat bacterial infections. They work by either killing the bacteria or preventing them from reproducing, allowing the body’s immune system to fight off the infection. Antibiotics are usually taken orally in the form of pills, capsules, or liquid solutions, or sometimes administered intravenously. They are not effective against viral infections, and using them inappropriately can lead to antibiotic resistance.
```

Ký hiệu “A:” là định dạng lời nhắc tường minh thường được sử dụng trong các bài toán trả lời câu hỏi. Ở đây, bạn dùng ký hiệu này để thông báo cho mô hình rằng phần tiếp theo sẽ chứa câu trả lời mong đợi. Trong ví dụ này, chưa rõ việc sử dụng ký hiệu này mang lại lợi ích gì so với việc không dùng, nhưng chúng ta sẽ dành việc phân tích chi tiết hơn cho các ví dụ sau. Giả sử rằng thông tin ở trên vẫn còn quá dài và bạn muốn tóm tắt thêm. Thật vậy, bạn hoàn toàn có thể yêu cầu mô hình tóm tắt nội dung thành một câu duy nhất như sau:

Prompt 

```
Antibiotics are a type of medication used to treat bacterial infections. They work by either killing the bacteria or preventing them from reproducing, allowing the body’s immune system to fight off the infection. Antibiotics are usually taken orally in the form of pills, capsules, or liquid solutions, or sometimes administered intravenously. They are not effective against viral infections, and using them inappropriately can lead to antibiotic resistance.

Explain the above in one sentence:
```

Output:

```
Antibiotics are medications used to treat bacterial infections by either killing the bacteria or stopping them from reproducing, but they are not effective against viruses and overuse can lead to antibiotic resistance.
```

Mặc dù không cần quá chú trọng vào độ chính xác của đầu ra ở trên—vấn đề này sẽ được đề cập chi tiết hơn trong một hướng dẫn sau—mô hình đã cố gắng tóm tắt đoạn văn thành một câu duy nhất. Bạn có thể đưa ra những chỉ dẫn thông minh hơn, nhưng phần này sẽ được trình bày chi tiết hơn trong chương sau. Bạn hoàn toàn có thể tạm dừng tại đây và tự thực hành để xem liệu mình có thu được kết quả tốt hơn hay không.

## Information Extraction 

Mặc dù các mô hình ngôn ngữ được huấn luyện chủ yếu để thực hiện việc tạo văn bản tự nhiên và các tác vụ liên quan, chúng cũng rất giỏi trong việc thực hiện phân loại cũng như nhiều tác vụ xử lý ngôn ngữ tự nhiên (NLP) khác.

Dưới đây là một ví dụ về lời nhắc (prompt) nhằm trích xuất thông tin từ một đoạn văn cho trước.

```
Author-contribution statements and acknowledgements in research papers should state clearly and specifically whether, and to what extent, the authors used AI technologies such as ChatGPT in the preparation of their manuscript and analysis. They should also indicate which LLMs were used. This will alert editors and reviewers to scrutinize manuscripts more carefully for potential biases, inaccuracies and improper source crediting. Likewise, scientific journals should be transparent about their use of LLMs, for example when selecting submitted manuscripts.

Mention the large language model based product mentioned in the paragraph above:
```

Output:

```
The large language model based product mentioned in the paragraph above is ChatGPT.
```

Đến lúc này, rõ ràng là bạn có thể yêu cầu mô hình thực hiện các tác vụ khác nhau chỉ bằng cách hướng dẫn nó cách thức thực hiện. Đây là một khả năng mạnh mẽ mà các nhà phát triển sản phẩm AI đã và đang khai thác để xây dựng những sản phẩm và trải nghiệm ấn tượng.

## Question Answering

Một trong những cách hiệu quả nhất để mô hình đưa ra các câu trả lời cụ thể là cải thiện định dạng của lời nhắc (prompt). Như đã trình bày ở phần trước, một lời nhắc có thể kết hợp các thành phần như hướng dẫn, ngữ cảnh, đầu vào và chỉ thị đầu ra nhằm đạt được kết quả tốt hơn. Mặc dù các thành phần này không bắt buộc phải có, việc sử dụng chúng đã trở thành một thực hành tốt, bởi vì mức độ cụ thể trong hướng dẫn càng cao thì kết quả thu được càng tốt. Dưới đây là ví dụ minh họa cách xây dựng một lời nhắc theo cấu trúc rõ ràng hơn.

```
Answer the question based on the context below. Keep the answer short and concise. Respond "Unsure about answer" if not sure about the answer.

Context: Teplizumab traces its roots to a New Jersey drug company called Ortho Pharmaceutical. There, scientists generated an early version of the antibody, dubbed OKT3. Originally sourced from mice, the molecule was able to bind to the surface of T cells and limit their cell-killing potential. In 1986, it was approved to help prevent organ rejection after kidney transplants, making it the first therapeutic antibody allowed for human use.

Question: What was OKT3 originally sourced from?

Answer:
```

Output:

```
Mice.
```

## Text Classification

Cho đến nay, bạn đã sử dụng các hướng dẫn đơn giản để thực hiện một nhiệm vụ. Với tư cách là một kỹ sư thiết kế lời nhắc (prompt engineer), bạn cần nâng cao khả năng đưa ra các hướng dẫn hiệu quả hơn. Tuy nhiên, đó chưa phải là tất cả! Bạn cũng sẽ nhận thấy rằng đối với những trường hợp sử dụng phức tạp hơn, chỉ cung cấp hướng dẫn thôi là chưa đủ. Đây chính là lúc bạn cần suy nghĩ sâu hơn về bối cảnh và các yếu tố khác nhau có thể sử dụng trong một lời nhắc. Các yếu tố khác mà bạn có thể cung cấp bao gồm input data hoặc examples .

```
Classify the text into neutral, negative or positive. 

Text: I think the food was okay. 
Sentiment:
```

Output:

```
Neutral
```

Bạn đã đưa ra hướng dẫn phân loại văn bản và mô hình đã phản hồi bằng 'Neutral' , điều này là chính xác. Không có gì sai ở đây, nhưng hãy giả sử rằng điều bạn thực sự cần là mô hình phải trả về nhãn theo đúng định dạng bạn yêu cầu. Vì vậy, thay vì Neutral , bạn muốn nó trả về neutral . Làm thế nào để đạt được điều này? Có nhiều cách khác nhau để thực hiện việc này. Ở đây, bạn quan tâm đến tính cụ thể, do đó càng cung cấp nhiều thông tin trong lời nhắc (prompt), kết quả thu được càng tốt. Bạn có thể thử đưa ra các ví dụ để làm rõ hành vi đúng cần thiết. Hãy thử lại:

```
Classify the text into neutral, negative or positive. 

Text: I think the vacation is okay.
Sentiment: neutral 

Text: I think the food was okay. 
Sentiment:

```

Output:

```
Neutral
```

Tuyệt vời! Lần này mô hình đã trả về neutral , chính là nhãn cụ thể mà bạn đang tìm kiếm. Có vẻ như ví dụ được cung cấp trong lời nhắc đã giúp mô hình đưa ra đầu ra một cách chính xác và cụ thể hơn.


Để làm nổi bật lý do vì sao đôi khi việc cụ thể hóa là quan trọng, hãy xem ví dụ dưới đây và xác định vấn đề:

```
Classify the text into nutral, negative or positive. 
Text: I think the vacation is okay.
Sentiment:
```

Output:

```
Neutral
```

Vấn đề ở đây là gì? Như một gợi ý, nhãn giả định `nutral` hoàn toàn bị mô hình bỏ qua. Thay vào đó, mô hình lại xuất ra nhãn `Neutral` do có xu hướng thiên lệch về nhãn này. Tuy nhiên, hãy giả sử rằng điều bạn thực sự mong muốn là nhãn `nutral` . Bạn sẽ khắc phục vấn đề này như thế nào? Có thể bạn sẽ thử bổ sung mô tả cho các nhãn hoặc thêm nhiều ví dụ hơn vào lời nhắc (prompt)? Nếu bạn chưa chắc chắn, chúng ta sẽ thảo luận một số giải pháp trong các phần tiếp theo.


## Conversation

Có lẽ một trong những điều thú vị nhất bạn có thể đạt được thông qua Prompt Engineering là hướng dẫn hệ thống LLM về cách hành xử, mục đích và bản sắc của nó. Phương pháp này đặc biệt hữu ích khi bạn đang xây dựng các hệ thống hội thoại như chatbot hỗ trợ khách hàng.

Ví dụ, hãy cùng tạo một hệ thống hội thoại có khả năng đưa ra các câu trả lời mang tính kỹ thuật và khoa học hơn đối với các câu hỏi. Lưu ý cách bạn trực tiếp chỉ định cho mô hình cách hành xử thông qua phần hướng dẫn—phương pháp này đôi khi được gọi là “gợi ý vai trò” (role prompting).

Prompt: 

```
The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.

Human: Hello, who are you?
AI: Greeting! I am an AI research assistant. How can I help you today?
Human: Can you tell me about the creation of blackholes?
AI:
```

Output:

```
Sure! Black holes are regions of spacetime where the gravitational force is so strong that nothing, not even light, can escape from it. They are created when a very massive star dies and its core collapses in on itself, forming a singularity of infinite density. The intense gravity of the singularity pulls in all the matter and radiation around it, creating the black hole.
```

Trợ lý nghiên cứu AI của chúng ta nghe có vẻ quá kỹ thuật, phải không? Được rồi, hãy thay đổi hành vi này và hướng dẫn hệ thống đưa ra các câu trả lời dễ tiếp cận hơn.

Prompt:

```
The following is a conversation with an AI research assistant. The assistant answers should be easy to understand even by primary school students.

Human: Hello, who are you?
AI: Greeting! I am an AI research assistant. How can I help you today?
Human: Can you tell me about the creation of black holes?
AI:
```

Output:

```
Sure! Black holes are created when a very massive star runs out of fuel and collapses in on itself. The gravity of the star is so strong that nothing, not even light, can escape its pull. This creates a point in space-time with an intense gravitational force called a black hole.
```

Bạn đã đạt được một số tiến triển. Bạn có thể tiếp tục cải thiện hơn nữa. Nếu bạn thêm nhiều ví dụ hơn, bạn có thể thu được kết quả tốt hơn nữa.

## Code Generation

Một ứng dụng mà các LLMs thực hiện rất hiệu quả là sinh mã. Copilot là một ví dụ điển hình cho ứng dụng này. Có vô số tác vụ sinh mã có thể thực hiện được nhờ các lời nhắc (prompt) được thiết kế thông minh. Dưới đây là một vài ví dụ minh họa.

Đầu tiên, hãy thử một chương trình đơn giản để chào người dùng.

Prompt:

```
/*
Ask the user for their name and say "Hello"
*/
```

Output:

```
let name = prompt("What is your name?");
console.log(`Hello, ${name}!`);
```

Lưu ý rằng bạn thậm chí không cần phải chỉ định ngôn ngữ cần sử dụng.

Hãy chuyển sang một mức độ khác. Ví dụ dưới đây minh họa khả năng mạnh mẽ của các LLMs khi dành thêm một chút nỗ lực để thiết kế các lời nhắc.

Prompt:

```
"""
Table departments, columns = [DepartmentId, DepartmentName]
Table students, columns = [DepartmentId, StudentId, StudentName]
Create a MySQL query for all students in the Computer Science Department
"""
```

Output:

```
SELECT StudentId, StudentName 
FROM students 
WHERE DepartmentId IN (SELECT DepartmentId FROM departments WHERE DepartmentName = 'Computer Science');
```

Điều này thật ấn tượng. Trong trường hợp này, bạn đã cung cấp dữ liệu về lược đồ cơ sở dữ liệu và yêu cầu mô hình tạo ra một truy vấn MySQL hợp lệ.


## Reasoning

Có lẽ một trong những nhiệm vụ khó khăn nhất đối với một LLM hiện nay là nhiệm vụ đòi hỏi một dạng suy luận nào đó. Suy luận là một trong những lĩnh vực thú vị nhất do các loại ứng dụng phức tạp có thể được phát triển từ các LLM.

Đã có một số cải tiến trong các tác vụ liên quan đến năng lực toán học. Tuy nhiên, cần lưu ý rằng các LLM hiện tại vẫn gặp khó khăn trong việc thực hiện các tác vụ suy luận, do đó đòi hỏi các kỹ thuật Prompt Engineering nâng cao hơn nữa. Chúng tôi sẽ trình bày những kỹ thuật nâng cao này trong hướng dẫn tiếp theo. Trước mắt, chúng tôi sẽ giới thiệu một vài ví dụ cơ bản nhằm minh họa khả năng tính toán số học.

Prompt: 

```
What is 9,000 * 9,000?
```

Output:

```
81,000,000
```

Hãy thử một điều gì đó khó hơn.


Prompt

```
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 

A: 
```

Output:

```
No, the odd numbers in this group add up to an odd number: 119.
```

Điều đó là không đúng! Hãy thử cải thiện điều này bằng cách nâng cao lời nhắc.

Prompt:

```
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 

Solve by breaking the problem into steps. First, identify the odd numbers, add them, and indicate whether the result is odd or even. 
```

Output:

```
Odd numbers: 15, 5, 13, 7, 1
Sum: 41 
41 is an odd number.
```

Tốt hơn nhiều, đúng không? Nhân tiện, chúng tôi đã thử nhiệm vụ này vài lần và mô hình thỉnh thoảng vẫn thất bại. Nếu bạn cung cấp các hướng dẫn rõ ràng hơn kết hợp với các ví dụ minh họa, điều đó có thể giúp đạt được kết quả chính xác hơn.

Trong phần tiếp theo, chúng ta sẽ trình bày thêm các khái niệm và kỹ thuật nâng cao hơn nữa trong lĩnh vực Prompt Engineering nhằm cải thiện hiệu suất trên tất cả những nhiệm vụ này cũng như các nhiệm vụ phức tạp hơn.

