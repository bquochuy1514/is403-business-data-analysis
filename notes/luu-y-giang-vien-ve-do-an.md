# Lưu ý của giảng viên về đồ án IS403

## Nguồn thông tin

- Nguồn thứ nhất: nội dung người dùng cung cấp, được trích xuất từ bản ghi âm lời dặn của giảng viên.
- Nguồn thứ hai: lời giảng viên trong buổi học mới, do người dùng thuật lại. Phần này được ghi riêng bên dưới, không phải đề xuất của Codex.
- Nguồn thứ ba: người dùng chuyển bản văn bản được tạo từ các đoạn ghi âm buổi học tiếp theo. Hai tệp đính kèm được gửi lần này có nội dung giống hệt nhau. Các mục **“Ghi âm bổ sung”** bên dưới ghi lại ý trong bản chuyển giọng nói/tóm tắt, không phải bản chép nguyên văn từng câu của thầy.
- Đây là yêu cầu/định hướng được nghe từ lớp, **không thay thế đề cương môn học bằng văn bản**. Khi có điểm mâu thuẫn hoặc chưa rõ, cần hỏi lại giảng viên.

## Cập nhật sau buổi giới thiệu đồ án [Người dùng thuật lại]

- Nhóm đã hoàn thành buổi giới thiệu 5 slide; **giảng viên đã duyệt đề tài** dự đoán khả năng mua hàng từ phiên truy cập website và nhóm có thể bắt đầu thực hiện.
- Giảng viên yêu cầu **khảo sát kỹ 17 thuộc tính đầu vào** của dataset trước khi làm. Người dùng suy đoán thầy có thể lo về mức liên quan hoặc tính đúng đắn của một số thuộc tính; đây **không phải lý do do giảng viên nêu**.

## Ghi âm bổ sung: góp ý đề tài của các nhóm khác [Lời thầy qua bản chuyển giọng nói/tóm tắt]

> Đây là góp ý cho **từng nhóm được nêu**, không tự động trở thành yêu cầu về dataset hoặc mô hình của nhóm dự đoán mua hàng.

- **Nhóm dự báo giá cổ phiếu:** mục tiêu là dự báo giá đóng cửa hằng ngày. Thầy gợi ý có thể đối chiếu bộ dữ liệu trong paper với dữ liệu giá mới thu thập; cần làm rõ các biến đầu vào (giá mở/đóng/cao/thấp, khối lượng và các chỉ số tự tính như RSI, MACD, MA). Các phương pháp được nêu gồm ARIMA, Ridge Regression, LightGBM, LSTM, Transformer và tổ hợp bằng trung bình có trọng số; nếu dùng cách tổ hợp này phải hiểu công thức và cách xác định trọng số.
- **Nhóm 3 — hành vi tiêu dùng siêu thị:** dữ liệu được giới thiệu khoảng 1,2 triệu dòng, 12 thuộc tính, với đầu ra dự kiến là quy mô giỏ hàng và chỉ số tiêu dùng. Nhóm nêu Apriori (luật kết hợp), K-Means (phân cụm), lọc cộng tác (gợi ý) và ARIMA (chuỗi thời gian). Thầy nhận xét như vậy ôm nhiều bài toán độc lập, khối lượng nặng và thiên về Khai phá dữ liệu; gợi ý tập trung hơn vào bài toán chuỗi thời gian nếu tiếp tục, còn làm tất cả thì phải hiểu rõ từng thuật toán.
- **Nhóm 4 — dự đoán khách hàng rời bỏ dịch vụ:** đây là bài toán phân lớp hai nhãn; nhóm trình bày dataset khoảng 12,5 GB, khoảng 22.000 khách hàng và mô hình lai LSTM–GRU–LightGBM/ensemble. Thầy nhắc kiểm tra tỷ lệ hai nhãn; kết quả thực nghiệm thấp hơn paper có thể bình thường nếu dữ liệu khác, còn cao hơn bất thường thì nên rà soát phương pháp.
- **Nhóm 5 — dự báo lượng hàng qua cảng:** mục tiêu là dự báo tổng tấn hàng của từng cảng trong 7 ngày tiếp theo, từ dữ liệu theo địa điểm kể từ năm 2019. Thầy yêu cầu thống kê rõ số dòng dữ liệu của từng cảng để đánh giá độ tin cậy của bài toán chuỗi thời gian.

