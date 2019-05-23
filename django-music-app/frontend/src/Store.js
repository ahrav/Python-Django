import React from 'react'

export const Store = React.createContext()

const initialState = {
    songs: []
}

const reducer = (state, action) => {
    switch (action.type) {
        case 'FETCH_DATA':
            return {songs: action.payload}
        case 'ADD_SONG':
            return {songs: state.songs.concat(action.payload)}
        case 'REMOVE_SONG':
            return {songs: state.songs.filter(song => song.id !== action.payload)}
        default:
            return state
    }
}

export const StoreProvider = props => {
    const [state, dispatch] = React.useReducer(reducer, initialState)
    const value = { state, dispatch }
    return (
        <Store.Provider value={value}>{props.children}</Store.Provider>
    )
}