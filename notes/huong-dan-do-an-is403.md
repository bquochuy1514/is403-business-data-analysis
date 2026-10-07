# Hướng dẫn đồ án IS403 Phân tích dữ liệu kinh doanh

## Mục đích tài liệu

Tài liệu này giải thích đồ án môn IS403 cần làm gì, theo cách đủ rõ để một thành viên mới trong nhóm có thể hiểu và tham gia. Nội dung dựa trên đề cương môn học, slide giới thiệu và thông tin hiện nhóm đang hiểu từ lớp.

## Cách đọc nhãn nguồn

- **[Slide/đề cương]**: thông tin xuất hiện trong ảnh đề cương hoặc slide giới thiệu môn mà người dùng đã cung cấp.
- **[Người dùng nghe trên lớp - chưa xác minh]**: thông tin người dùng thuật lại; cần hỏi lại giảng viên nếu ảnh hưởng đến phạm vi hoặc yêu cầu nộp bài.
- **[Đề xuất của Codex]**: gợi ý, diễn giải, ví dụ hoặc kế hoạch do Codex đưa ra; không phải yêu cầu chính thức của môn.

> **Lưu ý:** danh sách website lấy dữ liệu hiện chỉ thuộc nhóm “người dùng nghe trên lớp - chưa xác minh”; chưa có văn bản xác nhận trong thư mục dự án.

## 1. Đồ án thực chất là gì? [Diễn giải của Codex từ yêu cầu chính thức]

Đồ án là một **bài phân tích dữ liệu cho một vấn đề kinh doanh cụ thể**. Nhóm phải dùng dữ liệu thật để:

1. xác định vấn đề cần giải quyết;
2. hiểu, chuẩn bị và khám phá dữ liệu;
3. lựa chọn phương pháp phân tích/mô hình phù hợp;
4. thực nghiệm, đánh giá kết quả;
5. chuyển kết quả thành kết luận hoặc khuyến nghị có ý nghĩa với doanh nghiệp.

Đồ án **không** chỉ là tải một dataset và chạy nhiều thuật toán. Mỗi phương pháp phải trả lời được một câu hỏi liên quan đến bài toán, và phải có lý do chọn phương pháp đó.

## 2. Yêu cầu đã biết của môn học [Slide/đề cương]

### Tổ chức nhóm

- Mỗi nhóm gồm **4–5 sinh viên**.
- Đăng ký nhóm và đồ án trên Moodle **trước buổi học thứ 3**.
- Các thành viên đều phải đóng góp và tham gia báo cáo vào những buổi cuối.

### Đề xuất đề tài cần nêu

Khi đăng ký hoặc giới thiệu đề tài, nhóm cần mô tả:

- **Vấn đề:** mô tả ngắn gọn; đầu vào, đầu ra, kiểu dữ liệu và ứng dụng kỳ vọng.
- **Phương pháp/công cụ:** các thuật toán ML/DM hoặc công cụ dự kiến sử dụng.
- **Bộ dữ liệu:** nguồn, phạm vi và dữ liệu sẽ dùng.

### Sản phẩm cần nộp/trình bày

- **Source code** và `README.txt`: hướng dẫn setup, compile và chạy đồ án.
- **Báo cáo PDF:** trình bày kết quả dưới dạng bài báo.
- **Slide PowerPoint:**
    - giới thiệu vấn đề và dataset;
    - chi tiết các phương pháp phân tích dữ liệu/ML;
    - kết quả của các đánh giá, phát hiện mới và kết luận;
    - khó khăn, đề xuất và giải pháp.
- **Thuyết trình và demo:** khoảng 15 phút.
- Nếu dùng thư viện, package hoặc source code có sẵn, phải khai báo trong báo cáo và slide.

### Tiêu chí đánh giá đã biết

- Độ khó/thách thức của đề tài.
- Mức phù hợp và chất lượng của phương pháp/giải pháp được chọn.
- Tính chặt chẽ của thực nghiệm và đánh giá.
- Chất lượng báo cáo và thuyết trình.

## 3. Cách chọn một đề tài tốt [Đề xuất của Codex]

Một đề tài phù hợp cần thỏa cả bốn điều kiện:

