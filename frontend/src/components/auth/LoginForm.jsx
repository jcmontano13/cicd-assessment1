    import { useState } from 'react';
    import axios from 'axios';

    export default function LoginForm() {
      const [email, setEmail] = useState('');
      const [password, setPassword] = useState('');
      const [error, setError] = useState('');

      const handleLogin = async (e) => {
        e.preventDefault();
        try {
          const res = await axios.post(`${import.meta.env.VITE_API_URL}/api/login/`, {
            email,
            password,
          });
          localStorage.setItem('token', res.data.token);
          window.location.href = '/dashboard'; // or use React Router
        } catch (err) {
          setError('Invalid credentials');
        }
      };

      return (
        <form onSubmit={handleLogin}>
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
          <button type="submit">Login</button>
          {error && <p>{error}</p>}
        </form>
      );
    }