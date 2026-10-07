# Chương 1 Tổng quan về Phân tích dữ liệu kinh doanh

## Nguồn và mức độ chi tiết

- Nguồn hiện tại: tóm tắt Chương 1 do người dùng cung cấp từ Google NotebookLM.
- Đây là ghi chú học tập có cấu trúc, không phải bản sao nguyên văn slide.
- Khi cần công thức, ví dụ cụ thể, hình minh họa, diễn giải đầy đủ hoặc danh sách chưa được nêu hết trong bản tóm tắt, phải báo người dùng để gửi ảnh slide liên quan; không tự suy diễn là nội dung có trong tài liệu.

## 1. Phân tích dữ liệu và phân tích dữ liệu kinh doanh

### Khái niệm

**Phân tích dữ liệu (Data Analysis)** là quá trình tìm kiếm, kiểm tra, làm sạch và mô hình hóa dữ liệu nhằm rút ra thông tin có giá trị, từ đó hỗ trợ ra quyết định.

### Data Analysis và Data Analytics

| Khái niệm          | Trọng tâm                                                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Data Analysis**  | Nghiêng về thống kê và mô tả; phân tích dữ liệu quá khứ/hiện tại để giải thích điều đã xảy ra.                                      |
| **Data Analytics** | Phạm vi rộng hơn; dùng công cụ và quy trình để biến dữ liệu thô thành thông tin có thể dự báo và đề xuất hành động trong tương lai. |

### Bốn cấp độ phân tích

| Cấp độ                     | Câu hỏi trọng tâm              | Mục đích                                            |
| -------------------------- | ------------------------------ | --------------------------------------------------- |
| **Descriptive - mô tả**    | Điều gì đã xảy ra?             | Tóm tắt, mô tả hiện trạng và kết quả trong quá khứ. |
| **Diagnostic - chẩn đoán** | Vì sao điều đó xảy ra?         | Tìm nguyên nhân, yếu tố liên quan và khác biệt.     |
| **Predictive - dự báo**    | Điều gì có khả năng sẽ xảy ra? | Dự đoán kết quả/trạng thái tương lai.               |
| **Prescriptive - đề xuất** | Nên hành động thế nào?         | Đề xuất hướng hành động tối ưu.                     |

## 2. Dữ liệu trong phân tích kinh doanh

### Dữ liệu kinh doanh

Dữ liệu kinh doanh có thể gồm thông tin về tài chính, khách hàng, sản phẩm, thị trường và dữ liệu từ hệ thống vận hành như ERP, CRM, bán hàng, marketing.

### Phân loại dữ liệu

| Tiêu chí            | Loại dữ liệu        | Ví dụ/đặc điểm trong slide                        |
| ------------------- | ------------------- | ------------------------------------------------- |
| Cấu trúc            | **Structured**      | Dữ liệu có cấu trúc, thường ở dạng bảng.          |
| Cấu trúc            | **Unstructured**    | Văn bản, hình ảnh.                                |
| Cấu trúc            | **Semi-structured** | XML, JSON.                                        |
| Nguồn gốc/thời điểm | **Real-time**       | Dữ liệu phát sinh/cập nhật theo thời gian thực.   |
| Nguồn gốc           | **External**        | Dữ liệu đến từ bên ngoài tổ chức/hệ thống nội bộ. |

### Kiểu dữ liệu và thang đo

| Nhóm                    | Kiểu/thang đo            | Đặc điểm                                        |
| ----------------------- | ------------------------ | ----------------------------------------------- |
| Categorical - phân loại | Nominal - định danh      | Các nhóm không có thứ tự.                       |
| Categorical - phân loại | Binary - nhị phân        | Hai giá trị; có thể đối xứng hoặc bất đối xứng. |
| Categorical - phân loại | Ordinal - thứ bậc        | Các nhóm có thứ tự.                             |
| Numeric - số            | Interval-scaled - khoảng | Không có gốc 0 thực sự; ví dụ nhiệt độ.         |
| Numeric - số            | Ratio-scaled - tỷ lệ     | Có gốc 0 thực sự; ví dụ tiền tệ, số lượng.      |
| Numeric - số            | Discrete - rời rạc       | Giá trị đếm/rời rạc.                            |
| Numeric - số            | Continuous - liên tục    | Giá trị có thể nhận liên tục trên một khoảng.   |

### Tiền xử lý dữ liệu

