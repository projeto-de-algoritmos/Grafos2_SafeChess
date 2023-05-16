# Safe Chess

**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/013181  |  Adne Moretti Moreira |
| 20/018205  |  Gabriel Moretti de Souza |

## Sobre
Esse projeto tem como objetivo realizar um pequeno jogo, em que o jogador terá um tabuleiro de xadrez de tamanho alterável, onde poderá escolher a posição de algumas peças do time branco e irá visualizar um caminho seguro para o rei percorrer sem estar sob ataque dessas peças. O destino e início do caminho do rei são também definidos pelo jogador. Neste jogo as peças do time branco não poderão se mover.

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação 
**Linguagem**: Python<br>
**Framework**: --<br>

Para rodar o projeto basta rodar o arquivo python com o comando: 

```python main.py```

E iniciar inserindo os seus valores. 

## Uso 
Seguindo o explicado anteriormente, no tópico Sobre, o jogador primeiro irá definir o tamanho do tabuleiro **N**, de no mínimo 4, o inserindo na entrada.
Logo após, o jogador poderá escolher o número de peças do time branco, que está limitado entre 1 e N. Após inserir esse número, o jogador irá inserir suas posições, juntamente ao tipo de peça que será inserido determinado pela sua sigla, dentro de algumas opções disponibilizadas. 

Após a inserção dessas posições, o jogador poderá escolher qual seria a posição em que o rei do time preto se encontra. Caso essa posição já esteja sob ataque de alguma peça do time inimigo, o jogo já se encerra, retornando "Fim de Jogo".

Caso a posição esteja segura, o jogador agora deverá inserir qual seria a posição de destino do rei.

Por fim, o jogo irá retornar se esse caminho seria possível, e, caso for, retornará qual é esse caminho, demonstrando as casas do tabuleiro de xadrez as quais o rei passou para alcançar seu destino.
