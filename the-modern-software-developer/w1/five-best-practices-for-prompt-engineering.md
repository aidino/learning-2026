# Tips to enhance your prompt-engineering abilities

Bài viết được dịch từ: https://cloud.google.com/blog/products/application-development/five-best-practices-for-prompt-engineering

Khi các công cụ được trang bị trí tuệ nhân tạo ngày càng phổ biến, prompt engineering đang trở thành một kỹ năng mà các nhà phát triển cần làm chủ. Các mô hình ngôn ngữ lớn (LLMs) và các mô hình nền sinh tổng hợp khác đòi hỏi các chỉ thị bằng ngôn ngữ tự nhiên mang tính bối cảnh, cụ thể và được cá thể hóa để tạo ra kết quả mong muốn. Điều này đồng nghĩa với việc các nhà phát triển cần soạn các prompt rõ ràng, súc tích và giàu thông tin.

Trong bài viết này, chúng ta sẽ khám phá các thực hành tốt nhất giúp bạn trở thành một chuyên gia prompt engineering hiệu quả hơn. Bằng cách áp dụng các lời khuyên của chúng tôi, bạn có thể bắt đầu xây dựng các ứng dụng mang tính cá nhân hóa cao hơn, chính xác hơn và nhạy bén hơn về mặt bối cảnh. Vậy hãy cùng bắt đầu ngay thôi!

## Tip #1: Know the model’s strengths and weaknesses - Hiểu rõ điểm mạnh và điểm yếu của mô hình

Khi các mô hình AI không ngừhttps://cloud.google.com/blog/products/application-development/five-best-practices-for-prompt-engineeringng phát triển và trở nên phức tạp hơn, điều thiết yếu đối với các nhà phát triển là phải nắm vững cả khả năng lẫn giới hạn của chúng. Việc hiểu rõ những điểm mạnh và điểm yếu này sẽ giúp bạn—nhà phát triển—tránh mắc phải sai lầm và xây dựng các ứng dụng an toàn, đáng tin cậy hơn.

Ví dụ, một mô hình trí tuệ nhân tạo được huấn luyện để nhận diện ảnh việt quất có thể không nhận diện được ảnh dâu tây. Tại sao vậy? Bởi vì mô hình này chỉ được huấn luyện trên tập dữ liệu gồm các ảnh việt quất. Nếu một nhà phát triển sử dụng mô hình này để xây dựng ứng dụng nhằm nhận diện cả việt quất lẫn dâu tây, ứng dụng đó rất có thể đưa ra những dự đoán sai lệch, dẫn đến kết quả kém hiệu quả và trải nghiệm người dùng không tốt.

Điều quan trọng cần lưu ý là các mô hình AI có khả năng mang tính thiên lệch. Nguyên nhân là do các mô hình AI được huấn luyện trên dữ liệu được thu thập từ thế giới thực, do đó có thể phản ánh những bất cân bằng về quyền lực vốn đã ăn sâu trong cấu trúc phân tầng xã hội của chúng ta. Nếu dữ liệu dùng để huấn luyện một mô hình AI mang tính thiên lệch, thì chính mô hình đó cũng sẽ bị thiên lệch. Điều này có thể dẫn đến những vấn đề nghiêm trọng nếu mô hình được sử dụng để đưa ra các quyết định ảnh hưởng đến con người, chẳng hạn như củng cố thêm các định kiến xã hội. Việc giải quyết các thiên lệch này là rất quan trọng nhằm đảm bảo tính công bằng của dữ liệu, thúc đẩy bình đẳng và khẳng định trách nhiệm đối với công nghệ AI. Các kỹ sư viết lời nhắc (prompt engineers) cần nhận thức rõ về những hạn chế hoặc thiên lệch trong quá trình huấn luyện mô hình để có thể xây dựng lời nhắc một cách hiệu quả hơn, đồng thời hiểu được loại lời nhắc nào là khả thi đối với một mô hình cụ thể.

