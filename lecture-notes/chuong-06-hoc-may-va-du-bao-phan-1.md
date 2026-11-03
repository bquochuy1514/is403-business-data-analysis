# Chương 6 – Học máy và bài toán dự báo (Phần 1)

## Nguồn và phạm vi

- Nguồn: bản tóm tắt nội dung slide Chương 6 Phần 1 do người dùng cung cấp; chưa đối chiếu trực tiếp với slide gốc.
- Nội dung gồm ba phần: ML/DL trong phân tích chuỗi thời gian, SVM cho phân loại và SVR cho hồi quy.
- Các số tham chiếu dính vào bản tóm tắt không đi kèm danh mục trang hoặc tài liệu nên được lược bỏ. Các ký hiệu toán bị lỗi khi sao chép được viết lại.
- Các đoạn **“Lưu ý phương pháp của Codex”** là giải thích hoặc hiệu chỉnh kỹ thuật, không phải lời trích từ slide.

## 1. Machine Learning (ML) và Deep Learning (DL) trong phân tích chuỗi thời gian

### Machine Learning

**Học máy (ML)** dùng dữ liệu quá khứ để xây dựng mô hình dự đoán thay vì chỉ dựa vào một bộ luật cố định do con người viết sẵn. Trong nhiều cách làm chuỗi thời gian truyền thống, người thực hiện phải tạo các thuộc tính đầu vào từ dữ liệu, chẳng hạn giá trị của những ngày trước.

Các phương pháp được bản tóm tắt nêu:

| Phương pháp | Vai trò/ý tưởng trong bản tóm tắt |
| --- | --- |
| Linear Regression | Mô hình hóa quan hệ tuyến tính để dự báo giá trị số. |
| Decision Tree | Chia dữ liệu theo các điều kiện trên thuộc tính để đưa ra dự đoán. |
| Random Forest | Kết hợp nhiều cây quyết định nhằm giảm sự phụ thuộc vào một cây đơn lẻ. |
| KNN | Dựa trên những quan sát quá khứ có thuộc tính tương tự. |
| Support Vector Regression (SVR) | Dự báo giá trị số; có thể dùng kernel để mô hình hóa quan hệ phi tuyến. |

Theo bản tóm tắt, các cách ML truyền thống có thể cần thiết kế thuộc tính thủ công và gặp khó khăn với phụ thuộc thời gian dài hoặc quan hệ phi tuyến phức tạp.

**Lưu ý phương pháp của Codex:** đây không phải hạn chế đúng với *mọi* thuật toán ML. Cây quyết định đơn lẻ cũng có thể **quá khớp** dữ liệu; Random Forest thường được dùng để giảm rủi ro đó, chứ không thể nói cả hai đều tự hạn chế quá khớp. SVR với kernel phi tuyến không bảo đảm độ chính xác cao trên mọi dataset. Khi dự báo chuỗi thời gian bằng các phương pháp trên, cần tạo đầu vào từ các mốc quá khứ và đánh giá theo thứ tự thời gian phù hợp.

### Deep Learning

**Học sâu (DL)** dùng mạng nơ-ron nhiều lớp để học các biểu diễn từ dữ liệu. Bản tóm tắt nêu các kiến trúc thường dùng cho dữ liệu chuỗi:

| Kiến trúc | Ý tưởng chính |
| --- | --- |
| RNN | Truyền trạng thái ẩn từ bước thời gian trước sang bước sau; có thể khó học quan hệ rất dài do hiện tượng biến mất đạo hàm. |
| LSTM | Dùng các cổng để điều tiết việc lưu và truyền thông tin, giúp xử lý quan hệ dài tốt hơn RNN cơ bản trong nhiều trường hợp. |
| GRU | Kiến trúc có cổng đơn giản hơn LSTM, thường có ít tham số hơn. |
| CNN | Trích xuất mẫu hình cục bộ trong chuỗi; có thể dùng riêng hoặc kết hợp với kiến trúc khác. |
| Transformer | Dùng cơ chế tự chú ý (*self-attention*) thay cho kết nối hồi tiếp làm cơ chế chính, cho phép xử lý song song nhiều vị trí trong chuỗi. |

**Lưu ý phương pháp của Codex:** LSTM không loại bỏ hoàn toàn mọi khó khăn với chuỗi dài; GRU không chắc luôn huấn luyện nhanh hơn trong mọi cấu hình; Transformer cũng có chi phí tính toán/bộ nhớ đáng kể khi chuỗi dài. Đây là các lựa chọn cần kiểm chứng bằng dữ liệu và thiết kế thực nghiệm cụ thể.

## 2. Support Vector Machine (SVM) cho phân loại

### Siêu phẳng, lề và vector hỗ trợ

Với SVM tuyến tính hai lớp, ranh giới phân loại là siêu phẳng:

