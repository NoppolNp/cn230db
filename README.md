# Stock Price Change Analyzer

## Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [Features](#features)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Database Schema](#database-schema)

## Overview
ในตลาดหุ้นนั้นการหาจุดที่ดีที่สุดในการซื้อเป็นเรื่องที่สำคัญเพราะจะทำให้เราสร้างรายได้ได้ แต่ทำยังไงถึงจะรู้ได้หละว่าควรซื้อเมื่อไหร่? หนึ่งในวิธีการนั้นก็คือการหาcycleของหุ้นตัวนั้นๆและวิธีหาcycleวิธีการหนึ่งก็คือการหาช่วงที่มีการเปลี่ยนแปลงของราคาอย่างรวดเร็วนั่นเอง โปรเจกต์นี้จึงจัดอันดับเดือนที่มีปการเปลี่ยนแปลงของราคามากที่สุด 5 อันดับแรก เพื่อเป็นการหาช่วงที่ดีในการซื้อหุ้นอต่ละตัวเก็บไว้นั่นเอง

## Purpose
    -เพื่อศึกษาวิธีการดึงข้อม฿ลโดยใช้requests ใน python
    -เพื่อศึกษาการใช้งานsqlite3
    -เพื่อสร้างเครื่องมือประยุกต์ที่สามารถนำไปใช้จริงได้

## Features
    - สามารถเลือกหุ้นได้ว่าจะดูตัวไหน เปลี่ยนได้ที่ dataCreator.py ตัวแปร symbol
    - สามารถเลือกช่วงวันที่ที่ต้องการได้ เปลี่ยนได้ที่ dataCreator.py ตัวแปร start_date, end_date

## Usage
    - run dataCreator.py เพื่อสร้าง database ไฟล์ (polygon_stock_data.db)
    - run mosChange.py เพื่อดูว่า5อันดับเดือนที่ราคาเปลี่ยนมากที่สุด(percentage)

## Dependencies
    Python 3.8+
    SQLite3 (standard with Python)
    requests (install via pip)

## Database Schema
Table: stock_prices
| Column | Type               | Description               |
| ------ | ------------------ | ------------------------- |
| date   | TEXT (Primary Key) | Trading date (ISO format) |
| open   | REAL               | Opening stock price       |
| close  | REAL               | Closing stock price       |

