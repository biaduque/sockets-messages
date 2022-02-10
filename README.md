# sockets-messages
Repositório com projeto de chat desenvolvido através da comunicação de sockets em Python

**→ Criação de um chat mensagem com python** 

- Para configurar o cliente e o servidor, utilizei o comando ipconfig no cmd, para assim, verificar o endereço ip da minha máquina

```bash
ipconfig
```

### Sobre a execução:

*Ao rodar o cliente e o servidor, temos um exemplo de **Chat ping pong**, onde o servidor fica disponível e esperando alguma solicitação do cliente.*

### Conclusões

- O P2P em Python é mais simples e rápido para gerar os resultados, porém, sabe-se que a aplicação UDP apesar de rápida, pode apresentar suas desvantagens, devido à alta dependência entre cliente e servidor e a fragilidade de perda de pacotes entre eles, já que não acontece nenhuma verificação
- O P2P tanto em Python, nesse exemplo, apresenta indexação por ***flooding***, visto que varios clientes podem se comunicar com um único servidor.

*** 

***Tutorial seguido:***

[https://www.youtube.com/watch?v=IbzGL_tjmv4](https://www.youtube.com/watch?v=IbzGL_tjmv4)