## Ghi âm bổ sung: bài giảng về dự báo chuỗi thời gian [Lời thầy qua bản chuyển giọng nói/tóm tắt]

- **Đơn biến:** dự báo biến mục tiêu từ lịch sử của chính biến đó, ví dụ dùng mức tiêu thụ điện các ngày trước để dự báo ngày tiếp theo.
- **Đa biến:** dùng lịch sử biến mục tiêu cùng các chuỗi biến phụ trợ tương ứng về thời gian, ví dụ thêm nhiệt độ/độ ẩm khi dự báo điện năng, hoặc giá mở/cao/thấp và khối lượng khi dự báo giá cổ phiếu.
- Theo bản tóm tắt, thầy nhận xét mô hình đa biến *có thể* tận dụng thêm thông tin bối cảnh và nhắc các nhóm phải nói rõ đang chạy đơn biến, đa biến hay đối sánh cả hai; nếu dùng đa biến, cần chỉ ra cụ thể các biến phụ trợ.

**Lưu ý phương pháp của Codex:** nội dung này nói về **dự báo chuỗi thời gian**. Không gọi bài toán phân loại từng phiên truy cập website của nhóm mình là “chuỗi thời gian đa biến” chỉ vì có nhiều thuộc tính đầu vào. Thêm biến cũng không bảo đảm kết quả luôn tốt hơn.

## Ghi âm bổ sung: tiến độ, seminar và báo cáo cuối [Lời thầy qua bản chuyển giọng nói/tóm tắt]

### Tiến độ và mẫu báo cáo

- Các nhóm **dự kiến** báo cáo vào tuần 10–11; bản tóm tắt nói có thêm khoảng 2 tuần để tổng hợp và viết báo cáo. Thầy đang xem xét cân đối lại hạn nộp, nên đây **chưa phải lịch/hạn nộp đã chốt**.
- Thầy dự định cung cấp đường dẫn mẫu báo cáo trên Overleaf, kèm lựa chọn tải mẫu Word hoặc LaTeX. Tài liệu người dùng gửi **chưa có đường dẫn mẫu**.

### Seminar trước lớp

- Mỗi nhóm có khoảng **15 phút trình bày** và **5–10 phút trả lời phản biện** (khoảng 20–25 phút tổng cộng).
- Với **mô hình đã học trên lớp**, tập trung vào tham số và cách cài đặt thực tế, không lặp lại toàn bộ lý thuyết cơ bản.
- Với **mô hình mới/tự tìm hiểu thêm** (ví dụ thầy nêu LightGBM, Random Forest), cần trình bày thêm lý thuyết tổng quan và cơ chế hoạt động vì thầy có thể hỏi sâu.
- Với **SVM/SVR**, bản tóm tắt nhắc tham số `C`, loại kernel, `epsilon`, hàm dự báo/phân loại và trọng số `w`, độ lệch `b`; khi nhiều biến khó vẽ trực quan, thầy muốn trình bày hàm và các trọng số thay cho đồ thị.
- Với **ARIMA**, nêu cụ thể `(p, d, q)` và cách tìm (ví dụ `auto_arima` hay dò thủ công).
- Với **RNN/LSTM/CNN**, trình bày kiến trúc: số lớp, số unit/neuron, hàm kích hoạt và cách nối các tầng; bản tóm tắt nói không cần trình bày chi tiết công thức tích chập hoặc các cổng LSTM.

**Lưu ý phương pháp của Codex:** bản tóm tắt gộp SVM phân loại với SVR hồi quy. `epsilon` là tham số thường gắn với **SVR**, không được tự ghi là tham số bắt buộc cho mọi SVM phân loại. Với kernel phi tuyến cũng không nên hứa luôn có thể in một phương trình tuyến tính theo các thuộc tính gốc cùng bộ trọng số `w` dễ đọc; cần đối chiếu yêu cầu cụ thể của thầy khi nhóm thực sự chọn cấu hình SVM.

