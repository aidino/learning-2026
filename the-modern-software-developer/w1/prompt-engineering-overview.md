# Prompt engineering: overview and guide

Bài viết được dịch từ: https://cloud.google.com/discover/what-is-prompt-engineering

Sự nổi lên của các mô hình ngôn ngữ lớn (LLMs) đã mở ra những khả năng thú vị cho tương tác giữa con người và máy tính. Tuy nhiên, để khai thác tối đa tiềm năng của những mô hình AI mạnh mẽ này, một kỹ năng then chốt là cần thiết: **prompt engineering**. Lĩnh vực đang phát triển nhanh chóng này tập trung vào việc xây dựng các prompt hiệu quả nhằm khơi mở khả năng của các LLM, giúp chúng hiểu được ý định, tuân theo chỉ dẫn và tạo ra đầu ra như mong muốn. Khi mức độ tương tác của chúng ta với AI ngày càng gia tăng trong nhiều ứng dụng khác nhau, prompt engineering đóng vai trò thiết yếu trong việc đảm bảo các tương tác diễn ra chính xác, phù hợp và an toàn.

## What is prompt engineering?
Prompt engineering là nghệ thuật và khoa học thiết kế, tối ưu hóa các prompt nhằm hướng dẫn các mô hình trí tuệ nhân tạo, đặc biệt là các mô hình ngôn ngữ lớn (LLMs), sinh ra những phản hồi mong muốn. Bằng cách xây dựng cẩn thận các prompt, bạn cung cấp cho mô hình bối cảnh, hướng dẫn và ví dụ giúp mô hình hiểu được ý định của bạn và đưa ra phản hồi một cách có ý nghĩa. Hãy coi đây như việc cung cấp một bản đồ dẫn đường cho trí tuệ nhân tạo, định hướng nó tới đầu ra cụ thể mà bạn kỳ vọng.

## What is a prompt for AI?
Trong bối cảnh trí tuệ nhân tạo (AI), một prompt là đầu vào bạn cung cấp cho mô hình nhằm kích hoạt một phản hồi cụ thể. Prompt có thể xuất hiện dưới nhiều dạng khác nhau, từ những câu hỏi hoặc từ khóa đơn giản đến các chỉ dẫn phức tạp, đoạn mã lập trình hoặc thậm chí cả các mẫu văn bản sáng tạo. Tính hiệu quả của prompt trực tiếp ảnh hưởng đến chất lượng và mức độ phù hợp của đầu ra do AI tạo ra.

## What do you need for prompt engineering?
Một số yếu tố then chốt góp phần tạo nên việc Prompt Engineering hiệu quả. Việc làm chủ những yếu tố này cho phép bạn giao tiếp một cách hiệu quả với các mô hình AI và khai thác tối đa tiềm năng của chúng.

### Prompt format
Cấu trúc và phong cách của lời nhắc (prompt) của bạn đóng vai trò quan trọng trong việc định hướng phản hồi của mô hình AI. Các mô hình khác nhau có thể phản ứng tốt hơn với những định dạng cụ thể, chẳng hạn như:

Định dạng của lời nhắc (prompt) ảnh hưởng đáng kể đến cách mô hình AI diễn giải yêu cầu của bạn. Các mô hình khác nhau có thể phản ứng tốt hơn với các định dạng cụ thể, ví dụ như câu hỏi bằng ngôn ngữ tự nhiên, lệnh trực tiếp hoặc đầu vào có cấu trúc với các trường rõ ràng. Việc hiểu rõ năng lực và định dạng ưa thích của mô hình là yếu tố thiết yếu để xây dựng những lời nhắc hiệu quả.

### Context and examples

Việc cung cấp bối cảnh và các ví dụ liên quan trong lời nhắc giúp mô hình AI hiểu rõ hơn về nhiệm vụ mong muốn và tạo ra kết quả chính xác, phù hợp hơn. Chẳng hạn, nếu bạn đang yêu cầu một câu chuyện sáng tạo, việc đưa vào vài câu mô tả sắc thái hoặc chủ đề mong muốn có thể cải thiện đáng kể chất lượng đầu ra.

### Fine-tuning and adapting

Việc thực hiện fine-tuning mô hình AI trên các tác vụ hoặc lĩnh vực cụ thể bằng cách sử dụng các prompt được thiết kế riêng có thể nâng cao hiệu năng của mô hình. Ngoài ra, việc điều chỉnh các prompt dựa trên phản hồi từ người dùng hoặc đầu ra của mô hình cũng có thể tiếp tục cải thiện chất lượng phản hồi của mô hình theo thời gian.

