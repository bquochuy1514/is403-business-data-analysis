# Chương 4 – Hồi quy Logistic

## Nguồn và phạm vi

- Nguồn: bản tóm tắt nội dung slide Chương 4 do người dùng cung cấp; chưa đối chiếu trực tiếp với từng trang slide gốc.
- Nội dung gồm bốn chủ đề: hồi quy Logistic nhị phân, ước lượng tham số, hồi quy Logistic đa lớp và đánh giá mô hình.
- Các số tham chiếu trang/slide bị dính vào bản tóm tắt và các ký hiệu toán bị lỗi khi sao chép đã được lược bỏ hoặc viết lại. Nếu cần xác nhận cách ký hiệu, ví dụ tính toán hay yêu cầu chính xác của giảng viên, cần xem slide gốc.
- Những đoạn ghi **“Lưu ý phương pháp của Codex”** là phần giải thích hoặc hiệu chỉnh, không phải lời trích từ slide.

## 1. Hồi quy Logistic nhị phân

### Bài toán

- **Hồi quy tuyến tính** thường dùng để dự đoán một giá trị số liên tục, ví dụ một lượng tiền hoặc một mức tiêu thụ.
- **Hồi quy Logistic nhị phân** dùng để ước tính xác suất một quan sát thuộc lớp `1` trong bài toán có hai lớp `0` và `1`.

Ví dụ trong đề tài IS403: quy ước `Revenue = TRUE` là lớp `1` (phiên có mua hàng), còn `Revenue = FALSE` là lớp `0` (phiên không mua hàng). Đây là **ví dụ liên hệ do Codex thêm**, không phải ví dụ đã xác nhận từ slide Chương 4.

### Hàm Sigmoid và quy tắc gán nhãn

Trước tiên mô hình kết hợp các thuộc tính đầu vào thành một giá trị:

$$
z = \beta_0 + \beta_1x_1 + \cdots + \beta_mx_m.
$$

Hàm Sigmoid biến `z` thành một giá trị trong khoảng `(0, 1)`:

$$
p = \sigma(z) = \frac{1}{1 + e^{-z}}.
$$

Ở đây `p` được hiểu là xác suất ước tính cho lớp `1`. Với **ngưỡng minh họa** `0,5`: nếu `p > 0,5` thì dự đoán lớp `1`; ngược lại dự đoán lớp `0`.

**Lưu ý phương pháp của Codex:** `0,5` là ngưỡng thường dùng để minh họa, không phải ngưỡng bắt buộc trong mọi bài toán. Với dữ liệu hai lớp mất cân bằng, cần xem mục tiêu đánh giá trước khi chọn ngưỡng.

### Odds và Logit

Với `0 < p < 1`, **odds** của lớp `1` là `p/(1-p)`. **Logit** là logarit tự nhiên của odds:

$$
\operatorname{logit}(p)
= \ln\!\left(\frac{p}{1-p}\right)
= \beta_0 + \beta_1x_1 + \cdots + \beta_mx_m.
$$

Logit đưa xác suất trong khoảng `(0, 1)` về một giá trị trên toàn trục số thực, nhờ đó mô hình liên kết xác suất với tổ hợp tuyến tính của các thuộc tính.

## 2. Ước lượng tham số bằng Maximum Likelihood Estimation (MLE)

### Likelihood và Log-Likelihood

Giả sử nhãn `yᵢ` nhận giá trị `0` hoặc `1`, và `pᵢ = σ(βᵀxᵢ)` là xác suất mô hình ước tính cho quan sát `i`. Trong mô hình Logistic nhị phân, nhãn được mô hình hóa theo phân phối Bernoulli với xác suất `pᵢ`.

Với các quan sát độc lập có điều kiện theo đầu vào, **likelihood** là:

$$
L(\beta) = \prod_{i=1}^{n} p_i^{y_i}(1-p_i)^{1-y_i}.
$$

Lấy logarit để chuyển tích thành tổng, ta được **log-likelihood**:

$$
\ell(\beta)
= \sum_{i=1}^{n}\left[y_i\ln p_i+(1-y_i)\ln(1-p_i)\right].
$$

MLE tìm các hệ số `β` sao cho kết quả quan sát được có likelihood lớn nhất theo mô hình.

### Hai cách tối ưu được nêu

- **Newton–Raphson:** dùng đạo hàm bậc nhất (gradient) và ma trận đạo hàm bậc hai (Hessian) để cập nhật tham số. Việc tính hoặc xử lý Hessian có thể tốn chi phí khi số thuộc tính lớn.
- **Gradient Descent:** cập nhật tham số theo hướng làm giảm hàm mất mát. Khi không xét thành phần điều chuẩn, **Cross-Entropy/Log Loss trung bình** là log-likelihood đổi dấu và chia cho số quan sát:

$$
\mathcal{L}(\beta)=-\frac{1}{n}\ell(\beta).
$$

