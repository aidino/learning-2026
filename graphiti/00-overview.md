# Overview

## What is a Knowledge Graph?

**Graphiti** giúp bạn **tạo** và **truy vấn** các Knowledge Graphs có khả năng tiến hóa theo thời gian. Knowledge Graphs là một mạng lưới gồm các sự kiện liên kết với nhau, ví dụ như “Kendra yêu giày Adidas.” Mỗi sự kiện được biểu diễn dưới dạng một “bộ ba” gồm hai thực thể (hoặc nút): “Kendra” và “giày Adidas”, cùng mối quan hệ giữa chúng (hoặc cạnh): “yêu”.

Knowledge Graphs đã được nghiên cứu rộng rãi trong lĩnh vực tìm kiếm thông tin. Điều làm nên tính độc đáo của Graphiti là khả năng tự động xây dựng Knowledge Graphs đồng thời xử lý các mối quan hệ thay đổi và duy trì bối cảnh lịch sử.

![](https://files.buildwithfern.com/zep.docs.buildwithfern.com/2025-12-18T18:07:13.390Z/images/graphiti-graph-intro.gif)

Graphiti xây dựng các đồ thị tri thức động, có nhận thức về thời gian, nhằm biểu diễn các mối quan hệ phức tạp và không ngừng thay đổi giữa các thực thể theo thời gian. Hệ thống này tiếp nhận cả dữ liệu phi cấu trúc lẫn dữ liệu có cấu trúc, và đồ thị kết quả có thể được truy vấn bằng cách kết hợp các phương pháp dựa trên thời gian, tìm kiếm toàn văn, tìm kiếm ngữ nghĩa và các thuật toán đồ thị.

Với Graphiti, bạn có thể xây dựng các ứng dụng LLM như:
- Các trợ lý học hỏi từ các tương tác của người dùng, tích hợp kiến thức cá nhân với dữ liệu động từ các hệ thống doanh nghiệp như hệ thống quản lý quan hệ khách hàng (CRM) và nền tảng thanh toán.
- Các tác tử tự chủ thực hiện các tác vụ phức tạp, suy luận dựa trên những thay đổi trạng thái đến từ nhiều nguồn động khác nhau.

Graphiti hỗ trợ một loạt ứng dụng đa dạng trong các lĩnh vực như bán hàng, dịch vụ khách hàng, y tế, tài chính và nhiều lĩnh vực khác, cho phép khả năng ghi nhớ dài hạn và suy luận dựa trên trạng thái đối với cả các trợ lý và tác nhân.

## Graphiti and Zep

Graphiti là nền tảng cốt lõi tạo nên lớp ngữ cảnh (context layer) của Zep dành cho các trợ lý và tác nhân được vận hành bởi LLM.

Chúng tôi rất hào hứng khi công bố mã nguồn mở Graphiti, bởi chúng tôi tin rằng tiềm năng của nó vượt xa những ứng dụng liên quan đến ngữ cảnh.

## Why Graphiti? 

Chúng tôi rất hứng thú với GraphRAG của Microsoft, một công cụ mở rộng phương pháp chia nhỏ văn bản trong kỹ thuật RAG bằng cách sử dụng đồ thị để mô hình hóa tốt hơn tập hợp tài liệu và cung cấp biểu diễn này thông qua các kỹ thuật tìm kiếm ngữ nghĩa và tìm kiếm trên đồ thị. Tuy nhiên, GraphRAG chưa giải quyết được vấn đề cốt lõi của chúng tôi: công cụ này chủ yếu được thiết kế cho các tài liệu tĩnh và không xử lý vốn có các khía cạnh thời gian của dữ liệu.

Graphiti được thiết kế từ đầu nhằm xử lý hiệu quả thông tin liên tục thay đổi, tìm kiếm hỗn hợp dựa trên ngữ nghĩa và đồ thị, cũng như khả năng mở rộng:

- Nhận thức về yếu tố thời gian: Theo dõi sự thay đổi của các sự kiện và mối quan hệ theo thời gian, cho phép thực hiện các truy vấn tại một thời điểm cụ thể. Các cạnh trong đồ thị bao gồm siêu dữ liệu thời gian để ghi lại vòng đời của các mối quan hệ.
- Xử lý theo từng giai đoạn (Episodic Processing): Tiếp nhận dữ liệu dưới dạng các giai đoạn rời rạc, duy trì nguồn gốc dữ liệu và cho phép trích xuất từng phần các thực thể và mối quan hệ.
- Các loại thực thể tùy chỉnh (Custom Entity Types): Hỗ trợ định nghĩa các loại thực thể đặc thù theo lĩnh vực, từ đó cho phép biểu diễn tri thức chính xác hơn trong các ứng dụng chuyên biệt.
- Tìm kiếm hỗn hợp (Hybrid Search): Kết hợp tìm kiếm ngữ nghĩa và tìm kiếm toàn văn BM25, đồng thời có khả năng sắp xếp lại thứ tự kết quả dựa trên khoảng cách từ một nút trung tâm, ví dụ như “Kendra”.
- Khả năng mở rộng (Scalable): Được thiết kế để xử lý các tập dữ liệu lớn, với khả năng song song hóa các lần gọi LLM nhằm xử lý hàng loạt mà vẫn bảo toàn tính tuần tự về mặt thời gian của các sự kiện.
- Hỗ trợ nhiều nguồn dữ liệu: Có thể xử lý cả văn bản phi cấu trúc và dữ liệu JSON có cấu trúc.
