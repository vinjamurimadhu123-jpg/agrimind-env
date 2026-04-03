# 🌾 AgriMindEnv – AI Farming Decision Environment

## 🚀 Overview

AgriMindEnv is a real-world AI training environment that simulates farming decision-making.

Farmers often face uncertainty in:
- Crop selection
- Weather changes
- Market price fluctuations

This environment allows AI agents to learn how to make optimal farming decisions using real-world signals.

---

## 🎯 Objective

Train an AI agent to:
- Select the best crop
- Choose proper farming techniques
- Maximize profit under uncertainty

---

## 🧠 Observation Space

The agent receives:

- Soil Type
- Weather Data (rainfall, temperature)
- Market Prices
- Budget

---

## ⚙️ Action Space

The agent must decide:

- Crop selection
- Fertilizer type
- Irrigation method
- Selling time

---

## 🎮 Tasks

### 🟢 Easy
- Choose best crop

### 🟡 Medium
- Crop + fertilizer + irrigation

### 🔴 Hard
- Full decision-making:
  - Crop
  - Fertilizer
  - Irrigation
  - Selling strategy

---

## 🏆 Reward Function

Reward is based on:

- Profit (primary factor)
- Sustainability
- Risk handling

Score range: 0.0 – 1.0

---

## 🧪 Grading

Each task includes a deterministic grader:
- Evaluates agent performance
- Produces reproducible scores

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python inference.py