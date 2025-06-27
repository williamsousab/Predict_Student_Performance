<div align="center">
<img src="https://github.com/williamsousab/Predict_Student_Performance/blob/main/images/dataset-cover.jpg?raw=true" width="700px" />
</div>

## Análise Exploratória de Dados (EDA)

# 🎓 Predict Student Performance

Projeto de análise e predição de desempenho acadêmico com base em fatores socioeconômicos, hábitos de estudo, sono e frequência. Desde a exploração dos dados até a criação de uma API e dashboard interativo.

---

## 📁 Dataset

- Fonte: [Kaggle – Predict Student Performance Dataset](https://www.kaggle.com/datasets/stealthtechnologies/predict-student-performance-dataset)
- Atributos:
  - `Study Hours`
  - `Sleep Hours`
  - `Socioeconomic Score`
  - `Attendance (%)`
  - `Grades` (target)

---

## 🔍 Análise Exploratória de Dados (EDA)

- Estatísticas descritivas com `pandas`
- Visualizações com `matplotlib` e `seaborn` (histogramas, densidade, boxplots)
- Matriz de correlação → forte relação entre `Study Hours` e `Grades` (corr = 0.81)
- Regressão Linear Múltipla com `statsmodels`

---

## 🧠 Modelos de Machine Learning

### 🔹 Regressão Linear
- R²: 0.74
- MSE: 19.27

### 🔹 Random Forest Regressor
- R²: 0.98 ✅
- MSE: 1.44

### 🔧 Ajuste de Hiperparâmetros
- Utilização de `GridSearchCV` para otimizar Random Forest
- Validação Cruzada com `cross_val_score`

---

## 🛠️ Tecnologias e Bibliotecas

- Python 3.11+
- `pandas`, `numpy`
- `seaborn`, `matplotlib`
- `scikit-learn`, `statsmodels`
- `Flask` (API REST)
- `Dash` (Interface de Previsão)
- `joblib` (salvar modelos treinados)

---

## 🚀 Funcionalidades

- Treinamento e avaliação de modelos preditivos
- Exportação do modelo em `.pkl` para uso em produção
- API REST para prever notas com dados novos
- Dashboard `Dash` com entrada de dados em tempo real

---
