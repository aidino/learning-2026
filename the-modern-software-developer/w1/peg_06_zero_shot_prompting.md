# Zero-Shot Prompting   

Nội dung được dịch từ: https://www.promptingguide.ai/techniques/zeroshot

Các mô hình ngôn ngữ lớn (LLM) hiện nay, chẳng hạn như GPT-3.5 Turbo, GPT-4 và Claude 3, được tinh chỉnh để tuân theo các chỉ thị và được huấn luyện trên lượng dữ liệu khổng lồ. Việc huấn luyện quy mô lớn khiến những mô hình này có khả năng thực hiện một số tác vụ theo cách “không có mẫu” (zero-shot). Gợi ý không có mẫu nghĩa là lời nhắc (prompt) được sử dụng để tương tác với mô hình sẽ không chứa bất kỳ ví dụ hay minh họa nào. Lời nhắc không có mẫu trực tiếp hướng dẫn mô hình thực hiện một tác vụ mà không cần cung cấp thêm bất kỳ ví dụ nào để định hướng hành vi của mô hình.

Chúng tôi đã thử nghiệm một vài ví dụ về gợi ý không có mẫu trong phần trước. Dưới đây là một trong những ví dụ đó (tức là phân loại văn bản) mà chúng tôi đã sử dụng:

Prompt:

```
Classify the text into neutral, negative or positive. 
Text: I think the vacation is okay.
Sentiment:
```

Output:

```
Neutral
```


Lưu ý rằng trong lời nhắc ở trên, chúng ta không cung cấp cho mô hình bất kỳ ví dụ nào về văn bản kèm theo phân loại tương ứng của chúng; LLM đã hiểu khái niệm “cảm xúc” — đây chính là khả năng zero-shot đang phát huy tác dụng.

Việc điều chỉnh theo hướng dẫn (instruction tuning) đã được chứng minh là cải thiện khả năng học zero-shot (Wei et al., 2022). Instruction tuning về cơ bản là khái niệm tinh chỉnh (finetuning) các mô hình trên các tập dữ liệu được mô tả thông qua các chỉ dẫn. Hơn nữa, RLHF (học tăng cường từ phản hồi con người – reinforcement learning from human feedback) đã được áp dụng nhằm mở rộng quy mô instruction tuning, trong đó mô hình được căn chỉnh để phù hợp hơn với sở thích của con người. Phát triển gần đây này là nền tảng vận hành các mô hình như ChatGPT. Chúng ta sẽ thảo luận chi tiết về tất cả các phương pháp và tiếp cận nêu trên trong các phần tiếp theo.

Khi phương pháp zero-shot không hiệu quả, việc cung cấp các minh họa hoặc ví dụ trong lời nhắc được khuyến nghị — dẫn đến kỹ thuật prompting với vài mẫu (few-shot prompting). Trong phần tiếp theo, chúng ta sẽ trình bày cụ thể về few-shot prompting.

