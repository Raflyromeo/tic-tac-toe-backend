# Tic-Tac-Toe Backend 🎮

Server backend untuk game Tic Tac Toe Multiplayer berbasis real-time. Dibuat dengan Flask dan Socket.IO untuk mendukung sinkronisasi gerakan antar pemain secara instan.

## 🚀 Teknologi
- **Python 3.10+**
- **Flask 3.x** (Web Framework)
- **Flask-SocketIO 5.x** (Real-time Communication)
- **Flask-CORS** (Cross-Origin Resource Sharing)
- **Eventlet 0.36+** (Networking Engine)

## 🛠️ Fitur
- **Room Management**: Membuat dan bergabung ke ruangan menggunakan kode unik.
- **Real-time Sync**: Sinkronisasi papan permainan antar pemain menggunakan WebSocket.
- **Game Logic**: Validasi langkah dan penentuan pemenang di sisi server.
- **Auto Cleanup**: Menghapus data ruangan secara otomatis jika semua pemain keluar.

## 📦 Cara Menjalankan
1. Pastikan Python sudah terinstal.
2. Buat virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. Instal dependensi:
   ```bash
   pip install flask flask-socketio flask-cors eventlet
   ```
4. Jalankan server:
   ```bash
   python app.py
   ```
   Server akan berjalan di `http://localhost:5000`.

## 🔗 Repository Terkait
- **Frontend**: [tic-tac-toe-gabutan](https://github.com/Raflyromeo/tic-tac-toe-gabutan)

---
Dibuat dengan ❤️ oleh [Rafly Romeo](https://github.com/Raflyromeo)
