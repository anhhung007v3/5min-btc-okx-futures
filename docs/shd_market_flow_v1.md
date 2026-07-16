\# Trading Brain SHD - Market Intelligence Flow V1



Ngày: 2026-07-16



\---



\# 1. Mục tiêu



Market Intelligence Flow định nghĩa cách Trading Brain SHD quan sát và đánh giá thị trường.



Mục tiêu:



\- Không tạo tín hiệu mua bán trực tiếp.

\- Không quản lý Position.

\- Không quyết định vào lệnh.



Market Brain chỉ có nhiệm vụ:



Quan sát → Phân tích → Mô tả trạng thái thị trường.



\---



\# 2. Nguyên tắc kiến trúc



Market Layer:



Market Data



&#x20;   ↓



MarketEngine



&#x20;   ↓



MarketState



&#x20;   ↓



MarketContext



&#x20;   ↓



DecisionEngine





Market Layer chỉ cung cấp thông tin.



Decision Layer mới quyết định hành động.



\---



\# 3. Market Data Input



Nguồn dữ liệu:



\- OHLCV

\- Price

\- Volume

\- ATR

\- Indicators





MarketBrain không phụ thuộc trực tiếp vào nguồn dữ liệu.



Nó chỉ nhận market\_data.



\---



\# 4. MarketState



MarketState là trạng thái hiện tại của thị trường.



V1 gồm:





direction



Ý nghĩa:



Hướng chính của thị trường.



Giá trị dự kiến:



\- UP

\- DOWN

\- NONE





\---



trend\_strength



Ý nghĩa:



Độ mạnh của xu hướng.





\---



volatility



Ý nghĩa:



Mức biến động hiện tại.





\---



movement\_ok



Ý nghĩa:



Xác nhận thị trường có chuyển động đủ điều kiện để xem xét hành động.





\---



timestamp



Thời điểm cập nhật trạng thái.



\---



\# 5. Market Context



Sau khi phân tích, MarketBrain tạo:



MarketContext





Bao gồm:



\- Symbol

\- Timeframe

\- MarketState

\- Current Price

\- ATR

\- Volume Ratio





Luồng:



MarketBrain



&#x20;   ↓



MarketContext



&#x20;   ↓



DecisionEngine



\---



\# 6. Market Condition V1



Các trạng thái thị trường ban đầu:





TREND\_UP



Điều kiện:



\- Hướng tăng.

\- Trend strength phù hợp.

\- Movement hợp lệ.





\---



TREND\_DOWN



Điều kiện:



\- Hướng giảm.

\- Trend strength phù hợp.

\- Movement hợp lệ.





\---



RANGE



Điều kiện:



\- Không có xu hướng rõ.

\- Không đủ điều kiện phát triển.





\---



HIGH\_VOLATILITY



Điều kiện:



\- Biến động quá lớn.

\- Cần hạn chế hành động.





\---



NO\_TRADE



Điều kiện:



\- Dữ liệu không đủ.

\- Thị trường không phù hợp.



\---



\# 7. Quyền hạn của Market Brain



Market Brain:



ĐƯỢC:



\- Phân tích trạng thái.

\- Đánh giá điều kiện thị trường.

\- Tạo MarketContext.





KHÔNG:



\- Mở lệnh.

\- Đóng lệnh.

\- Tính vốn.

\- Bỏ qua Risk.



\---



\# 8. Giao tiếp với Decision Brain



Luồng:



MarketContext



&#x20;   +



PositionContext





&#x20;   ↓





DecisionEngine





DecisionEngine sử dụng MarketContext để hiểu:



\- Thị trường đang ở đâu.

\- Có phù hợp phát triển hành động không.



\---



\# 9. Phát triển tương lai



Market Intelligence V2 có thể bổ sung:



\- Trend regime detection.

\- Momentum state.

\- Liquidity state.

\- Market score.

\- Opportunity detection.





\---



\# Ghi chú



Market Intelligence Flow V1 là tài liệu nền tảng cho Market Brain SHD.



Mọi thay đổi logic phân tích thị trường cần cập nhật tài liệu này trước khi code.

