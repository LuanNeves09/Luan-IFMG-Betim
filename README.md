# Laboratório de Redes: Servidor HTTP & Camada de Transporte

> **Disciplina:** Redes de Computadores  
> **Tema:** Protocolo TCP/IP e HTTP Sockets  

## Sobre o Projeto
Este projeto consiste na implementação e modificação de um **Servidor Web (HTTP) utilizando Sockets em Python**. O objetivo principal é analisar o comportamento da Camada de Transporte (TCP) através do monitoramento de pacotes no **Wireshark**.

Para tornar a análise visual e interativa, foi desenvolvido um **Dashboard Front-End** que permite simular diferentes cenários de tráfego de rede (transferência de arquivos pequenos, imagens e grandes volumes de dados).

---

## Funcionalidades Implementadas

### Backend (Python)
- **Sockets TCP/IP:** Implementação pura sem frameworks web (como Flask/Django).
- **Suporte a Arquivos Binários:** Modificação do código original para permitir leitura de imagens (`.jpg`, `.png`) utilizando modo `rb`.
- **MIME Types Dinâmicos:** Identificação automática do tipo de arquivo para envio do cabeçalho `Content-Type` correto.
- **Tratamento de Erros:** Respostas HTTP 404 personalizadas.

### Frontend (Dashboard)
- **Interface Interativa:** Painel para disparo de requisições.
- **Cache Busting:** Script JS para forçar novas conexões TCP a cada clique (evitando cache do navegador).
- **Cenários de Teste:**
  1.  **Ping Rápido:** Arquivo de texto minúsculo (Handshake + Push simples).
  2.  **Mídia:** Carregamento de imagem (Teste de integridade de dados binários).
  3.  **Fluxo Intenso:** Download de arquivo grande (>5MB) para visualização de *Janelas Deslizantes* e *Segmentação TCP*.

---

## Estrutura do Projeto

```text
├── server.py           # O código fonte do Servidor (Socket)
├── README.md           # Documentação
└── htdocs/             # Arquivos públicos (Site)
    ├── index.html      # O Dashboard
    ├── style.css       # Estilos visuais
    ├── script.js       # Lógica de requisição
    ├── pequeno.txt     # Payload de teste leve
    ├── medio.jpg       # Payload de teste binário
    ├── favicon.ico     # Ícone exibido na aba do navegador 
    └── grande.txt      # Payload de teste pesado (Gerado automaticamente)