### Khung bài báo cáo hoàn chỉnh

- Báo cáo theo dạng bài báo khoa học, độ dài **khoảng 12–15 trang**, có thể viết bằng Word hoặc LaTeX. **Tiếng Việt được phép**; tiếng Anh được khuyến khích nếu nhóm có khả năng.
- Các mục được bản tóm tắt liệt kê: **Tóm tắt** (bối cảnh, phương pháp, kết quả chính); **Giới thiệu** (bài toán, input/output, bối cảnh, lý do, thách thức, hướng giải quyết); **Nghiên cứu liên quan** (công trình và thuật toán trước đây); **Phương pháp** (mô hình nhóm triển khai); **Thực nghiệm và đánh giá** (chỉ số, bảng/biểu đồ, phân tích vì sao kết quả khác nhau); **Kết luận và hướng phát triển** (kết quả đạt được và cải tiến).
- Ví dụ chỉ số được thầy nêu trong bản tóm tắt: **Accuracy, Precision, Recall, F1** cho phân loại; **RMSE, MAE, R²** cho dự báo giá trị số. Chỉ số lạ hoặc chưa học trên lớp thì cần giải thích ý nghĩa.

**Lưu ý về bản tóm tắt:** phần này nói “5 phần chính” nhưng thực tế liệt kê **6 mục nếu tính cả Tóm tắt**. Giữ đủ các mục đã nêu; khi có template chính thức thì theo template. Thông tin cũ về việc nộp code và báo cáo trước buổi báo cáo 2 ngày nằm trong **ghi chú bạn học**, còn hạn nộp mới vẫn đang được thầy xem xét; không tự coi các mốc này đã được thay thế hay chốt lại.

## Nội dung người dùng trích xuất từ ghi âm lời giảng viên

### 1. Mức kỳ vọng về phương pháp

- Ngoài các phương pháp đã học trong phần lý thuyết, sinh viên nên tự tìm hiểu và áp dụng thêm một số phương pháp mới.
- Nên cố gắng thực hiện nhiều phương pháp trên bộ dữ liệu; ước lượng giảng viên nêu là khoảng **8–10 phương pháp**.
- Nhóm chỉ dùng các phương pháp đã học hoặc các phương pháp quá đơn giản có thể không được đánh giá cao bằng nhóm nghiên cứu và thực hiện thêm phương pháp mới.

### 2. Yêu cầu khi đánh giá kết quả

- Phải thể hiện mức độ hiểu các phương pháp mới đã dùng.
- Không chỉ nêu “phương pháp A tốt hơn phương pháp B”.
- Cần giải thích vì sao kết quả khác nhau, dựa trên đặc điểm dữ liệu, giả định, cách biểu diễn dữ liệu, khả năng của phương pháp và chỉ số đánh giá phù hợp.

### 3. Đề xuất cải tiến

- Sau phần đánh giá và giải thích, phải đề xuất phương án cải tiến.
- Phần đề xuất cải tiến được nhấn mạnh là rất quan trọng đối với một báo cáo tốt nghiệp hoặc bài báo khoa học tốt.
- Đề xuất cần xuất phát từ kết quả và hạn chế thực tế của đồ án, không chỉ là ý tưởng chung chung.

## Lời giảng viên về báo cáo giới thiệu đồ án (người dùng thuật lại từ buổi học mới)

> **Nguồn: lời thầy do người dùng thuật lại.** Toàn bộ mục này ghi lại yêu cầu của giảng viên, không phải ý tưởng hay yêu cầu do Codex tự đề xuất. Đây là yêu cầu cho **báo cáo giới thiệu đồ án**, không đồng nhất với báo cáo/thuyết trình cuối kỳ.

### 1. Hình thức, thời gian và đăng ký đề tài

