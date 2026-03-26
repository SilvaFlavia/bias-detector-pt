# 🔍 BiasDetector-PT

**Automated bias detection workflow for LLM outputs in Brazilian Portuguese**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![AI-Powered](https://img.shields.io/badge/AI-LLM%20Powered-orange.svg)]()

> *"Building responsible AI requires humans in the loop with real judgment."*  
> — Flávia Silva, Senior AI Trainer & RLHF Specialist

---

## 🌍 Why This Project Exists

Most bias detection tools are designed for **English-language outputs**.

There is a critical gap for **Brazilian Portuguese (PT-BR)** — especially when considering:

- Cultural nuance  
- Regional diversity  
- Local linguistic patterns  
- Brazilian social context  

**BiasDetector-PT** was created to address this gap.

Built from extensive experience in **large-scale AI training, evaluation, and ethics review workflows**.

---

## 🎯 What It Does

BiasDetector-PT is a **multi-turn automated workflow** that:

1. Receives LLM-generated text in Portuguese  
2. Evaluates across **6 bias categories**  
3. Generates a **structured report**  
4. Supports **follow-up questions**  
5. Outputs results as **JSON**  

---

## 📊 Bias Categories

| Category | Description | Severity |
|----------|------------|----------|
| 🚻 Viés de Gênero | Gender stereotypes | HIGH |
| 🌍 Viés Racial/Étnico | Racial/ethnic bias | HIGH |
| 💰 Viés Socioeconômico | Class assumptions | MEDIUM |
| 🗺️ Viés Regional Brasileiro | Regional stereotypes | MEDIUM |
| 🔄 Viés de Confirmação | One-sided reasoning | MEDIUM |
| ⚡ Confiança Excessiva | Overconfidence / hallucination risk | HIGH |

---

## 🚀 Quick Start

### Clone repository

git clone https://github.com/YOUR_USERNAME/bias-detector-pt.git  
cd bias-detector-pt  

---

### Install dependencies

pip install -r requirements.txt  

---

### Set API key

export ANTHROPIC_API_KEY="your-api-key-here"  

---

### Run

python src/bias_detector.py  

---

### Programmatic usage

from src.bias_detector import analyze_bias, format_report  

text = "Homens naturalmente têm mais aptidão para programação."  
analysis = analyze_bias(text)  

print(format_report(analysis))  

---

## 📋 Output Example

BiasDetector-PT — Relatório de Análise  

AVALIAÇÃO GERAL: REPROVADO  
Score: 8/10  

Viés de Gênero: DETECTADO  
Trecho: "Homens naturalmente têm mais aptidão..."  

Sugestão:  
"Pessoas com interesse em lógica..."  

---

## 🔄 Multi-Turn Workflow

Exemplo:

> Analisar texto  
> Por que isso é viés?  
> Como reescrever?  

---

## 🏗️ Architecture

bias-detector-pt/  
├── src/  
│   └── bias_detector.py  
├── examples/  
├── docs/  
├── tests/  
├── requirements.txt  
└── README.md  

---

## 🎯 Use Cases

- AI Training Teams  
- Content Review  
- HR & Recruiting  
- NLP Research  
- Journalism  

---

## 📚 Documentation

docs/bias-taxonomy-pt.md  
docs/methodology.md  
docs/use-cases.md  

---

## 🤝 Contributing

Contributions welcome:

- New bias categories  
- Datasets  
- Integrations  

---

## 👩‍💻 Author

Flávia Silva  
Senior AI Trainer & RLHF Specialist  

📍 Rio de Janeiro, Brazil  
🌍 Remote global  
📧 flavia_marinelli@hotmail.com  

Experience:

- Senior AI Trainer — large-scale AI programs  
- AI Annotator — multilingual projects  
- AI Evaluation Specialist — LLM systems  

---

## 📄 License

MIT License  

---

*Built from real-world AI evaluation experience.*
