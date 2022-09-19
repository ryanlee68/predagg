import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { styled } from '@mui/material/styles';
import Checkbox from '@mui/material/Checkbox';
import '../css/form.css';
import Stack from '@mui/material/Stack';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
// import InputBase from '@mui/material/InputBase';
// import Box from '@mui/material/Box';
// import InputLabel from '@mui/material/InputLabel';
// import TextField from '@mui/material/TextField';
// import FormControl from '@mui/material/FormControl';

export default function form() {
  const CssTextField = styled(TextField)({
    '& label.Mui-focused': {
      color: 'white',
    },
    '& .MuiInput-underline:after': {
      borderBottomColor: 'white',
    },
    '& .MuiOutlinedInput-root': {
      '& fieldset': {
        borderColor: 'black',
      },
      '&:hover fieldset': {
        borderColor: 'white',
      },
      '&.Mui-focused fieldset': {
        borderColor: 'white',
      },
    },
  });

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const arrOfStr = data.getAll('crn');
    const arrOfNum = [];
    arrOfStr.forEach(str => {
      arrOfNum.push(Number(str));
    });
    console.log(arrOfNum)
    };
    
  return (
    <div>
      <CssTextField label="UnitProt ID" id="custom-css-outlined-input" className='form2'/>
      <br></br>
      <br></br>
      <div className='botform'>
        <CssTextField label="Sequence" multiline minRows='10' id="custom-css-outlined-input" />
        <FormGroup>
        <Stack spacing={2}>
          <Stack direction="row" spacing={2}>
            <FormControlLabel control={<Checkbox/>} label="IUPred3" />
            <FormControlLabel control={<Checkbox/>} label="ESpiritz" />
            <FormControlLabel control={<Checkbox/>} label="SPOT-DISORDER" />
          </Stack>
          <Stack direction="row" spacing={2}>
            <FormControlLabel control={<Checkbox/>} label="flDPnn" />
            <FormControlLabel control={<Checkbox/>} label="Disomine" />
            <FormControlLabel control={<Checkbox/>} label="RawMSA" />
          </Stack>
          <Stack direction="row" spacing={2}>
            <FormControlLabel control={<Checkbox/>} label="Metapredict" />
            <FormControlLabel control={<Checkbox/>} label="AlphaFold" />
          </Stack>
        </Stack>
        </FormGroup>
      </div>
    </div>
  );
}
