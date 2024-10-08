import React from "react";
import mystyle from "./css/chatheader.module.css";
import profilepic from "./images/profile.jpeg";
import videocall from "./images/video.jpeg";
import call from "./images/addcall.jpeg";
function ChatHeader(){
    return(
        <header className={mystyle.container}>
            <div>
                <img src={profilepic} id={mystyle.prof} />
                <div className={mystyle.room}>
                    <h5>name</h5>
                    <h6>online</h6>                   

                </div>   
                    
                    <div className={mystyle.calls}>
                        <img className={mystyle.img} src={call} alt="Call" />
                        <img className={mystyle.img} src={videocall} alt="video call" />
                        
                    </div> 

            </div>

                             
                
                    
                   
                  


        </header>
    );
}

export default ChatHeader