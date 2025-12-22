# LLM Settings 

Nội dung được dịch từ: https://www.promptingguide.ai/introduction/settings

Khi thiết kế và kiểm thử các lời nhắc (prompt), bạn thường tương tác với mô hình ngôn ngữ lớn (LLM) thông qua một giao diện lập trình ứng dụng (API). Bạn có thể cấu hình một số tham số nhất định để thu được các kết quả khác nhau cho các lời nhắc của mình. Việc điều chỉnh các thiết lập này rất quan trọng nhằm cải thiện độ tin cậy và mức độ phù hợp của các phản hồi; đồng thời, việc xác định các giá trị thiết lập phù hợp cho từng trường hợp sử dụng cụ thể đòi hỏi một chút thực nghiệm. Dưới đây là các thiết lập phổ biến mà bạn sẽ gặp phải khi sử dụng các nhà cung cấp LLM khác nhau:

**Temperature** — Nói ngắn gọn, nhiệt độ càng thấp thì kết quả càng mang tính tất định hơn, theo nghĩa rằng ký hiệu (token) tiếp theo có xác suất cao nhất luôn được chọn. Việc tăng nhiệt độ có thể dẫn đến mức độ ngẫu nhiên cao hơn, từ đó khuyến khích đầu ra đa dạng hoặc sáng tạo hơn. Về bản chất, bạn đang gia tăng trọng số cho các ký hiệu khác có thể xuất hiện. Về mặt ứng dụng, bạn có thể muốn sử dụng giá trị nhiệt độ thấp hơn đối với các tác vụ như trả lời câu hỏi dựa trên sự kiện (fact-based QA) nhằm khuyến khích các phản hồi chính xác và súc tích hơn. Đối với việc sinh thơ hoặc các tác vụ sáng tạo khác, việc tăng giá trị nhiệt độ có thể mang lại lợi ích.

**Top P** – Một kỹ thuật lấy mẫu kết hợp với nhiệt độ, còn được gọi là lấy mẫu nhân (nucleus sampling), cho phép bạn kiểm soát mức độ xác định của mô hình. Nếu bạn đang tìm kiếm các câu trả lời chính xác và mang tính sự thật, hãy giữ giá trị này ở mức thấp. Ngược lại, nếu bạn muốn các phản hồi đa dạng hơn, hãy tăng giá trị này lên cao hơn. Khi sử dụng **Top P**, chỉ những token chiếm tổng xác suất bằng `top_p` mới được xem xét để sinh ra phản hồi; do đó, một giá trị top_p thấp sẽ chọn những phản hồi có độ tin cậy cao nhất. Điều này đồng nghĩa với việc một giá trị `top_p` cao sẽ cho phép mô hình xem xét nhiều từ khả thi hơn, bao gồm cả những từ ít có khả năng xuất hiện hơn, dẫn đến đầu ra đa dạng hơn.

> Khuyến nghị chung là điều chỉnh chỉ một trong hai tham số: nhiệt độ (temperature) hoặc Top P, chứ không nên điều chỉnh cả hai cùng lúc.

**Max Length** Bạn có thể kiểm soát số lượng token mà mô hình sinh ra bằng cách điều chỉnh tham số max length . Việc xác định độ dài tối đa giúp bạn tránh các phản hồi quá dài hoặc không liên quan, đồng thời kiểm soát chi phí.

**Stop Sequences** Một stop sequence là một chuỗi ký tự khiến mô hình ngừng sinh các token. Việc xác định các dãy ký tự dừng là một phương pháp khác để kiểm soát độ dài và cấu trúc phản hồi của mô hình. Ví dụ, bạn có thể yêu cầu mô hình sinh danh sách gồm tối đa 10 mục bằng cách thêm "11" làm dãy ký tự dừng.

**Frequency Penalty** Hệ số phạt tần suất – Tính năng `frequency penalty` áp dụng một hình phạt lên token tiếp theo tỷ lệ thuận với số lần token đó đã xuất hiện trong cả phản hồi và lời nhắc. Hệ số phạt tần suất càng cao, khả năng một từ xuất hiện lại càng thấp. Thiết lập này làm giảm sự lặp lại các từ trong phản hồi của mô hình bằng cách áp dụng hình phạt cao hơn đối với những token xuất hiện nhiều lần.

**Presence Penalty** Hệ số phạt hiện diện – Tính năng presence penalty cũng áp dụng hình phạt đối với các token bị lặp lại, tuy nhiên khác với hệ số phạt tần suất, mức hình phạt được áp dụng như nhau cho mọi token bị lặp, bất kể số lần lặp là bao nhiêu. Một token xuất hiện hai lần hay mười lần đều chịu cùng một mức hình phạt. Thiết lập này ngăn mô hình lặp lại quá nhiều các cụm từ trong phản hồi của nó. Nếu bạn mong muốn mô hình tạo ra văn bản đa dạng hoặc sáng tạo hơn, bạn có thể tăng hệ số phạt hiện diện; ngược lại, nếu cần mô hình tập trung hơn vào chủ đề, hãy thử giảm hệ số phạt hiện diện.

> Tương tự như `temperature` và `top_p` , khuyến nghị chung là chỉ điều chỉnh một trong hai thông số: `hệ số phạt tần suất` hoặc `hệ số phạt hiện diện`, chứ không nên điều chỉnh cả hai cùng lúc.

