\# Trading Brain SHD - Decision Flow V1



Ngày: 2026-07-16



\---



\# 1. Mục tiêu



Decision Flow V1 định nghĩa cách Trading Brain SHD đưa ra quyết định.



Mục tiêu:



\- Không giao dịch dựa trên một tín hiệu đơn lẻ.

\- Quyết định dựa trên trạng thái thị trường.

\- Quyết định dựa trên trạng thái vị thế.

\- Tách biệt rõ:

&#x20;   - Quan sát

&#x20;   - Quyết định

&#x20;   - Kiểm tra rủi ro

&#x20;   - Thực thi



\---



\# 2. Nguyên tắc kiến trúc



Trading Brain SHD gồm các tầng:



Market Layer



&#x20;   ↓



Decision Layer



&#x20;   ↓



Risk Layer



&#x20;   ↓



Position Layer



&#x20;   ↓



Execution Layer





Quyền hạn:



Market:

\- Quan sát.

\- Phân tích trạng thái.



Decision:

\- Đề xuất hành động.



Risk:

\- Cho phép hoặc từ chối.



Position:

\- Quản lý vòng đời vị thế.



Execution:

\- Thực hiện hành động.



\---



\# 3. Decision Flow khi chưa có Position



Trạng thái:



NO\_POSITION





Luồng:



Market Data



&#x20;   ↓



MarketBrain



&#x20;   ↓



MarketContext



&#x20;   ↓



DecisionEngine





Decision có thể trả về:



WAIT



Lý do:

\- Không có cơ hội.

\- Thị trường chưa rõ xu hướng.





PREPARE



Lý do:

\- Có dấu hiệu hình thành cơ hội.

\- Chưa đủ điều kiện vào.





ENTER



Lý do:

\- Điều kiện chiến lược đạt.

\- Chờ RiskEngine kiểm tra.





\---



\# 4. Decision Flow khi đang có Position



Trạng thái:



POSITION\_ACTIVE





Luồng:



PositionState



&#x20;   +



MarketContext



&#x20;   ↓



DecisionEngine





Decision có thể trả về:





HOLD



Khi:

\- Vị thế đang hoạt động bình thường.





DEVELOP



Khi:

\- Vị thế an toàn.

\- Có thể phát triển theo kế hoạch.





MANAGE



Khi:

\- Cần bảo vệ lợi nhuận.

\- Thị trường thay đổi.





EXIT



Khi:

\- Điều kiện thoát xuất hiện.

\- Risk yêu cầu đóng vị thế.





\---



\# 5. Stage Management



Position Lifecycle:



STAGE\_0



Ý nghĩa:



\- Vị thế mới mở.

\- Chưa được xác nhận.





↓



STAGE\_1



Ý nghĩa:



\- Giá đi đúng hướng.

\- Vị thế được bảo vệ.





↓



STAGE\_2



Ý nghĩa:



\- Vị thế có lợi nhuận.

\- Chuyển sang bảo vệ thành quả.





Stage không tự quyết định giao dịch.



Stage chỉ cung cấp trạng thái cho DecisionEngine.



\---



\# 6. Risk Control



DecisionEngine:



KHÔNG:



\- Bỏ qua Risk.

\- Tự tính vốn.

\- Tự gửi lệnh.





Mọi hành động:



ENTER



DEVELOP



EXIT





phải đi qua RiskEngine.





Luồng:



Decision



&#x20;   ↓



RiskEngine



&#x20;   ↓



RiskContext



&#x20;   ↓



PositionManager



\---



\# 7. Data Contract



Các module giao tiếp bằng Context.





Market:



MarketContext





Decision:



DecisionContext





Position:



PositionContext





Risk:



RiskContext





Không truyền trực tiếp dữ liệu nội bộ giữa module.



\---



\# 8. Mục tiêu phát triển tiếp theo



Phiên bản tiếp theo cần xây dựng:



Decision Flow V2



Bao gồm:



\- Market Opportunity Detection.

\- Entry Planning.

\- Exit Planning.

\- Integration với Execution.





\---



\# Ghi chú



Decision Flow V1 là tài liệu nền tảng cho việc phát triển Decision Brain SHD.



Mọi thay đổi logic quyết định trong tương lai cần cập nhật tài liệu này trước khi code.

