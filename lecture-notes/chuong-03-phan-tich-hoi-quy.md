# Chương 3 – Phân tích hồi quy

## Nguồn và phạm vi

- Nguồn: bản tóm tắt Chương 3 do người dùng cung cấp; chưa đối chiếu từng trang với slide gốc.
- Nội dung gồm: tương quan, hồi quy tuyến tính đơn và bội, hồi quy phi tuyến, Gradient Descent, đánh giá mô hình.
- Các mục **“Lưu ý phương pháp của Codex”** bên dưới là phần giải thích/hiệu chỉnh để tránh áp dụng sai; không phải lời trích từ slide. Nếu cần biết chính xác slide viết gì hoặc làm bài theo công thức của giảng viên, hãy gửi ảnh trang liên quan.

## 1. Tương quan và hồi quy

### Phân tích tương quan

Tương quan mô tả **mức độ và chiều hướng liên hệ** giữa các biến. Theo bản tóm tắt:

- Với **biến phân loại/định danh**, có thể dùng kiểm định Chi-square (`χ²`) để xem hai thuộc tính có độc lập hay không.
- Với **biến số**, hệ số tương quan Pearson `r ∈ [−1, 1]` đo mức độ liên hệ **tuyến tính**: `r > 0` là cùng chiều, `r < 0` là ngược chiều, `r = 0` là không có tương quan tuyến tính theo thước đo này.

**Lưu ý phương pháp của Codex:** tương quan hoặc kết quả Chi-square không tự chứng minh biến này là _nguyên nhân_ của biến kia. `r = 0` cũng không loại trừ quan hệ phi tuyến.

### Mô hình hồi quy

Hồi quy mô tả hoặc dự đoán biến kết quả `Y` từ một hay nhiều biến đầu vào `X`, với các tham số `θ` của mô hình:

`Y ≈ f(X, θ)`

Bản tóm tắt liệt kê các cách phân loại: tuyến tính/phi tuyến, một biến/nhiều biến giải thích, tham số/phi tham số/bán tham số, đối xứng/bất đối xứng. Cần ảnh slide nếu muốn xác định ý nghĩa chính xác của cặp “đối xứng/bất đối xứng” trong bài giảng.

## 2. Hồi quy tuyến tính đơn

Mô hình dự đoán từ **một biến đầu vào** `X`:

`Ŷᵢ = β₀ + β₁Xᵢ`

- `β₀`: hệ số chặn; giá trị dự đoán khi `X = 0` nếu trường hợp này có ý nghĩa trong dữ liệu.
- `β₁`: hệ số góc; mức thay đổi dự đoán của `Y` khi `X` tăng một đơn vị.
- `Yᵢ − Ŷᵢ`: phần dư/sai số dự đoán của quan sát `i`.

Phương pháp **bình phương tối thiểu (OLS)** tìm các hệ số để tối thiểu hóa tổng bình phương phần dư:

`SSE = Σᵢ(Yᵢ − Ŷᵢ)²`

Bản tóm tắt nhắc đến giải bằng OLS, thử–sai hoặc Gradient Descent. **Lưu ý phương pháp của Codex:** OLS là tiêu chuẩn tối ưu hóa; công thức giải trực tiếp và Gradient Descent là hai cách tìm hệ số theo tiêu chuẩn đó. “Thử–sai” chỉ nên hiểu là cách minh họa, không phải lựa chọn chính cho thực nghiệm có thể lặp lại.

## 3. Hồi quy tuyến tính bội

Với `k` biến đầu vào:

`Yᵢ = β₀ + β₁Xᵢ₁ + … + βₖXᵢₖ + εᵢ`

Giá trị dự đoán từ mô hình là `Ŷᵢ = β₀ + β₁Xᵢ₁ + … + βₖXᵢₖ`; **không cộng** sai số ngẫu nhiên `εᵢ` vào giá trị dự đoán.

### Các giả định cần chú ý

Bản tóm tắt nêu ba ý về phân phối chuẩn của sai số, phương sai bằng nhau và tính độc lập. Cách viết trong bản tóm tắt dễ gây nhầm rằng _các biến đầu vào_ phải có phương sai bằng nhau hoặc hoàn toàn độc lập với nhau.

**Lưu ý phương pháp của Codex:** trong hồi quy tuyến tính thông thường, các giả định cần xem xét là quan hệ tuyến tính theo tham số, kỳ vọng sai số có điều kiện bằng 0, tính độc lập/phụ thuộc phù hợp với thiết kế dữ liệu, phương sai sai số không đổi khi dùng suy luận OLS chuẩn, và **không có đa cộng tuyến hoàn hảo**. Biến đầu vào không cần có phương sai bằng nhau hay độc lập hoàn toàn. Giả định phần dư gần phân phối chuẩn chủ yếu hỗ trợ các phép suy luận trong mẫu nhỏ; không phải điều kiện bắt buộc để tính hệ số OLS.

