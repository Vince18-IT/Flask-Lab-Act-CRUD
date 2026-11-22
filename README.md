# SCHOOL v1.0 — Student Management System

A full-stack Student Information Management web application built with **Python Flask**, **SQLite3**, **W3.CSS**, and **Webcam.js**, featuring complete CRUD functionality and real-time webcam photo capture.

## Features

- **User Authentication:** Session-based login and logout protection (`alpha@uc.com`, `bravo@uc.com`, `charlie@uc.com`).
- **Full Student CRUD:** Create, view, edit, and delete student records (`ID No.`, `Lastname`, `Firstname`, `Course`, `Level`, and `Image`).
- **Two-Column Registration Page (`/register`):** Real-time input preview syncing paired with a live `4:3` mirrored webcam snapshot capture.
- **Modal-Based Add & Edit (`/main`):** Quick-entry modals with integrated webcam capture, retake toggle, and non-destructive photo updates.
- **Automatic Image Management:** Decodes Base64 snapshots into `static/images/<idno>.jpg`, stores relative paths in SQLite, and removes orphaned image files upon student deletion.

## Tech Stack

- **Backend:** Python 3, Flask
- **Database:** SQLite3 (`db/school.db`)
- **Frontend:** HTML5, Jinja2, W3.CSS (`static/w3.css`), JavaScript
- **Camera Capture:** Webcam.js (`static/js/webcam.min.js`)

## Project Structure

```text
Flask-Lab-Act-CRUD/
├── db/
│   ├── dbhelper.py
│   └── school.db
├── static/
│   ├── images/
│   ├── js/
│   │   └── webcam.min.js
│   └── w3.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── main.html
│   └── register.html
└── app.py