### Multi-turn conversations

Thiết kế các prompt dành cho các Multi-turn conversations cho phép người dùng tương tác liên tục và có nhận thức về ngữ cảnh với mô hình AI, từ đó nâng cao trải nghiệm tổng thể của người dùng.


## Types of prompts
Có nhiều loại lời nhắc được sử dụng trong trí tuệ nhân tạo, mỗi loại phục vụ một mục đích cụ thể:

### Direct prompts (Zero-shot)
Lời nhắc không mẫu (zero-shot) là việc cung cấp cho mô hình một hướng dẫn hoặc câu hỏi trực tiếp mà không kèm theo bất kỳ ngữ cảnh hay ví dụ bổ sung nào.

Một ví dụ về trường hợp này là việc sinh ý tưởng, trong đó mô hình được yêu cầu tạo ra các ý tưởng sáng tạo hoặc các giải pháp tư duy phản biện. Một ví dụ khác là tóm tắt (Summarization) hoặc dịch thuật, trong đó mô hình được yêu cầu tóm tắt hoặc dịch một đoạn nội dung nào đó.

### One-, few- and multi-shot prompts

Phương pháp này bao gồm việc cung cấp cho mô hình một hoặc nhiều ví dụ về các cặp đầu vào–đầu ra mong muốn **trước khi đưa ra lời nhắc thực tế.** Điều này có thể giúp mô hình hiểu rõ hơn về nhiệm vụ và tạo ra các phản hồi chính xác hơn.

### Chain of Thought Prompts

Việc đặt câu hỏi theo phương pháp chuỗi suy luận (CoT) khuyến khích mô hình phân tích lập luận phức tạp thành một chuỗi các bước trung gian, từ đó dẫn đến đầu ra cuối cùng toàn diện và có cấu trúc rõ ràng hơn.

### Zero-shot CoT Prompts

Kết hợp phương pháp đặt câu hỏi theo chuỗi suy luận với phương pháp đặt câu hỏi không có ví dụ minh họa (zero-shot) bằng cách yêu cầu mô hình thực hiện các bước suy luận, điều này thường tạo ra đầu ra chất lượng cao hơn.

## Use cases and examples of prompt engineering

Dưới đây là một số ví dụ và trường hợp sử dụng cụ thể minh họa cách Prompt engineering giúp tạo ra đầu ra được cá nhân hóa và phù hợp.

### Language and Text Generation

| Scenario         | Instructions                                                                                                                                     | Example Prompt                                                                                                                                                                                                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Creative Writing | Tạo các lời nhắc xác định thể loại, giọng điệu, phong cách và các điểm cốt truyện để hướng dẫn mô hình AI tạo ra những câu chuyện hấp dẫn.       | "Write a short story about a young woman who discovers a magical portal in her attic."<br>“Hãy viết một truyện ngắn về một cô gái trẻ phát hiện ra một cánh cổng thần kỳ trong gác xép nhà mình.”                                                                                                     |
| Summarization    | Cung cấp cho AI văn bản và yêu cầu nó tạo ra các bản tóm tắt ngắn gọn, bao quát đầy đủ những thông tin trọng yếu.                                | “Summarize the main points of the following news article on climate change."<br>“Tóm tắt các điểm chính trong bài báo sau đây về biến đổi khí hậu.”                                                                                                                                                   |
| Translation      | Chỉ định rõ ngôn ngữ nguồn và ngôn ngữ đích để AI có thể dịch chính xác văn bản đồng thời bảo toàn trọn vẹn ý nghĩa và ngữ cảnh.                 | "Translate the following text from English to Spanish: 'The quick brown fox jumps over the lazy dog.'"                                                                                                                                                                                                |
| Dialogue         | Thiết kế các lời nhắc mô phỏng cuộc hội thoại, cho phép trí tuệ nhân tạo tạo ra phản hồi bắt chước tương tác giữa con người và duy trì ngữ cảnh. | "You are a friendly chatbot helping users troubleshoot their computer problems. Respond to the user's query: 'My computer won't turn on.'"<br>“Bạn là một chatbot thân thiện hỗ trợ người dùng khắc phục sự cố máy tính. Hãy trả lời truy vấn của người dùng: ‘Máy tính của tôi không bật lên được.’” |

### Question Answering

