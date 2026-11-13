# Đề tài hiện tại: dự đoán khả năng mua hàng từ phiên truy cập website

## Trạng thái và tên đề tài

**Tên đề tài đã được giảng viên duyệt sau buổi giới thiệu 5 slide:**

> Dự đoán khả năng mua hàng từ dữ liệu phiên truy cập website thương mại điện tử: Đánh giá thực nghiệm các mô hình phân loại

Tên đề tài đặt **câu hỏi dự đoán** lên trước. Việc đánh giá, so sánh mô hình là cách kiểm chứng giải pháp, không phải mục tiêu kinh doanh tự thân. Không đưa “học sâu”, “thời gian thực”, “tăng doanh thu” hoặc tên thuật toán cụ thể vào tiêu đề khi nhóm chưa xác nhận sẽ làm được các phần đó.

## Bài toán và kết quả đồ án hướng tới [Quyết định của nhóm và diễn giải của Codex]

- **Đơn vị quan sát:** một phiên truy cập website, không phải toàn bộ lịch sử của một khách hàng.
- **Đầu vào:** dataset có 17 thuộc tính đầu vào và thầy yêu cầu khảo sát kỹ cả 17. Nhóm đã chọn **16 thuộc tính cho so sánh chính**, **không dùng `PageValues` trong lần so sánh này** vì chưa rõ thời điểm/cách tính; xem [quy ước thực nghiệm](../reports/quy-uoc-thuc-nghiem-chung.md). Đây không phải kết luận cột này chắc chắn rò rỉ nhãn.
- **Đầu ra:** nhãn `Revenue` cho biết phiên có dẫn đến giao dịch mua hàng (`TRUE`) hay không (`FALSE`). Đây **không phải số tiền doanh thu**.
- **Mục tiêu cuối:** xây dựng một quy trình có thể lặp lại để dự đoán mua/không mua; đánh giá nhiều mô hình phân loại trên cùng bài toán, chọn mô hình phù hợp theo tiêu chí đã giải thích, chỉ ra điểm mạnh/yếu, giới hạn dữ liệu và đề xuất cải tiến.
- **Ý nghĩa kinh doanh tiềm năng:** giúp người vận hành website hiểu tín hiệu liên quan đến việc mua hàng và cân nhắc cách hỗ trợ quyết định trên website. Dataset và đánh giá mô hình **không tự chứng minh** rằng triển khai mô hình sẽ làm tăng tỷ lệ mua hoặc doanh thu; muốn kết luận điều đó cần thử nghiệm tác động thực tế.

Ví dụ để hiểu vì sao cần so sánh: dữ liệu có 10.422 phiên không mua và 1.908 phiên mua. Một mô hình luôn đoán “không mua” có thể đạt khoảng 84,5% accuracy mà bỏ sót mọi phiên mua. Vì vậy nhóm không thể chỉ nhìn một con số hoặc tuyên bố một mô hình “tốt nhất” khi chưa nêu rõ chỉ số và mục đích đánh giá.

## Dataset và paper [Nguồn đã xác minh]

