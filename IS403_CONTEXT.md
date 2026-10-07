# IS403 — Project Context

## Môn học

- **Mã môn:** IS403
- **Tên môn:** Phân tích dữ liệu kinh doanh (Data Analysis in Business)
- **Công cụ theo đề cương:** R hoặc Python; Anaconda, Jupyter Notebook/Google Colab và Microsoft Excel.

## Nội dung chính

1. Nhập môn phân tích dữ liệu và thống kê mô tả. Xem ghi chú: [`notes/chuong-01-tong-quan.md`](notes/chuong-01-tong-quan.md).
2. Phân tích diễn giải: ước lượng, kiểm định giả thuyết, ANOVA, Chi-square. Ghi chú tóm tắt: [Phần 1](notes/chuong-02-phan-tich-dien-giai-phan-1.md) và [Phần 2 – phân tích phương sai](notes/chuong-02-phan-tich-dien-giai-phan-2.md).
3. Hồi quy: đơn biến, đa biến và phi tuyến. Ghi chú tóm tắt: [`notes/chuong-03-phan-tich-hoi-quy.md`](notes/chuong-03-phan-tich-hoi-quy.md).
4. Hồi quy Logistic.
5. Dự báo chuỗi thời gian: ARIMA, ARIMAX, SARIMA, SARIMAX.
6. Học máy và bài toán dự báo: cây quyết định, SVM, RNN/LSTM/GRU, Isolation Forest.
7. Mô hình cấu trúc tuyến tính (SEM).

## Chương 0 — Giới thiệu môn học

### Mục tiêu môn học

- Hiểu và trình bày các khái niệm cơ bản của phân tích dữ liệu kinh doanh (PTDLKD).
- Nắm kiến thức và có thể lập trình mô phỏng các kỹ thuật/phương pháp phân tích dữ liệu và dự báo.
- Vận dụng thống kê mô tả trên nhiều loại dữ liệu kinh doanh; tìm hiểu, nghiên cứu, phân tích, áp dụng và đánh giá một giải pháp cho bài toán cụ thể.
- Làm việc nhóm hiệu quả.

### Kế hoạch nội dung theo buổi

| Buổi | Nội dung                                                         |
| ---- | ---------------------------------------------------------------- |
| 1    | Chương 1: Tổng quan bài toán phân tích dữ liệu và thống kê mô tả |
| 2–3  | Chương 2: Phân tích diễn giải dữ liệu                            |
| 4    | Chương 3: Phân tích hồi quy                                      |
| 5    | Chương 4: Hồi quy Logistic                                       |
| 6–7  | Chương 5: Mô hình dự báo theo chuỗi thời gian                    |
| 8–9  | Chương 6: Học máy và bài toán dự báo                             |
| 10   | Chương 7: Mô hình cấu trúc tuyến tính (SEM)                      |
| 11   | Ôn tập và trao đổi về đồ án                                      |

### Quy định và deliverables đồ án môn học

- Làm theo nhóm, **4–5 sinh viên/nhóm**.
- Mỗi nhóm chọn một vấn đề/chủ đề cần giải quyết, nêu rõ bộ dữ liệu và các thuật toán thuộc ML/DM dự kiến dùng.
- Đăng ký nhóm và đồ án trên Moodle **trước buổi học thứ 3**.
- Phần mô tả đề tài cần có:
    - vấn đề ngắn gọn; đầu vào, đầu ra, kiểu dữ liệu và ứng dụng kỳ vọng;
    - các thuật toán/công cụ dự kiến dùng;
    - bộ dữ liệu sử dụng.
- Báo cáo vào các buổi cuối; mọi thành viên phải có đóng góp và cùng báo cáo.
- Sản phẩm nộp/giao:
    - source code cùng `README.txt` hướng dẫn setup, compile và chạy;
    - báo cáo PDF theo dạng bài báo;
    - PowerPoint gồm: giới thiệu vấn đề/dataset, chi tiết phương pháp DL/ML, các kết quả đánh giá và phát hiện/kết luận, khó khăn–đề xuất–giải pháp;
    - thuyết trình và demo khoảng **15 phút**.
- Nếu dùng thư viện/package/source code có sẵn, phải khai báo trong báo cáo và slide.

