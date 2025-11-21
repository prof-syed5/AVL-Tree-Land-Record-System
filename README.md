# AVL-Tree-Land-Record-System
Land Records Management System using AVL Tree — a Python-based DSA project for storing, searching, deleting and displaying land plots with balanced tree operations.

## Overview

The Land Records Management System is a Lab Project built using Python with a custom AVL Tree implementation and a Streamlit GUI. The system manages land plot records efficiently using the self-balancing AVL Tree structure.

This project ensures fast operations — O(log n) time complexity for insert, search, delete, and traversal.

## Features

- Add new land record

- Search record by Plot Number

- Delete record

- View all sorted records (AVL inorder traversal)

- Streamlit-based GUI frontend

-  Pure Data Structures (NO CSV / NO Database)

- Clean, modular, object-oriented backend


## Tech Stack

- Python 3.10+

- Streamlit (Frontend)

- Dataclasses

- AVL Tree Implementation

- OOP Concepts


## Project Structure

- Land-Records-Management-AVL
  -  app.py                      # Streamlit GUI interface
  -  land_Recod-Management.py        # Backend AVL Tree logic
  -  README.md                   # Documentation file
  -  Project_Report.md         # Viva/report documentation

## How to Run the Project

1️- Install Dependencies

pip install streamlit

2️- Run the Streamlit App

streamlit run app.py

The browser will automatically launch the UI.


## Backend Logic (AVL Tree)

The project uses a self-balanced AVL Tree to store land records. AVL is chosen due to:

- Fast searching

- Automatic height balancing

- Rotations (LL, RR, LR, RL)

- Predictable time complexity


Operations implemented:

- Insert Node

- Delete Node

- Left/Right Rotation

- Balance Factor Check

- Inorder Traversal

- Search by Key (Plot Number)


## Streamlit Interface

The GUI allows the user to:

- Enter plot details

- View structured tables

- Get search results in readable format

- Perform delete operations


The frontend and backend communicate through the LandRecordsManager class.


## Learning Outcomes

By building this project, the student learns:

- AVL Tree fundamentals

- Self-balancing tree logic

- OOP design patterns

- GUI integration with backend logic

- Practical implementation of DSA concepts


## Developer

Syed Nalain Abbas (Prof.SYED)

Superior University Lahore

A hardworking student who implemented AVL Tree integration with Streamlit to create a fully functional DSA project.


## Support

If this project helped you:

⭐ Give a star on GitHub
