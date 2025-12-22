# General Tips for Designing Prompts 

Nội dung được dịch từ: https://www.promptingguide.ai/introduction/tips

Dưới đây là một số mẹo cần ghi nhớ khi bạn thiết kế các lời nhắc của mình:

## Start Simple

Khi mới bắt đầu thiết kế lời nhắc (prompt), bạn cần ghi nhớ rằng đây thực chất là một quá trình lặp đi lặp lại, đòi hỏi rất nhiều thử nghiệm để đạt được kết quả tối ưu. Việc sử dụng một nền tảng thử nghiệm đơn giản do OpenAI hoặc Cohere cung cấp là một điểm khởi đầu tốt.

Bạn có thể bắt đầu với những lời nhắc đơn giản, sau đó dần bổ sung thêm các yếu tố và ngữ cảnh khác khi hướng tới những kết quả tốt hơn. Việc lặp lại và điều chỉnh lời nhắc trong suốt quá trình là vô cùng quan trọng vì lý do này. Khi đọc hướng dẫn này, bạn sẽ thấy nhiều ví dụ minh họa rằng tính cụ thể, tính đơn giản và sự súc tích thường mang lại kết quả tốt hơn.

Khi đối mặt với một nhiệm vụ lớn bao gồm nhiều tiểu nhiệm vụ khác nhau, bạn có thể thử phân chia nhiệm vụ đó thành các tiểu nhiệm vụ đơn giản hơn, rồi từng bước xây dựng và mở rộng giải pháp khi đã đạt được những kết quả khả quan hơn. Cách tiếp cận này giúp tránh việc đưa quá nhiều độ phức tạp vào quy trình thiết kế lời nhắc ngay từ giai đoạn đầu.

## The Instruction 

Bạn có thể thiết kế các lời nhắc hiệu quả cho nhiều tác vụ đơn giản bằng cách sử dụng các lệnh để hướng dẫn mô hình về mục tiêu bạn muốn đạt được, chẳng hạn như “Viết”, “Phân loại”, “Tóm tắt”, “Dịch”, “Sắp xếp”, v.v.

Lưu ý rằng bạn cũng cần thực hiện nhiều thử nghiệm để xác định phương án nào mang lại hiệu quả tốt nhất. Hãy thử các hướng dẫn khác nhau với các từ khóa, ngữ cảnh và dữ liệu khác nhau nhằm tìm ra giải pháp tối ưu nhất cho từng trường hợp sử dụng và nhiệm vụ cụ thể của bạn. Thông thường, ngữ cảnh càng cụ thể và liên quan trực tiếp đến nhiệm vụ bạn đang thực hiện thì kết quả càng tốt. Vai trò của việc lấy mẫu và bổ sung thêm ngữ cảnh sẽ được đề cập chi tiết hơn trong các hướng dẫn sắp tới.

