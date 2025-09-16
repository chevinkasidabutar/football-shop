# BolaBaleStore

Nama : Chevinka Queen Cilia Sidabutar
Kelas : PBP-F
NPM : 2406437376
Link : https://chevinka-queen-footballshop.pbp.cs.ui.ac.id 

TUGAS 2
#1 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    1. Membuat direktori baru yaitu direktori football-shop untuk dijadikan direktori untuk project django baru
    2. Tahap selanjutnya membuat virtual environment dengan command:
            'python3 -m venv env', 
    lalu mengaktifkan virtual environment, instalasi dependencies, dan start project dengan command:
            'django-admin startproject football_shop .'
    3. Membuat aplikasi baru dengan nama main untuk menangani bagian utama aplikasi dengan menjalankan perintah:
            'python manage.py startapp main'
    yang akan membuat folder main berisi struktur aplikasi Django seperti views.py, models.py, dan file lainnya
    4. Selanjutnya, saya membuat folder templates/main/ di dalam aplikasi main untuk menyimpan file template HTML 
    yang digunakan untuk menampilkan halaman web, saya membuat file main.html yang akan menampilkan informasi seperti nama toko, nama lengkap, dan kelas
    5. Saya kemudian mendefinisikan model Product di dalam file models.py aplikasi main. Model ini akan mewakili produk yang dijual di aplikasi.
    6. Setelah mendefinisikan model Product, saya menjalankan perintah migrasi untuk mengupdate database dengan model baru
    7. Setelah model dan database siap, saya membuat view di file views.py untuk mengambil data produk dan menampilkan produk di halaman web. Fungsi show_main() akan mengambil semua produk dari database dan mengirimkan data tersebut ke template HTML untuk dirender
    8. Selanjutnya, saya mengonfigurasi routing URL untuk aplikasi main. Hal ini dilakukan dengan menambahkan entry di file urls.py di dalam aplikasi main. Agar URL aplikasi main dikenali oleh proyek Django, saya menambahkan include() pada urls.py di direktori proyek
    9. Setelah semuanya dikonfigurasi, saya menjalankan server Django menggunakan perintah:
            'python manage.py runserver'
       Kemudian, saya membuka browser dan mengakses http://localhost:8000/ untuk memeriksa apakah tampilan berjalan dengan baik
    10. Saya menambahkan unit test di file tests.py aplikasi main. Test ini bertujuan untuk menguji apakah produk berhasil ditambahkan dan ditampilkan dengan benar dan menjalankan perintah :
            'python manage.py test'
    11. Setelah aplikasi berjalan dengan baik di lokal, saya men-deploy aplikasi ke PWS (Pacil Web Service)
    12. Selesai
    
#2 Bagan Django
   <img width="1224" height="1540" alt="Bagan_Django" src="https://github.com/user-attachments/assets/d4ba1a31-dd25-4159-81da-55021c7acea9" />
   
#3 Peran settings.py
    menyimpan konfigurasi utama untuk aplikasi Django, dan berfungsi mengatur berbagai hal mulai dari pengaturan aplikasi, database, keamanan, hingga pengelolaan file statis dan media, supaya aplikasi bisa berjalan dengan baik, misal:
    - Untuk pengaturan umum aplikasi 
        pada bagian DEBUG, ini menentukan apakah aplikasi berjalan dalam mode pengembangan (True) atau produksi (False)
        Pada bagian ALLOWED_HOSTS, menentukan doamin yang diizinkan untuk mengakses aplikasi
        Pada bagian INSTALLED_APPS: Daftar aplikasi yagn digunakan dalam proyek, ini termasuk apliaksi Django default
    - Untuk pengaturan Database
        DATABASES, mengonfigurasi database yagn digunakan, apakah menggunakan SQLite, atau yang lainnya. Ini juga mengatur seperti nama database, user, password, dan host
    - Pengaturan Static dan Media Files
        STATIC_URL : Menentukan URL dan lokasi file statik (seperti gambar, CSS, dan JavaScript) yang digunakan aplikasi
    - Pengaturan Keamanan
        SECRET_KEY: Kunci rahasia yang digunakan Django untuk keamanan, seperti tanda tangan digital
    - Pengaturan Middleware
        MIDDLEWARE: Daftar middleware yang menangani request dan response aplikasi. Middleware ini bisa mengelola berbagai hal seperti keamanan, sesi, dan header respons
    - Pengaturan Templating
        TEMPLATES: Menentukan pengaturan template, termasuk direktori tempat Django mencari file HTML dan pengaturan mesin templating yang digunakan untuk merender tampilan
    - Pengaturan URL
        ROOT_URLCONF: Menentukan modul Python yang berisi konfigurasi URL routing utama untuk aplikasi
    - Pengaturan Waktu dan Lokalisasi
        LANGUAGE_CODE dan TIME_ZONE: Mengonfigurasi bahasa dan zona waktu default aplikasi.
        USE_I18N dan USE_L10N: Menentukan apakah aplikasi mendukung internasionalisasi dan lokalisasi

