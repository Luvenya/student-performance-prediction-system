# Student Performance Prediction System

## Group 9

**Project No. 6 – Student Performance Prediction System (ML)**

### Group Members

1. **LUVENYA A/P NUEKEY NICHOLAS** — BIT 2410-1699
2. **RIFA MOST NAFISA ISLAM** — BIT 2410-2048
3. **SHAHAD MUAAZ** — BIT 2410-2468
4. **SHIAM MD OBIDUR RAHMAN** — BIT 2410-2050

---

## Project Description

The **Student Performance Prediction System** is a machine learning-based system designed to predict student academic performance and identify students who may be at academic risk.

The system uses student academic data to classify students into different risk levels and provides AI-generated intervention recommendations to support timely academic assistance.

---

## Main Objectives

* Predict student academic performance using machine learning.
* Identify students who may be at **Low, Medium, or High academic risk**.
* Identify important academic risk factors.
* Generate personalized intervention recommendations using AI.
* Provide an application/dashboard for viewing student risk information.
* Support academic advisors in making timely intervention decisions.

---

## System Features

* Student performance prediction.
* Academic risk classification.
* Student information and performance analysis.
* Risk factor identification.
* AI-generated intervention recommendations.
* Academic risk dashboard/application.
* Model evaluation using standard machine learning metrics.
* Testing and validation of core system features.

---

## Technologies Used

* **Python**
* **Scikit-learn**
* **Pandas**
* **Google Colab / Jupyter Notebook**
* **Streamlit**
* **Google Gemini API**
* **JSON**
* **GitHub**

---

## Machine Learning Model

The system uses a **Random Forest Classifier** to classify students into three academic risk levels:

* **Low Risk**
* **Medium Risk**
* **High Risk**

The model uses relevant student academic features such as:

* Average assessment score
* Assessment count
* Studied credits
* Number of previous attempts

The dataset is divided into training and testing sets using an **80/20 stratified split**.

### Model Configuration

* Algorithm: Random Forest Classifier
* Number of trees: 200
* Random state: 42
* Class weighting: Balanced

### Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Classification report
* Confusion matrix

---

## AI Workflow

The system integrates an AI workflow to generate academic intervention recommendations.

### Workflow

```text
Student Risk Data
       ↓
Risk Factor Identification
       ↓
Knowledge Base Retrieval
       ↓
Integrated Prompt
       ↓
Google Gemini
       ↓
Intervention Recommendation
```

The AI recommendation component is designed to provide professional, supportive, non-judgmental, and action-oriented recommendations based on the student's identified risk factors.

---

## Knowledge Base

The system uses a **Student Academic Intervention Knowledge Base** containing risk levels, risk factors, intervention rules, and advisor guidance.

The main risk levels are:

* **Low Risk** – Routine monitoring
* **Medium Risk** – Early intervention
* **High Risk** – Immediate intervention

Potential risk factors include academic performance, attendance, missed assignments, and participation.

---

## Dataset

The project uses the **Open University Learning Analytics Dataset (OULAD)**.

The dataset contains information related to students, courses, assessments, registration, and student assessment performance.

Relevant dataset files include:

* `studentInfo.csv`
* `studentRegistration.csv`
* `courses.csv`
* `assessments.csv`
* `studentAssessment.csv`

> Dataset files are stored in the `data/` directory.

---

## Repository Structure

```text
student-performance-prediction-system/
│
├── app/
│   ├── frontend/
│   └── backend/
│
├── data/
│   └── Dataset files
│
├── docs/
│   ├── report/
│   ├── slides/
│   └── poster/
│
├── model/
│   ├── Trained model
│   └── Model training files
│
├── notebook/
│   └── Jupyter/Colab notebooks
│
├── result/
│   ├── Evaluation results
│   ├── Tables
│   └── Figures
│
├── src/
│   └── Source and utility code
│
├── test/
│   └── Testing files
│
├── LICENSE
├── README.md
└── requirements.txt
```

### Folder Descriptions

| Folder      | Description                                                 |
| ----------- | ----------------------------------------------------------- |
| `app/`      | Main application, including frontend and backend components |
| `data/`     | Dataset and data-related files                              |
| `docs/`     | Project report, presentation slides, and poster             |
| `model/`    | Trained machine learning model and model training files     |
| `notebook/` | Jupyter/Google Colab notebooks and experiments              |
| `result/`   | Model evaluation results, tables, and figures               |
| `src/`      | Supporting source code, preprocessing, and utility code     |
| `test/`     | System and model testing files                              |

---

## Project Timeline

* **Week 1:** Planning and Data Collection
* **Week 2:** Model and AI Integration
* **Week 3:** Application Development
* **Week 4:** Evaluation and Finalization
* **Week 5:** Presentation

---

## Project Deliverables

The final project includes:

* **Final Application/System**
* **Project Report**
* **Presentation Slides**
* **Project Poster/Infographic**
* **Machine Learning Model**
* **AI Workflow and Intervention Recommendation System**
* **Testing and Evaluation Results**

---

## Project Status

**Current Stage: Evaluation and Finalization**

The system prototype and core machine learning/AI components have been developed. The project is currently focused on integrating the final application components, testing the system, evaluating performance, completing documentation, and preparing the final presentation materials.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Luvenya/student-performance-prediction-system.git
```

Navigate to the project directory:

```bash
cd student-performance-prediction-system
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## Running the Application

The application can be run using the project's application entry point.

Example:

```bash
streamlit run app.py
```

> The exact command may be updated according to the final application structure.

---

## Team

**Group 9 – Project No. 6**

Student Performance Prediction System (ML)
