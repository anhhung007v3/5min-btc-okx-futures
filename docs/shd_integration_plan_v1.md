\# Trading Brain SHD - Integration Plan V1



Ngày: 2026-07-16



\---



\# 1. Mục tiêu



Integration Plan V1 định nghĩa cách kết nối các module của Trading Brain SHD thành một hệ thống hoạt động hoàn chỉnh.



Mục tiêu:



\- Các module giao tiếp đúng trách nhiệm.

\- Không module nào vượt quyền.

\- Dữ liệu đi qua Context rõ ràng.

\- Dễ kiểm tra, mở rộng và debug.



\---



\# 2. Nguyên tắc Integration



SHD không vận hành theo kiểu:



Signal → Order





SHD vận hành theo:



Observe



↓



Understand



↓



Decide



↓



Validate



↓



Act



↓



Learn





\---



\# 3. Kiến trúc luồng chính





Market Data



&#x20;   ↓



MarketEngine



&#x20;   ↓



MarketBrain



&#x20;   ↓



MarketState



&#x20;   ↓



MarketContext





&#x20;   ↓





DecisionEngine



&#x20;   ↓



DecisionContext





&#x20;   ↓





RiskEngine



&#x20;   ↓



RiskContext





&#x20;   ↓





PositionManager





&#x20;   ↓





Execution Layer





\---



\# 4. Market Pipeline





Input:



\- OHLCV

\- Price

\- Volume

\- Indicators





Process:



MarketEngine nhận dữ liệu.



MarketBrain phân tích trạng thái.





Output:



MarketContext





Market Layer không được:



\- Vào lệnh.

\- Đóng lệnh.

\- Quản lý vốn.



\---



\# 5. Decision Pipeline





Input:



\- MarketContext

\- PositionContext





Process:



DecisionEngine đánh giá:





Nếu chưa có Position:



WAIT



PREPARE



ENTER





Nếu đang có Position:



HOLD



DEVELOP



MANAGE



EXIT





Output:



DecisionContext





\---



\# 6. Risk Pipeline





Decision không được tự thực thi.





Mọi hành động cần qua:



RiskEngine





Input:



DecisionContext





Output:



RiskContext





RiskEngine có quyền:



\- Cho phép.

\- Từ chối.





\---



\# 7. Position Pipeline





PositionManager chịu trách nhiệm:



\- Tạo Position.

\- Cập nhật Position.

\- Theo dõi vòng đời.





StageEngine chịu trách nhiệm:



\- STAGE\_0

\- STAGE\_1

\- STAGE\_2





Stage chỉ là trạng thái.



Không phải quyết định giao dịch.



\---



\# 8. Execution Pipeline





Execution Layer:



Nhận hành động đã được kiểm tra.





Nhiệm vụ:



\- Gửi lệnh.

\- Theo dõi trạng thái thực thi.

\- Báo cáo kết quả.





Execution không tự quyết định.



\---



\# 9. Main Brain Loop V1





Chu kỳ hoạt động:





1\. Nhận Market Data





2\. Phân tích Market State





3\. Tạo MarketContext





4\. Đánh giá Decision





5\. Kiểm tra Risk





6\. Quản lý Position





7\. Thực thi nếu được phép





8\. Lưu trạng thái





\---



\# 10. Data Contract





Các module giao tiếp qua:





MarketContext



DecisionContext



PositionContext



RiskContext





Không truyền trực tiếp object nội bộ giữa module.



\---



\# 11. Module cần phát triển tiếp





Sau Integration Plan V1:





\- Xây dựng Main Brain Loop.

\- Kết nối MarketBrain với DecisionEngine.

\- Kết nối DecisionEngine với RiskEngine.

\- Kết nối RiskEngine với PositionManager.

\- Thêm Monitoring.





\---



\# 12. Ghi chú





Integration Plan V1 là bản thiết kế trước khi triển khai hệ thống chạy thực tế.





Mọi thay đổi kiến trúc lớn cần cập nhật tài liệu trước khi code.