## Tip #2: Be as specific as possible - Hãy càng cụ thể càng tốt

Các mô hình AI có khả năng hiểu nhiều loại lời nhắc khác nhau. Chẳng hạn, PaLM 2 của Google có thể hiểu các lời nhắc bằng ngôn ngữ tự nhiên, văn bản đa ngôn ngữ và thậm chí cả mã lập trình như Python và JavaScript. Mặc dù các mô hình AI có thể rất am hiểu, chúng vẫn chưa hoàn hảo và có thể diễn giải sai các lời nhắc không đủ cụ thể. Để giúp các mô hình AI xử lý được tính mơ hồ, điều quan trọng là phải thiết kế lời nhắc một cách chính xác nhằm đạt được kết quả mong muốn.

Giả sử bạn muốn mô hình AI của mình tạo ra công thức làm 50 chiếc bánh nướng xanh (blueberry muffin) thuần chay. Nếu bạn đưa vào lời nhắc: “Công thức làm bánh nướng xanh là gì?”, mô hình sẽ không biết rằng bạn cần làm tới 50 chiếc. Do đó, khả năng cao là mô hình sẽ không liệt kê khối lượng nguyên liệu lớn hơn cần thiết hoặc không bao gồm các mẹo giúp bạn nướng số lượng lớn bánh này một cách hiệu quả hơn. Mô hình chỉ có thể dựa vào ngữ cảnh được cung cấp. Một lời nhắc hiệu quả hơn sẽ là: “Tôi đang tổ chức tiệc cho 50 khách mời. Hãy tạo một công thức làm 50 chiếc bánh nướng xanh.” Khi đó, mô hình có khả năng cao hơn sẽ đưa ra phản hồi phù hợp với yêu cầu của bạn và đáp ứng đúng các yêu cầu cụ thể.

## Tip #3: Utilize contextual prompts - Sử dụng lời nhắc có tính ngữ cảnh

Sử dụng thông tin ngữ cảnh trong các yêu cầu đầu vào (prompt) của bạn để giúp mô hình hiểu sâu hơn về nhu cầu của bạn. Các yêu cầu có tính ngữ cảnh có thể bao gồm nhiệm vụ cụ thể mà bạn muốn mô hình thực hiện, bản sao mẫu của đầu ra mà bạn kỳ vọng, hoặc một nhân cách (persona) cần mô phỏng—từ chuyên gia tiếp thị, kỹ sư cho đến giáo viên trung học phổ thông. Việc xác định rõ giọng điệu và góc nhìn cho mô hình AI sẽ cung cấp cho nó một “bản thiết kế” về giọng điệu, phong cách và chuyên môn tập trung mà bạn mong muốn, từ đó nâng cao chất lượng, mức độ phù hợp và hiệu quả của đầu ra.

Trong trường hợp bánh muffin việt quất, điều quan trọng là phải xây dựng yêu cầu đầu vào dựa trên bối cảnh cụ thể của tình huống. Mô hình có thể cần nhiều thông tin ngữ cảnh hơn là chỉ đơn thuần tạo một công thức nấu ăn cho 50 người. Nếu công thức phải đáp ứng tiêu chí thuần chay, bạn có thể yêu cầu mô hình trả lời bằng cách nhập vai một đầu bếp thuần chay giàu kinh nghiệm.

Bằng cách cung cấp các yêu cầu đầu vào có tính ngữ cảnh, bạn có thể đảm bảo các tương tác với AI diễn ra một cách liền mạch và hiệu quả nhất có thể. Mô hình sẽ nhanh chóng nắm bắt được yêu cầu của bạn và từ đó tạo ra các phản hồi chính xác và sát với ngữ cảnh hơn.

## Tip #4: Provide AI models with examples 

