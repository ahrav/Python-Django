import React, { useContext, useState, useEffect } from 'react'
import axios from 'axios'
import { Store } from '../../Store'

const SongDetail = props => {
    const { state, dispatch } = useContext(Store)
    const [loadedSong, setLoadedSong] = useState()

    useEffect(() => {
        axios.get(`http://localhost:8000/api/v1/songs/${props.match.params.songId}`)
            .then(res => {
                console.log(res)
                setLoadedSong(res.data)
            })
            .catch(err => console.log(err))
    }, [props.match.params.songId])


    const deleteSongHandler = id => {
        axios.delete(`http://localhost:8000/api/v1/songs/${id}`)
          .then(res => {
            dispatch({type: 'REMOVE_SONG', payload: id})
          })
          .catch(err => console.log(err))
      }

    let song = <p style={{ textAlign: 'center' }}>Please select a Song!</p>
    if ( props.match.params.id ) {
    song = <p style={{ textAlign: 'center' }}>Loading...!</p>;
    }
    if (loadedSong) {
        song = (
            <div>
                <h1>{loadedSong.title}</h1>
                <h2>{loadedSong.artist}</h2>
                <div>
                    <button onClick={(id) => deleteSongHandler(loadedSong.id)}>Delete</button>
                </div>
            </div>
        )
    }

    return song
}

export default SongDetail