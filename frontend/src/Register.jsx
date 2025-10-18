import { useState } from 'react';

export default function Register() {
  const [form, setForm] = useState({ email: '', display_name: '', password: '' });
  const [message, setMessage] = useState('');

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    console.log('API URL:', import.meta.env.VITE_API_URL);
    e.preventDefault();
    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL}/api/register/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      });
      const data = await res.json();
      setMessage(data.message || 'Registration failed');
    } catch (error) {
      setMessage('Network error or server unreachable');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="email" placeholder="Email" onChange={handleChange} required />
      <input name="display_name" placeholder="Display Name" onChange={handleChange} required />
      <input name="password" type="password" placeholder="Password" onChange={handleChange} required />
      <button type="submit">Register</button>
      {message && <p>{message}</p>}
    </form>
  );
}