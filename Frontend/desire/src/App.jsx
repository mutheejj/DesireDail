import ChatHeader from "./chatheader";
import Home from "./home";
import Nav_menu from "./nav_menu";
import Messages from "./messages";
import Calls from "./calls";
import Typing from "./typing";
import Chat from "./chat";

function App() {
  return (
    <>
    
    <Home></Home> 
    <Nav_menu></Nav_menu>
      
    <ChatHeader></ChatHeader>

    <Messages></Messages>
    <Calls></Calls>
     <Typing></Typing>
     <Chat></Chat>
    </>
  );
}

export default App;