| Scenario                                                      | Instructions                                                                                                                                                                   | Example Prompt                                                                                                                                                                                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Open-Ended Questions<br>Các câu hỏi mở<br>                    | Xây dựng các lời nhắc nhằm khuyến khích mô hình AI cung cấp những câu trả lời toàn diện và giàu thông tin dựa trên cơ sở tri thức của nó.                                      | "Explain the concept of quantum computing and its potential impact on the future of technology."<br>“Giải thích khái niệm điện toán lượng tử và tác động tiềm năng của nó đối với tương lai của công nghệ.”                      |
| Specific Questions                                            | Thiết kế các lời nhắc hướng đến thông tin cụ thể, giúp mô hình AI truy xuất được những câu trả lời chính xác từ ngữ cảnh được cung cấp hoặc từ cơ sở tri thức nội tại của nó.  | "What is the capital of France?" or "According to the provided text, what are the main causes of deforestation?"<br>“Thủ đô của Pháp là gì?” hoặc “Theo đoạn văn được cung cấp, những nguyên nhân chính gây nạn phá rừng là gì?” |
| Multiple Choice Questions<br>                                 | Đưa ra các câu hỏi có nhiều lựa chọn, yêu cầu mô hình AI phân tích và chọn đáp án phù hợp nhất dựa trên sự hiểu biết của nó về ngữ cảnh.                                       | "Who wrote the Harry Potter series? A) J.R.R. Tolkien, B) J.K. Rowling, C) Stephen King"<br>“Ai là tác giả của loạt tiểu thuyết Harry Potter? A) J.R.R. Tolkien, B) J.K. Rowling, C) Stephen King”                               |
| Hypothetical Questions<br>Các câu hỏi giả định<br><br>        | Xây dựng các câu hỏi nhằm khám phá các tình huống giả định, cho phép mô hình AI suy luận, phỏng đoán và đưa ra các kết quả hoặc giải pháp khả thi.                             | "What would happen if humans could travel at the speed of light?"<br>Điều gì sẽ xảy ra nếu con người có thể di chuyển với tốc độ ánh sáng?                                                                                       |
| Opinion-Based Questions<br>Các câu hỏi dựa trên quan điểm<br> | Thiết kế các lời nhắc nhằm khơi gợi quan điểm hoặc ý kiến của mô hình AI về một chủ đề cụ thể, đồng thời khuyến khích mô hình đưa ra lập luận và cơ sở để bảo vệ quan điểm đó. | "Do you believe that artificial intelligence will eventually surpass human intelligence? Why or why not?"<br>“Bạn có tin rằng trí tuệ nhân tạo cuối cùng sẽ vượt qua trí tuệ con người hay không? Vì sao có hoặc vì sao không?”  |

### Code Generation

| Scenario          | Instructions                                                                                                                                         | Example Prompt                                                                                                                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Code Completion   | Cung cấp cho mô hình AI một đoạn mã chưa hoàn chỉnh và yêu cầu nó đề xuất hoặc hoàn thành phần mã còn thiếu dựa trên ngữ cảnh và ngôn ngữ lập trình. | "Write a Python function to calculate the factorial of a given number."<br>“Viết một hàm Python để tính giai thừa của một số đã cho.”                                                       |
| Code Translation  | Chỉ định ngôn ngữ lập trình nguồn và ngôn ngữ lập trình đích để AI có thể dịch mã trong khi vẫn bảo toàn chức năng và cú pháp.                       | "Translate the following Python code to JavaScript: def greet(name): print('Hello,', name)"<br>“Dịch đoạn mã Python sau đây sang JavaScript: def greet(name): print('Hello,', name)”        |
| Code Optimization | Yêu cầu mô hình AI phân tích đoạn mã hiện có và đề xuất các cải tiến nhằm nâng cao hiệu quả, khả năng đọc hiểu hoặc hiệu năng.                       | "Optimize the following Python code to reduce its execution time."<br>“Tối ưu hóa đoạn mã Python sau đây để giảm thời gian thực thi.”                                                       |
| Code Debugging    | Cung cấp cho AI đoạn mã chứa lỗi và yêu cầu nó xác định các lỗi đó cũng như đề xuất các giải pháp tiềm năng cho những vấn đề đã phát hiện.           | "Debug the following Java code and explain why it is throwing a NullPointerException."<br>“Gỡ lỗi đoạn mã Java sau đây và giải thích lý do vì sao nó ném ra ngoại lệ NullPointerException.” |

