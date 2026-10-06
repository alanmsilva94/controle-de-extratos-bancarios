# Controle de Extratos Bancários

Painel web de **controle mensal de recebimento de extratos** (contas correntes, poupanças e investimentos), feito em **um único arquivo HTML** com CSS e JavaScript puros. Sem servidor, sem dependências, sem build: abra o `index.html` no navegador e os dados ficam salvos no próprio navegador.

> **Dados 100% fictícios.** As contas, números e datas deste repositório são inventados. O projeto não tem vínculo com nenhuma instituição real.

## Funcionalidades

- **Grade anual**: uma linha por conta e uma coluna por mês, com o status de cada extrato (Não solicitado, Solicitado, Enviado, Pendente, Não se aplica). Clique na célula para avançar o status ou edite datas e observações.
- **Pendências**: lista dos extratos atrasados segundo a regra configurável (dias após a solicitação), com opção de destacar ou filtrar.
- **Progresso por mês**: percentual de extratos recebidos em cada competência.
- **Contas**: cadastro de contas (nome, tipo, instituição, identificador), ordenação por tipo e ativação/inativação. O tipo e a instituição são detectados pelo nome da conta.
- **Seleção em lote**: marque várias células e aplique um status de uma vez ("Marcar enviado").
- **Filtros e busca**, **tema claro/escuro** e **impressão** da grade.
- **Backup e dados**: exportar e importar backup (`.json`), exportar a grade em `.csv` e apagar todos os dados do navegador.
- **Exercícios por ano**: troque o ano na barra superior; cada ano tem o seu histórico.

## Como usar

1. Baixe o repositório (ou só o `index.html`) e abra no navegador. Não precisa de internet, exceto pela fonte Inter (Google Fonts), que tem alternativa do sistema.
2. Para ver o painel preenchido, gere os dados de exemplo e importe-os:

   ```bash
   python gerar_dados_exemplo.py          # cria dados_exemplo/backup-exemplo.json
   ```

   No painel: **Configurações → Backup e dados → Importar backup (.json)** e escolha `dados_exemplo/backup-exemplo.json`. (Já existe uma cópia pronta na pasta `dados_exemplo/`.)
3. Para usar com as suas contas, edite a constante `CONTAS_BASE` no início do script do `index.html` ou cadastre pelo botão **Nova conta**.

> Os dados ficam no `localStorage` do navegador (chave `controle-extratos-v1`). Faça backups periódicos pelo botão **Fazer backup agora**.

## Estrutura

```
controle-de-extratos-bancarios/
├── index.html                 aplicação completa (HTML + CSS + JS)
├── gerar_dados_exemplo.py     gera um backup fictício para demonstração
├── dados_exemplo/
│   └── backup-exemplo.json    backup fictício pronto para importar
├── LICENSE
└── README.md
```

## Tecnologias

HTML5 · CSS3 (variáveis, tema claro/escuro, grid) · JavaScript (ES2020, sem frameworks) · `localStorage` · Python 3 (apenas para gerar os dados de exemplo)

## Segurança e privacidade

- Nenhum dado sai do navegador: não há requisições a servidores próprios nem envio de informações.
- Não há contas, números, e-mails ou chaves reais no repositório.

## Licença

MIT — veja [LICENSE](LICENSE).