$$
w^\top x+b=0.
$$

Mục tiêu cơ bản là chọn ranh giới có **lề phân tách lớn** giữa hai lớp. **Support vectors** là các quan sát có ảnh hưởng đến vị trí ranh giới; trong trường hợp lề mềm, chúng có thể nằm trên biên, trong vùng biên hoặc bị phân loại sai.

Khi chuẩn hóa ràng buộc theo dạng `yᵢ(wᵀxᵢ + b) ≥ 1`, khoảng cách từ siêu phẳng trung tâm tới **mỗi** biên là `1/‖w‖`, còn **độ rộng toàn bộ vùng lề** giữa hai biên là `2/‖w‖`.

**Lưu ý phương pháp của Codex:** bản tóm tắt ghi `Margin = 1/‖w‖` nhưng không nói rõ đang tính **nửa lề** hay **toàn bộ lề**. Hai cách diễn đạt trên giúp tránh nhầm khi dùng công thức.

### Hard margin và soft margin

- **Hard margin:** yêu cầu hai lớp có thể được phân tách hoàn hảo bằng ranh giới đang xét; nhạy với điểm nhiễu và không phù hợp khi dữ liệu không phân tách được.
- **Soft margin:** cho phép một số quan sát vi phạm biên thông qua các biến chùng `ξᵢ`. Tham số phạt `C` điều chỉnh mức đánh đổi giữa lề rộng và việc phạt các vi phạm.

### Kernel SVM

Kernel cho phép SVM xử lý quan hệ phi tuyến bằng cách tính độ tương tự tương ứng với một không gian đặc trưng khác, mà không nhất thiết phải tạo tường minh tất cả tọa độ mới. Các kernel trong bản tóm tắt:

| Kernel | Biểu thức minh họa |
| --- | --- |
| Linear | `K(x, x′) = xᵀx′` |
| Polynomial | `K(x, x′) = (γxᵀx′ + r)^d` |
| RBF / Gaussian | `K(x, x′) = exp(−γ‖x − x′‖²)` |
| Sigmoid | `K(x, x′) = tanh(γxᵀx′ + r)` |

Các tham số như `C`, `γ`, `r` và `d` phụ thuộc loại kernel và cách cài đặt, cần ghi lại khi thực nghiệm.

### Bài toán đối ngẫu và SMO

Theo bản tóm tắt, có thể chuyển bài toán tối ưu từ dạng **nguyên thủy (primal)** sang dạng **đối ngẫu (dual)** thông qua Lagrangian và các nhân tử `αᵢ`. **SMO (Sequential Minimal Optimization)** giải bài toán đối ngẫu bằng cách cập nhật một cặp nhân tử `αᵢ, αⱼ` mỗi bước thay vì tối ưu toàn bộ cùng lúc.

**Lưu ý phương pháp của Codex:** SMO là một **thuật toán giải bài toán tối ưu của SVM**, không phải một nhãn dự đoán hay một loại dữ liệu đầu vào. Bản tóm tắt chưa đủ để xác nhận giảng viên yêu cầu sinh viên tự cài đặt SMO.

## 3. Support Vector Regression (SVR) cho hồi quy

**SVR** dùng ý tưởng của SVM cho bài toán dự báo **giá trị số liên tục** `y ∈ ℝ`, thay vì chọn giữa hai nhãn như SVM phân loại.

- SVR đặt một vùng sai số chấp nhận được rộng `±ε` quanh hàm dự báo, thường gọi là **ống `ε`**. Sai lệch nằm trong vùng này không bị phạt bởi mất mát `ε`-insensitive.
- Quan sát nằm ngoài ống mới bị tính phần sai lệch vượt quá `ε`; bản tóm tắt ký hiệu biến chùng phía trên là `ξᵢ`, phía dưới là `ξᵢ*`.
- SVR cũng có thể dùng kernel Linear, Polynomial hoặc RBF để mô hình hóa quan hệ phi tuyến.

**Lưu ý phương pháp của Codex:** `ε` là tham số của **SVR**, không phải tham số bắt buộc của SVM dùng để **phân loại**. Đề tài hiện tại của nhóm dự đoán `Revenue = TRUE/FALSE`, nên nếu dùng họ máy vector hỗ trợ thì phần phù hợp trực tiếp là **SVM phân loại**; SVR là kiến thức của chương học, không phải mô hình mặc định cho nhãn `Revenue`.

## Khi cần xem slide gốc

- Công thức và ví dụ tính lề, bài toán primal/dual, Lagrangian hoặc các bước SMO theo ký hiệu của giảng viên.
- Ví dụ cụ thể về lựa chọn kernel và tham số cho SVM/SVR.
- Các thí nghiệm chuỗi thời gian của chương, nếu cần biết kiến trúc hoặc cách chia dữ liệu chính xác mà giảng viên trình bày.
