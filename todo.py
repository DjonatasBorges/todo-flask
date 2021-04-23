from flask import Flask, jsonify, request

todo = Flask(__name__)

todos = [
    {
        "userId": 1,
        "id": 0,
        "title": "Começar e caminhar para ser um DEV.",
        "completed": False
    },
    {
        "userId": 1,
        "id": 1,
        "title": "Iniciar lógica de programação com Python3.",
        "completed": False
    },
    {
        "userId": 1,
        "id": 2,
        "title": "Conclusão do Curso do Guanabara.",
        "completed": False
    },
    {
        "userId": 1,
        "id": 3,
        "title": "Conclusão de todos os exercícios do curso do Guanabara com revisão.",
        "completed": False
    },
    {
        "userId": 1,
        "id": 4,
        "title": "Iniciar exercícios PythonBrasil.",
        "completed": False
    },
    {
        "userId": 1,
        "id": 5,
        "title": "Terminar a lista de exercícios PythonBrasil.",
        "completed": False
    },
    {
        "userId": 1,
        "id": 6,
        "title": "Iniciar aprendizado em Api.",
        "completed": False
    },
    {
        "userId": 1,
        "id": 7,
        "title": "Ficar mestre em Api.",
        "completed": False
    },
    {
        "userId": 1,
        "id": 8,
        "title": "Iniciar Django e Flask.",
        "completed": False
    },
    {
        "userId": 1,
        "id": 9,
        "title": "Dominar Django e Flask.",
        "completed": False
    },
    {
        "userId": 1,
        "id": 10,
        "title": "Conseguir um emprego como desenvolvedor Python.",
        "completed": False
    }
]


@todo.route('/')
def obter_todos():
    return jsonify(todos)


@todo.route('/<int:indice>', methods=['GET'])
def obter_todo_por_indice(indice):
    return jsonify(todos[indice])


@todo.route('/tarefa', methods=['POST'])
def postar_novo_todo():
    postar = request.get_json()
    todos.append(postar)
    return jsonify(postar, 200)


@todo.route('/tarefa/<int:indice>', methods=['PUT'])
def repost(indice):
    repostagem = request.get_json()
    todos[indice].update(repostagem)

    return jsonify(todos[indice], 200)


@todo.route('/tarefa/<int:indice>', methods=['DELETE'])
def deletar(indice):
    try:
        if todos[indice] is not None:
            deletado = todos[indice]
            del todos[indice]
            return jsonify(f'Foi excluído a postagem {deletado}', 200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão', 404)


todo.run(port=5500, host='localhost', debug=True)
