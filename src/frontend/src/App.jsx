import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import Survey from './pages/Survey';
import LearningPlans from './pages/LearningPlans';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="survey" element={<Survey />} />
            <Route path="learning-plans" element={<LearningPlans />} />
          </Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
