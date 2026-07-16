\# Trading Brain SHD - Main Brain Loop V1



Ngày: 2026-07-16



\---



\# 1. Mục tiêu



Main Brain Loop là chu trình vận hành trung tâm của Trading Brain SHD.



Nhiệm vụ:



\- Kết nối tất cả module.

\- Điều phối luồng dữ liệu.

\- Đảm bảo mỗi module làm đúng trách nhiệm.

\- Tạo nền tảng cho hệ thống chạy liên tục.



\---



\# 2. Triết lý vận hành



SHD không chạy theo:



Signal → Order





SHD chạy theo:



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



Record





\---



\# 3. Main Loop Overview





Trading Cycle





START



↓



Load System State



↓



Receive Market Data



↓



Analyze Market



↓



Create Market Context



↓



Evaluate Decision



↓



Risk Validation



↓



Position Management



↓



Execution



↓



Save State



↓



WAIT Next Cycle





\---



\# 4. Step 1 - Load System State





Khi khởi động:





Load:



\- Current Position

\- Capital State

\- Stage State

\- Previous Decisions





Mục tiêu:



Bot có thể restart mà không mất trạng thái.



\---



\# 5. Step 2 - Market Observation





Input:



\- OHLCV

\- Price

\- Volume

\- Indicators





Process:



MarketEngine



↓



MarketBrain





Output:



MarketContext





\---



\# 6. Step 3 - Decision





Input:



MarketContext



\+



PositionContext





Process:



DecisionEngine





Output:



DecisionContext





Ví dụ:





Không có Position:



WAIT



PREPARE



ENTER





Có Position:



HOLD



DEVELOP



MANAGE



EXIT





\---



\# 7. Step 4 - Risk Gate





Mọi hành động phải qua RiskEngine.





Input:



DecisionContext





Output:



RiskContext





RiskEngine có quyền:



ALLOW



hoặc



DENY





Decision không được bypass Risk.



\---



\# 8. Step 5 - Position Management





PositionManager:





Nếu ALLOW:



\- Tạo Position.

\- Cập nhật Position.

\- Thay đổi Stage.





Nếu DENY:



\- Không thay đổi Position.





\---



\# 9. Step 6 - Execution





Execution Layer:





Nhận hành động đã được xác nhận.





Nhiệm vụ:



\- Gửi lệnh.

\- Theo dõi kết quả.

\- Cập nhật trạng thái.





Execution không tự quyết định.



\---



\# 10. Step 7 - State Persistence





Sau mỗi cycle:





Lưu:



\- Position State

\- Risk State

\- Decision History

\- Trade Journal





Mục tiêu:



Có thể audit lại toàn bộ hành vi của Brain.



\---



\# 11. Error Handling





Mỗi cycle phải bảo vệ:





\- API lỗi.

\- Dữ liệu thiếu.

\- Module lỗi.





Nguyên tắc:





Lỗi không được làm mất State.





\---



\# 12. Cycle Timing





V1:





Mỗi cycle chạy theo timeframe.





Ví dụ:



5 phút





Một cycle:





09:00



↓



09:05



↓



09:10





\---



\# 13. Future Extension





Main Loop V2 có thể bổ sung:





\- Event driven architecture.

\- Multi timeframe analysis.

\- Learning module.

\- Performance monitoring.

\- Adaptive strategy.





\---



\# 14. Ghi chú





Main Brain Loop V1 là bản thiết kế trước khi triển khai controller thực tế.





Mọi thay đổi luồng vận hành phải cập nhật tài liệu trước khi code.