1. **Có câu hỏi kinh doanh cụ thể.** Ví dụ: “Yếu tố nào ảnh hưởng đến doanh thu?” hoặc “Doanh thu tháng tới sẽ là bao nhiêu?”
2. **Có dữ liệu phù hợp.** Dataset phải có biến cần thiết để trả lời câu hỏi và đủ dữ liệu để phân tích.
3. **Có phương pháp phù hợp với kiểu câu hỏi.** Không chọn thuật toán chỉ vì nó phức tạp.
4. **Kết quả có thể diễn giải.** Nhóm phải nói được kết quả có ý nghĩa gì và doanh nghiệp nên làm gì tiếp theo.

### Câu hỏi tốt và câu hỏi chưa tốt

| Loại     | Ví dụ                                                                | Nhận xét                                  |
| -------- | -------------------------------------------------------------------- | ----------------------------------------- |
| Tốt      | “Dự báo doanh thu bán lẻ theo tháng để lập kế hoạch tồn kho.”        | Có mục tiêu, biến kết quả và ứng dụng rõ. |
| Tốt      | “Phân tích yếu tố liên quan đến khả năng khách hàng rời bỏ dịch vụ.” | Có thể dùng thống kê, Logistic và ML.     |
| Chưa tốt | “Phân tích dataset bán hàng bằng Python.”                            | Chỉ nêu công cụ, chưa có vấn đề cần giải. |
| Chưa tốt | “Dùng tất cả thuật toán đã học.”                                     | Không có lý do phương pháp và quá rộng.   |

## 4. Nguồn dữ liệu và cách sử dụng

### Các nguồn được nhắc tới [Người dùng nghe trên lớp - chưa xác minh]

| Nguồn                | Điều người dùng nhớ đã được nhắc        | Nhận xét của Codex                                                                                                       |
| -------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Kaggle Datasets**  | Có thể là nơi thầy gợi ý lấy dataset.   | Nên ưu tiên khi bắt đầu; kiểm tra mô tả, giấy phép, số dòng và các cột dữ liệu.                                          |
| **Investing.com**    | Có thể là nơi thầy gợi ý lấy data.      | Phù hợp hơn với dữ liệu thị trường tài chính theo thời gian; kiểm tra cách dữ liệu được phép tải/thu thập.               |
| **Papers with Code** | Có thể là nơi thầy gợi ý tham khảo.     | Thường hữu ích hơn để tìm paper, phương pháp, benchmark hoặc code hơn là dataset business. Phải trích dẫn nếu tham khảo. |
| **PhysioNet**        | Có thể là nơi thầy gợi ý lấy data.      | Thường là dữ liệu y tế/sinh lý; cần hỏi thầy trước nếu muốn dùng cho môn phân tích dữ liệu kinh doanh.                   |
| **Web công khai**    | Người dùng có nhắc “web thu thập data”. | Chỉ thu thập khi điều khoản nguồn cho phép; lưu nguồn, thời điểm và cách thu thập.                                       |

## 5. Quy trình thực hiện khuyến nghị [Đề xuất của Codex]

### Giai đoạn A - Chốt hướng đề tài, dữ liệu và roadmap phương pháp

1. Xác định một vấn đề kinh doanh trung tâm và các câu hỏi nghiên cứu con liên kết với nhau.
2. Tìm rồi xác minh dataset: nguồn gốc, license, mô tả cột, đơn vị quan sát, phạm vi thời gian và các giới hạn dữ liệu.
3. Kiểm tra dataset có thể hỗ trợ một roadmap khoảng 8–10 phương pháp một cách hợp lý hay không; không chọn thuật toán chỉ để đủ số lượng.
4. Phân biệt phương pháp đã học với phương pháp mới cần tự nghiên cứu; ghi mục đích, đầu vào/đầu ra và cách đánh giá của từng phương pháp.
5. Viết đề cương ngắn: vấn đề, câu hỏi, dữ liệu, roadmap phương pháp, kết quả mong đợi và giá trị kinh doanh.

### Giai đoạn B - Chuẩn bị dữ liệu

1. Lưu dữ liệu gốc, không sửa đè lên bản gốc.
2. Ghi nguồn, ngày tải, giấy phép/cách sử dụng và ý nghĩa các cột.
3. Kiểm tra kiểu dữ liệu, dòng trùng, giá trị thiếu, giá trị bất thường và đơn vị đo.
4. Làm sạch/tích hợp/biến đổi dữ liệu; ghi lại mọi quyết định để tái lập được.
5. Tạo một dataset đã xử lý dùng cho các bước sau.

