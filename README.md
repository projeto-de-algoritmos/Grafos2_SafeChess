# Safe Chess

**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/0013181  |  Adne Moretti Moreira |
| 20/0018205  |  Gabriel Moretti de Souza |

## Sobre
Esse projeto tem como objetivo realizar um pequeno jogo, em que o jogador terá um tabuleiro de xadrez de tamanho alterável, onde poderá escolher a posição de algumas peças do time branco e irá visualizar um caminho seguro para o rei percorrer sem estar sob ataque dessas peças. O destino e início do caminho do rei são também definidos pelo jogador. Neste jogo as peças do time branco não poderão se mover.

## Screenshots
![Screenshot from 2023-05-16 01-39-40](https://github.com/projeto-de-algoritmos/Grafos2_SafeChess/assets/78612945/1febe828-a0f4-46b2-80ef-982b38133835)
![Screenshot from 2023-05-16 01-42-47](https://github.com/projeto-de-algoritmos/Grafos2_SafeChess/assets/78612945/47bd3337-3c83-406a-a954-a9bffe8f7cb5)
![Screenshot from 2023-05-16 01-38-55](https://github.com/projeto-de-algoritmos/Grafos2_SafeChess/assets/78612945/7fd22d08-c009-4c33-bd71-d0dbf9175e70)
![Screenshot from 2023-05-16 01-38-13](https://github.com/projeto-de-algoritmos/Grafos2_SafeChess/assets/78612945/e5a0b4b1-5a54-445a-961a-aa2784f7c554)

## Vídeo

[https://youtu.be/Z9l9epaKuWE](https://youtu.be/Z9l9epaKuWE)

## Instalação 
**Linguagem**: Python<br>
**Framework**: --<br>

Para rodar o projeto basta rodar o arquivo python com o comando: 

```python main.py```

ou

```python3 main.py```

E iniciar inserindo os seus valores. 

## Uso 
Seguindo o explicado anteriormente, no tópico Sobre, o jogador primeiro irá definir o tamanho do tabuleiro **N**, o inserindo na entrada.
Logo após, o jogador poderá escolher o número de peças do time branco. Após inserir esse número, o jogador irá inserir suas posições, juntamente ao tipo de peça que será inserido determinado pelo seu nome, dentro de algumas opções disponibilizadas. 

Após a inserção dessas posições, o jogador poderá escolher qual seria a posição em que o rei do time preto se encontra. Caso essa posição já esteja sob ataque de alguma peça do time inimigo, o jogo já se encerra, retornando "Fim de Jogo".

O jogador agora deverá inserir qual seria a posição de destino do rei.

Por fim, o jogo irá retornar se esse caminho seria possível, e, caso for, retornará qual é esse caminho, demonstrando as casas do tabuleiro de xadrez as quais o rei passou para alcançar seu destino.
