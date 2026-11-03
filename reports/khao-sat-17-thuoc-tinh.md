# Khảo sát ban đầu 17 thuộc tính — Online Shoppers Purchasing Intention

## Phạm vi và nguồn

- **Yêu cầu từ thầy:** khảo sát kỹ 17 thuộc tính đầu vào trước khi triển khai mô hình. Đây là bản khảo sát **ban đầu**, chưa phải quyết định giữ hoặc bỏ thuộc tính.
- **Nguồn ý nghĩa thuộc tính:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset). Bản CSV được chép từ file người dùng đã tải trước đây; SHA-256 `B3055EE355F59134D851D32641183CB4A8B45DEF7124D2F50442A042F358E0D9`, khớp mã đã ghi trong [`IS403_CONTEXT.md`](../IS403_CONTEXT.md). Bản gốc trong repo: [`data/raw/online_shoppers_intention.csv`](../data/raw/online_shoppers_intention.csv).
- **Cách kiểm tra thống kê:** chạy `python src/audit_dataset.py` ở thư mục gốc repo; script chỉ đọc CSV và không sửa dữ liệu.
- **Đơn vị quan sát:** một phiên truy cập website. Có **12.330 phiên**, **17 thuộc tính đầu vào** và một cột nhãn `Revenue`.

## Kiểm tra tổng quát trên CSV

| Mục                           | Kết quả                                     |
| ----------------------------- | ------------------------------------------- |
| Số dòng                       | 12.330                                      |
| Số cột                        | 18 = 17 đầu vào + `Revenue`                 |
| Ô trống hoặc ký hiệu `?`      | 0 trong toàn bộ CSV                         |
| `Revenue = TRUE`              | 1.908 phiên (15,47%)                        |
| `Revenue = FALSE`             | 10.422 phiên (84,53%)                       |
| Dòng trùng toàn bộ 18 giá trị | 125 dòng so với các dòng xuất hiện trước đó |

**Lưu ý:** trùng toàn bộ giá trị không chứng minh hai bản ghi là cùng một phiên, vì CSV không có mã phiên. **Chưa xóa** các dòng này. Giá trị `0` cũng không tự động là dữ liệu thiếu; với các cột đếm trang, nó thường có nghĩa phiên không xem loại trang đó.

## Ý nghĩa và giá trị của 17 thuộc tính

| Thuộc tính                | Hiểu đơn giản                                                                                                                          | Quan sát trong CSV                                              | Điều cần kiểm tra trước khi dùng                                                           |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `Administrative`          | Số trang thuộc nhóm `Administrative` mà khách đã xem trong phiên; nguồn UCI không nêu cụ thể nội dung từng trang.                      | Số nguyên từ 0 đến 27.                                          | Thông tin được ghi nhận đến thời điểm dự đoán nào?                                         |
| `Administrative_Duration` | Tổng thời gian ở nhóm trang `Administrative`.                                                                                          | Từ 0 đến 3.398,75; 5.903 phiên bằng 0.                          | Đơn vị thời gian và cách tổng hợp cần đối chiếu nguồn gốc.                                 |
| `Informational`           | Số trang cung cấp thông tin mà khách đã xem.                                                                                           | Số nguyên từ 0 đến 24; 9.699 phiên bằng 0.                      | Phân biệt 0 hợp lệ với thiếu dữ liệu.                                                      |
| `Informational_Duration`  | Tổng thời gian ở nhóm trang `Informational`.                                                                                           | Từ 0 đến 2.549,375; 9.925 phiên bằng 0.                         | Kiểm tra đơn vị và thời điểm sẵn có.                                                       |
| `ProductRelated`          | Số trang liên quan đến sản phẩm đã xem.                                                                                                | Số nguyên từ 0 đến 705; trung vị 18.                            | Giá trị rất lớn có phải phiên dài thật hay bất thường?                                     |
| `ProductRelated_Duration` | Tổng thời gian ở nhóm trang sản phẩm.                                                                                                  | Từ 0 đến 63.973,52223; trung vị khoảng 598,94.                  | Giá trị lớn và đơn vị thời gian cần xem kỹ.                                                |
| `BounceRates`             | Chỉ số từ Google Analytics về tỷ lệ vào một trang rồi rời đi mà không có tương tác tiếp.                                               | Từ 0 đến 0,2; 5.518 phiên bằng 0.                               | UCI mô tả ý nghĩa ở mức trang; cách quy về một giá trị cho phiên chưa được giải thích rõ.  |
| `ExitRates`               | Chỉ số về tỷ lệ một trang là trang cuối trước khi rời website.                                                                         | Từ 0 đến 0,2; trung vị khoảng 0,025.                            | Cần hiểu cách tổng hợp ở mức phiên và thời điểm biết giá trị.                              |
| `PageValues`              | Giá trị trung bình gắn với các trang đã được xem trước giao dịch theo mô tả của UCI; **không phải số tiền khách chi trong phiên này**. | Từ 0 đến 361,7637419; 9.600 phiên bằng 0.                       | **Ưu tiên kiểm tra** cách tính và tính sẵn có trước khi dự đoán; không vội giữ hoặc bỏ.    |
| `SpecialDay`              | Mức độ gần một ngày đặc biệt có thể ảnh hưởng hành vi mua.                                                                             | Sáu mức từ 0 đến 1; 11.079 phiên bằng 0.                        | Xem cách mã hóa mức độ gần ngày đặc biệt.                                                  |
| `Month`                   | Tháng diễn ra phiên truy cập.                                                                                                          | 10 giá trị khác nhau; nhiều nhất là `May` và `Nov`.             | Là loại dữ liệu phân nhóm, không phải số liên tục.                                         |
| `OperatingSystems`        | Mã loại hệ điều hành.                                                                                                                  | 8 mã số khác nhau.                                              | Các mã là **nhãn nhóm**, không có thứ bậc số học; chưa có bảng tên hệ điều hành tương ứng. |
| `Browser`                 | Mã loại trình duyệt.                                                                                                                   | 13 mã số khác nhau.                                             | Không suy ra trình duyệt cụ thể từ mã nếu không có bảng đối chiếu.                         |
| `Region`                  | Mã khu vực của phiên truy cập.                                                                                                         | 9 mã số khác nhau.                                              | Không suy ra địa danh cụ thể từ mã nếu không có bảng đối chiếu.                            |
| `TrafficType`             | Mã nhóm nguồn/lưu lượng truy cập.                                                                                                      | 20 mã số khác nhau.                                             | Không suy ra kênh truy cập cụ thể từ mã nếu không có bảng đối chiếu.                       |
| `VisitorType`             | Khách quay lại, khách mới hoặc loại khác.                                                                                              | `Returning_Visitor`: 10.551; `New_Visitor`: 1.694; `Other`: 85. | Nhóm `Other` rất ít; cần chú ý khi mô hình hóa và diễn giải.                               |
| `Weekend`                 | Phiên có diễn ra vào cuối tuần hay không.                                                                                              | `TRUE`: 2.868; `FALSE`: 9.462.                                  | Kiểu có/không, không phải số liên tục.                                                     |