### Image Generation
| Scenario                                            | Instructions                                                                                                                                                                                        | Example Prompt                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Photorealistic Images<br>Hình ảnh siêu thực<br><br> | Tạo các lời nhắc mô tả chi tiết hình ảnh mong muốn, bao gồm các đối tượng, khung cảnh, ánh sáng và phong cách, nhằm tạo ra những hình ảnh chân thực và chất lượng cao.                              | "A photorealistic image of a sunset over the ocean with palm trees silhouetted against the sky."<br>“Một hình ảnh siêu thực về cảnh hoàng hôn trên biển, với những cây cọ in bóng mờ trên nền bầu trời.”                                                                                                           |
| Artistic Images<br>Hình ảnh nghệ thuật<br>          | Thiết kế các lời nhắc nêu rõ phong cách nghệ thuật, kỹ thuật và chủ đề để hướng dẫn mô hình AI tạo ra những hình ảnh bắt chước các trào lưu nghệ thuật cụ thể hoặc gợi lên những cảm xúc nhất định. | "An impressionist painting of a bustling city street with people walking under umbrellas in the rain."<br>Một bức tranh theo trường phái Ấn tượng về một con phố thành thị nhộn nhịp, nơi những người đi bộ đang bước đi dưới những chiếc ô giữa cơn mưa.                                                          |
| Abstract Images<br>Hình ảnh trừu tượng<br><br>      | Xây dựng các lời nhắc khuyến khích mô hình AI tạo ra những hình ảnh mang tính gợi mở, sử dụng các yếu tố hình khối, màu sắc và kết cấu để khơi gợi cảm xúc hoặc biểu đạt các khái niệm.             | "An abstract image representing the concept of hope, using bright colors and flowing shapes."<br>“Một hình ảnh trừu tượng thể hiện khái niệm ‘hy vọng’, sử dụng màu sắc rực rỡ và các đường nét uốn lượn.”                                                                                                         |
| Image Editing<br>Chỉnh sửa ảnh<br><br>              | Cung cấp cho AI một hình ảnh hiện có và chỉ định các thay đổi mong muốn, từ đó cho phép mô hình chỉnh sửa và cải thiện hình ảnh theo đúng hướng dẫn đã nêu.                                         | "Change the background of this photo to a starry night sky and add a full moon." or "Remove the person from this image and replace them with a cat."<br>“Thay đổi nền của bức ảnh này thành bầu trời đêm đầy sao và thêm một vầng trăng tròn.” hoặc “Xóa người trong hình này đi và thay thế họ bằng một con mèo.” |

## Strategies for writing better prompts
Việc phát triển các prompt hiệu quả đòi hỏi một cách tiếp cận mang tính chiến lược. Hãy xem xét những chiến lược sau đây nhằm nâng cao kỹ năng Prompt engineering của bạn:

### 1. Set Clear Goals and Objectives:

| Chiến lược (Tactic)                                                      | Prompt Example                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sử dụng các động từ hành động để xác định rõ hành động mong muốn<br><br> | "Write a bulleted list that summarizes the key findings of the attached research paper"<br>“Hãy viết một danh sách các điểm chính dưới dạng gạch đầu dòng, tóm tắt những phát hiện quan trọng của bài báo nghiên cứu đính kèm.”                                     |
| Xác định độ dài và định dạng mong muốn của đầu ra<br><br>                | "Compose a 500-word essay discussing the impact of climate change on coastal communities."<br>“Hãy viết một bài luận dài 500 từ bàn luận về tác động của biến đổi khí hậu đối với các cộng đồng ven biển.”                                                          |
| Xác định đối tượng mục tiêu<br><br>                                      | "Write a product description for a new line of organic skincare products, targeting young adults concerned with sustainability."<br>Hãy viết một mô tả sản phẩm cho dòng mỹ phẩm chăm sóc da hữu cơ mới, hướng đến đối tượng thanh niên quan tâm đến tính bền vững. |

### 2. Provide Context and Background Information:

| Chiến lược (Tactic)                                     | Prompt Example                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bao gồm các sự kiện và dữ liệu liên quan<br><br>        | "Given that global temperatures have risen by 1 degree Celsius since the pre-industrial era, discuss the potential consequences for sea level rise."<br>“Với việc nhiệt độ toàn cầu đã tăng 1 độ C kể từ thời kỳ tiền công nghiệp, hãy thảo luận về những hậu quả tiềm tàng đối với mức nước biển dâng.” |
| Tham khảo các nguồn hoặc tài liệu cụ thể<br><br>        | "Based on the attached financial report, analyze the company's profitability over the past five years."<br>Dựa trên báo cáo tài chính đính kèm, hãy phân tích khả năng sinh lời của công ty trong năm năm qua.                                                                                           |
| Định nghĩa các thuật ngữ và khái niệm then chốt<br><br> | "Explain the concept of quantum computing in simple terms, suitable for a non-technical audience."<br>Hãy giải thích khái niệm điện toán lượng tử bằng những thuật ngữ đơn giản, phù hợp với đối tượng độc giả không có chuyên môn kỹ thuật.                                                             |

