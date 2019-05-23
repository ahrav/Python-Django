import React, { useContext } from 'react'
import { Formik, Field, Form, ErrorMessage } from 'formik'
import axios from 'axios'
import * as Yup from 'yup'
import { Store } from '../../Store'
import './NewSong.css'
import styled from 'styled-components'

export const Input = styled.input`
  width: 300px;
  height: 35px;
  border: 1px solid #ccc;
  background-color: #fff;
`;

export const Button = styled.button`
  width: 300px;
  height: 35px;
  background-color: #5995ef;
  color: #fff;
  border-radius: 3px;
`;


const initialValues = {
    title: '',
    artist: ''
}

const NewSong = props => {
    const { state, dispatch } = useContext(Store)
    return (
        <div>
        <h1>Add Song</h1>
            <Formik
                initialValues={initialValues}
                validationSchema={Yup.object().shape({
                    title: Yup.string().required("Title is required").min(2, 'Title must be longer than 2 characters'),
                    artist: Yup.string().required('Artist is required').min(2, 'Artist must be longer than 2 characters')
                })} 
                onSubmit={(values, actions) => {
                    axios.post('http://localhost:8000/api/v1/songs/', values)
                        .then(res => {
                            values.artist = ''
                            values.title = ''
                            actions.setSubmitting(false)
                            return dispatch({
                                type: 'ADD_SONG',
                                payload: res.data
                            })
                        })
                        .catch(err => {
                            console.log(err)
                            actions.setSubmitting(false);
                        })
                }}
            >
                {({ values, handleBlur, error, touched, isSubmitting, setFieldValue}) => (
                    <Form className="Form">
                        <React.Fragment>
                            <Field name="title" type="text" placeholder="Enter Song Title"/>
                            <ErrorMessage name="title">{msg => <div>{msg}</div>}</ErrorMessage>
                            <Field name="artist" type="text" placeholder="Enter Artist Name"/>
                            <ErrorMessage name="artist">{msg => <div>{msg}</div>}</ErrorMessage>
                            <button type="submit" disabled={isSubmitting}>
                                Add Song
                            </button>
                        </React.Fragment>
                    </Form>
                )}

            </Formik>
        </div>
    )
}

export default NewSong