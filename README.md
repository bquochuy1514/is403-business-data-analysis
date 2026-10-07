# IS403 — Phân tích dữ liệu kinh doanh

Repo lưu ghi chú môn học và chuẩn bị đồ án. **Đề tài đang được nhóm chọn để đăng ký, chưa được giảng viên duyệt:**

> Dự đoán khả năng mua hàng từ dữ liệu phiên truy cập website thương mại điện tử: Đánh giá thực nghiệm các mô hình phân loại

## Bài toán

Từ các thuộc tính mô tả một phiên truy cập website, dự đoán phiên đó có dẫn đến giao dịch mua hàng hay không. Nhãn cần dự đoán là `Revenue` (`TRUE`/`FALSE`), **không phải số tiền doanh thu**. Nhóm dự kiến thử và đánh giá các phương pháp phân loại đã tồn tại, giải thích sự khác biệt giữa kết quả, nêu giới hạn và đề xuất cải tiến. Danh sách mô hình và thiết kế thực nghiệm chưa chốt; chưa có kết quả để khẳng định mô hình nào tốt nhất hoặc tác động đến doanh thu.

- **Dataset dùng để đăng ký:** [Online Shoppers Purchasing Intention trên Kaggle](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset). [UCI](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset) là nguồn gốc của bộ dữ liệu.
- **Paper tham khảo:** [*Modeling online customer purchase intention behavior applying different feature engineering and classification techniques*](https://link.springer.com/article/10.1007/s44163-023-00086-0). Nhóm không cam kết tái lập nguyên quy trình của paper.

## Tình trạng hiện tại

Ưu tiên trước mắt là thống nhất đề tài với nhóm, điền tên đề tài cùng link paper/dataset vào sheet cho giảng viên kiểm tra, rồi chuẩn bị phần giới thiệu **tối đa 5 slide**. Chưa có mã nguồn hoặc thực nghiệm trong repo. Các thư mục `data/`, `notebooks/`, `src/` và `reports/` trong [cấu trúc đề xuất](notes/huong-dan-do-an-is403.md) sẽ chỉ được tạo khi có nội dung thực tế.

## Tài liệu trong repo

- [`IS403_CONTEXT.md`](IS403_CONTEXT.md): trạng thái và quyết định để tiếp tục ở chat mới.
- [`notes/de-tai-du-doan-mua-hang.md`](notes/de-tai-du-doan-mua-hang.md): mục tiêu đồ án, mức phù hợp với lời thầy và những điểm chưa chốt.
- [`notes/luu-y-giang-vien-ve-do-an.md`](notes/luu-y-giang-vien-ve-do-an.md): lời dặn của giảng viên do người dùng cung cấp, tách khỏi phần diễn giải của Codex.
- [`notes/huong-dan-do-an-is403.md`](notes/huong-dan-do-an-is403.md): hướng dẫn tổng quát và lịch sử các hướng từng khảo sát.
- [`lecture-notes/`](lecture-notes/): bản tóm tắt các chương học.
- `slides/`: PDF bài giảng giữ riêng trên máy, đã được `.gitignore` bỏ qua. Không giả định thư mục này có sẵn trên bản sao repo khác.

`README.md` này giới thiệu repo hiện tại. Khi có source code để nộp, nhóm sẽ bổ sung hướng dẫn cài đặt/chạy cụ thể trong `README.txt` theo đề cương môn học.
