import React from 'react'
import Form from '../components/Form'

const Login = () => {
  return (
    <div className="bg-pink-400">
      <Form method="login" route="api/token/"/>
    </div>
  )
}

export default Login

