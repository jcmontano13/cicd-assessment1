import { useState } from 'react';

export default function Register() {
  const [form, setForm] = useState({
    email: '',
    display_name: '',
    password: '',
  });

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL}/api/register/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      });

      const data = await res.json();
      if (res.ok) {
        alert(data.message || 'Registration successful');
      } else {
        alert(data.message || 'Registration failed');
      }
    } catch (error) {
      alert('Network error or server unreachable');
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="email"
        placeholder="Email"
        value={form.email}
        onChange={handleChange}
        required
      />
      <input
        name="display_name"
        placeholder="Display Name"
        value={form.display_name}
        onChange={handleChange}
        required
      />
      <input
        name="password"
        type="password"
        placeholder="Password"
        value={form.password}
        onChange={handleChange}
        required
      />
      <button type="submit">Register</button>
    </form>
  );
}