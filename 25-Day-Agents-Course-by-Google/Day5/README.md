# Production Observability

Agent Starter Pack bao gồm khả năng quan sát ở cấp độ sản xuất mà không cần cấu hình. Tích hợp sẵn Cloud Trace, Log Analytics và BigQuery.

Agent của bạn đã được triển khai. Nhưng thực tế nó đang làm gì?

Agent Starter Pack bao gồm khả năng quan sát trong môi trường sản xuất. Không cần cấu hình nào.

Khả năng quan sát đạt chuẩn sản xuất đầy đủ mà các doanh nghiệp cần, được tích hợp sẵn ngay từ ngày đầu tiên.

Hai cấp độ quan sát, được cấu hình tự động:

1. **Agent Telemetry:** Cloud Trace ghi lại mọi thao tác thực thi - các cuộc gọi LLM với latency breakdown - thời gian thực thi công cụ - khả năng hiển thị toàn bộ luồng hội thoại.
2. **Prompt-Response Logging (Auto-enabled)**: Toàn bộ quy trình đầu cuối được triển khai thông qua Terraform - Log Analytics + Log Buckets với thời gian lưu trữ tùy chỉnh - BigQuery Delta Lake với các chế độ xem tùy chỉnh để dễ dàng truy vấn - Không có dữ liệu nhạy cảm trong nhật ký - tất cả nội dung được ghi vào GCS.

Deploy with one command:

```bash
uvx agent-starter-pack create my-agent -a adk_base -d agent_engine
make deploy
```

Hầu hết các đội phát triển phải mất hàng tuần để thiết lập hạ tầng quan sát. Bạn sẽ có ngay trong vài phút. Không cần cấu hình. Không cần thiết lập. Không cần công cụ giám sát tùy chỉnh. Chỉ cần triển khai và bắt đầu giám sát.