### Dạng ma trận

Khi ma trận thiết kế `X` có hạng cột đầy đủ, nghiệm OLS dạng đóng là:

`β̂ = (XᵀX)⁻¹XᵀY`

Nếu `XᵀX` không khả nghịch thì không thể dùng trực tiếp công thức nghịch đảo này; có thể cần loại biến trùng tuyến tính hoặc dùng cách giải số phù hợp.

## 4. Hồi quy phi tuyến và Gradient Descent

### Các dạng hồi quy phi tuyến được nêu

- **Dạng tham số:** hàm đa thức (_polynomial_), hàm mũ (_exponential_), logarit (_logarithmic_), lũy thừa (_power_).
- **Dạng phi tham số:** _kernel smoothing_, hồi quy dựa trên láng giềng gần (_nearest-neighbor regression_).

**Lưu ý phương pháp của Codex:** hồi quy đa thức có thể phi tuyến theo `X` nhưng vẫn **tuyến tính theo hệ số** `β`; vì vậy không phải mọi mô hình có đường cong đều cần một bộ tối ưu phi tuyến riêng.

### Gradient Descent (GD)

GD cập nhật tham số theo hướng làm giảm hàm chi phí `J(θ)` (ví dụ MSE):

`θⱼ ← θⱼ − η · ∂J(θ)/∂θⱼ`

Trong đó `η` là **tốc độ học** (_learning rate_). Ba cách lấy dữ liệu cho mỗi lần cập nhật:

| Cách                              | Dữ liệu dùng để cập nhật                  |
| --------------------------------- | ----------------------------------------- |
| Batch Gradient Descent            | Toàn bộ tập huấn luyện                    |
| Stochastic Gradient Descent (SGD) | Một quan sát được chọn ở mỗi lần cập nhật |
| Mini-batch Gradient Descent       | Một nhóm nhỏ quan sát                     |

## 5. Đánh giá mô hình dự đoán

Đặt `eᵢ = Yᵢ − Ŷᵢ` là sai số trên `n` quan sát được đánh giá.

| Chỉ số      | Công thức                                          | Cách hiểu                                                                        |
| ----------- | -------------------------------------------------- | -------------------------------------------------------------------------------- | --- | ------------------------------------------------- |
| SAE         | `Σᵢ                                                | eᵢ                                                                               | `   | Tổng sai số tuyệt đối.                            |
| MAE         | `(1/n)Σᵢ                                           | eᵢ                                                                               | `   | Sai số tuyệt đối trung bình; cùng đơn vị với `Y`. |
| SSE         | `Σᵢeᵢ²`                                            | Tổng bình phương sai số.                                                         |
| MSE         | `(1/n)Σᵢeᵢ²`                                       | Bình phương sai số trung bình; phạt sai số lớn mạnh hơn.                         |
| RMSE        | `√MSE`                                             | Cùng đơn vị với `Y`; nhạy với sai số lớn.                                        |
| R²          | `1 − SSE/SST`                                      | Mức cải thiện so với dự đoán bằng trung bình trong cách định nghĩa thông thường. |
| Adjusted R² | Điều chỉnh `R²` theo số biến giải thích và cỡ mẫu. | Hữu ích khi so sánh một số mô hình hồi quy trên cùng dữ liệu.                    |

**Lưu ý phương pháp của Codex:** `R²` không luôn nằm trong `[0, 1]`; trên tập kiểm tra hoặc một số mô hình, nó có thể âm. Không có quy tắc chung rằng `R² > 0,5` là “đạt”. `Adjusted R²` phạt việc thêm biến không hữu ích nhưng **không tự ngăn quá khớp**; vẫn cần đánh giá trên dữ liệu chưa dùng để huấn luyện và xét mục tiêu kinh doanh. Với dữ liệu theo thời gian, phải chia train/test theo thời gian để tránh dùng thông tin tương lai.

## Khi cần ảnh slide bổ sung

- Ví dụ tính OLS hoặc Gradient Descent từng bước; công thức hàm chi phí giảng viên dùng.
- Bảng/biểu đồ giải thích các giả định hồi quy và cách kiểm tra chúng.
- Ý nghĩa của phân loại “đối xứng/bất đối xứng”.
- Công thức `R²`, `Adjusted R²` đúng theo slide và ví dụ đánh giá mô hình.
