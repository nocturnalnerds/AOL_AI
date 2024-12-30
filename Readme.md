LANGKAH RUN APLIKASINYA

prequisites yang dibutuhkan untuk menjalankan aplikasi

1. python@3.11 https://www.python.org/downloads/release/python-3110/
2. npm@.10.2.4 https://nodejs.org/en/download
3. Vscode (or Equivalent text Editor)

4. ⁠Membuat new folder dan buka folder kosong tersebut di VS code
5. ⁠Ketik di terminal
   > > git clone https://github.com/nocturnalnerds/AOL_AI.git
6. Masuk ke dala directory dengan
   > > cd AOL_AI
7. Buat virtual environment dengan mengetik di terminal:
   4.1 Jika di Windows OS
   > > python -m venv env
   4.2 Jika di Linux based OS (Linux Distro, MacOS & Others)
   > > python3 -m venv env
8. Aktivasi Python Environtment -> ⁠Ketik di terminal
   5.1 Jika di Windows OS
   > > .\venv\Scripts\activate.bat
   5.2 Jika di Linux based OS (Linux Distro, MacOS & Others)
   > > source env/bin/activate
9. Install semua requirements dengan ketik:
   6.1 Jika di Windows OS
   > > pip install -r requirements.txt
   6.2 Jika di Linux based OS (Linux Distro, MacOS & Others)
   > > pip3 install -r requirements.txt
10. Run server backend
    > > python 3.11 app.py
11. ⁠Buka terminal baru dengan click tombol + disebelah kanan tulisan powershell/terminal
12. ⁠Ketik di terminal
    > > cd .clients\client2\
13. ⁠Ketik di terminal
    > > npm i
14. ⁠Ketik di terminal
    > > npm run dev
15. ⁠Jika semua dependencies sudah terinstall dengan benar dan tidak ada error, server python sudah menyala, react sudah jalan, webnya sudah bisa digunakan. Biasanya pada http://localhost:5173/ namun sesuaikan Kembali pada server yang ada di terminalnya.
