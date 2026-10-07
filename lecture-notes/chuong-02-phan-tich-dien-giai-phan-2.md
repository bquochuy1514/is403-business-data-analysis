# Chương 2 – Phân tích diễn giải dữ liệu, Phần 2: Phân tích phương sai

## Nguồn và phạm vi

- Nguồn: bản tóm tắt nội dung slide do người dùng cung cấp. Ghi chú này chưa được đối chiếu từng trang với slide gốc.
- Phạm vi: sáu chủ đề của **Chương 2, Phần 2**: tổng quan ANOVA/ANCOVA, Levene, ANOVA một yếu tố, Tukey, ANOVA hai yếu tố và ANCOVA.
- Công thức, ví dụ, điều kiện áp dụng và cách xử lý vi phạm giả định có thể còn thiếu. Khi cần độ chính xác ở mức giải bài hoặc làm đồ án, yêu cầu ảnh slide liên quan để đối chiếu.

## 1. Tổng quan về phân tích phương sai

**ANOVA** (*Analysis of Variance*) kiểm tra liệu trung bình của biến kết quả có khác nhau giữa các nhóm được tạo theo một hay nhiều yếu tố hay không. Với `k` nhóm, giả thuyết vô hiệu là:

`H₀: μ₁ = μ₂ = … = μₖ`

**ANCOVA** (*Analysis of Covariance*) bổ sung các biến liên tục gọi là **hiệp biến** (*covariates*) khi so sánh trung bình giữa các nhóm.

Theo tóm tắt slide, ANOVA phân tách biến thiên **giữa nhóm** (`SSB`) và **trong nhóm** (`SSW`), chuyển chúng thành bình phương trung bình (`MSB`, `MSW`), rồi tính:

`F_stat = MSB / MSW`

So sánh `F_stat` với giá trị tới hạn `F_crit` hoặc dùng p-value để quyết định có bác bỏ `H₀` hay không. Bác bỏ `H₀` nghĩa là **có ít nhất một trung bình nhóm khác**, chưa chỉ ra nhóm nào khác và không tự chứng minh quan hệ nhân quả.

## 2. Kiểm định Levene

Levene's test kiểm tra giả định **đồng nhất phương sai** giữa các nhóm độc lập:

`H₀: σ₁² = σ₂² = … = σₖ²`

Với mức ý nghĩa `α = 0,05` trong ví dụ tóm tắt:

- `p > 0,05`: **chưa đủ bằng chứng bác bỏ** giả thuyết các phương sai bằng nhau.
- `p ≤ 0,05`: có bằng chứng chống lại giả thuyết phương sai bằng nhau; cần cân nhắc cách phân tích phù hợp.

**Lưu ý khi áp dụng:** không nên viết “chấp nhận `H₀`” hoặc xem Levene là điều kiện *bắt buộc tuyệt đối* cho mọi ANOVA. Kết quả không có ý nghĩa thống kê không chứng minh các phương sai bằng nhau; khi phương sai khác nhau, có thể cân nhắc Welch ANOVA hoặc phương án khác tùy dữ liệu. Đây là lưu ý phương pháp của Codex để tránh diễn giải quá mức, không phải nội dung được xác nhận từ slide.

## 3. ANOVA một yếu tố (One-way ANOVA)

Một yếu tố phân các quan sát thành `k` nhóm độc lập. Mục tiêu là kiểm định trung bình của biến kết quả có giống nhau ở các nhóm không.

### Phân rã biến thiên

`SST = SSB + SSW`

- `SST`: tổng biến thiên.
- `SSB` (*between groups*): biến thiên giữa các trung bình nhóm.
- `SSW` (*within groups*): biến thiên của các quan sát quanh trung bình nhóm tương ứng.

Với tổng số quan sát `N`:

`MSB = SSB / (k − 1)`  
`MSW = SSW / (N − k)`  
`F_stat = MSB / MSW`

Theo quy tắc trong bản tóm tắt, nếu `F_stat > F_crit` thì bác bỏ `H₀`: tồn tại khác biệt về trung bình giữa **ít nhất hai nhóm**. Chỉ số `SSB` thể hiện sự khác biệt giữa nhóm trong dữ liệu; không nên mặc nhiên gọi đó là biến thiên “do yếu tố gây ra” nếu thiết kế nghiên cứu chưa cho phép kết luận nhân quả.

## 4. Hậu kiểm Tukey