Khi tạo lời nhắc (prompt) cho các mô hình AI, việc cung cấp ví dụ là rất hữu ích. Điều này là do lời nhắc đóng vai trò như những chỉ dẫn dành cho mô hình, và các ví dụ có thể giúp mô hình hiểu rõ hơn yêu cầu của bạn. Một lời nhắc kèm theo ví dụ thường có dạng như sau: “Dưới đây là một số công thức nấu ăn mà tôi thích — hãy tạo một công thức mới dựa trên những công thức tôi đã cung cấp.” Lúc này, mô hình có thể hiểu được khả năng và nhu cầu của bạn để chế biến món bánh này.

## Tip #5: Experiment with prompts and personas - Thử nghiệm với các lời nhắc và nhân cách

Cách bạn xây dựng lời nhắc (prompt) ảnh hưởng trực tiếp đến đầu ra của mô hình. Bằng việc sáng tạo khám phá các yêu cầu khác nhau, bạn sẽ nhanh chóng hiểu được cách mô hình cân nhắc các câu trả lời của mình, cũng như điều gì xảy ra khi bạn tích hợp kiến thức chuyên ngành (Domain Knowledge), chuyên môn và kinh nghiệm thực tiễn của bản thân vào sức mạnh của một mô hình ngôn ngữ lớn (large language model) có hàng tỷ tham số.

Hãy thử nghiệm với các từ khóa khác nhau, cấu trúc câu đa dạng và độ dài lời nhắc biến đổi để tìm ra “công thức hoàn hảo”. Đừng ngần ngại hóa thân vào nhiều vai trò khác nhau: từ các vai trong công việc như “kỹ sư sản phẩm” hay “nhân viên chăm sóc khách hàng”, đến những vai trong đời sống như người bà, một đầu bếp nổi tiếng—và khám phá mọi chủ đề, từ nấu ăn cho đến lập trình!

Bằng cách xây dựng những yêu cầu độc đáo và sáng tạo, giàu hàm chứa chuyên môn và kinh nghiệm cá nhân, bạn có thể xác định được lời nhắc nào mang lại đầu ra lý tưởng nhất cho mình. Việc tiếp tục tinh chỉnh lời nhắc—một quá trình được gọi là “hiệu chỉnh” (tuning)—sẽ giúp mô hình hiểu sâu hơn và xây dựng được khuôn khổ rõ ràng hơn cho đầu ra tiếp theo của bạn.

## Tip #6: Try chain-of-thought prompting - Thử kỹ thuật gợi ý theo chuỗi lập luận

Prompting chuỗi lập luận là một kỹ thuật nhằm cải thiện khả năng suy luận của các mô hình ngôn ngữ lớn (LLM). Kỹ thuật này hoạt động bằng cách chia nhỏ một vấn đề phức tạp thành các bước nhỏ hơn, sau đó yêu cầu LLM cung cấp lập luận trung gian cho từng bước. Điều này giúp LLM hiểu sâu hơn về vấn đề và tạo ra các câu trả lời chính xác, giàu thông tin hơn. Nhờ đó, bạn sẽ dễ dàng hiểu rõ hơn câu trả lời và đảm bảo rằng LLM thực sự đang nắm bắt được bản chất của vấn đề.

## Conclusion

Prompt engineering là một kỹ năng mà mọi lao động, ở mọi ngành nghề và tổ chức, đều cần có khi các công cụ tích hợp trí tuệ nhân tạo ngày càng phổ biến. Hãy nhớ áp dụng năm mẹo thiết yếu này trong lần tới bạn tương tác với một mô hình AI, để từ đó tạo ra các đầu ra chính xác như mong muốn. Trí tuệ nhân tạo sẽ không ngừng phát triển và tự hoàn thiện liên tục trong quá trình chúng ta sử dụng nó; do đó, tôi khuyến khích bạn luôn ghi nhớ rằng hành trình học tập—cả đối với con người lẫn máy móc—là một hành trình vô tận. Chúc bạn thực hành Prompt Engineering thật vui vẻ!