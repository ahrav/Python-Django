import React, { useState, useEffect } from "react"
import Modal from '../Modal/Modal'
import axios from 'axios'
import TodoContext from '../../todo-context'
import './Todo.css'

const Todo = props => {
    const [modal, setModal] = useState(false)
    const [viewCompleted, setViewCompleted] = useState(false)
    const [title, setTitle] = useState('')
    const [description, setDescription] = useState('')
    const [completed, setCompleted] = useState(false)
    const [todoList, setTodoList] = useState([])
    const [todoId, setTodoId] = useState()

    useEffect(() => {
      axios.get("http://localhost:8000/api/todos/")
        .then(res => {
          setTodoList(todoList.concat(res.data)
        )})
        .catch(err => console.log(err))
    }, [])

    const toggle = () => {
      setModal(!modal);
    };

    const handleSubmit = ({item}) => {
      toggle();
      if (item.todoId) {
        console.log(item)
        console.log(todoList)
        axios
          .put(`http://localhost:8000/api/todos/${item.todoId}/`, item)
          .then(res => {
            const newListt = todoList.filter(todo => todo.id !== item.todoId)
            setTodoList([...newListt, res.data])
          })
          .catch(err => console.log(err))
        return;
      }
      axios
        .post("http://localhost:8000/api/todos/", item)
        .then(res =>{
          setTodoList([...todoList, res.data])})
        .catch(err => console.log(err))
    };

    const handleDelete = item => {
      axios
        .delete(`http://localhost:8000/api/todos/${item.id}`)
          .then(res => {
            const newList = todoList.filter(val => val.id !== item.id)
            setTodoList(newList)
          })
          .catch(err => console.log(err))
    };

    const createItem = () => {
      setTitle('')
      setDescription('')
      setCompleted(false)
      setModal(!modal)
    };

    const editItem = item => {
      setTitle(item.title)
      setDescription(item.description)
      setCompleted(item.completed)
      setModal(!modal)
      setTodoId(item.id)
    };

    const displayCompleted = status => {
      if (status) {
        return setViewCompleted(true);
      }
      return setViewCompleted(false);
    };

    const renderTabList = () => {
      return (
        <div className="my-5 tab-list">
          <span
            onClick={() => displayCompleted(true)}
            className={viewCompleted ? "active" : ""}
          >
            complete
          </span>
          <span
            onClick={() => displayCompleted(false)}
            className={viewCompleted ? "" : "active"}
          >
            Incomplete
          </span>
        </div>
      );
    };
    const renderItems = () => {
      const newItems = todoList.filter(
        item => item.completed === viewCompleted
      );
      return newItems.map(item => (
        <li
          key={item.id}
          className="list-group-item d-flex justify-content-between align-items-center"
        >
          <span
            className={`todo-title mr-2 ${
              viewCompleted ? "completed-todo" : ""
            }`}
            title={item.title}
          >
            {item.title}
          </span>
          <span>
            <button
              onClick={() => editItem(item)}
              className="btn btn-secondary mr-2"
            >
              Edit
            </button>
            <button
              onClick={() => handleDelete(item)}
              className="btn btn-danger"
            >
              Delete
            </button>
          </span>
        </li>
      ));
    };
    return (
      <div>
        <TodoContext.Provider value={{title: title, description: description, completed: completed, toggle: toggle, onSave: handleSubmit, setTitle: setTitle, setDescription: setDescription, setCompleted: setCompleted, todoId: todoId}}>
      <main className="content">
        <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row ">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="">
                <button onClick={createItem} className="btn btn-primary">
                  Add task
                </button>
              </div>
              {renderTabList()}
              <ul className="list-group list-group-flush">
                {renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {modal ? (
          <Modal/>
        ) : null}
      </main>
      </TodoContext.Provider>
      </div>
    );
}
export default Todo