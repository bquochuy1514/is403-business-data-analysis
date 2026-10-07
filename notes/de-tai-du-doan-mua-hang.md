# Đề tài hiện tại: dự đoán khả năng mua hàng từ phiên truy cập website

## Trạng thái và tên đề tài

**Tên nhóm chọn để đăng ký, chưa được giảng viên duyệt:**

> Dự đoán khả năng mua hàng từ dữ liệu phiên truy cập website thương mại điện tử: Đánh giá thực nghiệm các mô hình phân loại

Tên đề tài đặt **câu hỏi dự đoán** lên trước. Việc đánh giá, so sánh mô hình là cách kiểm chứng giải pháp, không phải mục tiêu kinh doanh tự thân. Không đưa “học sâu”, “thời gian thực”, “tăng doanh thu” hoặc tên thuật toán cụ thể vào tiêu đề khi nhóm chưa xác nhận sẽ làm được các phần đó.

## Bài toán và kết quả đồ án hướng tới [Quyết định của nhóm và diễn giải của Codex]

- **Đơn vị quan sát:** một phiên truy cập website, không phải toàn bộ lịch sử của một khách hàng.
- **Đầu vào dự kiến:** các thuộc tính mô tả phiên truy cập trong dataset. Dataset có 17 thuộc tính đầu vào; cần kiểm tra thuộc tính nào thật sự có sẵn tại thời điểm muốn dự đoán.
- **Đầu ra:** nhãn `Revenue` cho biết phiên có dẫn đến giao dịch mua hàng (`TRUE`) hay không (`FALSE`). Đây **không phải số tiền doanh thu**.
- **Mục tiêu cuối:** xây dựng một quy trình có thể lặp lại để dự đoán mua/không mua; đánh giá nhiều mô hình phân loại trên cùng bài toán, chọn mô hình phù hợp theo tiêu chí đã giải thích, chỉ ra điểm mạnh/yếu, giới hạn dữ liệu và đề xuất cải tiến.
- **Ý nghĩa kinh doanh tiềm năng:** giúp người vận hành website hiểu tín hiệu liên quan đến việc mua hàng và cân nhắc cách hỗ trợ quyết định trên website. Dataset và đánh giá mô hình **không tự chứng minh** rằng triển khai mô hình sẽ làm tăng tỷ lệ mua hoặc doanh thu; muốn kết luận điều đó cần thử nghiệm tác động thực tế.

Ví dụ để hiểu vì sao cần so sánh: dữ liệu có 10.422 phiên không mua và 1.908 phiên mua. Một mô hình luôn đoán “không mua” có thể đạt khoảng 84,5% accuracy mà bỏ sót mọi phiên mua. Vì vậy nhóm không thể chỉ nhìn một con số hoặc tuyên bố một mô hình “tốt nhất” khi chưa nêu rõ chỉ số và mục đích đánh giá.

## Dataset và paper [Nguồn đã xác minh]

