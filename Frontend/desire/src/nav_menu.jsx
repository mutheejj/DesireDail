import React from "react";
import navstyle from "./css/nav_m.module.css";

import home from "./images/home.jpeg";
import search from "./images/search.jpeg";
import save from "./images/save.jpeg";
import share from "./images/share.jpeg";
import setting from "./images/settings.jpeg";
import dark from "./images/dark.jpeg";
import light from "./images/light.jpeg";
import logo from "./images/logo.jpeg";
import profile from "./images/profile.jpeg";

function Nav_menu(){
    
    
    return(
        <nav className={navstyle.nav_menu}>
            <img src={logo} className={navstyle.nav_img} style={{width :"100px", height : "100px",borderRadius : "50%", }}></img>
            <a href="#" className={navstyle.nav_link}>
                <img src={home} alt="" className={navstyle.nav_img}></img>
                <figcaption className={navstyle.figcaption}>home</figcaption>
            </a>
            <a href="#" className={navstyle.nav_link}>
            <img src={search} alt="" className={navstyle.nav_img}></img>
                <figcaption className={navstyle.figcaption}>search</figcaption>
            </a>
            <a href="#" className={navstyle.nav_link}>
                <img src={save} alt="" className={navstyle.nav_img}></img>
                <figcaption className={navstyle.figcaption}>save</figcaption>
            </a>
            <a href="#" className={navstyle.nav_link}>
                <img src={share} alt="" className={navstyle.nav_img}></img>
                <figcaption className={navstyle.figcaption}>share</figcaption>
            </a>
            <a href="#" className={navstyle.nav_link}>
                <img src={setting} alt="" className={navstyle.nav_img}></img>
                <figcaption className={navstyle.figcaption}>setting</figcaption>
            </a>
            
            
            <a href="#" className={navstyle.nav_link}>
                <img src={profile} className={navstyle.profile_img}></img>
            </a>
            
        </nav>
        

    );
}

export default Nav_menu