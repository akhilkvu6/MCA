
# 📘 README

<div align="center">

# 🖥️ E25_InstallationOfLaravel

### NSA Lab – Installation of Laravel

</div>

---

# 🎯 Aim

To install and configure the Laravel PHP framework on Ubuntu using Apache, MariaDB, PHP, and Composer.

---

# 📘 Introduction

Laravel is a modern open-source PHP web application framework used for developing secure, scalable, and dynamic web applications.

Laravel provides:

* elegant syntax
* MVC architecture
* database abstraction
* authentication
* routing
* dependency management
* testing support

Laravel is widely used for:

* web applications
* REST APIs
* enterprise applications
* e-commerce systems
* content management systems

---

# 🧠 What is Laravel?

Laravel is a PHP framework developed for simplifying web application development.

It follows the:

* MVC (Model View Controller) architecture

Laravel handles:

* routing
* database operations
* authentication
* session management
* caching
* security

---

# ⚙️ Features of Laravel

## 📌 Elegant Syntax

Easy and readable code structure.

---

## 📌 MVC Architecture

Separates:

* business logic
* presentation
* database operations

---

## 📌 Built-in Authentication

Provides secure login and registration systems.

---

## 📌 Database ORM (Eloquent)

Simplifies database interaction using models.

---

## 📌 Blade Templating Engine

Powerful template engine for frontend development.

---

## 📌 Artisan CLI

Command-line tool for Laravel operations.

---

## 📌 Security Features

Protection against:

* SQL Injection
* CSRF attacks
* XSS attacks

---

# ❓ Why Laravel?

Laravel is popular because it is:

* scalable
* secure
* developer-friendly
* fast to develop
* well documented

The experiment manual highlights Laravel as:

* Progressive Framework
* Scalable Framework
* Community Framework

---

# 📈 Advantages of Laravel

## 🚀 Progressive Framework

Large documentation and tutorials help beginners learn easily.

---

## 📊 Scalable Framework

Supports high traffic applications using:

* Redis
* caching
* queue systems

---

## 🌍 Community Support

Large global developer community and packages ecosystem.

---

# ⚙️ System Requirements

Before installing Laravel, ensure:

| Requirement         | Purpose            |
| ------------------- | ------------------ |
| Ubuntu/Linux        | Operating System   |
| Apache              | Web Server         |
| PHP                 | Backend Language   |
| MariaDB/MySQL       | Database           |
| Composer            | Dependency Manager |
| Internet Connection | Download packages  |

---

# 🪜 Step 1: Install Apache Web Server

Apache is used to host Laravel applications.

## 📌 Install Apache

```bash id="m4x8qp"
sudo apt install apache2
```

---

## 📌 Start Apache Service

```bash id="v7n2zk"
sudo systemctl start apache2
```

---

## 📌 Verify Apache Status

```bash id="q9p1wr"
sudo systemctl status apache2
```

---

# 🌐 What is Apache?

Apache is a web server responsible for:

* handling HTTP requests
* serving web pages
* hosting websites

---

# 🧩 Step 2: Install PHP and Extensions

Laravel requires PHP and several extensions.

## 📌 Install PHP Packages

```bash id="x5m2vq"
sudo apt install php php-cli php-common php-mbstring php-xml php-zip php-mysql php-pgsql php-sqlite3 php-json php-bcmath php-gd php-tokenizer php-xmlwriter
```

---

# 📦 Important PHP Extensions

| Extension    | Purpose            |
| ------------ | ------------------ |
| php-cli      | PHP command line   |
| php-mysql    | MySQL connectivity |
| php-xml      | XML processing     |
| php-json     | JSON handling      |
| php-mbstring | Multi-byte strings |
| php-gd       | Image processing   |

---

# 🗄️ Step 3: Install MariaDB Database Server

MariaDB is used as the database server.

## 📌 Install MariaDB

```bash id="k3v8zp"
sudo apt install mariadb-server
```

---

# 🧠 What is MariaDB?

MariaDB is an open-source relational database system derived from MySQL.

Used for:

* storing application data
* database management
* SQL query execution

---

# 🔐 Login to MariaDB

```bash id="p7n1wr"
sudo mysql -u root -p
```

---

# 🗃️ Create Database

```sql id="t4m9qx"
CREATE DATABASE laravel_db;
```

---

# 👤 Create Database User

```sql id="v8x2zk"
CREATE USER 'laravel_user'@'localhost' IDENTIFIED BY 'secretpassword';
```

---

# 🔓 Grant Permissions

```sql id="m2q7vp"
GRANT ALL ON laravel_db.* TO 'laravel_user'@'localhost';
```

---

# 💾 Save Privileges

```sql id="x9p4wr"
FLUSH PRIVILEGES;
```

---

# 🚪 Exit Database

```sql id="q5n8zk"
QUIT;
```

---

# 📦 Step 4: Install Composer

Composer is the dependency manager for PHP.

---

# 🧠 What is Composer?

Composer manages:

