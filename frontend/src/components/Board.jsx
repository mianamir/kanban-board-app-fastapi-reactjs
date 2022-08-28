import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import Column from './Column';


const Container = styled.div`
    display: flex;
    `

function Board(){
    const initialData = {
        tasks: {},
        columns: {},
        columnOrder: []
      }
      const [board, setBoard] = useState(initialData);
    
      useEffect(() => {
        fetchBoard().then((data) => setBoard(data));
      }, []);
    
      // get data from backend 
      async function fetchBoard(){
        const res = await fetch('/board');    
        console.log(res);
        return res.board;
      }
    return (
        <Container>
            Board
        </Container>
    );
}


export default Board;