- **Link dataset dùng trên sheet và slide:** [Online Shoppers Purchasing Intention Dataset — Kaggle](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset).
- **Nguồn gốc để ghi công/xác minh thuộc tính:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset). Bản CSV người dùng tải từ Kaggle và bản tải từ UCI giống hệt nhau từng byte (đã đối chiếu SHA-256 ngày 07/10/2026).
- **Paper tham khảo:** [_Modeling online customer purchase intention behavior applying different feature engineering and classification techniques_](https://link.springer.com/article/10.1007/s44163-023-00086-0), Md. Shahriare Satu và Syed Faridul Islam, _Discover Artificial Intelligence_, 2023. Paper nghiên cứu cùng bài toán trên dataset này và thực nghiệm nhiều kỹ thuật xử lý dữ liệu/mô hình phân loại. Nhóm tham khảo cách làm và kết quả; **không cam kết tái lập nguyên quy trình tác giả**.

## Phù hợp với yêu cầu môn học thế nào?

### Những điều giảng viên đã dặn [Lời thầy do người dùng cung cấp]

Theo [`luu-y-giang-vien-ve-do-an.md`](luu-y-giang-vien-ve-do-an.md): buổi giới thiệu có tối đa **5 slide**, mở đầu bằng thành viên và tên đề tài; có thể ghi tên đề tài, link paper, link dataset vào sheet để thầy kiểm tra. Với hướng so sánh phương pháp có sẵn, cần nêu rõ bài toán, dataset, các thuộc tính, input/output và tên các thuật toán **dự kiến**, chưa cần chạy xong thực nghiệm trong buổi giới thiệu. Về đồ án hoàn chỉnh, thầy khuyến khích tìm hiểu thêm phương pháp chưa học trên lớp, cố gắng khoảng **8–10 phương pháp**, giải thích vì sao kết quả khác nhau và đề xuất cải tiến. Con số 8–10 là mức thầy nói nên cố gắng/ước lượng, chưa có xác nhận đó là số lượng bắt buộc hoặc cách tính các bước tiền xử lý vào số phương pháp.

### Cách nhóm chọn thực hiện [Đề tài đã được duyệt; quy ước so sánh chính đã triển khai]

Nhóm chọn **thực nghiệm và so sánh các phương pháp phân loại đã tồn tại**, gồm phương pháp trong môn học khi phù hợp và phương pháp cần tự học thêm. “Mới” đối với người học không đồng nghĩa với “thuật toán mới do tác giả paper phát minh”. Nhóm không tuyên bố tái lập phương pháp mới của paper. Vì vậy, yêu cầu tìm thêm dataset thứ hai dành cho nhánh làm theo phương pháp mới của paper **chưa được xem là yêu cầu mặc định cho hướng nhóm chọn**. Thầy đã duyệt đề tài; chưa có thông tin riêng về việc thầy duyệt từng chi tiết thiết kế thực nghiệm.

Các phương pháp mô tả/trực quan hóa, kiểm định và tiền xử lý có thể hỗ trợ bài toán, nhưng không tự động tính chúng thành đủ số mô hình phân loại. Không cần áp dụng tất cả các chương học nếu chúng giải bài toán khác (ví dụ dự báo chuỗi thời gian hay dự đoán một giá trị liên tục).

## Sau buổi giới thiệu [Tiến độ và đề xuất của Codex]

Buổi giới thiệu 5 slide đã hoàn thành và đề tài được thầy duyệt. Thầy yêu cầu khảo sát kỹ 17 thuộc tính đầu vào. Đã có [bản khảo sát ban đầu](../reports/khao-sat-17-thuoc-tinh.md) dựa trên CSV gốc và mô tả của UCI; nhóm đã ghi quyết định cho so sánh chính trong [quy ước thực nghiệm](../reports/quy-uoc-thuc-nghiem-chung.md). Người dùng suy đoán thầy có thể lo một số thuộc tính không liên quan hoặc không đúng; **đây là suy đoán của người dùng, không phải lý do thầy đã nêu**.

Phạm vi đã chọn cho lần so sánh chính là **phân loại offline trên bản ghi phiên tổng hợp**, không tuyên bố dự đoán thời gian thực. N01 khảo sát 17 thuộc tính, N02 chọn 16 đầu vào và N03 đã chạy trên Colab: chia 9.861 phiên học/2.469 phiên kiểm tra, chuẩn bị 73 cột đầu vào và lưu `is403_train_chung.csv`, `is403_test_chung.csv` tại Drive nhóm `Dữ liệu và quy ước`. Notebook `IS403 | Chuẩn bị dữ liệu và đánh giá chung.ipynb` chứa code và hàm đánh giá; **notebook/CSV xử lý chưa được chép vào repo**. Việc tiếp theo là để từng thành viên làm notebook mô hình riêng trong Drive `Thực nghiệm`, kiểm tra kết quả, tổng hợp và giải thích sự khác biệt, giới hạn, cải tiến rồi hoàn thiện báo cáo/slide cuối.

### Bổ sung từ ghi âm về buổi báo cáo cuối [Lời thầy qua bản chuyển giọng nói/tóm tắt]

- Seminar dự kiến **15 phút trình bày và 5–10 phút hỏi đáp**. Nếu dùng mô hình đã học trên lớp, nhóm cần nói rõ tham số/cách cài đặt; nếu dùng mô hình mới tự tìm hiểu (thầy nêu Random Forest làm ví dụ), cần trình bày thêm ý tưởng và cơ chế. Đây là yêu cầu cho **báo cáo cuối**, không phải yêu cầu thêm cho 5 slide giới thiệu đã nộp.
- Bài báo cáo dạng bài báo khoa học khoảng **12–15 trang**, có tóm tắt, giới thiệu nêu rõ input/output, nghiên cứu liên quan, phương pháp, thực nghiệm/đánh giá và kết luận/hướng phát triển. Với bài toán phân loại của nhóm, bản tóm tắt nêu Accuracy, Precision, Recall, F1 làm ví dụ; nhóm đã chọn bốn chỉ số này cho lần so sánh chính. Cần trình bày bảng/biểu đồ kết quả và lý giải khác biệt, không chỉ xếp hạng mô hình.
- Bài báo cáo có thể viết bằng **tiếng Việt**; thầy dự định cung cấp template trên Overleaf với lựa chọn Word/LaTeX, nhưng **chưa có link mẫu** trong thông tin người dùng gửi. Lịch báo cáo **dự kiến** tuần 10–11 và hạn nộp vẫn đang được cân đối.
- Trong góp ý cho nhóm dự đoán churn, thầy nhắc kiểm tra **tỷ lệ hai nhãn** và rà soát phương pháp nếu kết quả cao bất thường so với paper. Đây là lời góp ý cho nhóm khác; với dữ liệu mua/không mua của nhóm mình, kiểm tra mất cân bằng nhãn cũng là việc **Codex đề xuất** dựa trên đặc điểm dataset, không phải chỉ thị riêng thầy đưa cho nhóm này.

Các chi tiết khác trong ghi âm (dự báo cổ phiếu, chuỗi thời gian, ARIMA, SVR, kiến trúc mạng nơ-ron) xem [`luu-y-giang-vien-ve-do-an.md`](luu-y-giang-vien-ve-do-an.md); không tự thêm những mô hình hoặc bài toán đó vào đề tài hiện tại.

## Chưa chốt / không được nói là đã hoàn thành

- Đề tài đã được thầy duyệt; chưa có thông tin xác nhận thầy đã duyệt riêng từng thuật toán, cách xử lý thuộc tính hoặc thiết kế thực nghiệm.
- Tám mô hình đã được phân công (Logistic Regression, Naive Bayes, KNN, Decision Tree, Random Forest, SVM, AdaBoost, Gradient Boosting), nhưng cấu hình từng mô hình và việc có bổ sung mô hình/thí nghiệm phụ chưa chốt. Cách chia, biểu diễn dữ liệu và bốn chỉ số chung cho **lần so sánh chính** đã được triển khai.
- Chưa có dữ liệu theo từng thời điểm trong phiên để chứng minh khả năng dự đoán khi khách đang truy cập. `PageValues` **không dùng trong so sánh chính**; chưa được xác định là chắc chắn rò rỉ nhãn.
- Chưa chạy mô hình, chưa có kết quả so sánh, mô hình được chọn hay chứng cứ về tác động kinh doanh thực tế.
