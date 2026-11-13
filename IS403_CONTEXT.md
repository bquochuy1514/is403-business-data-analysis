# IS403 — Project Context

## Môn học

- **Mã môn:** IS403
- **Tên môn:** Phân tích dữ liệu kinh doanh (Data Analysis in Business)
- **Công cụ theo đề cương:** R hoặc Python; Anaconda, Jupyter Notebook/Google Colab và Microsoft Excel.

## Nội dung chính

1. Nhập môn phân tích dữ liệu và thống kê mô tả. Xem ghi chú: [`lecture-notes/chuong-01-tong-quan.md`](lecture-notes/chuong-01-tong-quan.md).
2. Phân tích diễn giải: ước lượng, kiểm định giả thuyết, ANOVA, Chi-square. Ghi chú tóm tắt: [Phần 1](lecture-notes/chuong-02-phan-tich-dien-giai-phan-1.md) và [Phần 2 – phân tích phương sai](lecture-notes/chuong-02-phan-tich-dien-giai-phan-2.md).
3. Hồi quy: đơn biến, đa biến và phi tuyến. Ghi chú tóm tắt: [`lecture-notes/chuong-03-phan-tich-hoi-quy.md`](lecture-notes/chuong-03-phan-tich-hoi-quy.md).
4. Hồi quy Logistic. Ghi chú tóm tắt: [`lecture-notes/chuong-04-hoi-quy-logistic.md`](lecture-notes/chuong-04-hoi-quy-logistic.md).
5. Dự báo chuỗi thời gian: ARIMA, ARIMAX, SARIMA, SARIMAX. Ghi chú hiện có mới gồm phần [đơn biến/đa biến](lecture-notes/chuong-05-du-bao-chuoi-thoi-gian.md) từ bản chuyển giọng nói.
6. Học máy và bài toán dự báo: cây quyết định, SVM, RNN/LSTM/GRU, Isolation Forest. Đã có [ghi chú Chương 6 Phần 1](lecture-notes/chuong-06-hoc-may-va-du-bao-phan-1.md) từ bản tóm tắt slide do người dùng cung cấp; phần này tập trung ML/DL cho chuỗi thời gian, SVM và SVR.
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

