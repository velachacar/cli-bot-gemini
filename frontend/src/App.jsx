import { useState } from 'react'
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import { Button, Container, Form, FormLabel, Overlay, OverlayTrigger, Tooltip } from 'react-bootstrap';
import { fetchData } from './helpers/axiosHelper';
import { DotLottieReact } from '@lottiefiles/dotlottie-react';

function App() {
  const [fadeout, setFadeout] = useState(false);
  const [allMsg, setAllMsg] = useState([
    {
      user: "ai",
      tools: "",
      content: "Hello, I´m Chatbotty, ask me anything. If you want to know my skills, check the ? icon on top of the chat",
      verbose: "",
      status: "fulfilled"
    }
  ]);
  const[newMsg, setNewMsg] = useState("");
  const[isVerbose, setIsVerbose] = useState(false);
  const[background, setBackground] = useState("base-bg");

  const handleChange = (e) => {
    e.preventDefault()
    setNewMsg(e.target.value)
  }

  const handleSubmit = async () => {
    try {
      const userMsg = {user: "user", content: newMsg}
      const loadingMsg = {user: "ai", content: "loading", loading: true}

      setAllMsg(prev => [...prev, userMsg, loadingMsg]);
      

      const result = await fetchData('/get_response', 'POST', {"prompt": newMsg, "isVerbose": isVerbose})
      console.log(result);
      setNewMsg("")
      const split_result = result.data.response.stdout.split("Final response:")
      if (isVerbose){
        const split_verbose = split_result[1].split("verbose")
        console.log(split_verbose)
        setAllMsg(prev => [...prev.slice(0,-1), {user: "ai", tools: split_result[0],content: split_verbose[0], verbose: split_verbose[1]}])
      }
      else{
        setAllMsg(prev => [...prev.slice(0,-1), {user: "ai", tools: split_result[0],content: split_result[1], verbose: ""}])
      }
      

    } catch (error) {
      console.log(error);
      alert('Error')
    }
  }

  return (
    <>
      <div className={`onboard-screen text-center ${fadeout? 'fadeout':''}`} >
        
      
      <DotLottieReact
        src="https://lottie.host/c78f59ec-de95-4cd3-92d2-57cbf0bd3c3e/mGbvB8oPrT.lottie"
        loop
        autoplay
        speed={0.5}
        className='onboard-lottie mx-auto'
      />
      <h1>Welcome to Chatbotty, your Gemini powered ai agent <br /> for file management and simple calculations :)</h1>
      <Button variant="success" onClick={() => setFadeout(true)} disabled={fadeout} className='onboard-btn'>
         Start Chatbotty
      </Button>
      </div>
      
      
      <Container className='chat-window p-5'>
        <header className='d-flex px-3'>
          <h1>
            Chatbotty<OverlayTrigger
          key={'bottom'}
          placement={'bottom'}
          overlay={
            <Tooltip id={`tooltip-bottom`}>
              <h2>Skills:</h2>
              <p>get_file_content: Gets a file content from the specified directory, limited to 10000 characters plus a disclaimer, constrained to the working directory.</p>
              <p>get_files_info: Lists files in the specified directory along with their sizes, constrained to the working directory.</p>
              <p>run_python_file: Runs a python file from the specified directory, capturing STDOUT and STDERR, has a 30 second timeout, and constrained to the working directory.</p>
              <p>write_file: Writes into a file in the specified directory, creating it if it doesnt exist, constrained to the working directory.</p>
            </Tooltip>
          }
        >
          <Button variant="secondary" className='tooltip-btn rounded-circle'>?</Button>
        </OverlayTrigger>
        <Button className={`btn-info verbose-btn ${isVerbose}`} onClick={()=>setIsVerbose(!isVerbose)} >
          <i className={isVerbose?'bi bi-check2-circle':'bi bi-x-circle'} ></i>
          {isVerbose?' verbose':' default'}
        </Button>
        </h1>
        <div className='bg-buttons ms-auto d-flex align-items-center'>
          <Button className={`bg-btn base-bg`} onClick={()=>setBackground("base-bg")} />
          <Button className={`bg-btn red-bg`} onClick={()=>setBackground("red-bg")} />
          <Button className={`bg-btn green-bg`} onClick={()=>setBackground("green-bg")} />
          <Button className={`bg-btn blue-bg`} onClick={()=>setBackground("blue-bg")} />
        </div>
          
        </header>
        <main className={`border border-1 rounded-4 ${background}`}>
          {
            allMsg.map((msg, idx)=>{
              return(
                <p key={idx} className={msg.user}>
                  {msg.loading ?
                  <span className="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                  :
                  <>
                  {msg.tools && <span className='msg-tools'>Tools: {msg.tools}</span>} 
                  <span className='msg-content'>{msg.content}</span>
                  {msg.verbose && <span className='msg-verbose'>{msg.verbose}</span>}
                  <img src={`../src/assets/images/${msg.user}.png`} className={`msg-icon ${msg.user}`}></img>
                  </>
                  }
                </p>
              )
            })
          }
          
        <div>
          <Form className='mt-3'>
            <Form.Group controlId='formMsgContent'>
              <textarea 
                className='msg-window'
                name='msg-content'
                value={newMsg}
                onChange={handleChange}
                rows="4"
                onSubmit={handleSubmit}
              />
              <Button className='send-msg-button' onClick={handleSubmit}><i className="bi bi-arrow-right-circle"></i></Button>
              {/* <Form.Control as="textarea" className='msg-window' type='textarea' placeholder='Write your prompt :)' onChange={onChange}/> */}
            </Form.Group>
          </Form>
        </div>
        </main>
        <footer>
          <span>Made by Carlos Vela Chávez</span>
        </footer>
      </Container>
    </>
  )
}

export default App
