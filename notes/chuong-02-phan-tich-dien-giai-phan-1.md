# Chương 2 Phân tích diễn giải dữ liệu Phần 1

## Nguồn và phạm vi

- Nguồn hiện tại: tóm tắt do người dùng cung cấp từ Google NotebookLM.
- Phạm vi: **Phần 1** của Chương 2; chưa phải ghi chú đầy đủ toàn bộ chương.
- Khi cần công thức đầy đủ, điều kiện áp dụng chi tiết, ví dụ tính toán, bảng giá trị tới hạn hoặc nội dung chưa có ở đây, yêu cầu người dùng gửi ảnh slide thay vì tự suy diễn.

## Mục tiêu phần học

Phần này giới thiệu các phương pháp của **thống kê suy luận (Inferential Statistics)**: dùng thông tin từ mẫu để suy ra hoặc kiểm tra các đặc trưng của tổng thể.

## 1. Ước lượng tham số tổng thể

### Khái niệm

Ước lượng tham số tổng thể (Population Parameter Estimation) dùng dữ liệu từ **mẫu (sample)** để suy ra tham số của **tổng thể (population)**, chẳng hạn trung bình, phương sai hoặc tỷ lệ.

### Phân phối Z và t

| Phân phối                        | Khi sử dụng theo ghi chú                                       | Đặc điểm                                  |
| -------------------------------- | -------------------------------------------------------------- | ----------------------------------------- |
| **Z - chuẩn hóa**                | Biết phương sai/độ lệch chuẩn tổng thể, hoặc mẫu lớn `n > 30`. | Phân phối chuẩn hóa.                      |
| **t - Student's t-distribution** | Không biết phương sai tổng thể và mẫu nhỏ `n ≤ 30`.            | Dạng chuông, có đuôi dày hơn phân phối Z. |

### Ước lượng khoảng tin cậy

- Lập khoảng tin cậy **một phía** hoặc **hai phía** cho trung bình tổng thể, dựa vào phân phối Z hoặc t theo điều kiện phù hợp.
- Lập khoảng tin cậy cho **tỷ lệ tổng thể**; trong ghi chú này áp dụng phân phối Z với mẫu lớn.

> Cần ảnh slide nếu phải ghi công thức khoảng tin cậy, mức tin cậy thường dùng, giả định mẫu hoặc ví dụ số.

## 2. Kiểm định giả thuyết

### Quy trình bốn bước

1. Thiết lập **giả thuyết vô hiệu** `H₀` và **đối thuyết** `Hₐ`.
2. Xác định **tiêu chuẩn kiểm định** `T` từ dữ liệu mẫu.
3. Chọn **mức ý nghĩa** `α`, qua đó xác định giá trị tới hạn và miền bác bỏ/chấp nhận.
4. Tính giá trị quan sát của tiêu chuẩn kiểm định và kết luận chấp nhận hoặc bác bỏ `H₀`.

### Các bài toán được nêu

- **Kiểm định trung bình một tổng thể với giá trị cho trước:** so sánh trung bình mẫu với một chuẩn/quy định.
- **Kiểm định trung bình hai tổng thể độc lập:** đánh giá khác biệt giữa hai trung bình tổng thể; có các trường hợp mẫu lớn/nhỏ và biết/chưa biết phương sai.
- **Kiểm định phương sai hai tổng thể bằng F-test:** kiểm tra tính đồng nhất hoặc mức biến động dữ liệu giữa hai nhóm.

> Cần ảnh slide nếu cần quy tắc chọn kiểm định, công thức thống kê kiểm định, giả định độc lập/chuẩn, p-value, miền bác bỏ hoặc bài tập mẫu.

## 3. Kiểm định Chi-square

### Mục đích

Kiểm định Chi-square (Chi bình phương) dùng để đánh giá **tính độc lập** hoặc mối liên hệ có ý nghĩa thống kê giữa hai biến phân loại (categorical variables).

### Ý tưởng thực hiện

- So sánh **tần suất quan sát** với **tần suất kỳ vọng** trong trường hợp hai biến hoàn toàn độc lập.
- Với bảng chéo có `r` hàng và `c` cột, bậc tự do được nêu là:

`df = (r - 1)(c - 1)`

> Cần ảnh slide nếu cần công thức tần suất kỳ vọng, thống kê Chi-square, điều kiện áp dụng (ví dụ tần suất kỳ vọng tối thiểu), cách diễn giải kết quả hoặc ví dụ bảng chéo.

## Tình trạng ghi chú Chương 2

Phần 1 gồm ước lượng tham số tổng thể, kiểm định giả thuyết và kiểm định Chi-square. Phần 2 về phân tích phương sai được ghi riêng tại [Chương 2 – Phần 2](chuong-02-phan-tich-dien-giai-phan-2.md). Cả hai ghi chú dựa trên bản tóm tắt do người dùng cung cấp; cần đối chiếu slide nếu cần chi tiết đầy đủ.