- Báo cáo giới thiệu cần ngắn gọn, **tối đa 5 slide**.
- Phần bắt buộc đầu tiên là **giới thiệu thành viên nhóm và tên đề tài**.
- Sinh viên có **2 tuần để chuẩn bị và nộp lại phần giới thiệu đồ án**. Chưa có ngày nộp cụ thể trong thông tin người dùng cung cấp.
- Khi đã chốt đồ án, có thể trao đổi với giảng viên vào cuối giờ; hoặc ghi **tên đề tài, link bài báo (paper) và link dữ liệu (dataset)** vào sheet đăng ký nhóm để giảng viên kiểm tra.

### 2. Nếu làm theo bài báo có đề xuất phương pháp mới

- **Thông tin bài báo:** nêu tên bài báo, tác giả, nơi xuất bản và năm xuất bản.
- **Bài toán và phương pháp:** trình bày bài toán nhóm tác giả giải quyết; nói ngắn gọn phương pháp mới là gì và dựa trên cơ sở nào. **Chưa đi sâu vào lý thuyết chi tiết** của phương pháp ở giai đoạn giới thiệu.
- **Dữ liệu thực nghiệm:** chỉ rõ các bộ dữ liệu được dùng trong bài báo và trả lời trực tiếp **có/không lấy được** các bộ dữ liệu đó.
- Không bắt buộc chạy thực nghiệm trên tất cả bộ dữ liệu của bài báo. Ví dụ, lấy được cả 5 bộ nhưng chỉ chọn 3 bộ để thực nghiệm vẫn được chấp nhận.
- Nếu chỉ lấy được **1 bộ dữ liệu từ bài báo**, cần tìm và khảo sát thêm **1 bộ dữ liệu tương tự**, rồi chạy thực nghiệm phương pháp trên bộ dữ liệu mới đó.
- **Phương pháp đối chứng (baselines):** chỉ cần liệt kê tên các phương pháp mà bài báo dùng để so sánh; **chưa cần chạy thực nghiệm các baseline** trong buổi báo cáo giới thiệu.

### 3. Nếu làm theo bài báo không đề xuất phương pháp mới, chỉ so sánh phương pháp có sẵn

- **Bài toán và dữ liệu:** đi sâu hơn vào phát biểu bài toán, xác định rõ bộ dữ liệu sẽ xử lý và khảo sát các thuộc tính của dữ liệu.
- **Input/Output:** làm rõ đầu vào và đầu ra cụ thể. Với bài toán dự báo, chỉ ra dữ liệu đầu vào và đại lượng cần dự báo; với bài toán phân lớp/dự đoán, chỉ ra các thuộc tính đầu vào và thuộc tính đầu ra/nhãn.
- **Thuật toán dự kiến:** sau khi giới thiệu dữ liệu và bài toán, chỉ cần liệt kê tên các thuật toán/phương pháp cụ thể dự kiến chạy thực nghiệm (ví dụ A, B, C, D).

## Bổ sung từ ghi chú của bạn học do người dùng chuyển lại

> **Nguồn: bạn học ghi lại lời thầy, người dùng chuyển cho Codex.** Đây là lời dặn được thuật lại, chưa đối chiếu bản ghi âm hay thông báo chính thức. Người dùng đã xác nhận **8–10 phương pháp là lời dặn mới**; số lượng trong ghi chú cũ không còn áp dụng cho kế hoạch hiện tại.

- Với **thuật toán đã học trên lớp**, khi báo cáo không cần trình bày lại toàn bộ lý thuyết; tập trung nêu **thông số/cách cài đặt đã dùng**. Ghi chú bạn học chưa nói rõ câu này áp dụng cho buổi giới thiệu hay báo cáo cuối, nên không tự mở rộng thành yêu cầu cho cả hai.
- **Source code và file báo cáo** cần nộp **trước buổi báo cáo 2 ngày**. Ghi chú chưa nêu ngày cụ thể và chưa nói rõ đây là buổi báo cáo nào; cần đối chiếu lịch/thông báo của lớp.
- **Buổi 5** gửi slide **giới thiệu đồ án**, tối đa **5 slide**. Mốc “buổi 5” bổ sung cho lời dặn trước đó về thời gian chuẩn bị 2 tuần; nếu lịch thực tế không khớp, hỏi lại thầy.
- Ghi chú bạn học còn viết hai câu dưới nhãn “Hướng 1/2”: **“đọc hiểu bài báo (có thể làm phương pháp D, E, F)”** và **“tìm bộ dữ liệu có sẵn, sau đó thực nghiệm”**. Chưa rõ bạn học dùng chữ “hướng” để ghi lại cách thầy phân loại đồ án hay để tóm tắt trình tự làm việc.
- **Người dùng xác nhận lại:** hai **loại đồ án thầy nói** là (1) làm theo paper **đề xuất phương pháp mới**, hoặc (2) làm theo paper **chỉ so sánh phương pháp có sẵn**, tương ứng hai mục hướng dẫn báo cáo giới thiệu ở trên.

