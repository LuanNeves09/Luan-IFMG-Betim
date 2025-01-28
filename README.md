# Redes-Transporte-TP


# Trabalho Prático: Explorando a Camada de Transporte do Modelo TCP/IP

## Objetivo
Neste trabalho, os alunos irão explorar a camada de transporte do modelo TCP/IP, utilizando e modificando um servidor Python disponível no repositório GitLab: [Acessar Repositório](https://gitlab.betim.ifmg.edu.br/virgil.almeida/redes-transporte-tp). O objetivo é aprofundar o entendimento sobre o funcionamento do protocolo TCP e do HTTP, analisar conexões e pacotes utilizando o Wireshark, e implementar funcionalidades adicionais para o servidor, garantindo compatibilidade com um navegador (browser) como cliente.

## Referências
- [RFC 7230 - Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing](https://datatracker.ietf.org/doc/html/rfc7230)  
- [Introdução ao Protocolo HTTP - MDN Web Docs](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview)  
- [Wireshark - HTTP Traffic Analysis](https://wiki.wireshark.org/HTTP)  

## Atividades

1. **Preparação do Ambiente**
   - Clone o repositório fornecido e configure o ambiente de desenvolvimento.
   - Familiarize-se com o código do servidor Python para entender como ele responde às solicitações de um cliente HTTP.

2. **Análise com o Wireshark**
   - Utilize o Wireshark para monitorar o tráfego de rede gerado pelo servidor.
   - Acesse o servidor utilizando um navegador como cliente (por exemplo, Chrome ou Firefox).
   - Identifique:
     - As conexões TCP abertas.
     - As sequências de pacotes trocadas durante o envio de arquivos de tamanhos variados.

3. **Implementação de Funcionalidades**
   - Modifique o servidor para:
     - Atender solicitações HTTP de navegadores, fornecendo arquivos de diferentes tamanhos.
     - Garantir que o envio e recebimento de dados sejam compatíveis com as expectativas de um cliente HTTP.
   - Certifique-se de que os dados transferidos sejam corretamente exibidos no navegador.

4. **Avaliação de Segurança**
   - Analise as vulnerabilidades potenciais na implementação do servidor HTTP.

## Entrega
Cada grupo deverá entregar:
- Relatório contendo:
  - Capturas de tela do Wireshark, destacando as conexões TCP abertas e as sequências de pacotes observadas durante solicitações HTTP no navegador.
  - Explicação detalhada das alterações implementadas no código do servidor.
  - Discussão sobre as vulnerabilidades identificadas e as melhorias sugeridas.
- Código modificado, com comentários explicativos, em um repositório próprio ou na forma de arquivo compactado.

## Prazo de Entrega
Data apresentada no AVA

## Critérios de Avaliação
- **Funcionamento do servidor modificado:** (50%)  
- **Análise detalhada no Wireshark:** (20%)  
- **Qualidade do relatório:** (20%)  
- **Discussão sobre segurança e melhorias propostas:** (10%)    


## Projeto base

https://www.codementor.io/@joaojonesventura/building-a-basic-http-server-from-scratch-in-python-1cedkg0842