#4 Cara kerja migrasi database Django
    1. Menulis model di models.py diaman semua perubahan atau penambahan struktur data yang ingin dibuat seperti tabel kolom atau relasi antar tabel. Misalnya membuat model product dengan kolom name, price, description
    2. Setelah membuat atau mengubah model, kita menjalankan command:
        'python manage.py makemigrations'
    yang akan membuat file migrasi dimana mencatat perubahan yang dibuat di model, seperti menambah tabel atau kolom baru di database
    3. Setelah membuat migrasi, kita bisa memperbarui database dengan command:
        'python manage.py migrate'
    4. Selanjutnya setelah migrasi, kita bisa memeriksa apakah perubahan yang kita buat sudah diterapkan ke database
    5. Jika ada perubahan lain yang ingin dilakukan ke model, kita bisa update models.py, membuat migrasi baru, dan jalankan migrate lagi.


#5 Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Django dipilih sebagai framework untuk pemula karena menyediakan banyak fitur bawaan yang siap digunakan, seperti sistem autentikasi, admin interface, dan pengelolaan database, sehingga pemula bisa fokus pada pengembangan aplikasi tanpa perlu membangun semuanya dari awal. Dengan menggunakan pola MVT (Model-View-Template) yang terstruktur, Django memisahkan logika aplikasi, tampilan, dan data dengan jelas, yang membuat kode lebih mudah dipahami dan dikelola

#6 Feedback terhadap asisten dosen
    Asisten dosen sangat membantu dalam memandu saya melalui setiap tahap tutorial 0-1. Selama proses, asdos selalu siap dan responsif dalam memberikan solusi terhadap permasalahan yang saya hadapi, baik selama tutorial maupun pengerjaan tugas. Respon yang diberikan sangat memudahkan saya untuk memahami materi dan membantu progres belajar saya. Terimakasih asdos 


TUGAS 3
#1 Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data delivery merupakan proses pengiriman data dari satu komponen ke komponen lain dalam sebuah platform. Data delivery dibutuhkan karena:
    1.Tanpa data delivery, platform tidak bisa berjalan karena komponen tidak dapat saling bertukar informasi
    2.Menjamin data yang tersimpan di server sama dengan yang diterima oleh pengguna
    3.Memberikan pengalaman pengguna yang lancar dengan pengiriman data yang cepat dan juga optimal
    4.Melindungi data sensitif dengan enkripsi agar tidak mudah bocor saat dikirimkan
    5.Mendukung pertumbuhan jumlah pengguna tanpa menurunkan performa sistem

#2 Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    JSON lebih populer dan lebih banyak dipakai dibanding XML untuk kebutuhan modern, khususnya di web dan API karena :
    1. Format JSON lebih singkat, tidak perlu tag buka-tutup seperti XML
    2. Struktur JSON mirip objek di JavaScript, jadi lebih gampang dipahami programmer
    3. Ukuran kecil jadi lebih hemat bandwidth
    Sehingga JSON lebih baik untuk kebutuhan modern karena parsing cepat, ringan, dan mudah dipakai. Namun, XML tetap relevan di kasus khusus yang butuh struktur dan validasi yang ketat

#3 Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
    `is_valid()` dipakai untuk check apakah data yang dimasukan ke form sudah sesuai dengan aturan validasi yang sudah ditentukan
    - Untuk cara kerja `is_valid()` itu sendiri :
        - Jika semua input valid, `is_valid()` mengembalikan `True`.  
        - Jika ada input yang tidak sesuai, `is_valid()` mengembalikan `False` dan form akan menampilkan error
    - `is_valid()` dibutuhkan untuk :
        1. memastikan data yang masuk sesuai format (misalnya email valid, angka dalam rentang yang benar, dll)
        2. data yang tidak valid tidak akan diproses ke tahap selanjutnya
        3. mencegah input aneh/berbahaya masuk ke sistem
        4. memberikan feedback yang jelas jika ada kesalahan input

#4 Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    - `csrf_token` (Cross-Site Request Forgery token) adalah fitur keamanan yang mencegah serangan CSRF, yaitu serangan di mana penyerang memanfaatkan sesi login user untuk melakukan aksi tanpa izin user
    - Jika form tidak menggunakan `csrf_token`, penyerang bisa membuat website palsu yang mengirim request ke aplikasi kita atas nama user yang sedang login, sehingga data bisa diubah atau aksi berbahaya dilakukan tanpa sepengetahuan user. Contoh: transfer uang, mengganti password, atau menghapus data tanpa sepengetahuan user
    - Hal tersebut dapat dimanfaatkan oleh penyerang dengan cara
    1. User login ke aplikasi asli 
    2. Penyerang mengarahkan user ke halaman palsu
    3. Halaman palsu tersebut mengirim request ke server aplikasi dengan identitas user
    4. Server salah mengira request itu asli karena tidak ada validasi token

#5 Step-by-step Implementasi Checklist Tugas
    1. Membuat views di `main/views.py` untuk:
     - Menampilkan daftar produk (halaman utama)
     - Menampilkan detail produk
     - Menambah produk (form)
     - Menampilkan data produk dalam format XML, JSON, XML by ID, dan JSON by ID
    2. Menambahkan URL pattern di `main/urls.py` untuk semua views di atas, lalu meng-include `main/urls.py` di `football_shop/urls.py`.
    3. Membuat file HTML di `main/templates/` untuk halaman utama, form tambah produk, dan detail produk.
       Menambahkan tombol "Add Product" dan "Read More" pada halaman utama.
    4. Menjalankan server lokal, menguji semua fitur (tambah, lihat, detail, XML/JSON)
    5. deploy aplikasi ke PWS.
    6. Menulis README
    7. Selesai