Một số chuyên gia khuyến nghị đặt phần hướng dẫn ở đầu lời nhắc. Một khuyến nghị khác là sử dụng một ký hiệu phân tách rõ ràng (ví dụ: “###”) để tách biệt phần hướng dẫn và phần ngữ cảnh.

Ví dụ:

```
### Instruction ###
Translate the text below to Spanish:

Text: "hello!"
```

## Specificity

Hãy mô tả rất chi tiết và rõ ràng về hướng dẫn cũng như nhiệm vụ bạn muốn mô hình thực hiện. Càng mô tả tỉ mỉ và chi tiết thì kết quả thu được càng tốt. Yêu cầu này đặc biệt quan trọng khi bạn mong muốn một kết quả đầu ra nhất định hoặc một phong cách sinh nội dung cụ thể. Không tồn tại các token hay từ khóa cụ thể nào đảm bảo mang lại kết quả tốt hơn. Điều quan trọng hơn cả là việc xây dựng một cấu trúc lời nhắc (prompt) hợp lý và mô tả đầy đủ. Thực tế cho thấy, việc cung cấp các ví dụ minh họa ngay trong lời nhắc là một phương pháp rất hiệu quả nhằm đạt được đầu ra theo đúng định dạng mong muốn.

Khi thiết kế lời nhắc, bạn cũng cần lưu ý đến độ dài của lời nhắc vì có những giới hạn nhất định về chiều dài tối đa cho phép. Hãy cân nhắc mức độ cụ thể và chi tiết phù hợp: việc đưa vào quá nhiều thông tin không cần thiết không nhất thiết là một chiến lược tốt. Các chi tiết được đưa vào phải có tính liên quan và góp phần hỗ trợ trực tiếp cho nhiệm vụ đang thực hiện. Đây là một yếu tố đòi hỏi bạn phải thử nghiệm và điều chỉnh nhiều lần. Chúng tôi khuyến khích mạnh mẽ việc thử nghiệm liên tục và lặp đi lặp lại để tối ưu hóa lời nhắc sao cho phù hợp nhất với ứng dụng cụ thể của bạn.

Ví dụ, hãy thử một lời nhắc đơn giản nhằm trích xuất thông tin cụ thể từ một đoạn văn bản.

```
Extract the name of places in the following text. 

Desired format:
Place: <comma_separated_list_of_places>

Input: "Although these developments are encouraging to researchers, much is still a mystery. “We often have a black box between the brain and the effect we see in the periphery,” says Henrique Veiga-Fernandes, a neuroimmunologist at the Champalimaud Centre for the Unknown in Lisbon. “If we want to use it in the therapeutic context, we actually need to understand the mechanism.“"
```

Output

```
Place: Champalimaud Centre for the Unknown, Lisbon
```

## Avoid Impreciseness - Tránh sự thiếu chính xác

Với các mẹo nêu trên về việc trình bày chi tiết và cải thiện định dạng, người dùng dễ sa vào bẫy cố gắng quá “thông minh” khi xây dựng lời nhắc, từ đó vô tình tạo ra những mô tả thiếu chính xác. Thường thì cách tốt hơn là đưa ra yêu cầu cụ thể và trực tiếp. Ở đây, phép so sánh tương tự như trong giao tiếp hiệu quả: càng trực tiếp, thông điệp càng được truyền đạt một cách hiệu quả.

Ví dụ, bạn có thể quan tâm đến việc tìm hiểu khái niệm Prompt Engineering. Bạn có thể thử một câu hỏi như sau:

```
Explain the concept prompt engineering. Keep the explanation short, only a few sentences, and don't be too descriptive.
```

Rõ ràng là từ lời nhắc ở trên không thể xác định được số lượng câu cần sử dụng cũng như phong cách yêu cầu. Bạn vẫn có thể nhận được một số phản hồi khá tốt với các lời nhắc nêu trên, nhưng lời nhắc hiệu quả hơn sẽ là lời nhắc cụ thể, súc tích và đi thẳng vào trọng tâm. Ví dụ như:

```
Use 2-3 sentences to explain the concept of prompt engineering to a high school student.
```

## To do or not to do?

Một lời khuyên phổ biến khác khi thiết kế lời nhắc là tránh nêu những điều không nên làm, thay vào đó hãy nêu rõ những điều cần làm. Cách tiếp cận này khuyến khích tính cụ thể hơn và tập trung vào các chi tiết dẫn đến những phản hồi chất lượng cao từ mô hình.

Dưới đây là một ví dụ về một chatbot đề xuất phim gặp sự cố đúng vào điều mà tôi không mong muốn xảy ra, do cách tôi viết hướng dẫn — tức là tập trung vào những điều không nên làm.

```
The following is an agent that recommends movies to a customer. DO NOT ASK FOR INTERESTS. DO NOT ASK FOR PERSONAL INFORMATION.

Customer: Please recommend a movie based on my interests.
Agent: 
```

Output:

```
Sure, I can recommend a movie based on your interests. What kind of movie would you like to watch? Do you prefer action, comedy, romance, or something else?
```

Dưới đây là một lời nhắc tốt hơn:

```
The following is an agent that recommends movies to a customer. The agent is responsible to recommend a movie from the top global trending movies. It should refrain from asking users for their preferences and avoid asking for personal information. If the agent doesn't have a movie to recommend, it should respond "Sorry, couldn't find a movie to recommend today.".

Customer: Please recommend a movie based on my interests.
Agent:

```

Một số ví dụ nêu trên được lấy từ bài báo “Các thực hành tốt nhất về kỹ thuật prompt với API OpenAI”.

