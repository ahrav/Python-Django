import React from 'react'

const todoContext = React.createContext({
    title: '',
    description: '',
    completed: false,
    toggle: () => {},
    onSave: () => {},
    todoId: ''
})

export default todoContext