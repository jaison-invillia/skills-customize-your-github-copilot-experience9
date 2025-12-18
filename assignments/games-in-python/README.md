# 🎮 Jogos em Python — Forca (Hangman)

## 🎯 Objetivo

Desenvolver uma versão do jogo Forca em Python para praticar manipulação de strings, estruturas de repetição, condicionais e entrada do usuário.

## 📝 Tarefas

### 🛠️ Implementar o jogo principal

#### Descrição
Implemente a lógica do jogo Forca: escolha aleatória de palavra, recepção de palpites de letra, exibição do progresso atual e controle do número de tentativas.

#### Requisitos
O programa concluído deve:

- Selecionar palavras aleatoriamente a partir de uma lista pré-definida
- Aceitar palpites de letras e mostrar o progresso no formato _ _ _ (underscores para letras não reveladas)
- Rastrear e mostrar letras já tentadas (corretas e incorretas)
- Controlar o número de tentativas restantes e terminar o jogo quando acabarem
- Exibir mensagens claras de vitória ou derrota

### 🛠️ Recursos extras (opcionais)

#### Descrição
Adicione funcionalidades opcionais para praticar programação adicional.

#### Requisitos opcionais

- Implementar modos de dificuldade (ex.: mais/menos tentativas)
- Permitir carregar/salvar uma lista de palavras a partir de um arquivo `data.csv`
- Mostrar dicas ou permitir adivinhar a palavra inteira

## 💡 Dicas

- Use `random.choice()` para selecionar a palavra
- Separe a lógica do jogo em funções (ex.: `selecionar_palavra()`, `mostrar_progresso()`, `verificar_palpite()`)
- Valide a entrada do usuário (letras únicas, caracteres válidos)

## ▶️ Como executar

Abra um terminal no diretório `assignments/games-in-python` e execute:

```bash
python3 starter-code.py
```

Se você preferir um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 starter-code.py
```

## 📎 Entregáveis

- Código fonte modificado `starter-code.py` (ou seu próprio arquivo `.py`)
- Este `README.md` atualizado descrevendo como executar e o que foi implementado

## 📅 Data de entrega

Data configurada: 2025-11-18

## 📚 Recursos

- Use o arquivo `data.csv` na pasta `assignments/data-analysis` como exemplo de leitura de arquivos CSV, caso implemente carregamento de palavras a partir de CSV.

# 🎮 Hangman Game Challenge

Build the classic word-guessing game using Python strings, loops, and user input.

## � What You'll Build

Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

**Skills practiced:** String manipulation, loops, conditionals, random selection

## ✅ Must Have's

Your game must:
- Randomly select words from a predefined list
- Accept letter guesses and show current progress (_ _ _ format)
- Track incorrect guesses remaining
- End when word is guessed or attempts exhausted
- Display win/lose messages