### Giai đoạn C - Phân tích khám phá

1. Mô tả quy mô và đặc điểm chính của dữ liệu.
2. Dùng bảng thống kê: trung bình, trung vị, độ lệch chuẩn, phân vị... khi phù hợp.
3. Dùng biểu đồ: cột, đường, tán xạ, hộp... để phát hiện xu hướng, khác biệt và ngoại lệ.
4. Viết nhận xét cho từng phát hiện quan trọng; không chỉ chèn biểu đồ mà không giải thích.

### Giai đoạn D - Phân tích và mô hình hóa

1. Chuyển câu hỏi kinh doanh thành câu hỏi có thể kiểm tra bằng dữ liệu.
2. Dùng roadmap khoảng 8–10 phương pháp đã chốt; mỗi phương pháp phải có vai trò rõ ràng.
3. Nêu giả định, dữ liệu đầu vào, biến đầu ra và tiêu chí đánh giá của từng phương pháp.
4. Chạy thực nghiệm có thể lặp lại; lưu cấu hình và kết quả.
5. Chỉ so sánh trực tiếp các phương pháp cùng giải một mục tiêu; giải thích nguyên nhân của khác biệt kết quả, không chỉ báo metric.

### Giai đoạn E - Đánh giá và kết luận

1. Đánh giá kết quả bằng chỉ số/bằng chứng phù hợp.
2. Kiểm tra kết quả có hợp lý về mặt kinh doanh hay không.
3. Nêu giới hạn của dữ liệu và mô hình; không khẳng định quá mức.
4. Rút ra khuyến nghị/hành động tiếp theo và đề xuất cải tiến dựa trên giới hạn, kết quả thực nghiệm.
5. Hoàn thiện code, README, báo cáo, slide và demo.

## 6. Phương pháp áp dụng theo tiến độ học hiện tại

**Danh sách chương/phương pháp là [Slide/đề cương]. Cách áp dụng các chương vào đồ án là [Đề xuất của Codex].**

Có thể chọn dataset có tiềm năng dùng các phương pháp ở nhiều chương, rồi triển khai từng phần khi phù hợp với bài toán. Không cần áp dụng mọi chương vào cùng một đồ án.

| Nội dung môn                     | Có thể đóng góp vào đồ án                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------- |
| Chương 1: mô tả và trực quan hóa | Hiểu dataset, phát hiện xu hướng/ngoại lệ, mô tả bối cảnh bài toán.                         |
| Chương 2: ước lượng và kiểm định | Kiểm tra khác biệt/quan hệ có ý nghĩa thống kê giữa các nhóm.                               |
| Chương 3: hồi quy                | Phân tích biến ảnh hưởng hoặc dự báo một biến số liên tục.                                  |
| Chương 4: Logistic               | Dự đoán kết quả nhị phân như mua/không mua, rời bỏ/không rời bỏ.                            |
| Chương 5: chuỗi thời gian        | Dự báo doanh thu, nhu cầu, giá hoặc lượng bán theo thời gian.                               |
| Chương 6: học máy                | So sánh mô hình ML với cách tiếp cận khác cho bài toán dự báo/phân loại.                    |
| Chương 7: SEM                    | Chỉ dùng khi dữ liệu/câu hỏi phù hợp với mô hình cấu trúc và nhóm thực sự hiểu phương pháp. |

Theo nội dung giảng viên dặn qua ghi âm, nhóm nên hướng tới khoảng **8–10 phương pháp**, gồm một số phương pháp mới ngoài phần lý thuyết. Đây được ghi nhận là định hướng mạnh (“nên cố gắng/ước lượng”), không phải con số bắt buộc đã có trong đề cương văn bản. Mỗi phương pháp vẫn phải liên quan trực tiếp đến vấn đề hoặc câu hỏi con; không “nhét” thuật toán chỉ để đủ số lượng.

## 7. Hướng từng khảo sát [Lịch sử, chưa phải đề tài cuối]

> **Cập nhật:** Các ý về Online Retail II và Olist bên dưới là lịch sử khảo sát, không phải hướng đã chốt. Đề tài hiện tại và mục tiêu cuối được ghi tại [`de-tai-du-doan-mua-hang.md`](de-tai-du-doan-mua-hang.md); **link dataset dùng khi đăng ký/giới thiệu là [bản Kaggle](https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset)**, còn UCI là nguồn gốc bộ dữ liệu. Hai loại đồ án người dùng xác nhận là lời thầy (paper đề xuất phương pháp mới / paper so sánh phương pháp có sẵn), mốc 8–10 phương pháp và ghi chú bạn học về cách bắt đầu được phân biệt tại [`luu-y-giang-vien-ve-do-an.md`](luu-y-giang-vien-ve-do-an.md).

