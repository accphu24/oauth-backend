# Changelog

## 1.0.0 — 2026-09-04
- Deploy lại backend trên Render (project cũ bị xoá nhầm), bắt đầu đánh version từ đây.
- Đổi Client Secret mới cho GitHub OAuth App.
- Thêm HEAD handler cho route `/` (UptimeRobot check bằng HEAD, GET-only bị 405 Method Not Allowed).
