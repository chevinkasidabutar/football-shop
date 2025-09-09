# BolaBaleStore

Nama : Chevinka Queen Cilia Sidabutar
Kelas : PBP-F
NPM : 2406437376
Link : https://chevinka-queen-footballshop.pbp.cs.ui.ac.id 


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
    Link: [https://drive.google.com/file/d/1BJAZjQ8Tiu6UcU5Sp_MxMqZ__Opp6tD-/view?usp=sharing]

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