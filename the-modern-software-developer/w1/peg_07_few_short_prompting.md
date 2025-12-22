# Few-Shot Prompting 

Nội dung được dịch từ: https://www.promptingguide.ai/techniques/fewshot

Mặc dù các mô hình ngôn ngữ lớn thể hiện khả năng zero-shot đáng kinh ngạc, chúng vẫn chưa đạt được hiệu quả mong muốn đối với các tác vụ phức tạp hơn khi sử dụng thiết lập zero-shot. Kỹ thuật prompting với vài ví dụ có thể được áp dụng như một phương pháp hỗ trợ việc học trong bối cảnh (in-context learning), trong đó chúng ta cung cấp các ví dụ minh họa trong prompt nhằm định hướng mô hình đạt hiệu suất tốt hơn. Các ví dụ minh họa này đóng vai trò là điều kiện đầu vào (conditioning) cho các ví dụ tiếp theo, nơi chúng ta mong muốn mô hình sinh ra phản hồi tương ứng.

Theo Touvron et al. (2023), tính chất few-shot lần đầu tiên xuất hiện khi các mô hình được mở rộng đến một kích thước đủ lớn (Kaplan et al., 2020).

Hãy minh họa kỹ thuật few-shot prompting thông qua một ví dụ được trình bày trong Brown et al. (2020). Trong ví dụ này, nhiệm vụ là sử dụng đúng một từ mới trong một câu.

Prompt:

```
A "whatpu" is a small, furry animal native to Tanzania. An example of a sentence that uses the word whatpu is:
We were traveling in Africa and we saw these very cute whatpus.
 
To do a "farduddle" means to jump up and down really fast. An example of a sentence that uses the word farduddle is:
```

Output:

```
When we won the game, we all started to farduddle in celebration.
```

Ta có thể quan sát thấy rằng mô hình đã học được cách thực hiện nhiệm vụ chỉ với một ví dụ duy nhất (tức là 1-shot). Đối với những nhiệm vụ khó hơn, chúng ta có thể thử nghiệm bằng cách tăng số lượng ví dụ minh họa (ví dụ: 3-shot, 5-shot, 10-shot, v.v.).


Dựa trên các phát hiện của Min et al. (2022), dưới đây là một số lưu ý bổ sung về việc lựa chọn và thiết kế các ví dụ minh họa (demonstrations/exemplars) khi áp dụng kỹ thuật few-shot:

- không gian nhãn và phân bố của văn bản đầu vào được xác định bởi các ví dụ minh họa đều rất quan trọng (bất kể nhãn có đúng cho từng đầu vào cụ thể hay không)
- định dạng bạn sử dụng cũng đóng vai trò then chốt đối với hiệu năng; ngay cả khi bạn chỉ sử dụng các nhãn ngẫu nhiên, điều này vẫn tốt hơn nhiều so với việc hoàn toàn không có nhãn nào.
- các kết quả bổ sung còn cho thấy việc chọn nhãn ngẫu nhiên từ phân bố thực tế của các nhãn (thay vì từ phân bố đều) cũng mang lại lợi ích.

Hãy thử một vài ví dụ. Trước tiên, ta sẽ xét một ví dụ với các nhãn ngẫu nhiên (tức là các nhãn “Tiêu cực” và “Tích cực” được gán ngẫu nhiên cho các đầu vào):

Prompt:

```
This is awesome! // Negative
This is bad! // Positive
Wow that movie was rad! // Positive
What a horrible show! //
```

Output:

```
Negative
```

Chúng ta vẫn nhận được câu trả lời đúng, ngay cả khi các nhãn đã được ngẫu nhiên hóa. Lưu ý rằng chúng ta cũng giữ nguyên định dạng, điều này cũng góp phần hỗ trợ việc suy luận. Thực tế, qua các thử nghiệm thêm, dường như các mô hình GPT mới hơn mà chúng ta đang thử nghiệm ngày càng trở nên bền bỉ hơn trước cả những định dạng ngẫu nhiên. Ví dụ:

```
Positive This is awesome! 
This is bad! Negative
Wow that movie was rad!
Positive
What a horrible show! --
```

Output:

```
Negative
```

Định dạng ở trên hoàn toàn thiếu tính nhất quán, thế nhưng mô hình vẫn dự đoán đúng nhãn. Chúng ta cần tiến hành phân tích kỹ lưỡng hơn để xác minh xem hiện tượng này có còn đúng trong các tác vụ khác nhau và phức tạp hơn hay không, bao gồm cả các biến thể khác nhau của lời nhắc.


## Limitations of Few-shot Prompting

Kỹ thuật prompting với vài ví dụ (few-shot prompting) tiêu chuẩn hoạt động tốt đối với nhiều tác vụ, nhưng vẫn chưa phải là một phương pháp hoàn hảo, đặc biệt khi xử lý các tác vụ suy luận phức tạp hơn. Hãy cùng minh họa vì sao lại như vậy. Bạn còn nhớ ví dụ trước đây, trong đó chúng ta đã đưa ra tác vụ sau đây không?

```
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 

A: 
```

Nếu chúng ta thử lại lần nữa, mô hình sẽ đưa ra đầu ra như sau:

```
Yes, the odd numbers in this group add up to 107, which is an even number.

```

Đây không phải là câu trả lời đúng, điều này không chỉ làm nổi bật những hạn chế của các hệ thống này mà còn cho thấy nhu cầu về các kỹ thuật Prompt Engineering tiên tiến hơn.

Hãy thử thêm một số ví dụ để xem liệu phương pháp prompting với vài mẫu (few-shot prompting) có cải thiện kết quả hay không.

```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: The answer is False.

The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
A: The answer is True.

The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
A: The answer is True.

The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
A: The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A: 

```

Output:

```

The answer is True.

```

Điều đó không hiệu quả. Có vẻ như kỹ thuật prompting với vài ví dụ (few-shot prompting) là chưa đủ để thu được các phản hồi đáng tin cậy đối với loại bài toán suy luận này. Ví dụ nêu trên chỉ cung cấp thông tin cơ bản về nhiệm vụ. Nếu xem xét kỹ hơn, loại nhiệm vụ mà chúng ta đã giới thiệu đòi hỏi một số bước suy luận bổ sung. Nói cách khác, việc phân tách bài toán thành từng bước cụ thể và minh hoạ quy trình đó cho mô hình có thể mang lại hiệu quả cao hơn. Gần đây, kỹ thuật prompting dựa trên chuỗi lập luận (Chain-of-Thought – CoT) đã trở nên phổ biến nhằm giải quyết các bài toán suy luận phức tạp hơn, bao gồm các bài toán số học, suy luận thường thức và suy luận ký hiệu.


Nhìn chung, việc cung cấp các ví dụ dường như hữu ích trong việc giải quyết một số nhiệm vụ. Khi cả prompting không có ví dụ (zero-shot prompting) và prompting với vài ví dụ (few-shot prompting) đều không đủ hiệu quả, điều này có thể cho thấy những gì mô hình đã học được chưa đủ để thực hiện tốt nhiệm vụ đó. Trong trường hợp này, nên bắt đầu cân nhắc việc fine-tuning các mô hình của bạn hoặc thử nghiệm các kỹ thuật prompting nâng cao hơn. Tiếp theo, chúng ta sẽ thảo luận về một trong những kỹ thuật prompting phổ biến nhất — gọi là prompting chuỗi lập luận (chain-of-thought prompting) — vốn đã thu hút được rất nhiều sự quan tâm.