## Diễn giải và checklist của Codex

Các mục bên dưới là cách Codex chuyển lời dặn của giảng viên thành tiêu chí thực hiện; **không phải nguyên văn lời giảng viên**.

Trước đây Codex gọi hai câu “đọc paper trước / tìm dataset trước” là **paper-first / data-first**, tức hai cách bắt đầu tìm đề tài. **Đó là diễn giải của Codex, không phải hai loại đồ án được người dùng xác nhận là lời thầy.** Không dùng cách diễn giải này để thay thế phân loại paper có phương pháp mới / paper so sánh phương pháp có sẵn.

**Hai nghĩa khác nhau của “phương pháp mới”:** trong lời dặn về 8–10 phương pháp, “mới” có thể hiểu là **chưa học trên lớp, sinh viên phải tự tìm hiểu**; còn trong nhánh “paper đề xuất phương pháp mới”, “mới” là **phương pháp do tác giả bài báo đề xuất**. Vì vậy, chọn nhánh paper chỉ so sánh phương pháp có sẵn **không có nghĩa** đồ án được phép chỉ dùng các thuật toán đã học trên lớp. Đây là cách Codex phân biệt hai ngữ cảnh để tránh hiểu nhầm, cần hỏi lại thầy nếu tiêu chí chấm cụ thể chưa rõ.

### Phân biệt buổi giới thiệu và đồ án hoàn chỉnh

- Theo cách hiểu của Codex, các ý “chưa cần chạy baseline”, “chỉ cần liệt kê thuật toán” và “chưa đi sâu lý thuyết” chỉ áp dụng cho **buổi báo cáo giới thiệu**. Lời dặn trước đó về tìm hiểu thêm phương pháp mới, thử nghiệm, giải thích kết quả và đề xuất cải tiến vẫn là định hướng cho quá trình làm **đồ án hoàn chỉnh**.

### 4. Hệ quả cho cách chọn đề tài

- Không chọn đề tài chỉ đủ cho một mô hình đơn lẻ.
- Chọn dataset có thể hỗ trợ nhiều phương pháp một cách hợp lý; tránh “nhét” thuật toán chỉ để đủ số lượng.
- Xây một vấn đề kinh doanh trung tâm, sau đó chia thành các câu hỏi con liên kết để các nhóm phương pháp cùng đóng góp.
- Trước khi chốt đề tài, lập roadmap: phương pháp đã học, phương pháp mới sẽ tự nghiên cứu, mục đích của từng phương pháp và cách đánh giá.
- Chỉ so sánh trực tiếp các phương pháp cùng giải một bài toán. Ví dụ: so sánh các mô hình dự báo với nhau; không so sánh một mô hình dự báo với một thuật toán phân cụm.

## Checklist trước khi chốt đề tài

- [ ] Dataset có thể hỗ trợ nhiều phương pháp liên quan, hướng đến khoảng 8–10 phương pháp.
- [ ] Mỗi phương pháp có một câu hỏi hoặc vai trò rõ ràng trong bài toán.
- [ ] Có nhóm phương pháp cùng mục tiêu để so sánh công bằng.
- [ ] Có kế hoạch giải thích kết quả, không chỉ liệt kê metric.
- [ ] Có ý tưởng cải tiến dựa trên các hạn chế có thể quan sát được sau thực nghiệm.
- [ ] Có tài liệu/paper đáng tin cậy cho các phương pháp mới.
