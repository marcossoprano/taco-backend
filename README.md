
# Consultor TACO - Backend

Backend em **Django + MySQL** para consulta nutricional baseada na tabela TACO brasileira.

---

## 🚀 Como funciona
Informe o nome do alimento e a quantidade em gramas. O sistema retorna calorias, proteínas, carboidratos e gorduras proporcionais à quantidade informada.

---

## 🔗 Endpoint principal

**Consulta Nutricional**

`GET /api/alimentos/consulta/?nome=<nome_do_alimento>&quantidade=<gramas>`

Exemplo:
```
GET http://localhost:8000/api/alimentos/consulta/?nome=Arroz branco cozido&quantidade=150
```

---

## 🧪 Exemplos de teste

**Arroz branco cozido**
```http
GET http://localhost:8000/api/alimentos/consulta/?nome=Arroz branco cozido&quantidade=150
```
Resposta:
```json
{
  "nome": "Arroz branco cozido",
  "quantidade": 150.0,
  "calorias": 192.0,
  "proteinas": 3.75,
  "carboidratos": 42.15,
  "gorduras": 0.3
}
```

**Frango grelhado**
```http
GET http://localhost:8000/api/alimentos/consulta/?nome=Frango grelhado&quantidade=200
```
Resposta:
```json
{
  "nome": "Frango grelhado",
  "quantidade": 200.0,
  "calorias": 326.0,
  "proteinas": 64.0,
  "carboidratos": 0.0,
  "gorduras": 7.2
}
```

**Banana prata**
```http
GET http://localhost:8000/api/alimentos/consulta/?nome=Banana prata&quantidade=100
```
Resposta:
```json
{
  "nome": "Banana prata",
  "quantidade": 100.0,
  "calorias": 89.0,
  "proteinas": 1.0,
  "carboidratos": 22.8,
  "gorduras": 0.2
}
```

**Carne bovina grelhada**
```http
GET http://localhost:8000/api/alimentos/consulta/?nome=Carne bovina grelhada&quantidade=50
```
Resposta:
```json
{
  "nome": "Carne bovina grelhada",
  "quantidade": 50.0,
  "calorias": 116.0,
  "proteinas": 16.0,
  "carboidratos": 0.0,
  "gorduras": 5.35
}
```

**Leite integral**
```http
GET http://localhost:8000/api/alimentos/consulta/?nome=Leite integral&quantidade=250
```
Resposta:
```json
{
  "nome": "Leite integral",
  "quantidade": 250.0,
  "calorias": 152.5,
  "proteinas": 8.0,
  "carboidratos": 11.75,
  "gorduras": 8.25
}
```

---

## ⚙️ Como rodar o projeto

1. **Configure o arquivo `.env`** com suas credenciais do MySQL:
   ```env
   NAME=taco
   USER=root
   PASSWORD=11111111
   HOST=localhost
   PORT=3306
   ```
2. **Instale as dependências:**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Execute as migrações:**
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Popule o banco com alimentos principais:**
   ```powershell
   python manage.py popula_alimentos
   ```
5. **Importe alimentos do CSV (opcional):**
   ```powershell
   python manage.py importa_taco_csv
   ```
6. **Inicie o servidor:**
   ```powershell
   python manage.py runserver
   ```
7. **Teste o endpoint no Postman ou navegador.**

---

## 📦 Adaptações futuras
- Importação de alimentos via arquivo CSV
- Expansão da base de alimentos
- Melhorias na API e autenticação

---

Projeto inicial para consultoria alimentar usando TACO.