Khi ANOVA cho thấy có khác biệt tổng thể, **Tukey's post-hoc test** giúp xác định **những cặp nhóm nào** khác nhau. Bản tóm tắt nhắc tới **Tukey–Kramer** khi kích thước nhóm không bằng nhau.

Với hai nhóm `i`, `j`, tính chênh lệch trung bình tuyệt đối:

`D = |X̄ᵢ − X̄ⱼ|`

So sánh `D` với ngưỡng sai số tới hạn `T`; theo tóm tắt, `D > T` cho thấy cặp nhóm có khác biệt có ý nghĩa thống kê. Ngưỡng `T` và giả định áp dụng chưa có trong bản tóm tắt; cần xem slide gốc khi tính toán.

## 5. ANOVA hai yếu tố (Two-way ANOVA)

ANOVA hai yếu tố xem xét trung bình của biến kết quả theo **hai yếu tố phân nhóm** và có thể kiểm tra **tương tác** giữa chúng. Ba câu hỏi kiểm định là:

1. Yếu tố A có liên quan đến khác biệt trung bình không?
2. Yếu tố B có liên quan đến khác biệt trung bình không?
3. Tác động của một yếu tố có thay đổi theo mức của yếu tố còn lại không (tương tác `A × B`)?

Phân rã biến thiên theo bản tóm tắt:

`SST = SSA + SSB + SSAB + SSE`

Trong đó `SSA`, `SSB` là phần biến thiên gắn với từng yếu tố; `SSAB` gắn với tương tác; `SSE` là phần sai số còn lại. Các tỷ số kiểm định tương ứng là `MSA/MSE`, `MSB/MSE` và `MSAB/MSE`.

**Lưu ý khi áp dụng:** việc kiểm tra tương tác cần thiết kế dữ liệu phù hợp, đặc biệt là quan sát ở các tổ hợp mức của hai yếu tố. Bản tóm tắt chưa nêu đầy đủ các giả định, bậc tự do hay cách diễn giải khi tương tác có ý nghĩa; cần ảnh slide/ví dụ nếu làm bài toán cụ thể.

## 6. ANCOVA – phân tích hiệp phương sai

ANCOVA kết hợp ý tưởng của ANOVA và hồi quy tuyến tính: so sánh trung bình giữa các nhóm **sau khi điều chỉnh** ảnh hưởng của một hoặc nhiều hiệp biến liên tục. Mục đích là kiểm soát khác biệt do hiệp biến và có thể giảm phần biến thiên sai số, giúp so sánh chính xác hơn khi các giả định phù hợp.

Ví dụ khái niệm: nếu so sánh mức chi tiêu trung bình giữa các nhóm khách hàng, có thể đưa một biến liên tục liên quan đến chi tiêu vào mô hình để điều chỉnh. Ví dụ này do Codex thêm để dễ hiểu, **không phải ví dụ được xác nhận từ slide**.

**Lưu ý:** điều chỉnh hiệp biến không tự động loại bỏ mọi thiên lệch hay chứng minh quan hệ nhân quả. Cần xác định hiệp biến trước, kiểm tra mối liên hệ với biến kết quả và giả định mô hình khi thực nghiệm.

## Tóm tắt cách chọn phương pháp

| Muốn kiểm tra | Phương pháp trong phần này |
| --- | --- |
| Phương sai giữa các nhóm có tương tự không? | Levene |
| Trung bình khác nhau theo một yếu tố không? | One-way ANOVA |
| Sau ANOVA, cặp nhóm nào khác nhau? | Tukey / Tukey–Kramer |
| Hai yếu tố và tương tác liên quan thế nào đến trung bình? | Two-way ANOVA |
| So sánh nhóm sau khi điều chỉnh hiệp biến liên tục? | ANCOVA |

## Chỗ cần ảnh slide nếu học sâu hơn

- Ví dụ tính `SSB`, `SSW`, `MSB`, `MSW`, các bậc tự do và `F_crit`.
- Điều kiện/giả định và cách chọn kiểm định khi phương sai không đồng nhất.
- Công thức ngưỡng hậu kiểm Tukey/Tukey–Kramer và ví dụ so sánh cặp.
- Thiết kế dữ liệu, bảng ANOVA và cách diễn giải tương tác trong Two-way ANOVA.
- Giả định, công thức mô hình và ví dụ thực hành ANCOVA.
