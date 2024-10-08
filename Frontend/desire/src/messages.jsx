import mystyle from "./css/messages.module.css";

function Messages(){
    return (
        <div className={mystyle.messages}>
            <input type="text" placeholder="search" />
            <h1>hello world</h1>

        </div>
    );
}

export default Messages