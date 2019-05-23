import React from 'react'

const Song = props => {
    return (
        <article>
            <h4>Song Title: {props.title}</h4>
            <h5>Artist: {props.name}</h5>
        </article>
    )
}

export default Song