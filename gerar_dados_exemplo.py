"""Gera um backup .json de exemplo (dados 100% fictícios) para importar no painel.

Uso:
    python gerar_dados_exemplo.py
    -> cria dados_exemplo/backup-exemplo.json

No painel: Configurações > "Importar backup (.json)" e escolha o arquivo gerado.
"""
import json
import random
from datetime import date, datetime, timedelta
from pathlib import Path

random.seed(2026)
ANO = date.today().year
MES_ATUAL = date.today().month  # meses futuros ficam em branco

CONTAS = [
    ("BB C/C 1234-5", "Conta Corrente", "BB"),
    ("CEF C/C 00001-2", "Conta Corrente", "CEF"),
    ("Itaú C/C 12345-6", "Conta Corrente", "Itaú"),
    ("Bradesco C/C 54321-0", "Conta Corrente", "Bradesco"),
    ("Santander C/C 12-345678", "Conta Corrente", "Santander"),
    ("Bradesco Poupança 54321-0", "Poupança", "Bradesco"),
    ("Itaú Investimento Automático", "Investimento", "Itaú"),
    ("BB RF LP Corporativo", "Investimento", "BB"),
    ("Santander FIC FI Referenciado DI", "Investimento", "Santander"),
    ("XP - Investimentos C/C 1000000", "Investimento", "XP"),
    ("Safra CDB", "Investimento", "Safra"),
    ("BTG Pactual Investimento", "Investimento", "BTG"),
]

contas = [
    {"id": f"c{i}", "nome": n, "ident": "", "agencia": "", "tipo": t, "instituicao": inst,
     "ativo": True, "ordem": i}
    for i, (n, t, inst) in enumerate(CONTAS, start=1)
]

registros = {}
for c in contas:
    for mes in range(12):  # 0 = Jan ... 11 = Dez
        if mes + 1 > MES_ATUAL:
            continue
        ultimo = mes + 1 == MES_ATUAL
        sorteio = random.random()
        base = date(ANO, mes + 1, 1)
        solic = base + timedelta(days=random.randint(1, 8))
        receb = solic + timedelta(days=random.randint(1, 9))
        if c["tipo"] == "Poupança" and sorteio < 0.4:
            status, ds, dr = "na", "", ""
        elif ultimo and sorteio < 0.30:
            status, ds, dr = "solicitado", solic.isoformat(), ""
        elif ultimo and sorteio < 0.40:
            status, ds, dr = "pendente", solic.isoformat(), ""
        else:
            status, ds, dr = "enviado", solic.isoformat(), receb.isoformat()
        registros[f"{ANO}|{c['id']}|{mes}"] = {
            "status": status, "dataSolic": ds, "dataReceb": dr,
            "responsavel": "", "obs": "",
            "alterado": datetime(ANO, mes + 1, 15, 10, 0).isoformat() + ".000Z",
        }

dados = {
    "contas": contas,
    "registros": registros,
    "config": {"dias": 10, "modo": "destacar", "responsavel": "", "tema": "claro",
               "ultimoBackup": None,
               "escalada": "Para extratos não fornecidos em até 15 dias corridos, contatar o gerente de relacionamento "
                           "solicitando a segunda via em OFX / PDF, com cópia para a auditoria externa."},
    "ano": ANO,
    "versaoBase": 2,
}

saida = Path(__file__).resolve().parent / "dados_exemplo" / "backup-exemplo.json"
saida.parent.mkdir(exist_ok=True)
saida.write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(contas)} contas, {len(registros)} registros -> {saida}")
