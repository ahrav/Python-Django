import React, { useContext, useEffect } from 'react'
import axios from 'axios'
import { NavLink } from 'react-router-dom'
import { Store } from '../../Store'
import Song from './Song/Song'
import './Songs.css'

const Songs = props => {
    const { state, dispatch } = useContext(Store)

    useEffect(() => {
        axios.get('http://localhost:8000/api/v1/songs/')
        .then(res => {
            console.log(res)
            return dispatch({
            type: 'FETCH_DATA',
            payload: res.data
            })
        })
        .catch(err => console.log(err))
    }, [dispatch])


    const allSongs = state.songs.map(song => {
        return (
            <NavLink
             className="Songs"
             to ={`/songs/${song.id}`}
             key={song.id}><Song 
                title={song.title}
                name={song.artist}
            /></NavLink>
        )
    })
    return (
        allSongs
    )
}

export default Songs