Tiền xử lý có thể chiếm khoảng **60% thời gian** của một dự án phân tích. Bốn kỹ thuật chính:

1. **Data cleaning - làm sạch:** xử lý dữ liệu lỗi, thiếu, không nhất quán hoặc không hợp lệ.
2. **Data integration - tích hợp:** kết hợp dữ liệu từ các nguồn khác nhau.
3. **Data reduction - rút gọn:** giảm khối lượng/chiều dữ liệu nhưng giữ thông tin hữu ích.
4. **Data transformation/discretization - biến đổi hoặc rời rạc hóa:** thay đổi biểu diễn/chuẩn hóa dữ liệu, hoặc chuyển một số biến liên tục thành các khoảng/nhóm rời rạc.

## 3. Các phương pháp phân tích dữ liệu cơ bản

Các phương pháp được giới thiệu để giải các bài toán kinh doanh gồm:

- **Cluster Analysis - phân tích cụm:** nhóm các đối tượng tương đồng; dùng để khám phá phân khúc khách hàng hoặc cấu trúc ẩn.
- **Cohort Analysis - phân tích nhóm đối tượng:** theo dõi hành vi của nhóm người dùng có cùng đặc điểm qua các khoảng thời gian.
- **Regression Analysis - phân tích hồi quy:** mô hình hóa quan hệ giữa biến phụ thuộc và biến độc lập để dự báo xu hướng.
- **Neural Networks - mạng nơ-ron nhân tạo.**
- **Factor Analysis - phân tích nhân tố.**
- **Data Mining - khai thác dữ liệu.**
- **Text Analysis - phân tích văn bản.**
- **Decision Trees - cây quyết định.**

> Bản tóm tắt nói slide giới thiệu 10 phương pháp nhưng chỉ nêu tên 8 phương pháp ở trên. Nếu cần danh sách đủ 10 phương pháp hoặc mô tả từng phương pháp theo slide, yêu cầu ảnh các slide phần này.

## 4. Đo lường dữ liệu và thống kê mô tả

### Tổng thể và mẫu

- **Population - tổng thể:** toàn bộ đối tượng thuộc phạm vi nghiên cứu.
- **Sample - mẫu:** tập con đại diện được chọn từ tổng thể; dùng để giảm thời gian và chi phí nghiên cứu.

### Thước đo vị trí trung tâm

- **Mean - trung bình**
- **Median - trung vị**
- **Mode - mốt**
- **Quantiles/Quartiles - phân vị/tứ phân vị**

### Thước đo phân tán

- **Range - khoảng biến thiên**
- **IQR - khoảng tứ phân vị**
- **Variance - phương sai**
- **Standard Deviation - độ lệch chuẩn**
- **Standard Error - sai số chuẩn**

### Hình dáng phân phối

Đánh giá bằng:

- **Histogram - biểu đồ tần suất**
- **Skewness - độ lệch**
- **Kurtosis - độ nhọn**

## 5. Trực quan hóa dữ liệu

### Mục đích

Trực quan hóa dùng đồ họa để đơn giản hóa dữ liệu phức tạp, giúp nhận ra mẫu hình và xu hướng.

### Biểu đồ thường dùng

| Biểu đồ                                 | Mục đích chính                               |
| --------------------------------------- | -------------------------------------------- |
| Bar chart - cột                         | So sánh các nhóm.                            |
| Line chart - đường                      | Biểu diễn chuỗi thời gian.                   |
| Pie chart - tròn                        | Thể hiện tỷ lệ phần trăm.                    |
| Scatter plot / 3D scatter plot - tán xạ | Phân tích mối tương quan giữa 2 hoặc 3 biến. |
| Box plot - hộp                          | Tóm tắt phân bố và phát hiện ngoại lệ.       |

### Quy trình cơ bản

`Thu thập và làm sạch dữ liệu → chọn biểu đồ phù hợp → trực quan hóa`.

## Khi nào cần ảnh slide bổ sung

Gửi ảnh slide nếu cần một trong các nhu cầu sau:

- công thức, cách tính và ví dụ số cho các chỉ số thống kê;
- tiêu chí chọn biểu đồ, diễn giải biểu đồ hoặc case study;
- danh sách đầy đủ 10 phương pháp phân tích và ứng dụng minh họa;
- quy trình tiền xử lý chi tiết, công cụ hoặc mã R/Python có trong slide;
- nội dung bài tập, câu hỏi ôn tập hoặc phần mà bản tóm tắt không nhắc tới.
