import './App.css';
import FileUpload from './componenets/FileUpload';
import Navbar from './componenets/Navbar';
function App() {
  return (
    <div className="App">
      
      <Navbar/>
      <h1>Upload File to Cloudinary</h1>
      <FileUpload />
    </div>
  );
}

export default App;