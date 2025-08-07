@echo off
title V86 Android-x86 Web Server

REM Kiểm tra nếu python có sẵn
where python >nul 2>nul
IF ERRORLEVEL 1 (
    echo Python không được cài đặt hoặc chưa thêm vào PATH.
    echo Vui lòng cài Python tại https://www.python.org/downloads/
    pause
    exit /b
)

REM Chạy máy chủ HTTP
echo Đang khởi động máy chủ...
python -m http.server 8000

pause