### 3. Use Few-Shot Prompting:

| Chiến lược (Tactic)                                                | Prompt Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cung cấp một vài ví dụ về các cặp đầu vào–đầu ra mong muốn<br><br> | Input: "Cat" Output: "A small furry mammal with whiskers." Input: "Dog" Output: "A domesticated canine known for its loyalty." Prompt: "Elephant"<br>Đầu vào: "Mèo" Đầu ra: "Một loài động vật có vú nhỏ, lông xù và có râu." Đầu vào: "Chó" Đầu ra: "Loài chó được thuần hóa, nổi tiếng vì sự trung thành." Yêu cầu: "Voi"                                                                                                                                                                                                                                                                                                                                                                                             |
| Minh họa phong cách hoặc giọng điệu mong muốn<br><br>              | Example 1 (humorous): "The politician's speech was so dull, it could cure insomnia." Example 2 (formal): "The dignitary delivered an address that was both informative and engaging." Prompt: "Write a sentence describing the comedian's stand-up routine."<br>Ví dụ 1 (giọng hài hước): "Bài phát biểu của chính trị gia nhàm chán đến mức có thể chữa được chứng mất ngủ." Ví dụ 2 (giọng trang trọng): "Nhân vật quý tộc đã trình bày một bài phát biểu vừa mang tính thông tin vừa thu hút người nghe." Yêu cầu: "Viết một câu mô tả tiết mục biểu diễn hài đứng của nghệ sĩ hài."                                                                                                                                 |
| Hiển thị mức độ chi tiết mong muốn<br><br>                         | Example 1 (brief): "The movie was about a young boy who befriends an alien." Example 2 (detailed): "The science fiction film follows the story of Elliot, a lonely boy who discovers and forms a unique bond with an extraterrestrial stranded on Earth." Prompt: "Summarize the plot of the novel you just finished reading."<br>Ví dụ 1 (ngắn gọn): “Bộ phim kể về một cậu bé trẻ tuổi kết bạn với một sinh vật ngoài hành tinh.” Ví dụ 2 (chi tiết): “Bộ phim khoa học viễn tưởng kể về hành trình của Elliot, một cậu bé cô đơn phát hiện ra và thiết lập mối liên kết đặc biệt với một sinh vật ngoài hành tinh bị mắc kẹt trên Trái Đất.” Yêu cầu: “Tóm tắt cốt truyện của cuốn tiểu thuyết mà bạn vừa đọc xong.” |

### 4. Be Specific:

| Chiến lược (Tactic)                                              | Prompt Example                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sử dụng ngôn ngữ chính xác và tránh tính mơ hồ<br><br>           | Instead of: "Write something about climate change," use: "Write a persuasive essay arguing for the implementation of stricter carbon emission regulations."<br>Thay vì: “Hãy viết một điều gì đó về biến đổi khí hậu”, hãy dùng: “Hãy viết một bài luận thuyết phục lập luận ủng hộ việc áp dụng các quy định nghiêm ngặt hơn đối với lượng khí thải carbon.” |
| Định lượng yêu cầu của bạn bất cứ khi nào có thể<br><br>         | Instead of: "Write a long poem," use: "Write a sonnet with 14 lines that explores themes of love and loss."<br>Thay vì: “Hãy viết một bài thơ dài”, hãy dùng: “Hãy viết một bài thơ sonnet gồm 14 câu, khai thác chủ đề tình yêu và nỗi mất mát.”                                                                                                             |
| Phân chia các nhiệm vụ phức tạp thành những bước nhỏ hơn<br><br> | Instead of: "Create a marketing plan," use: "1. Identify the target audience. 2. Develop key marketing messages. 3. Choose appropriate marketing channels."<br>Thay vì: “Tạo một kế hoạch tiếp thị”, hãy sử dụng: “1. Xác định đối tượng mục tiêu. 2. Phát triển các thông điệp tiếp thị chủ chốt. 3. Lựa chọn các kênh tiếp thị phù hợp.”                    |

### 5. Iterate and Experiment:

