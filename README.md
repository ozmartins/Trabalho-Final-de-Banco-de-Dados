### Conexão com o banco de dados
Abra o arquivo ```settings.py```, localize a variável ```DATABASES``` e configure a conexão com seu banco de dados.

### Criação das tabelas exigidas pelo Django
Acesse o diretório ```footballleaguemanager\main``` e execute a seguinte linha de código
``` bash
python manage.py migrate
```

### Criação do super usuário do Django
``` bash
python manage.py createsuperuser
```

### Executando a aplicação
Acesse o diretório ```footballleaguemanager\main``` e execute a seguinte linha de código
``` bash
python manage.py runserver
```
