# Chương 5 – Dự báo chuỗi thời gian (ghi chú phần đơn biến và đa biến)

## Nguồn và phạm vi

- Nguồn: bản chuyển giọng nói/tóm tắt một đoạn ghi âm bài giảng do người dùng cung cấp; chưa đối chiếu với slide gốc.
- File này **chỉ ghi phần phân biệt chuỗi thời gian đơn biến và đa biến**. Chưa có nội dung chi tiết về ARIMA, ARIMAX, SARIMA hoặc SARIMAX từ bài giảng.
- Đoạn **“Lưu ý phương pháp của Codex”** là giải thích thêm, không phải lời thầy.

## 1. Chuỗi thời gian đơn biến

- Dùng lịch sử của **chính biến cần dự báo** để đoán giá trị tương lai của nó.
- Ví dụ trong bản tóm tắt: dùng lượng điện tiêu thụ những ngày trước để dự báo lượng điện tiêu thụ ngày tiếp theo; hoặc dùng giá cổ phiếu trước đây để dự báo giá ngày sau.

## 2. Chuỗi thời gian đa biến

- Dùng lịch sử của biến cần dự báo **cùng các biến phụ trợ có thông tin theo thời gian tương ứng**.
- Ví dụ dự báo điện năng: bên cạnh lịch sử tiêu thụ điện, có thể thêm chuỗi nhiệt độ, độ ẩm hoặc thời điểm sử dụng.
- Ví dụ dự báo giá cổ phiếu: bên cạnh giá đóng cửa, có thể thêm giá mở cửa, giá cao nhất, giá thấp nhất và khối lượng giao dịch theo ngày.
- Theo bản tóm tắt, thầy giải thích các biến phụ trợ có thể bổ sung bối cảnh, từ đó *có khả năng* cải thiện dự báo.

**Lưu ý phương pháp của Codex:** thêm biến không bảo đảm kết quả tốt hơn; cần kiểm tra biến đó có sẵn ở thời điểm dự báo, có cùng mốc thời gian và thực sự hữu ích hay không. “Đơn biến/đa biến” ở đây là cách gọi trong **bài toán chuỗi thời gian**, không tự áp cho bài toán phân loại từng phiên truy cập website của đề tài nhóm.

## 3. Lưu ý giảng viên khi báo cáo đồ án chuỗi thời gian

- Nói rõ nhóm dùng mô hình đơn biến, đa biến hay đối sánh cả hai.
- Nếu dùng đa biến, liệt kê cụ thể các biến phụ trợ đưa vào ngoài biến mục tiêu.

Các lưu ý khác từ ghi âm về seminar, báo cáo cuối và góp ý cho từng nhóm được lưu ở [`notes/luu-y-giang-vien-ve-do-an.md`](../notes/luu-y-giang-vien-ve-do-an.md).

## Khi cần slide/bản ghi bổ sung

- Công thức, giả định và ví dụ số cho các mô hình dự báo chuỗi thời gian.
- Nội dung ARIMA, ARIMAX, SARIMA, SARIMAX và cách chọn mô hình theo bài giảng.
