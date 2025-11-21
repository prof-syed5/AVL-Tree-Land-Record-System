# **_Project Report: Land Records Management System (AVL Tree)_**

**_Student:_** Syed Nalain Abbas (102) — 3B

**_Course:_** Data Structures and Algorithms

## **_1. Problem Statement_**

Develop a land-record management system that supports efficient insertion, searching, deletion, and sorted listing of land plots. An AVL Tree ensures balanced height and fast operations even as the dataset grows.

## **_2. Objectives_**

Implement an AVL Tree to maintain balance and guarantee O (log n) operations.

Provide core features: Add, Search, Delete, and List (Sorted).

Use object-oriented programming with proper encapsulation.

## **_Data Structures Used_**

**``AVL Tree:``** A self-balancing BST ensuring O(log n) insert, search, and delete.

## **_Design & Implementation_**

**_PlotRecord:_** Dataclass storing plot information.

**_AVLNode:_** Private node class containing key, value, height, left & right pointers.

**_AVLTree:_** Handles rotations, balancing, insert/delete/search, and inorder traversal.

**_LandRecordsManager:_** Wraps AVLTree and exposes user-friendly functions.

**_Index Modes_**

**_Plot Number_** (unique key)

**_Area (duplicates allowed)_** → tie-break using plot number

## **_Complexity Analysis_**

**``Insertion:``** O(log n)

**``Search:``**

Indexed key → O(log n)

Non-indexed key → O(n)

**``Deletion:``** O(log n)

**``Space:``** O(n)

## **_Demo Steps / Test Cases_**

1. Start program → choose indexing mode (Plot/Area).

2. Add multiple land records.

3. List all records → sorted output shown.

4. Search by plot or area.

5. Delete records (leaf, one child, two children).

## **_Edge Cases_**

Duplicate plot number (plot mode) → Error.

Searching a missing key → “Not found.”

## **_Future Enhancements_**

GUI using Tkinter or Streamlit.

SQLite-based storage for large datasets.

Range queries, pagination, and multi-key sorting.
