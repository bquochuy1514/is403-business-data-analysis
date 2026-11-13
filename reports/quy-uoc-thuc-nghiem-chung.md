# Quy ước thực nghiệm chung cho nhóm IS403

**Trạng thái (11/11/2026):** N01–N03 đã được thực hiện trên Google Drive/Colab. Các con số dưới đây là đầu ra các ô notebook người dùng đã chạy và gửi lại; sau khi thêm hướng dẫn Markdown, chưa xác nhận đã chạy lại toàn bộ notebook từ đầu. Notebook cùng hai CSV đã xử lý **chưa được chép vào repo**. Thầy đã duyệt **đề tài**, chưa có thông tin thầy duyệt riêng các quyết định thực nghiệm này.

## Quyết định phạm vi

Nhóm làm **thực nghiệm phân loại nhị phân trên dữ liệu phiên truy cập đã được ghi nhận**. Mô hình được học từ một số phiên có nhãn và kiểm tra trên các phiên chưa cho mô hình xem. Nhóm **không tuyên bố dự đoán theo thời gian thực khi khách còn đang duyệt website**, vì CSV hiện có là bản ghi tổng hợp theo phiên, không có chuỗi các ảnh chụp tại từng thời điểm trong phiên.

- **Đơn vị:** một phiên truy cập.
- **Nhãn cần dự đoán:** `Revenue = TRUE` là lớp `1` (có mua), `FALSE` là lớp `0` (không mua). Đây không phải số tiền doanh thu.
- **Bộ dữ liệu gốc:** [`data/raw/online_shoppers_intention.csv`](../data/raw/online_shoppers_intention.csv), lấy từ bản đã tải trước đó và đối chiếu SHA-256 với [UCI](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset). Không sửa đè bản gốc.
- **Thuộc tính dùng trong lần so sánh chính:** 16 trong 17 thuộc tính đầu vào. **Không dùng `PageValues` trong so sánh chính**, vì mô tả của UCI gắn nó với giá trị giao dịch và chưa rõ thời điểm/cách tính khi áp dụng cho một phiên mới. Đây là quyết định thận trọng của nhóm, **không phải kết luận cột này chắc chắn rò rỉ nhãn**.

Bảng khảo sát đầy đủ 17 thuộc tính ở [`khao-sat-17-thuoc-tinh.md`](khao-sat-17-thuoc-tinh.md). Khi triển khai, mọi thành viên cần dùng cùng dữ liệu đã chuẩn bị và cùng cách chia; không tự thêm/bỏ thuộc tính trong bảng so sánh chính. Nếu cần thử thêm, ghi đó là **thí nghiệm phụ** và giữ kết quả riêng.

## Cách chia và chuẩn bị dữ liệu đã triển khai

1. **Giữ nguyên 12.330 phiên** và 125 dòng trùng hoàn toàn vì CSV không có mã phiên để xác định chúng là lỗi. Theo 16 thuộc tính đầu vào được chọn, notebook tìm thấy 125 dòng trùng và **không có nhóm cùng đầu vào nhưng khác nhãn**. Mỗi nhóm dòng có 16 đầu vào giống nhau được đặt cùng phía khi chia để tránh trùng giữa phần học và phần kiểm tra.
2. Chia các nhóm khoảng **80% để học, 20% để kiểm tra** bằng `train_test_split(test_size=0.2, random_state=42, stratify=Revenue)` trên danh sách nhóm duy nhất. Kết quả theo số phiên: **9.861 học** (15,48% mua) và **2.469 kiểm tra** (15,47% mua). Tỷ lệ 80/20 là gần đúng theo số phiên vì thao tác chia theo nhóm.
3. Chín thuộc tính số được chuẩn hóa bằng `StandardScaler`; bảy thuộc tính dạng nhóm (`Month`, `OperatingSystems`, `Browser`, `Region`, `TrafficType`, `VisitorType`, `Weekend`) được mã hóa *one-hot*. `ColumnTransformer` học phép chuyển đổi **chỉ trên phần học** (`fit_transform`) và áp dụng cùng phép chuyển đổi lên phần kiểm tra (`transform`). Hai phía cùng có **73 cột đầu vào** sau chuyển đổi.
4. Hai CSV xuất ra có 73 cột đầu vào và cột `Revenue` ở cuối (**74 cột**); phiên bản in từ lần chạy Colab là **pandas 2.2.3** và **scikit-learn 1.6.1**. Mọi mô hình trong lần so sánh chính dùng đúng hai CSV và cùng thứ tự cột.