**Lưu ý phương pháp của Codex:** MLE là **mục tiêu ước lượng**; Newton–Raphson và Gradient Descent là **các cách tìm tham số** để tối ưu mục tiêu đó. Không nên xem chúng là ba mô hình phân loại khác nhau.

## 3. Hồi quy Logistic đa lớp

Khi nhãn có nhiều hơn hai lớp, bản tóm tắt nêu hai cách mở rộng:

### One-vs-Rest (OvR; còn gọi One-vs-All)

Với `K` lớp, huấn luyện `K` mô hình nhị phân. Mỗi mô hình phân biệt một lớp với tất cả các lớp còn lại; khi dự đoán, chọn lớp có điểm hoặc xác suất ước tính cao nhất.

### Softmax Regression (Multinomial Logistic Regression)

Mô hình tạo một giá trị `zₖ` cho mỗi lớp `k`, rồi dùng Softmax để chuyển chúng thành các xác suất có tổng bằng `1`:

$$
P(y=k\mid x)=\frac{e^{z_k}}{\sum_{j=1}^{K}e^{z_j}}.
$$

**Lưu ý phương pháp của Codex:** đề tài dự đoán `Revenue = TRUE/FALSE` hiện là bài toán **hai lớp**. Phần đa lớp là kiến thức của Chương 4, chưa phải phần nhóm cần áp dụng mặc định cho đề tài này.

## 4. Đánh giá mô hình dự đoán

### Ma trận nhầm lẫn

Sau khi so sánh nhãn dự đoán với nhãn thực tế, có bốn loại kết quả:

| Ký hiệu | Ý nghĩa khi coi `Revenue = TRUE` là lớp dương |
| --- | --- |
| TP | Dự đoán có mua và thực tế có mua. |
| TN | Dự đoán không mua và thực tế không mua. |
| FP | Dự đoán có mua nhưng thực tế không mua. |
| FN | Dự đoán không mua nhưng thực tế có mua. |

### Các chỉ số được nêu

| Chỉ số | Cách hiểu ngắn |
| --- | --- |
| Accuracy | Tỷ lệ dự đoán đúng trên tất cả quan sát. |
| Error Rate | Tỷ lệ dự đoán sai trên tất cả quan sát; bằng `1 − Accuracy`. |
| Sensitivity / Recall | Trong các trường hợp thực sự thuộc lớp dương, mô hình nhận ra được bao nhiêu. |
| Specificity | Trong các trường hợp thực sự thuộc lớp âm, mô hình nhận ra được bao nhiêu. |
| Precision | Trong các trường hợp mô hình dự đoán là dương, có bao nhiêu trường hợp đúng. |
| F1-score | Trung bình hài hòa của Precision và Recall. |

$$
F_1=\frac{2\,\mathrm{Precision}\,\mathrm{Recall}}
{\mathrm{Precision}+\mathrm{Recall}}.
$$

Với bài toán đa lớp, bản tóm tắt có nhắc **Weighted F1-score**, tức tổng hợp F1 của các lớp có xét đến số quan sát của từng lớp.

**Lưu ý phương pháp của Codex:** không có một chỉ số duy nhất luôn phù hợp. Đặc biệt, khi lớp mua hàng ít hơn lớp không mua hàng, Accuracy cao chưa đủ chứng minh mô hình nhận diện tốt các phiên mua hàng. Việc chọn chỉ số cuối cùng cho đồ án vẫn cần được nhóm quyết định và giải thích.

### Cách ước tính và trình bày kết quả

- **Holdout (Train/Test split):** chia dữ liệu thành phần dùng để học và phần dùng để kiểm tra.
- **Cross-Validation:** lặp việc huấn luyện/kiểm tra trên các phần chia khác nhau để ước tính kết quả ổn định hơn.
- **Bootstrap:** lấy mẫu lặp lại có hoàn lại để khảo sát sự biến động của kết quả.
- **ROC/AUC:** đường cong và chỉ số tổng hợp dùng để đánh giá khả năng phân biệt hai lớp ở các ngưỡng khác nhau.

**Lưu ý phương pháp của Codex:** ROC/AUC là **cách biểu diễn và chỉ số đánh giá**, không phải một phương pháp chia hoặc lấy mẫu dữ liệu như ba mục đứng trước.

## Khi cần xem slide gốc

- Ví dụ số cụ thể cho Sigmoid, Logit, MLE, Newton–Raphson hoặc Gradient Descent.
- Quy ước chính xác của giảng viên tại `p = 0,5` và cách chọn ngưỡng phân loại.
- Công thức/định nghĩa chi tiết của các chỉ số, ROC/AUC, Cross-Validation và Bootstrap theo slide.
- Phạm vi yêu cầu về Logistic đa lớp và Weighted F1-score trong bài tập hoặc đồ án.
