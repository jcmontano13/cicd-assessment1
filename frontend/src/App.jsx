import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Register from './Register';
import LoginPage from './pages/LoginPage'; // ✅ this wraps LoginForm
import Dashboard from './pages/Dashboard'; // ✅ optional placeholder

function App() {
  return (
    <Router>
      <div>
        <h1>My Web App</h1>
        <Routes>
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;