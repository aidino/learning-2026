# Chain-of-Thought Prompting

Nội dung được dịch từ: https://www.promptingguide.ai/techniques/cot

![Image Source: Wei et al. (2022)](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcot.1933d9fe.png&w=1080&q=75)

Nguồn ảnh: Wei et al. (2022)

Được giới thiệu trong nghiên cứu của Wei et al. (2022), kỹ thuật gợi ý chuỗi lập luận (Chain-of-Thought – CoT) cho phép mô hình thể hiện khả năng suy luận phức tạp thông qua các bước lập luận trung gian. Bạn có thể kết hợp kỹ thuật này với kỹ thuật gợi ý vài ví dụ (few-shot prompting) để đạt được kết quả tốt hơn trên các tác vụ phức tạp hơn, đòi hỏi quá trình suy luận trước khi đưa ra câu trả lời.

```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.

The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
A: Adding all the odd numbers (17, 19) gives 36. The answer is True.

The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
A: Adding all the odd numbers (11, 13) gives 24. The answer is True.

The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
A: Adding all the odd numbers (17, 9, 13) gives 39. The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A:
```

Output:

```
Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.
```

Ồ! Chúng ta có thể thấy một kết quả hoàn hảo khi cung cấp các bước lập luận. Thực tế, chúng ta có thể giải quyết nhiệm vụ này bằng cách đưa ra thậm chí ít ví dụ hơn, tức là chỉ cần một ví dụ dường như đã đủ:

```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.

The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A:
```

Output:

```
Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.

``` 

Lưu ý rằng các tác giả khẳng định đây là một khả năng nổi trội (emergent ability), xuất hiện khi sử dụng các mô hình ngôn ngữ đủ lớn.

## Zero-shot COT Prompting

![Image Source: Kojima et al. (2022)](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fzero-cot.79793bee.png&w=1080&q=75)

Image Source: Kojima et al. (2022)

Một ý tưởng mới đây xuất hiện gần đây hơn là khái niệm chuỗi suy luận không cần ví dụ (zero-shot CoT) (Kojima et al., 2022), về cơ bản bao gồm việc thêm cụm từ “Hãy suy luận từng bước một” vào lời nhắc gốc. Hãy thử một bài toán đơn giản và xem mô hình thực hiện như thế nào:

```
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?
```

Output:

```
11 apples

```

Câu trả lời là sai! Bây giờ hãy thử lại với lời nhắc đặc biệt.


```
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?

Let's think step by step.
```

Output

```
First, you started with 10 apples.
You gave away 2 apples to the neighbor and 2 to the repairman, so you had 6 apples left.
Then you bought 5 more apples, so now you had 11 apples.
Finally, you ate 1 apple, so you would remain with 10 apples.
```

Thật ấn tượng khi lời nhắc đơn giản này lại hiệu quả trong nhiệm vụ này. Điều này đặc biệt hữu ích trong những trường hợp bạn không có quá nhiều ví dụ để đưa vào lời nhắc.

## Automatic Chain-of-Thought (Auto-CoT)

Khi áp dụng kỹ thuật gợi ý chain-of-thought kèm các ví dụ minh họa, quá trình này đòi hỏi việc xây dựng thủ công các ví dụ hiệu quả và đa dạng. Nỗ lực thủ công như vậy có thể dẫn đến các giải pháp không tối ưu. Zhang et al. (2022) đề xuất một phương pháp loại bỏ hoàn toàn công sức thủ công bằng cách khai thác các mô hình ngôn ngữ lớn (LLMs) với lời nhắc “Hãy suy luận từng bước một” để tự động tạo ra các chuỗi lập luận cho từng ví dụ minh họa. Quá trình tự động này vẫn có thể phát sinh sai sót trong các chuỗi lập luận được sinh ra. Để giảm thiểu ảnh hưởng của những sai sót này, yếu tố đa dạng (Diversity) trong các ví dụ minh họa trở nên quan trọng. Công trình này đề xuất Auto-CoT—một phương pháp lấy mẫu các câu hỏi một cách đa dạng và sinh ra các chuỗi lập luận tương ứng nhằm xây dựng các ví dụ minh họa.

Auto-CoT bao gồm hai giai đoạn chính:

- Giai đoạn 1): Nhóm câu hỏi: phân chia các câu hỏi trong một tập dữ liệu cho trước thành một số cụm
- Giai đoạn 2): Lấy mẫu minh họa: chọn một câu hỏi tiêu biểu từ mỗi cụm và sinh chuỗi lập luận tương ứng cho câu hỏi đó bằng phương pháp Zero-Shot-CoT với các nguyên tắc kinh nghiệm đơn giản

Các simple heuristics có thể là độ dài của câu hỏi (ví dụ: 60 token) và số bước trong lập luận (ví dụ: 5 bước suy luận). Điều này khuyến khích mô hình sử dụng các minh họa đơn giản nhưng chính xác.

Quá trình này được minh họa bên dưới:

![](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fauto-cot.642d9bad.png&w=1200&q=75)

Nguồn ảnh: Zhang et al. (2022)

Mã nguồn cho Auto-CoT có sẵn [tại đây](https://github.com/amazon-science/auto-cot).