| Chiến lược (Tactic)                                  | Prompt Example                                                                                                                                          |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Thử các cách diễn đạt và từ khóa khác nhau<br><br>   | Rephrase your prompt using synonyms or alternative sentence structures.<br>Viết lại lời nhắc của bạn bằng các từ đồng nghĩa hoặc cấu trúc câu thay thế. |
| Điều chỉnh mức độ chi tiết và tính cụ thể<br><br>    | Add or remove information to fine-tune the output.<br>Thêm hoặc loại bỏ thông tin để điều chỉnh đầu ra một cách tinh vi.                                |
| Thử nghiệm với các độ dài lời nhắc khác nhau<br><br> | Experiment with both shorter and longer prompts to find the optimal balance.<br>Thử nghiệm cả lời nhắc ngắn và dài để tìm ra sự cân bằng tối ưu.        |

### 6. Leverage Chain of Thought Prompting:

| Chiến lược (Tactic)                                       | Prompt Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Khuyến khích suy luận từng bước<br><br>                   | "Solve this problem step-by-step: John has 5 apples, he eats 2. How many apples does he have left? Step 1: John starts with 5 apples. Step 2: He eats 2 apples, so we need to subtract 2 from 5. Step 3: 5 - 2 = 3. Answer: John has 3 apples left."<br>“Hãy giải bài toán này theo từng bước: John có 5 quả táo, anh ấy ăn mất 2 quả. Hỏi John còn lại bao nhiêu quả táo? Bước 1: John xuất phát với 5 quả táo. Bước 2: Anh ấy ăn mất 2 quả táo, do đó ta cần trừ 2 từ 5. Bước 3: 5 – 2 = 3. Đáp án: John còn lại 3 quả táo.” |
| Yêu cầu mô hình giải thích quá trình lập luận của nó<br>  | "Explain your thought process in determining the sentiment of this movie review: 'The acting was superb, but the plot was predictable.'"<br>“Hãy giải thích quy trình tư duy của bạn khi xác định sắc thái cảm xúc trong nhận xét phim sau: ‘Diễn xuất tuyệt vời, nhưng cốt truyện lại dễ đoán.’”                                                                                                                                                                                                                              |
| Hướng dẫn mô hình thực hiện một chuỗi lập luận hợp lý<br> | "To classify this email as spam or not spam, consider the following: 1. Is the sender known? 2. Does the subject line contain suspicious keywords? 3. Is the email offering something too good to be true?"<br>“Để phân loại email này là thư rác hay không phải thư rác, hãy xem xét các yếu tố sau: 1. Người gửi có được biết đến hay không? 2. Tiêu đề email có chứa các từ khóa khả nghi hay không? 3. Email có đang đề nghị một điều gì đó quá tốt để có thể tin được hay không?”   

Để biết thêm hướng dẫn về các thực hành tốt nhất trong Prompt Engineering, hãy tham khảo [Năm Thực hành Tốt nhất cho Prompt Engineering](https://cloud.google.com/blog/products/application-development/five-best-practices-for-prompt-engineering) trên Google Cloud.

## Benefits of prompt engineering

Prompt Engineering hiệu quả mang lại nhiều lợi ích, nâng cao khả năng và tính khả dụng của các mô hình AI:

- Cải thiện hiệu suất mô hình

Các prompt được xây dựng kỹ lưỡng giúp các mô hình AI tạo ra đầu ra chính xác hơn, liên quan hơn và giàu thông tin hơn, nhờ việc cung cấp hướng dẫn rõ ràng và bối cảnh phù hợp.

- Giảm thiểu thiên kiến và các phản hồi gây hại

Bằng cách kiểm soát cẩn thận đầu vào và định hướng trọng tâm của mô hình AI, kỹ thuật xây dựng lời nhắc (prompt engineering) giúp giảm thiểu thiên kiến và hạn chế rủi ro phát sinh nội dung không phù hợp hoặc gây tổn thương.

- Tăng cường khả năng kiểm soát và tính dự báo

Kỹ thuật xây dựng lời nhắc (prompt engineering) trao cho bạn quyền ảnh hưởng đến hành vi của mô hình AI, từ đó đảm bảo các phản hồi nhất quán và có thể dự báo được, phù hợp với các kết quả mong muốn của bạn.

- Trải nghiệm người dùng được cải thiện

Các lời nhắc rõ ràng và súc tích giúp người dùng tương tác hiệu quả hơn với các mô hình AI, từ đó mang lại trải nghiệm trực quan và hài lòng hơn.