**Giải thích ngắn:** chuẩn hóa giúp các cột có độ lớn khác nhau dễ dùng hơn cho một số mô hình; one-hot khiến mã nhóm như `Browser = 2` được hiểu là *một nhóm* chứ không phải số lớn gấp đôi `Browser = 1`. Làm các bước này từ tập học giúp tránh nhìn trước thông tin thống kê của tập kiểm tra.

## Cách đánh giá chung

Tất cả mô hình cần báo cáo ít nhất **Accuracy, Precision, Recall, F1** và bốn ô **TP, TN, FP, FN**, với **mua hàng (`Revenue = 1`) là lớp dương**. Notebook chung đã có hàm `danh_gia` dùng `confusion_matrix(labels=[0, 1])` và bốn chỉ số trên; khi không có dự đoán dương, hàm đặt chỉ số không xác định bằng 0 (`zero_division=0`). Không dùng phần kiểm tra để chọn tham số, chọn ngưỡng hoặc quyết định giữ/bỏ thuộc tính; nếu cần điều chỉnh, làm trên phần học rồi chỉ đánh giá phần kiểm tra khi đã chốt cấu hình.

**Mốc trên phần kiểm tra:** cách luôn đoán “không mua” đạt Accuracy **0,8453** nhưng TP=0, TN=2.087, FP=0, FN=382 và Precision/Recall/F1 của lớp mua đều bằng 0. Đây là lý do nhóm không đánh giá bằng mỗi Accuracy. Mốc này **không phải kết quả của một trong tám mô hình đã phân công**.

## Cách làm việc khi nhóm bắt đầu code

Notebook chuẩn `IS403 | Chuẩn bị dữ liệu và đánh giá chung.ipynb` và hai file `is403_train_chung.csv`, `is403_test_chung.csv` hiện ở **Drive nhóm → `Dữ liệu và quy ước`**. Người điều phối chạy notebook này và quản lý hai CSV; các thành viên đọc notebook chuẩn, sau đó tạo notebook mô hình riêng tại **Drive nhóm → `Thực nghiệm`**. Người làm hai mô hình có thể dùng một notebook với hai mục riêng và dán cùng link vào hai dòng Sheet `Phân công`. Chưa có notebook hay bộ dữ liệu đã xử lý trong repo; Drive là nơi chia sẻ bản đang dùng.

Đường dẫn `csv_path` trong notebook chuẩn trỏ vào **MyDrive của người điều phối**, không tự đúng trên tài khoản khác. Trong notebook riêng, từng thành viên lấy đường dẫn hai CSV từ Colab Files sau khi gắn Drive; nếu thư mục được chia sẻ chưa xuất hiện ở MyDrive, có thể thêm lối tắt vào MyDrive. Thành viên không chạy ô `to_csv` của notebook chuẩn: ô đó lưu vào `Path(csv_path).parent` và có thể ghi đè file chung nếu tài khoản có quyền sửa.

Trong mỗi notebook mô hình, thành viên cần ghi **tên mô hình, tham số, phiên bản thư viện, cách chạy, bảng chỉ số, nguồn đã dùng và nhận xét**: nhận đúng bao nhiêu phiên mua, bỏ sót bao nhiêu và vì sao kết quả có thể khác mô hình khác. Nếu mô hình có yếu tố ngẫu nhiên, ghi hạt giống. Các kết quả chỉ nên được so sánh khi đã kiểm tra chúng thực sự dùng cùng dữ liệu và cách tính.

## Giới hạn cần nêu khi báo cáo

- Bản ghi CSV là dữ liệu tổng hợp theo phiên; thí nghiệm này **chưa chứng minh** mô hình có thể can thiệp trong lúc khách đang mua hàng.
- `PageValues` được loại khỏi so sánh chính để giảm rủi ro về thời điểm và nguồn tạo ra thuộc tính. Có thể làm thí nghiệm phụ có/không có cột này sau, nhưng phải ghi rõ giới hạn.
- Kết quả trên dataset này chưa chứng minh triển khai mô hình sẽ tăng tỷ lệ mua hoặc doanh thu thực tế.
- Tỷ lệ hai nhãn lệch; cần đọc Precision/Recall/F1 cùng với Accuracy và số TP/TN/FP/FN.