### Retail giao dịch online

**Vấn đề kinh doanh trung tâm đang chốt:** nhà bán lẻ online cần khai thác dữ liệu giao dịch lịch sử để hiểu yếu tố tạo doanh thu và hỗ trợ quyết định về khách hàng, sản phẩm, bán kèm và kế hoạch bán hàng.

**Dataset đang khảo sát:** Online Retail II trên Kaggle, có nguồn UCI. Dataset chưa được xác nhận là dataset chính thức cho đến khi hoàn tất kiểm tra và người dùng tự chốt.

**Các câu hỏi con đang cân nhắc:**

- Giá trị bán hàng thay đổi thế nào theo thời gian, sản phẩm và quốc gia?
- Có những nhóm khách hàng nào theo hành vi và giá trị mua?
- Sản phẩm nào thường được mua cùng nhau?
- Giá trị bán hàng kỳ tới có thể dự báo ra sao?

**Lộ trình phương pháp:** chưa chốt. Phải lập bản đồ khoảng 8–10 phương pháp, gồm phương pháp đã học và phương pháp mới; từng phương pháp cần có vai trò, cách đánh giá và lý do phù hợp với dữ liệu.

Đây là lộ trình từng dự tính cho Online Retail II, không phải điều kiện đặt tên cho đề tài hiện tại.

## 8. Cấu trúc repo đề xuất [Đề xuất của Codex]

```text
IS403/
├─ data/
│  ├─ raw/                 # Dữ liệu gốc, không chỉnh sửa
│  └─ processed/           # Dữ liệu sau xử lý
├─ notebooks/              # Jupyter/Colab notebooks theo từng bước
├─ src/                    # Mã nguồn dùng lại được
├─ reports/                # Báo cáo, biểu đồ và slide thuyết trình đồ án
├─ slides/                 # PDF bài giảng giữ riêng trên máy, được Git bỏ qua
├─ lecture-notes/          # Ghi chú tóm tắt nội dung từng chương học
├─ notes/                  # Ghi chú đề tài, hướng dẫn đồ án, lời dặn của giảng viên
├─ README.md               # Cách cài đặt và chạy dự án
├─ .gitignore              # Bỏ qua slides/ và node_modules/ nếu có
└─ IS403_CONTEXT.md        # Context bền vững giữa các chat
```

## 9. Checklist cũ khi khảo sát Online Retail II [Đề xuất của Codex, không còn là việc cần làm ngay]

1. Xác nhận lại với giảng viên mức bắt buộc của mục tiêu 8–10 phương pháp, nếu có cơ hội.
2. Kiểm tra Online Retail II: nguồn, cột, đơn vị quan sát, đơn hủy, license và giới hạn dữ liệu.
3. Chốt một vấn đề kinh doanh trung tâm cùng các câu hỏi con liên kết.
4. Lập bản đồ phương pháp: đã học/mới, mục tiêu, đầu vào-đầu ra, cách đánh giá và nhóm phương pháp sẽ so sánh.
5. Tìm paper nền cho dataset/bài toán và paper/tài liệu đáng tin cho các phương pháp mới.
6. Chốt tên đề tài, mục tiêu, link dataset, link nguồn gốc và link paper trước khi làm slide giới thiệu.

## 10. Những điều cần xác nhận với giảng viên [Đề xuất của Codex]

- Nhóm có bắt buộc tự thu thập dữ liệu web hay được dùng hoàn toàn dataset Kaggle không?
- Con số khoảng 8–10 phương pháp là bắt buộc hay là mục tiêu khuyến khích; EDA, kiểm định và tiền xử lý có được tính vào số phương pháp đó không?
- Có phải dùng đúng website được gợi ý, hay có thể dùng nguồn công khai khác?
- Dataset tài chính/y tế có được chấp nhận khi môn nhấn mạnh dữ liệu kinh doanh không?
- Hạn đăng ký đề tài, mốc nộp tiến độ và định dạng báo cáo cụ thể là gì?
