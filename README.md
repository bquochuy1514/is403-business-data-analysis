# IS403 — Phân tích dữ liệu kinh doanh

Repo lưu ghi chú môn học và chuẩn bị đồ án. **Đề tài đã được giảng viên duyệt sau buổi giới thiệu 5 slide:**

> Dự đoán khả năng mua hàng từ dữ liệu phiên truy cập website thương mại điện tử: Đánh giá thực nghiệm các mô hình phân loại

## Bài toán

Từ các thuộc tính mô tả một phiên truy cập website, dự đoán phiên đó có dẫn đến giao dịch mua hàng hay không. Nhãn cần dự đoán là `Revenue` (`TRUE`/`FALSE`), **không phải số tiền doanh thu**. Nhóm sẽ thử và đánh giá các phương pháp phân loại đã tồn tại, giải thích sự khác biệt giữa kết quả, nêu giới hạn và đề xuất cải tiến. Quy ước cho lần so sánh chính đã được triển khai trong notebook chuẩn bị dữ liệu; các mô hình được phân công nhưng chưa có kết quả thực nghiệm.

- **Dataset dùng để đăng ký:** [Online Shoppers Purchasing Intention trên Kaggle](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset). [UCI](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset) là nguồn gốc của bộ dữ liệu.
- **Paper tham khảo:** [*Modeling online customer purchase intention behavior applying different feature engineering and classification techniques*](https://link.springer.com/article/10.1007/s44163-023-00086-0). Nhóm không cam kết tái lập nguyên quy trình của paper.

## Tình trạng hiện tại

Buổi giới thiệu 5 slide đã hoàn thành; thầy đã duyệt **đề tài** và yêu cầu khảo sát kỹ 17 thuộc tính đầu vào. N01 (khảo sát), N02 (phạm vi và thuộc tính) và N03 (chuẩn bị dữ liệu, chia dữ liệu, hàm đánh giá) đã được thực hiện trên Google Drive/Colab. Notebook `IS403 | Chuẩn bị dữ liệu và đánh giá chung.ipynb` đã chạy: 12.330 phiên, chọn 16 thuộc tính (không dùng `PageValues` trong so sánh chính), chia 9.861 phiên học và 2.469 phiên kiểm tra, chuyển thành 73 cột đầu vào. Hai file `is403_train_chung.csv` và `is403_test_chung.csv` nằm cùng notebook trong thư mục Drive nhóm `Dữ liệu và quy ước`. Chưa chạy tám mô hình đã phân công, chưa có kết quả so sánh mô hình. Repo vẫn giữ [CSV gốc](data/raw/online_shoppers_intention.csv) và [tài liệu quy ước](reports/quy-uoc-thuc-nghiem-chung.md); **notebook và hai CSV đã xử lý chỉ ở Drive nhóm, chưa có trong repo**.

## Tài liệu trong repo

- [`IS403_CONTEXT.md`](IS403_CONTEXT.md): trạng thái và quyết định để tiếp tục ở chat mới.
- [`notes/de-tai-du-doan-mua-hang.md`](notes/de-tai-du-doan-mua-hang.md): mục tiêu đồ án, mức phù hợp với lời thầy và những điểm chưa chốt.
- [`notes/luu-y-giang-vien-ve-do-an.md`](notes/luu-y-giang-vien-ve-do-an.md): lời dặn của giảng viên do người dùng cung cấp, tách khỏi phần diễn giải của Codex.
- [`notes/huong-dan-do-an-is403.md`](notes/huong-dan-do-an-is403.md): hướng dẫn tổng quát và lịch sử các hướng từng khảo sát.
- [`reports/khao-sat-17-thuoc-tinh.md`](reports/khao-sat-17-thuoc-tinh.md): ý nghĩa và thống kê của 17 thuộc tính; quyết định 16 thuộc tính dùng trong so sánh chính.
- [`reports/quy-uoc-thuc-nghiem-chung.md`](reports/quy-uoc-thuc-nghiem-chung.md): phạm vi, 16 thuộc tính dùng, cách chia/chuẩn bị dữ liệu và bộ chỉ số chung cho mọi mô hình.
- [`lecture-notes/`](lecture-notes/): bản tóm tắt các chương học.
- `slides/`: PDF bài giảng giữ riêng trên máy, đã được `.gitignore` bỏ qua. Không giả định thư mục này có sẵn trên bản sao repo khác.

`README.md` này giới thiệu repo hiện tại. Khi hoàn thành quy trình mô hình hóa, nhóm sẽ bổ sung hướng dẫn cài đặt/chạy toàn bộ đồ án trong `README.txt` theo đề cương môn học.
