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

The system uses student academic data to classify students into **Low, Medium, or High academic risk** levels and provides AI-generated intervention recommendations to support timely academic assistance.

---

## Main Objectives

* Predict student academic performance using machine learning.
* Identify students who may be at **Low, Medium, or High academic risk**.
* Identify important academic risk factors.
* Generate personalized intervention recommendations using AI.
* Provide an application for viewing student risk information.
* Support academic advisors in making timely intervention decisions.

---

## System Features

* Student performance prediction.
* Academic risk classification.
* Student information and performance analysis.
* Risk factor identification.
* AI-generated intervention recommendations.
* Academic risk dashboard/application.
* Machine learning model evaluation.
* System testing and validation.
* User testing and evaluation.

---

## Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **Streamlit**
* **Google Gemini API**
* **Google Colab / Jupyter Notebook**
* **JSON**
* **GitHub**
* **Git LFS** for the trained machine learning model

---

## Machine Learning Model

The system uses a **Random Forest Classifier** to classify students into three academic risk levels:

* **Low Risk**
* **Medium Risk**
* **High Risk**

### Model Features

The model uses relevant student academic features, including:

* Average assessment score
* Assessment count
* Studied credits
* Number of previous attempts

The dataset is divided into training and testing sets using an **80/20 stratified split**.

### Model Configuration

| Parameter        | Value                    |
| ---------------- | ------------------------ |
| Algorithm        | Random Forest Classifier |
| Number of Trees  | 200                      |
| Random State     | 42                       |
| Class Weight     | Balanced                 |
| Train/Test Split | 80/20                    |
| Target Classes   | Low, Medium, High        |

### Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Classification report
* Confusion matrix

The confusion matrix and other evaluation outputs are stored in the `results/` directory.

---

## AI Workflow

The system integrates an AI workflow to generate academic intervention recommendations based on the predicted student risk level and identified risk factors.

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

The AI recommendation component is designed to provide recommendations that are:

* Professional
* Supportive
* Non-judgmental
* Action-oriented
* Based on identified student risk factors

---

## Knowledge Base

The system uses a **Student Academic Intervention Knowledge Base** containing risk levels, risk factors, intervention rules, and advisor guidance.

### Risk Levels

* **Low Risk** – Routine monitoring
* **Medium Risk** – Early intervention
* **High Risk** – Immediate intervention

Potential risk factors include:

* Academic performance
* Attendance
* Missed assignments
* Student participation

The knowledge base is used together with the AI workflow to generate appropriate intervention recommendations.

---

## Dataset

The project uses the **Open University Learning Analytics Dataset (OULAD)**.

The dataset contains information related to students, courses, assessments, registration, and student assessment performance.

### Dataset Files

The following OULAD files are included in the `data/` directory:

* `OULAD.names`
* `studentInfo.csv`
* `studentRegistration.csv`
* `courses.csv`
* `assessments.csv`
* `studentAssessment.csv`
* `vle.csv`

> **Note:** The dataset is used for academic and project purposes as part of the student performance prediction system.

---

## Repository Structure

```text
student-performance-prediction-system/
│
├── app/
│   ├── .gitkeep
│   ├── ai_workflow_integration.py
│   ├── api_integration.py
│   ├── app.py
│   ├── knowledge_base_preparation.py
│   ├── llm_service.py
│   ├── ml_model_training_and_performance_evaluation.py
│   ├── model.py
│   ├── prompt_engineering.py
│   └── prototype.py
│
├── data/
│   ├── .gitkeep
│   ├── OULAD.names
│   ├── assessments.csv
│   ├── courses.csv
│   ├── studentAssessment.csv
│   ├── studentInfo.csv
│   ├── studentRegistration.csv
│   └── vle.csv
│
├── docs/
│   ├── AI Poster.pdf
│   ├── AI Project.pptx
│   └── Report.pdf
│
├── models/
│   ├── .gitkeep
│   └── risk_model.pkl
│
├── notebooks/
│   └── .gitkeep
│
├── results/
│   ├── .gitkeep
│   ├── User Testing.docx
│   └── confusion matrix
│
├── src/
│   └── .gitkeep
│
├── tests/
│   └── .gitkeep
│
├── .gitignore
└── README.md
```

### Folder Descriptions

| Folder       | Description                                                                  |
| ------------ | ---------------------------------------------------------------------------- |
| `app/`       | Main application, machine learning, AI workflow, and supporting Python files |
| `data/`      | OULAD dataset files used by the system                                       |
| `docs/`      | Final project report, presentation slides, and poster                        |
| `models/`    | Trained machine learning model                                               |
| `notebooks/` | Jupyter/Google Colab notebooks and experiments                               |
| `results/`   | Model evaluation results and user testing documentation                      |
| `src/`       | Reserved for additional reusable source and utility modules                  |
| `tests/`     | System and model testing files                                               |

---

## Results and Testing

The project includes model evaluation and system testing results.

The `results/` directory contains:

* **Confusion Matrix** – visualization of the model classification results.
* **User Testing.docx** – documentation of user testing and system feedback.

These results support the evaluation of the machine learning model and the overall system functionality.

---

## Project Documentation

The `docs/` directory contains the final project documentation:

* **Report.pdf** – Final project report
* **AI Project.pptx** – Project presentation slides
* **AI Poster.pdf** – Project poster/infographic

---

## Project Timeline

* **Week 1:** Planning and Data Collection
* **Week 2:** Initial Prototype and AI/ML Development
* **Week 3:** Application Development, AI Workflow Integration, and Core Feature Testing
* **Week 4:** Evaluation, Documentation, and Finalization
* **Week 5:** Final Presentation

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
* **User Testing Documentation**

---

## Project Status

**Current Stage: Evaluation and Finalization**

The Student Performance Prediction System has been developed with machine learning prediction, academic risk classification, AI-based intervention recommendations, and an application interface.

The project has also been tested and evaluated. Final documentation, presentation materials, poster, user testing results, and model evaluation results have been prepared.

The repository contains the project source code, dataset, documentation, evaluation results, and trained machine learning model.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Luvenya/student-performance-prediction-system.git
```

### 2. Navigate to the Project Directory

```bash
cd student-performance-prediction-system
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

> If using a virtual environment, activate the environment before installing the required packages.

---

## Running the Application

From the project root directory, run:

```bash
streamlit run app/app.py
```

The Streamlit application will start locally and provide access to the student performance prediction system.

---

## Machine Learning Model

The trained model is stored in:

```text
models/risk_model.pkl
```

Because the trained model file is larger than GitHub's normal file-size limit, **Git LFS** is used to manage the model file.

---

## Team

**Group 9 – Project No. 6**

**Student Performance Prediction System (ML)**

---