* PHP packages
* libraries
* dependencies

Laravel installation depends on Composer.

---

# 📌 Download Composer

```bash id="u4m7xp"
curl -sS https://getcomposer.org/installer | php
```

---

# 📌 Move Composer

```bash id="p8x2vq"
sudo mv composer.phar /usr/local/bin/composer
```

---

# 📌 Give Execute Permission

```bash id="v3n7zk"
sudo chmod +x /usr/local/bin/composer
```

---

# 📌 Verify Composer

```bash id="m6q1wr"
composer --version
```

---

# 🚀 Step 5: Install Laravel

Install Laravel using Composer.

## 📌 Navigate to Web Root

```bash id="x2v8qp"
cd /var/www/html
```

---

# 📌 Install Laravel Project

```bash id="k7m4zx"
sudo composer create-project laravel/laravel laravelapp
```

---

# 📌 Navigate to Project Folder

```bash id="q3x9vp"
cd laravelapp
```

---

# 🧠 Laravel Directory Structure

| Directory | Purpose                 |
| --------- | ----------------------- |
| app       | Application logic       |
| routes    | Route definitions       |
| public    | Public accessible files |
| resources | Views and assets        |
| config    | Configuration files     |
| database  | Database migrations     |

---

# ⚙️ Step 6: Configure Apache for Laravel

Apache virtual host configuration is required.

---

# 📌 Create Virtual Host File

```bash id="v5m2qw"
sudo vim /etc/apache2/sites-available/laravelapp.conf
```

---

# 📌 Virtual Host Configuration

```apache id="p4x7zn"
<VirtualHost *:80>

    ServerName your-domain-or-ip

    DocumentRoot /var/www/html/laravelapp/public

    <Directory /var/www/html/laravelapp>
        AllowOverride All
    </Directory>

</VirtualHost>
```

---

# 🔧 What is Virtual Host?

Virtual host allows Apache to:

* host multiple websites
* manage domains separately
* configure site-specific settings

---

# 📌 Enable Apache Rewrite Module

```bash id="t9m1qp"
sudo a2enmod rewrite
```

---

# 📌 Enable Virtual Host

```bash id="x6v3wr"
sudo a2ensite laravelapp.conf
```

---

# 📌 Restart Apache

```bash id="m8q2vx"
sudo systemctl restart apache2
```

---

# 🌐 Step 7: Run Laravel in Browser

Open browser and enter:

```text id="v4x7zp"
http://server-ip
```

If installation is successful, Laravel welcome page appears.

---

# 🔍 Verify Laravel Installation

## 📌 Check Laravel Version

```bash id="q1m8wr"
php artisan --version
```

---

# 📌 Run Laravel Development Server

```bash id="x5q2vp"
php artisan serve
```

---

# 📌 Default Laravel URL

```text id="m9v4zk"
http://127.0.0.1:8000
```

---

# 🧠 Important Laravel Commands

| Command                       | Purpose              |
| ----------------------------- | -------------------- |
| `php artisan serve`           | Start Laravel server |
| `php artisan migrate`         | Run migrations       |
| `php artisan make:model`      | Create model         |
| `php artisan make:controller` | Create controller    |
| `composer install`            | Install dependencies |

---

# 🔒 Security Features of Laravel

Laravel provides:

* CSRF protection
* Password hashing
* Authentication system
* SQL injection protection
* Route protection

---

# 📂 Laravel Workflow

```text id="p7x1wr"
Client Request
       ↓
Apache Web Server
       ↓
Laravel Routing
       ↓
Controller
       ↓
Model / Database
       ↓
View Response
```

---

# ✅ Advantages of Laravel

* Easy to learn
* Secure framework
* MVC architecture
* Large community support
* Fast development
* Built-in authentication
* Scalable applications

---

# ❌ Limitations

* Requires PHP knowledge
* Hosting configuration needed
* Slightly slower than lightweight frameworks

---

# 📚 Viva Questions

## 1️⃣ What is Laravel?

Laravel is an open-source PHP web application framework.

---

## 2️⃣ What is Composer?

Composer is a dependency manager for PHP.

---

## 3️⃣ What is MVC architecture?

MVC separates application into:

* Model
* View
* Controller

---

## 4️⃣ What is Artisan?

Artisan is Laravel’s command-line tool.

---

## 5️⃣ What is Apache?

Apache is a web server used to host websites.

---

## 6️⃣ What is MariaDB?

MariaDB is a relational database management system.

---

## 7️⃣ What is the purpose of `php artisan serve`?

It starts Laravel development server.

---

## 8️⃣ Why is `AllowOverride All` used?

It enables `.htaccess` functionality.

---

## 9️⃣ What is Laravel routing?

Routing maps URLs to application logic.

---

## 🔟 Why is Laravel popular?

Because it is secure, scalable, and developer-friendly.

---

# 🎓 Result

Thus, Laravel framework was installed and configured successfully on Ubuntu using Apache, PHP, Composer, and MariaDB.