- **Đề tài đã được giảng viên duyệt sau buổi giới thiệu 5 slide:** Dự đoán khả năng mua hàng từ dữ liệu phiên truy cập website thương mại điện tử: Đánh giá thực nghiệm các mô hình phân loại. Bài toán phân loại nhị phân: từ các thuộc tính của một phiên truy cập, dự đoán phiên đó có dẫn đến mua hàng (`Revenue`) hay không. So sánh mô hình là cách kiểm chứng giải pháp, không phải mục tiêu kinh doanh tự thân.
- **Link dataset dùng để đăng ký/giới thiệu:** [Online Shoppers Purchasing Intention Dataset trên Kaggle](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset). Đây là bản đăng lại của [bộ dữ liệu gốc trên UCI](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset); khi nói về xuất xứ vẫn ghi UCI. File CSV người dùng tải từ Kaggle và file CSV tải từ UCI đã được đối chiếu ngày 07/10/2026: cùng 1.072.063 byte, SHA-256 giống hệt (`B3055EE355F59134D851D32641183CB4A8B45DEF7124D2F50442A042F358E0D9`).
- **Paper tham khảo đã chọn:** [Modeling online customer purchase intention behavior applying different feature engineering and classification techniques](https://link.springer.com/article/10.1007/s44163-023-00086-0). Nhóm chọn hướng tự thực nghiệm, so sánh các phương pháp phân loại đã có; dùng paper để tham khảo, không nhận tái lập nguyên quy trình tác giả đề xuất.
- **Đích đến của đồ án:** xây dựng và đánh giá một quy trình dự đoán mua/không mua; so sánh công bằng các mô hình phù hợp, giải thích kết quả, nêu giới hạn và đề xuất cải tiến. Lần so sánh chính là **phân loại offline trên bản ghi phiên tổng hợp**, dùng 16 thuộc tính (**không dùng `PageValues` trong lần so sánh chính**), cùng dữ liệu học/kiểm tra và các chỉ số Accuracy/Precision/Recall/F1 với lớp mua là dương; không tuyên bố thời gian thực. Đây là quyết định của nhóm, không phải chi tiết đã được thầy duyệt. Tám mô hình đã được phân công nhưng cấu hình và kết quả chưa có. Không khẳng định dataset tự chứng minh có thể tăng doanh thu. Xem [`reports/quy-uoc-thuc-nghiem-chung.md`](reports/quy-uoc-thuc-nghiem-chung.md).
- **Việc thầy giao sau khi duyệt:** khảo sát kỹ **17 thuộc tính đầu vào** của dataset trước khi triển khai. N01 đã có bản khảo sát 17 thuộc tính trên Drive nhóm và [bản ghi trong repo](reports/khao-sat-17-thuoc-tinh.md); N02 chốt dùng 16 thuộc tính, không dùng `PageValues` trong so sánh chính vì chưa rõ cách tính/thời điểm có giá trị. **Chưa kết luận cột này chắc chắn rò rỉ nhãn.** Người dùng suy đoán thầy có thể lo một số thuộc tính không liên quan hoặc không phù hợp; **đó là suy đoán của người dùng, không phải lời thầy**.
- Olist, Online Retail II và hướng dự báo lượng bán là **lịch sử khảo sát**, không phải đề tài hiện tại.
- Khi chốt đề tài cần bảo đảm phù hợp ML/DM, có dataset, mô tả input/output và ứng dụng rõ ràng; quy trình báo cáo phải bao gồm xác định vấn đề, khảo sát nghiên cứu liên quan, chọn phương pháp, thực nghiệm/đánh giá và kết luận.
- Hướng dẫn đầy đủ về mục tiêu, yêu cầu và quy trình đồ án: [`notes/huong-dan-do-an-is403.md`](notes/huong-dan-do-an-is403.md).
- Lưu ý giảng viên qua ghi âm, lời dặn trên lớp và ghi chú bạn học: mốc **8–10 phương pháp là thông tin mới**; **buổi 5** gửi slide giới thiệu tối đa 5 slide; source code và file báo cáo nộp trước buổi báo cáo 2 ngày (chưa rõ buổi nào). **Người dùng xác nhận hai loại đồ án thầy nói:** paper đề xuất phương pháp mới hoặc paper chỉ so sánh phương pháp có sẵn. Ghi chú bạn học còn có hai câu “đọc bài báo trước / tìm dataset trước rồi thực nghiệm”; gọi chúng là cách bắt đầu (paper-first/data-first) là **diễn giải của Codex**, chưa được xác nhận là cách thầy phân loại đồ án. Xem [`notes/luu-y-giang-vien-ve-do-an.md`](notes/luu-y-giang-vien-ve-do-an.md).
- **Ghi âm bổ sung do người dùng chuyển:** buổi seminar cuối dự kiến khoảng **15 phút trình bày + 5–10 phút hỏi đáp**; báo cáo dạng bài báo khoa học khoảng **12–15 trang**, có tóm tắt, giới thiệu, nghiên cứu liên quan, phương pháp, thực nghiệm/đánh giá, kết luận/hướng phát triển. Mô hình đã học trên lớp cần nói rõ tham số và cách cài đặt; mô hình mới/tự tìm hiểu cần thêm lý thuyết tổng quan và cơ chế. Kết quả phải có bảng/biểu đồ và giải thích khác biệt. Thầy dự kiến đưa mẫu Overleaf (Word/LaTeX), cho phép báo cáo tiếng Việt. Báo cáo dự kiến tuần 10–11, **hạn nộp còn được cân đối, chưa chốt**. Ghi âm còn có góp ý cho các nhóm khác và bài giảng về chuỗi thời gian; không tự áp các yêu cầu riêng đó cho đề tài nhóm mình. Chi tiết và lưu ý kỹ thuật: [`notes/luu-y-giang-vien-ve-do-an.md`](notes/luu-y-giang-vien-ve-do-an.md).
- Ý tưởng từng cân nhắc: một ứng dụng ghi chú học phần bằng JavaScript/TypeScript; hiện **chưa quyết định triển khai**.

## Quy ước làm việc với Codex

- Xem file này là nguồn context bền vững khi bắt đầu chat mới trong thư mục dự án.
- Khi người dùng nói “cập nhật context”, cập nhật ngắn gọn file này với quyết định, tiến độ, tài liệu/dataset và việc kế tiếp.
- Không tự tạo ứng dụng hoặc thay đổi mã nguồn trừ khi người dùng yêu cầu rõ.
- `lecture-notes/` chứa ghi chú tóm tắt các chương; `notes/` chứa ghi chú về đề tài, hướng dẫn và lời dặn của giảng viên.
- Thư mục `slides/` chứa PDF bài giảng chỉ lưu cục bộ và được Git bỏ qua; không giả định các file này có sẵn trên máy khác. Khi cần lấy thông tin từ PDF: thử đọc/trích xuất theo cách phù hợp; nếu gặp khó khăn đáng kể thì **dừng ngay**, nói rõ phần không thể lấy được và gợi ý một hướng thay thế (ví dụ: người dùng gửi ảnh các trang cần thiết, bản văn bản/slide gốc, hoặc tóm tắt mục tiêu cần tìm). Không cố tiếp tục xử lý PDF lỗi/khó đọc.

## Trạng thái hiện tại

- **Đề tài và phạm vi:** Buổi giới thiệu 5 slide đã xong; thầy đã duyệt đề tài. N01 khảo sát đủ 17 thuộc tính. N02 chốt phân loại offline trên bản ghi phiên tổng hợp, dùng 16 thuộc tính và không dùng `PageValues` trong so sánh chính. Đây là quyết định của nhóm, không phải chi tiết thầy đã duyệt.
- **N03 đã chạy trên Colab:** Đọc 12.330 phiên, giữ 125 dòng trùng; không có nhóm cùng 16 đầu vào nhưng khác nhãn. Chia theo nhóm với `test_size=0.2`, `random_state=42` và tỷ lệ nhãn gần nhau: 9.861 phiên học (15,48% mua), 2.469 phiên kiểm tra (15,47% mua). Chuẩn hóa 9 cột số, one-hot 7 cột nhóm chỉ học từ phần học, tạo 73 cột đầu vào mỗi phía. Hai CSV chung có 74 cột kể cả `Revenue`. Hàm `danh_gia` trả Accuracy/Precision/Recall/F1 và TP/TN/FP/FN cho lớp mua (`1`). Mốc luôn đoán không mua trên phần kiểm tra: Accuracy 0,8453; TP=0, TN=2.087, FP=0, FN=382. Colab in pandas 2.2.3 và scikit-learn 1.6.1.
- **Nơi lưu và cách chia sẻ:** Notebook `IS403 | Chuẩn bị dữ liệu và đánh giá chung.ipynb` và hai file `is403_train_chung.csv`, `is403_test_chung.csv` nằm tại Drive nhóm → `Dữ liệu và quy ước`; **chưa được chép vào repo**. `csv_path` trong notebook trỏ MyDrive của Huy, không tự đúng trên tài khoản khác; ô `to_csv` có thể ghi đè file chung. Thành viên chỉ đọc notebook chuẩn, tự lấy đường dẫn hai CSV trong Colab của mình rồi làm notebook mô hình riêng tại Drive nhóm → `Thực nghiệm`. Sheet `Phân công` và bản thảo báo cáo ở Drive nhóm; Drive là nơi làm việc chung, repo lưu ghi chú và CSV gốc.
- **Phân công mô hình:** Huy Logistic Regression; Quang Naive Bayes và KNN; Duy Decision Tree và Random Forest; Trang SVM; Việt Anh AdaBoost; Phú Gradient Boosting. Chưa có kết quả của tám mô hình, bảng so sánh, báo cáo hoàn chỉnh hoặc slide cuối.
- **Cần xác minh:** Hướng dẫn Markdown để đặt ở đầu notebook đã được soạn, nhưng chưa xác minh người dùng đã dán, đã chạy lại toàn bộ notebook từ đầu sau lần chỉnh cuối, quyền xem Drive đã đúng hoặc cột quyết định trong Sheet N01 đã cập nhật. Template báo cáo và hạn nộp cuối chưa được xác nhận.
- **Tài liệu và sở thích làm việc:** Đã lưu ghi chú Chương 1–4, một phần Chương 5 và Chương 6 Phần 1 từ nội dung người dùng cung cấp; chưa đối chiếu đầy đủ slide gốc. Lời thầy về seminar/báo cáo cuối ở [`notes/luu-y-giang-vien-ve-do-an.md`](notes/luu-y-giang-vien-ve-do-an.md). Theo yêu cầu người dùng, không tự tạo lại `.py`, `src/` hoặc `tests/`; giải thích từng bước trước khi bổ sung code.
