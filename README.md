# teste-backend-amicci
Para visualizar a API em live preview acesse [https://teste-backend-amicci.onrender.com/api/demo/](https://teste-backend-amicci.onrender.com/api/demo/)

## Instruções
### `docker compose up --build  `
Ao utilizar esse comando o docker ira fazer as migrates, rodas os testes unitarios e colocar a API no ar no seguinte endereço [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


No endpoint [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) estara a lista com todas as rotas disponiveis.

## Endpoints
api/demo/categories/ [GET] - Obter todas categorias
api/demo/category/ [POST] - Cadastrar categoria
api/demo/category/<int:pk> [PUT] - Atualizar categoria
api/demo/category/<int:pk> [GET] - Obter categoria
api/demo/vendors/ [GET] - Obter vendedores
api/demo/vendor/ [POST] - Cadastrar vendedor
api/demo/vendor/<int:pk> [PUT] - Atualizar vendedor
api/demo/vendor/<int:pk> [GET] - Obter vendedor
api/demo/retailers/ [GET] - Obter varejistas
api/demo/retailer/ [POST] - Cadastrar varejista
api/demo/retailer/<int:pk> [PUT] - Atualizar varejista
api/demo/retailer/<int:pk> [GET] - Obter varejista
api/demo/briefings/ [GET] - Obter briefings
api/demo/briefing/ [POST] - Cadastrar briefing
api/demo/briefing/<int:pk> [PUT] - Atualizar briefing
api/demo/briefing/<int:pk> [GET] - Obter briefing