**Nguồn mô tả:** UCI giải thích các nhóm trang, chỉ số Google Analytics, `SpecialDay` và các thuộc tính bối cảnh. Những thống kê số lượng/giá trị trong bảng là kết quả kiểm tra CSV. Các câu ở cột cuối là **câu hỏi khảo sát của nhóm/Codex**, không phải kết luận của thầy.

## Nhãn đầu ra: `Revenue`

`Revenue` có hai giá trị: `TRUE` nếu phiên kết thúc bằng mua hàng, `FALSE` nếu không. Đây là **nhãn cần dự đoán** trong đề tài nhóm đã được duyệt, không phải một trong 17 đầu vào và không phải số tiền doanh thu.

Nhóm không mua chiếm khoảng 84,53%. Vì vậy, một mô hình luôn nói “không mua” cũng có thể có tỷ lệ đúng chung khoảng 84,53% nhưng không nhận ra phiên mua nào. Khi đánh giá, cần nhìn thêm khả năng nhận ra lớp mua hàng; chưa chốt bộ chỉ số cuối cùng.

## Một vài liên hệ mô tả với nhãn — chưa phải kết luận nguyên nhân

- Trung vị `ProductRelated` là **29** ở các phiên mua và **16** ở các phiên không mua.
- Trung vị `ProductRelated_Duration` là khoảng **1.109,91** ở nhóm mua và **510,19** ở nhóm không mua.
- Với `PageValues = 0`, **370/9.600** phiên mua (3,85%). Với `PageValues > 0`, **1.538/2.730** phiên mua (56,34%). Đây là chênh lệch rất lớn, nhưng **chưa đủ để kết luận** cột này an toàn cho mọi thời điểm dự đoán.
- `New_Visitor` có **422/1.694** phiên mua (24,91%); `Returning_Visitor` có **1.470/10.551** (13,93%). Các tỷ lệ này mô tả dataset, không chứng minh loại khách gây ra việc mua.

## Các quyết định còn mở trước khi giao dữ liệu chung cho người làm mô hình

1. **Dự đoán vào thời điểm nào?** Nếu dự đoán khi khách còn đang truy cập, nhóm chỉ được dùng những thông tin đã có lúc đó. CSV là bản tổng hợp theo phiên nên chưa tự chứng minh mọi giá trị đầu vào có sẵn trước khi kết quả mua hàng xảy ra.
2. **Xử lý `PageValues` thế nào?** UCI mô tả nó qua giá trị trang liên quan đến giao dịch. Cần xác minh cách tính và thời điểm có giá trị. Có thể xem xét đối chiếu kết quả **có/không có cột này**, nhưng đó mới là đề xuất thực nghiệm, chưa phải quyết định.
3. **Các mã phân nhóm xử lý ra sao?** `OperatingSystems`, `Browser`, `Region`, `TrafficType` được viết bằng số nhưng là mã nhóm; không nên mặc nhiên coi `4` lớn gấp đôi `2`.
4. **125 dòng trùng xử lý ra sao?** Cần quyết định và ghi lý do; không tự động xóa vì thiếu mã định danh phiên.
5. **Thống nhất cách chia dữ liệu và chỉ số** trước khi sáu người chạy mô hình, để kết quả có thể so sánh.

Tài liệu này là **bản khảo sát đầu tiên**. Chưa huấn luyện mô hình và chưa kết luận thuộc tính nào tốt nhất, có tác động nhân quả, hoặc chắc chắn phải loại bỏ.
