import React, { useEffect, useState } from "react";
// import { Routes, Route } from "react-router-dom";
import { AppBar, Typography } from '@mui/material';
import AthleteCard from "./AthleteCard";

function App(){
    const [athletesList, setAthletesList] = useState([])

    console.log(athletesList);

    useEffect(()=>{
        fetch("http://127.0.0.1:5000/")
        .then(r=>r.json())
        .then((athletes) => {setAthletesList(athletes)})
        .catch((error) => console.error(error))
    },[])
    

    return (
        <>
          <AppBar>
            <Typography>Know Your Athletes</Typography>
          </AppBar>
            <AthleteCard athletesList={athletesList}/>
        </>
    )
}

export default App