### Tiêu chí đánh giá đồ án

- Mức độ khó và thách thức khi thực hiện.
- Sự phù hợp, chất lượng của phương pháp/giải pháp chọn.
- Tính chặt chẽ của thực nghiệm và đánh giá phương pháp/giải pháp.
- Chất lượng slide thuyết trình và file báo cáo.

### Công cụ và tài nguyên tham khảo

- Công cụ có thể dùng: Excel, Python, Anaconda, SPSS, R, scikit-learn, pandas, PyTorch, TensorFlow, Apache Spark.
- Dataset thực nghiệm: [Kaggle](https://www.kaggle.com/) và [UCI Machine Learning Repository](https://archive.ics.uci.edu/).
- Tài liệu:
    1. Nguyễn Đình Thuận, _Giáo trình Phân tích dữ liệu kinh doanh_, NXB ĐHQG-HCM, 2024.
    2. James R. Evans, _Business Analytics: Methods, Models, and Decisions_, 3rd ed., 2019.
    3. Aileen Nielsen, _Practical Time Series Analysis: Prediction with Statistics and Machine Learning_, 2020.
    4. Peter Bruce, Andrew Bruce, Peter Gedeck, _Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python_, 2020.

## Định hướng đồ án

- Đã chốt hướng vấn đề kinh doanh trung tâm: dùng dữ liệu giao dịch retail online để hỗ trợ tăng doanh thu qua quyết định về khách hàng, sản phẩm, bán kèm và kế hoạch bán hàng. Chưa chốt tên đề tài chính thức, dataset cuối cùng, roadmap phương pháp hoặc paper.
- Khi chốt đề tài cần bảo đảm phù hợp ML/DM, có dataset, mô tả input/output và ứng dụng rõ ràng; quy trình báo cáo phải bao gồm xác định vấn đề, khảo sát nghiên cứu liên quan, chọn phương pháp, thực nghiệm/đánh giá và kết luận.
- Hướng dẫn đầy đủ về mục tiêu, yêu cầu và quy trình đồ án: [`notes/huong-dan-do-an-is403.md`](notes/huong-dan-do-an-is403.md).
- Lưu ý giảng viên qua ghi âm và lời dặn trên lớp: kỳ vọng 8–10 phương pháp cho đồ án hoàn chỉnh; báo cáo **giới thiệu** tối đa 5 slide, chuẩn bị trong 2 tuần, với nội dung khác nhau tùy bài báo có/không đề xuất phương pháp mới. Xem [`notes/luu-y-giang-vien-ve-do-an.md`](notes/luu-y-giang-vien-ve-do-an.md); các yêu cầu này được ghi riêng với phần Codex diễn giải.
- Ý tưởng từng cân nhắc: một ứng dụng ghi chú học phần bằng JavaScript/TypeScript; hiện **chưa quyết định triển khai**.

## Quy ước làm việc với Codex

- Xem file này là nguồn context bền vững khi bắt đầu chat mới trong thư mục dự án.
- Khi người dùng nói “cập nhật context”, cập nhật ngắn gọn file này với quyết định, tiến độ, tài liệu/dataset và việc kế tiếp.
- Không tự tạo ứng dụng hoặc thay đổi mã nguồn trừ khi người dùng yêu cầu rõ.
- Thư mục `slides/` có PDF của ít nhất hai chương học để tham khảo. Khi cần lấy thông tin từ PDF: thử đọc/trích xuất theo cách phù hợp; nếu gặp khó khăn đáng kể thì **dừng ngay**, nói rõ phần không thể lấy được và gợi ý một hướng thay thế (ví dụ: người dùng gửi ảnh các trang cần thiết, bản văn bản/slide gốc, hoặc tóm tắt mục tiêu cần tìm). Không cố tiếp tục xử lý PDF lỗi/khó đọc.

## Trạng thái hiện tại

Đã đọc đề cương môn học qua ảnh. Đã lưu ghi chú tóm tắt Chương 1, Chương 2 Phần 1–2 và Chương 3 từ nội dung người dùng cung cấp. Đang khảo sát Online Retail II và xây vấn đề/câu hỏi nghiên cứu cho đồ án.
