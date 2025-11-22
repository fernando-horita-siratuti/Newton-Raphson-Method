# Newton-Raphson Method — Python Implementation

![Python](https://img.shields.io/badge/python-3.8%2B-blue)

Group project of Computational Numerical Methods about the **Newton-Raphson Method** algorithm in Python.  
Finds roots of a real-valued function using symbolic differentiation (SymPy) and iterative numerical approximation.  
Designed for learning, experiments and small demonstrations of root-finding algorithms.

---

## Table of Contents
- [Highlights](#highlights)  
- [Requirements](#requirements)  
- [Quickstart](#quickstart)  
- [Repository Structure](#repository-structure)  
- [How It Works](#how-it-works) 
- [Example Test](#example-test)
- [Contact us](#contact-us)

---

## Highlights
- Uses **SymPy** for automatic symbolic differentiation (no need to calculate derivatives manually).
- **Dynamic Precision:** The output formatting automatically adjusts the number of decimal places based on the chosen `epsilon` (error tolerance).
- Focused on **clarity and readability**.

---

## Requirements
- Python 3.8+  
- **SymPy** library.

---

## Quickstart

```bash
# clone the repository
git clone https://github.com/fernando-horita-siratuti/Newton-Raphson.git

# install dependencies
pip install sympy
pip install math

# run the project
python3 main.py
````

-----

## Repository Structure

```bash
Newton-Raphson/
├─ functions.py          # Core Newton-Raphson algorithm implementation
├─ main.py               # User interface and execution script
└─ README.md             # Project documentation
```

-----

## How It Works

  - **Input Parsing:** Takes a mathematical function string (e.g., `x**2 - 9`) and converts it into a SymPy object.
  - **Symbolic Differentiation:** Automatically calculates the derivative f'(x) using calculus rules.
  - **Precision Calculation:** Determines the necessary decimal places based on the `epsilon` value ($log_{10}$ scale).
  - **Iteration:** Applies the formula $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ until the estimated error is smaller than epsilon or max iterations are reached.

-----

## Example Test

### Input:

```text
Informe a função f(x): x**2 - 2
Informe o valor inicial de x: 10
Informe o valor de epsilon: 0.00001
Informe o número máximo de iterações: 20
```

### Output:

```text
---------- Início do Método de Newton-Raphson ----------

Iteração 0: x = 10.00000, f(x) = 98.00000, Erro estimado = 4.90000

Iteração 1: x = 5.10000, f(x) = 24.01000, Erro estimado = 2.35392

Iteração 2: x = 2.74608, f(x) = 5.54095, Erro estimado = 1.00888

Iteração 3: x = 1.73719, f(x) = 1.01785, Erro estimado = 0.29296

Iteração 4: x = 1.44424, f(x) = 0.08582, Erro estimado = 0.02971

Iteração 5: x = 1.41453, f(x) = 0.00088, Erro estimado = 0.00031

Iteração 6: x = 1.41421, f(x) = 0.00000, Erro estimado = 0.00000

Raiz encontrada: x = 1.41421 após 7 iterações.
```

-----

## Contact us

<div align="center">
  <br><br>
     <i>Fernando Horita Siratuti - Undergraduate - 4th Semester, Computer Engineering @ CEFET-MG</i>
  <br><br>
  
  [![Gmail][gmail-badge]][gmail-autor2]
  [![Linkedin][linkedin-badge]][linkedin-autor2]
  [![GitHub][github-badge]][github-autor2]
  [![Instagram][instagram-badge]][instagram-autor2]
  
  <br><br>
     <i>Hugo Henrique Marques - Undergraduate - 4th Semester, Computer Engineering @ CEFET-MG</i>
  <br><br>
  
  [![Gmail][gmail-badge]][gmail-autor3]
  [![Linkedin][linkedin-badge]][linkedin-autor3]
  [![GitHub][github-badge]][github-autor3]
  [![Instagram][instagram-badge]][instagram-autor3]
  
  <br><br>
     <i>Vinicius Ramalho de Oliveira - Undergraduate - 4th Semester, Computer Engineering @ CEFET-MG</i>
  <br><br>
  
  [![Gmail][gmail-badge]][gmail-autor5]
  [![Linkedin][linkedin-badge]][linkedin-autor5]
  [![GitHub][github-badge]][github-autor5]
  [![Instagram][instagram-badge]][instagram-autor5]

</div>

[gmail-badge]: https://img.shields.io/badge/-Gmail-c14438?style=flat-square&logo=Gmail&logoColor=white
[linkedin-badge]: https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white
[github-badge]: https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white
[instagram-badge]: https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white

[gmail-autor2]: mailto:siratutifernando@gmail.com
[linkedin-autor2]: https://www.linkedin.com/in/fernando-siratuti-503ba8301/
[github-autor2]: https://github.com/fernando-horita-siratuti
[instagram-autor2]: https://www.instagram.com/siratuti_/

[gmail-autor3]: mailto:hugohmarques4@gmail.com
[linkedin-autor3]: https://www.linkedin.com/in/hugo-h-marques-980629216/
[github-autor3]: https://github.com/hugnarok
[instagram-autor3]: https://www.instagram.com/hugomarques_02/

[gmail-autor5]: mailto:ramalhooliveiravini@gmail.com
[linkedin-autor5]: https://www.linkedin.com/in/vin%C3%ADcius-ramalho-de-oliveira-4464b8327/
[github-autor5]: https://github.com/ViniciusRO22
[instagram-autor5]: https://www.instagram.com/_vinicius.ro_/
