"""
BiasDetector-PT — Exemplos de Uso
===================================
Examples demonstrating how to use BiasDetector-PT programmatically.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from bias_detector import analyze_bias, format_report

# ── EXAMPLE 1: Gender Bias ──────────────────────────────────────────────────
example_1 = {
    "text": """
    Para liderança em tecnologia, procuramos candidatos com perfil assertivo e decisivo.
    Homens naturalmente têm mais facilidade com raciocínio lógico e programação.
    Mulheres são melhores para funções de suporte e atendimento ao cliente.
    """,
    "context": "Descrição de vaga de emprego gerada por LLM"
}

# ── EXAMPLE 2: Clean Text (should PASS) ─────────────────────────────────────
example_2 = {
    "text": """
    Para liderança em tecnologia, buscamos pessoas com habilidades de comunicação,
    resolução de problemas e trabalho em equipe. Valorizamos perspectivas diversas
    e experiências variadas. Candidatos de todos os backgrounds são encorajados a aplicar.
    """,
    "context": "Descrição de vaga de emprego revisada"
}

# ── EXAMPLE 3: Regional + Socioeconomic Bias ────────────────────────────────
example_3 = {
    "text": """
    Nordestinos geralmente têm dificuldades com pontualidade e organização profissional.
    Profissionais do Sul do Brasil são reconhecidamente mais eficientes e qualificados.
    Para cargos de liderança, prefira candidatos de grandes centros urbanos.
    """,
    "context": "Orientação de RH gerada por IA"
}

# ── EXAMPLE 4: Overconfidence Bias ──────────────────────────────────────────
example_4 = {
    "text": """
    É cientificamente comprovado que pessoas introvertidas são menos produtivas em equipes.
    Com certeza absoluta, trabalho remoto sempre reduz a criatividade dos funcionários.
    Definitivamente, líderes extrovertidos têm melhores resultados de negócios.
    """,
    "context": "Artigo sobre gestão de pessoas"
}


def run_examples():
    """Run all examples and display reports."""
    
    examples = [
        ("Viés de Gênero em Vaga de Emprego", example_1),
        ("Texto Revisado — Deve ser APROVADO", example_2),
        ("Viés Regional e Socioeconômico", example_3),
        ("Viés de Confiança Excessiva", example_4),
    ]
    
    for title, example in examples:
        print(f"\n{'#'*60}")
        print(f"EXEMPLO: {title}")
        print(f"{'#'*60}")
        
        analysis = analyze_bias(
            text=example["text"],
            context=example["context"]
        )
        
        print(format_report(analysis))
        
        input("Pressione Enter para o próximo exemplo...")


if __name__ == "__main__":
    run_examples()
