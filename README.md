# BiasDetector-PT 🔍

**Automated bias detection workflow for LLM outputs in Brazilian Portuguese**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Powered by Claude](https://img.shields.io/badge/Powered%20by-Claude%20AI-orange.svg)](https://anthropic.com)

> *"Building responsible AI requires humans in the loop with real judgment."*  
> — Flávia Silva, Senior AI Trainer & RLHF Specialist

---

## 🌍 Why This Project Exists

There are several bias detection tools for English. **There are none specifically designed for Brazilian Portuguese** — with culturally relevant examples, Brazilian regional context, and documentation in PT-BR.

This project fills that gap.

Built by a Senior AI Trainer with 9+ years of professional RLHF and AI ethics review experience at Invisible Technologies, One Forma, Lionbridge, Appen, and Telus International.

---

## 🎯 What It Does

BiasDetector-PT is an **automated multi-turn workflow** that:

1. Receives any LLM-generated text in Portuguese
2. Analyzes it across **6 bias categories** specific to the Brazilian context
3. Generates a **structured report** with scores, problematic excerpts, and suggestions
4. Supports **follow-up questions** via multi-turn conversation
5. Exports results as **JSON** for integration into larger pipelines

---

## 📊 Bias Categories

| Category | Description | Severity |
|---|---|---|
| 🚻 **Viés de Gênero** | Gender stereotypes and exclusionary language | HIGH |
| 🌍 **Viés Racial/Étnico** | Racial or ethnic stereotypes | HIGH |
| 💰 **Viés Socioeconômico** | Class-based assumptions | MEDIUM |
| 🗺️ **Viés Regional Brasileiro** | Brazilian regional stereotypes (Norte, Nordeste, Sul) | MEDIUM |
| 🔄 **Viés de Confirmação** | Presenting only confirming evidence | MEDIUM |
| ⚡ **Viés de Confiança Excessiva** | Overconfident claims — hallucination risk | HIGH |

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/bias-detector-pt.git
cd bias-detector-pt
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your API key
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 4. Run interactive mode
```bash
python src/bias_detector.py
```

### 5. Or use programmatically
```python
from src.bias_detector import analyze_bias, format_report

text = "Homens naturalmente têm mais aptidão para programação."
analysis = analyze_bias(text, context="Texto de RH gerado por IA")
print(format_report(analysis))
```

---

## 📋 Output Example

```
============================================================
  BiasDetector-PT — Relatório de Análise
============================================================

🚨 AVALIAÇÃO GERAL: REPROVADO
   Score: 8/10
   Texto contém viés de gênero severo e viés regional moderado.

📊 ANÁLISE POR CATEGORIA:
----------------------------------------

  Viés de Gênero
  Status: DETECTADO (score: 9/10)
  Trecho: "Homens naturalmente têm mais aptidão para programação"
  Sugestão: "Pessoas com interesse em lógica têm aptidão para programação..."

  Viés Regional Brasileiro  
  Status: Não detectado

💡 RECOMENDAÇÕES:
  • Remover afirmações sobre aptidões naturais baseadas em gênero
  • Usar linguagem neutra e inclusiva
  • Basear afirmações em evidências, não em estereótipos
============================================================
```

---

## 🔄 Multi-Turn Workflow

BiasDetector-PT supports **multi-turn conversations** — after an analysis, you can ask follow-up questions:

```
> Analisar texto
[analysis runs]

> Por que o viés de gênero é problemático neste contexto específico?
[detailed explanation]

> Como eu reescreveria o parágrafo dois para ser mais inclusivo?
[suggested rewrite]
```

---

## 🏗️ Architecture

```
bias-detector-pt/
├── src/
│   └── bias_detector.py      # Core analysis engine + multi-turn workflow
├── examples/
│   └── usage_examples.py     # 4 real-world examples with expected outputs
├── docs/
│   ├── bias-taxonomy-pt.md   # Full bias taxonomy with Brazilian examples
│   ├── methodology.md        # How the scoring system works
│   └── use-cases.md          # Real-world use cases and integrations
├── tests/
│   └── test_examples.md      # Test cases with expected results
├── requirements.txt
└── README.md
```

---

## 🎯 Use Cases

- **AI Training Teams** — QA check before including LLM outputs in training datasets
- **Content Teams** — Review AI-generated content before publication
- **HR Departments** — Audit AI-generated job descriptions and HR communications
- **Researchers** — Systematic bias evaluation in Brazilian Portuguese NLP models
- **Journalism** — Fact-checking AI-assisted article generation

---

## 📚 Documentation

- [Bias Taxonomy (PT-BR)](docs/bias-taxonomy-pt.md) — Full taxonomy with Brazilian examples
- [Methodology](docs/methodology.md) — How scoring works
- [Use Cases](docs/use-cases.md) — Integration examples

---

## 🤝 Contributing

Contributions welcome — especially:
- Additional bias categories relevant to the Brazilian context
- Example datasets
- Integration with other tools (n8n, Zapier, etc.)

---

## 👩‍💻 Author

**Flávia Silva**  
Senior AI Trainer & RLHF Specialist  
9+ years at Invisible Technologies, One Forma, Lionbridge, Appen, Telus International  
📧 flavia_marinelli@hotmail.com  
📍 Rio de Janeiro, Brazil

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*This project was built from real-world AI ethics evaluation experience — not from theory.*
