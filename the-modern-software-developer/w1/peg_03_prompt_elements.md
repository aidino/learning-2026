# Elements of a Prompt 

Nội dung được dịch từ: https://www.promptingguide.ai/introduction/elements

Khi chúng ta khám phá ngày càng nhiều ví dụ và ứng dụng liên quan đến Prompt Engineering, bạn sẽ nhận thấy rằng một prompt thường bao gồm một số thành phần nhất định.

Một prompt có thể chứa bất kỳ thành phần nào sau đây:

- **Instruction**: Hướng dẫn — nhiệm vụ cụ thể hoặc chỉ thị mà bạn muốn mô hình thực hiện
- **Context**: Bối cảnh – thông tin bên ngoài hoặc bối cảnh bổ sung có thể định hướng mô hình đưa ra phản hồi tốt hơn
- **Input Data**: Dữ liệu đầu vào – dữ liệu hoặc câu hỏi mà chúng ta quan tâm nhằm tìm kiếm một phản hồi tương ứng
- **Output Indicator**: Chỉ báo đầu ra – loại hoặc định dạng của đầu ra.

Để minh họa rõ hơn các thành phần của lời nhắc (prompt), dưới đây là một lời nhắc đơn giản nhằm thực hiện nhiệm vụ phân loại văn bản:

```
Classify the text into neutral, negative, or positive

Text: I think the food was okay.

Sentiment:
```

Trong ví dụ lời nhắc ở trên, phần hướng dẫn tương ứng với nhiệm vụ phân loại: “Phân loại văn bản thành trung lập, tiêu cực hoặc tích cực”. Dữ liệu đầu vào tương ứng với phần “Tôi nghĩ món ăn cũng tạm được.”, và chỉ thị đầu ra được sử dụng là “Cảm xúc:”. Lưu ý rằng ví dụ cơ bản này không sử dụng ngữ cảnh, tuy nhiên ngữ cảnh cũng có thể được cung cấp như một phần của lời nhắc. Chẳng hạn, ngữ cảnh cho lời nhắc phân loại văn bản này có thể là các ví dụ bổ sung được đưa vào cùng lời nhắc nhằm giúp mô hình hiểu rõ hơn về nhiệm vụ và định hướng kiểu đầu ra mà bạn kỳ vọng.

Bạn không nhất thiết phải sử dụng cả bốn yếu tố trong một lời nhắc, và định dạng cụ thể phụ thuộc vào nhiệm vụ đang thực hiện. Chúng tôi sẽ trình bày thêm các ví dụ minh họa cụ thể hơn trong các hướng dẫn sắp tới.

