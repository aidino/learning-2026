# Introduction to AI Agents

Reference: https://www.promptingguide.ai/agents/introduction

Agent đang cách mạng hóa cách chúng ta tiếp cận các tác vụ phức tạp, khai thác sức mạnh của các mô hình ngôn ngữ lớn (LLMs) để làm việc thay mặt chúng ta và đạt được những kết quả ấn tượng. Trong hướng dẫn này, chúng ta sẽ đi sâu vào những nền tảng cơ bản của agent AI, khám phá các khả năng, các mẫu thiết kế và các ứng dụng tiềm năng của chúng.

## What is an Agent?

![](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fagent-components.6066d990.png&w=1080&q=75)

Trong hướng dẫn này, chúng ta định nghĩa agent là một hệ thống được điều khiển bởi LLM, được thiết kế nhằm thực hiện các hành động và giải quyết tự chủ các tác vụ phức tạp. Khác với các LLM truyền thống, agent AI không chỉ dừng lại ở việc sinh văn bản đơn thuần. Chúng được trang bị thêm nhiều khả năng khác, bao gồm:

- Lập kế hoạch và phản tư: Các tác nhân AI có thể phân tích một vấn đề, chia nhỏ nó thành các bước cụ thể và điều chỉnh cách tiếp cận dựa trên thông tin mới.
- Truy cập công cụ: Chúng có thể tương tác với các công cụ và nguồn tài nguyên bên ngoài, chẳng hạn như cơ sở dữ liệu, API và các ứng dụng phần mềm, nhằm thu thập thông tin và thực hiện các hành động.
- Bộ nhớ: Các tác nhân AI có khả năng lưu trữ và truy xuất thông tin, cho phép chúng học hỏi từ những kinh nghiệm trước đây và đưa ra các quyết định sáng suốt hơn.

## Why build with Agents?

Mặc dù các mô hình ngôn ngữ lớn (LLMs) nổi trội trong việc thực hiện những tác vụ đơn giản, chuyên biệt như dịch thuật hay soạn thảo email, chúng lại gặp hạn chế khi xử lý các tác vụ phức tạp và đa chiều đòi hỏi nhiều bước thực hiện, khả năng lập kế hoạch và suy luận. Những tác vụ phức tạp này thường yêu cầu truy cập vào các công cụ và thông tin bên ngoài phạm vi cơ sở tri thức của LLM.

Ví dụ, việc xây dựng một chiến lược tiếp thị có thể bao gồm việc nghiên cứu đối thủ cạnh tranh, phân tích xu hướng thị trường và truy cập dữ liệu đặc thù của doanh nghiệp. Các hành động này đòi hỏi thông tin từ thực tiễn, những hiểu biết mới nhất cũng như dữ liệu nội bộ của công ty—những nguồn thông tin mà một LLM hoạt động độc lập có thể không tiếp cận được.

Các tác tử AI đóng vai trò cầu nối để khắc phục khoảng cách này bằng cách kết hợp năng lực của LLM với các tính năng bổ sung như bộ nhớ, khả năng lập kế hoạch và khả năng tương tác với các công cụ bên ngoài.

Bằng cách khai thác những khả năng này, các tác nhân AI có thể giải quyết hiệu quả các nhiệm vụ phức tạp như:

- Xây dựng chiến lược tiếp thị
- Lên kế hoạch tổ chức sự kiện
- Cung cấp hỗ trợ khách hàng
- ...

## Common Use Cases for AI Agents

Dưới đây là danh sách không đầy đủ các trường hợp sử dụng phổ biến mà các tác nhân AI đang được áp dụng trong thực tiễn công nghiệp:

- Hệ thống đề xuất: Cá nhân hóa các đề xuất về sản phẩm, dịch vụ hoặc nội dung.
- Hệ thống hỗ trợ khách hàng: Xử lý các yêu cầu, giải quyết vấn đề và cung cấp hỗ trợ.
- Nghiên cứu: Thực hiện các khảo sát chuyên sâu trên nhiều lĩnh vực khác nhau, chẳng hạn như pháp lý, tài chính và y tế.
- Ứng dụng thương mại điện tử: Hỗ trợ trải nghiệm mua sắm trực tuyến, quản lý đơn hàng và cung cấp các đề xuất cá nhân hóa.
- Đặt chỗ: Hỗ trợ sắp xếp chuyến đi và lập kế hoạch sự kiện.
- Báo cáo: Phân tích khối lượng dữ liệu khổng lồ và tạo ra các báo cáo toàn diện.
- Phân tích tài chính: Phân tích xu hướng thị trường, đánh giá dữ liệu tài chính và lập báo cáo với tốc độ và độ chính xác chưa từng có.
