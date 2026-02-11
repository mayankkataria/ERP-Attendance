# ERP Attendance Management System

## Overview
This is a **role-based Attendance Management Web Application** built using **Bootstrap** in the frontend, **Python-Django** in the backend, and **PostgreSQL/SQLite** as the database deployed via **Docker** container. The application includes separate Admin and Employee panels where admins can manage employees through full **CRUD operations**, and employees can mark their attendance using **clock in/out functionality**. It also supports **session-based authentication** and **cookie management**, **pagination** for large records handling, and **PDF generation** for downloading attendance reports.

**Functionalities:**
- CRUD operations
- Authentication
- Search and filter
- Form validations
- AJAX implementation
- Download PDF
- Pagination
- Responsive design

## Credentials
**Superuser (admin) -**

Username - root

Password - Password1!

> You can also create your own superuser with command ``` docker-compose run web python manage.py createsuperuser ```

## 🚀 Launch App
Run ```docker-compose up``` and open [live app here](http://127.0.0.1:8000/)

## How to use
- Login with superuser credentials to open admin panel
- Then add employees from admin panel
- Logout from admin panel
- Login to employee panel by adding username of added employee and password as ```Arcgate1!```


## Application Demo Videos

[All samples](https://loom.com/invite/5d1cd534b3e946eba576de806df5862d)

### 1. Sign Up (Form Validations)

https://user-images.githubusercontent.com/52576282/180981795-bf72d08c-a6ac-46c0-99c2-5878ff6e68fb.mp4

<br>

### 2. Mark Attendance & Download PDF

https://user-images.githubusercontent.com/52576282/180981935-c434cde2-d526-44e8-9e43-691ebf35b193.mp4

<br>

### 3. Search & Filter

https://user-images.githubusercontent.com/52576282/180982046-3bdf39bd-52d6-45d1-a283-d6e1ce597247.mp4

<br>

### 4. Employee Panel

https://user-images.githubusercontent.com/52576282/180982144-650d6c4e-cedf-4d31-bc0e-d038a8cf927d.mp4

<br>

### 5. Sessions

https://user-images.githubusercontent.com/52576282/180982206-18df2301-2331-4c2e-9c49-4fae41bb8f81.mp4

<br>

### 6. Cookies

https://user-images.githubusercontent.com/52576282/180982397-2a2667b8-cd9f-4ed7-9e5e-a91ecaad8ab7.mp4