- **Link dataset dùng trên sheet và slide:** [Online Shoppers Purchasing Intention Dataset — Kaggle](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset).
- **Nguồn gốc để ghi công/xác minh thuộc tính:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset). Bản CSV người dùng tải từ Kaggle và bản tải từ UCI giống hệt nhau từng byte (đã đối chiếu SHA-256 ngày 07/10/2026).
- **Paper tham khảo:** [*Modeling online customer purchase intention behavior applying different feature engineering and classification techniques*](https://link.springer.com/article/10.1007/s44163-023-00086-0), Md. Shahriare Satu và Syed Faridul Islam, *Discover Artificial Intelligence*, 2023. Paper nghiên cứu cùng bài toán trên dataset này và thực nghiệm nhiều kỹ thuật xử lý dữ liệu/mô hình phân loại. Nhóm tham khảo cách làm và kết quả; **không cam kết tái lập nguyên quy trình tác giả**.

## Phù hợp với yêu cầu môn học thế nào?

### Những điều giảng viên đã dặn [Lời thầy do người dùng cung cấp]

Theo [`luu-y-giang-vien-ve-do-an.md`](luu-y-giang-vien-ve-do-an.md): buổi giới thiệu có tối đa **5 slide**, mở đầu bằng thành viên và tên đề tài; có thể ghi tên đề tài, link paper, link dataset vào sheet để thầy kiểm tra. Với hướng so sánh phương pháp có sẵn, cần nêu rõ bài toán, dataset, các thuộc tính, input/output và tên các thuật toán **dự kiến**, chưa cần chạy xong thực nghiệm trong buổi giới thiệu. Về đồ án hoàn chỉnh, thầy khuyến khích tìm hiểu thêm phương pháp chưa học trên lớp, cố gắng khoảng **8–10 phương pháp**, giải thích vì sao kết quả khác nhau và đề xuất cải tiến. Con số 8–10 là mức thầy nói nên cố gắng/ước lượng, chưa có xác nhận đó là số lượng bắt buộc hoặc cách tính các bước tiền xử lý vào số phương pháp.

### Cách nhóm chọn thực hiện [Quyết định của nhóm, chưa phải phê duyệt của thầy]

Nhóm chọn **thực nghiệm và so sánh các phương pháp phân loại đã tồn tại**, gồm phương pháp trong môn học khi phù hợp và phương pháp cần tự học thêm. “Mới” đối với người học không đồng nghĩa với “thuật toán mới do tác giả paper phát minh”. Nhóm không tuyên bố tái lập phương pháp mới của paper. Vì vậy, yêu cầu tìm thêm dataset thứ hai dành cho nhánh làm theo phương pháp mới của paper **chưa được xem là yêu cầu mặc định cho hướng nhóm chọn**; thầy vẫn là người kiểm tra và duyệt cách phân loại này.

Các phương pháp mô tả/trực quan hóa, kiểm định và tiền xử lý có thể hỗ trợ bài toán, nhưng không tự động tính chúng thành đủ số mô hình phân loại. Không cần áp dụng tất cả các chương học nếu chúng giải bài toán khác (ví dụ dự báo chuỗi thời gian hay dự đoán một giá trị liên tục).

## Buổi giới thiệu và công việc sau đó [Đề xuất của Codex]

Một cách chia **5 slide**: (1) thành viên và tên đề tài; (2) vấn đề/mục tiêu; (3) dataset và input/output; (4) paper và hướng thực nghiệm của nhóm; (5) các phương pháp dự kiến cùng kế hoạch đánh giá. Đây là bố cục đề xuất, không phải mẫu slide bắt buộc của thầy.

Sau buổi giới thiệu: tìm hiểu và kiểm tra dữ liệu; xác định thời điểm dự đoán để tránh dùng thông tin chưa có hoặc rò rỉ nhãn; chuẩn bị và chia dữ liệu; thử các phương pháp phù hợp trong cùng điều kiện; đánh giá bằng chỉ số phù hợp với dữ liệu mất cân bằng; giải thích khác biệt, giới hạn và đề xuất cải tiến; hoàn thiện source code, hướng dẫn chạy, báo cáo, slide cuối và demo.

## Chưa chốt / không được nói là đã hoàn thành

- Thầy **chưa duyệt** tên đề tài, nhánh thực hiện hay paper/dataset trên sheet.
- Chưa chốt danh sách 8–10 phương pháp, cấu hình, cách chia dữ liệu và chỉ số đánh giá cuối cùng.
- Chưa xác định thời điểm dự đoán hoặc quyết định giữ/bỏ các thuộc tính có nguy cơ không sẵn có tại thời điểm đó, đặc biệt `PageValues`.
- Chưa chạy mô hình, chưa có kết quả so sánh, mô hình được chọn hay chứng cứ về tác động kinh doanh thực tế.
