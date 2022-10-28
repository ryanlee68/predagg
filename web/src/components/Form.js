import * as React from 'react';
// import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import { styled } from '@mui/material/styles';
import Checkbox from '@mui/material/Checkbox';
import '../css/form.css';
import Stack from '@mui/material/Stack';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Button from '@mui/material/Button';
import theme from '../theme';
import { ThemeProvider } from '@mui/material/styles';
import Box from '@mui/material/Box';
import InputSlider from '../components/InputSlider';
// import InputBase from '@mui/material/InputBase';
// import Box from '@mui/material/Box';
// import InputLabel from '@mui/material/InputLabel';
// import TextField from '@mui/material/TextField';
// import FormControl from '@mui/material/FormControl';

export default function form() {

  // counter = 0;
  // const listItems = predictors.map((predict) =>
    
  // );

  // for (let i = 0; i < predictors.length; i++) {
  //   if (i % 3 == 0) {

  //   }
  // }

  const CssTextField = styled(TextField)({
    '& label.Mui-focused': {
      color: 'black',
    },
    '& .MuiInput-underline:after': {
      borderBottomColor: 'black',
    },
    '& .MuiOutlinedInput-root': {
      '& fieldset': {
        borderColor: 'black',
      },
      '&:hover fieldset': {
        borderColor: 'black',
      },
      '&.Mui-focused fieldset': {
        borderColor: 'black',
      },
    },
  });

  const predictors = ["IUPred3", "ESpiritz", "SPOT-DISORDER", "flDPnn", "Disomine", "RawMSA", "Metapredict", "AlphaFold"];
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    var dict = {};
    console.log("uniprotid: " + String(data.get('uniprotid')))
    console.log("sequence: " + String(data.get('sequence')))
    dict["uniprotid"] = String(data.get('uniprotid'))
    dict["sequence"] = String(data.get('sequence'))
    var dict2 = {};
    if (data.get("IUPred3") == 'on') {
      console.log("IUPred3: True")
      dict2["IUPred3"] = [true, data.get('IUPred3minscore')];
    }
    if (data.get("ESpiritz") == 'on') {
      console.log("ESpiritz: True")
      dict2["ESpiritz"] = [true];
    }
    if (data.get("SPOT-DISORDER") == 'on') {
      console.log("SPOT-DISORDER: True")
      dict2["SPOT-DISORDER"] = [true];
    }
    if (data.get("flDPnn") == 'on') {
      console.log("flDPnn: True")
      dict2["flDPnn"] = [true];
    }
    if (data.get("Disomine") == 'on') {
      console.log("Disomine: True")
      dict2["Disomine"] = [true];
    }
    if (data.get("RawMSA") == 'on') {
      console.log("RawMSA: True")
      dict2["RawMSA"] = [true];
    }
    if (data.get("Metapredict") == 'on') {
      console.log("Metapredict: True")
      dict2["Metapredict"] = [true, data.get('MetaPredictminscore')];
    }
    if (data.get("AlphaFold") == 'on') {
      console.log("AlphaFold: True")
      dict2["AlphaFold"] = [true];
    }
    dict['sequences'] = dict2
    console.log(dict)
    fetch('http://localhost:3000/api/response', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dict)
    })
    .then((response) => response.blob())
    .then((blob) => {
      
      // // Create blob link to download
      // const url = window.URL.createObjectURL(
      //   new Blob([blob]),
      // );
      // const link = document.createElement('a');
      // link.href = url;
      // // link.target = _self;
      // // link.setAttribute('target', '_self');
      // link.setAttribute(
      //   'download',
      //   `classes.csv`,
      // );

      // // Append to html link element page
      // // document.body.appendChild(link);

      // // Start download
      // link.click();
      
      // // Clean up and remove the link
      // // link.parentNode.removeChild(link);
      // // window.close();
      // // const navigate = useNavigate();
      // // navigate("/");
      // // window.location.reload(false);
    });
  };
    
  const predictorSlider = {
    IUPred3: 'IUPred3minscore',
    MetaPredict: 'MetaPredictminscore',
  };
  return (
    <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
      <div>
        <CssTextField name='uniprotid' label="UnitProt ID" id="custom-css-outlined-input" className='form2'/>
        <br></br>
        <br></br>
        <div className='botform'>
          <CssTextField name='sequence' label="Sequence" multiline minRows='10' id="custom-css-outlined-input" />
          <FormGroup>
            <Stack spacing={2}>
              <Stack direction="row" spacing={3}>
                <FormControlLabel name="IUPred3" control={<Checkbox/>} label="IUPred3" />
                <InputSlider predictorMinScore={predictorSlider.IUPred3} PredName={'IUPred3'}/>
                <FormControlLabel name='ESpiritz' control={<Checkbox/>} label="ESpiritz" />
                <FormControlLabel control={<Checkbox/>} name='SPOT-DISORDER' label="SPOT-DISORDER" />
              </Stack>
              <Stack direction="row" spacing={3}>
                <FormControlLabel control={<Checkbox/>} name='flDPnn' label="flDPnn" />
                <FormControlLabel control={<Checkbox/>} name='Disomine' label="Disomine" />
                <FormControlLabel control={<Checkbox/>} name='RawMSA' label="RawMSA" />
              </Stack>
              <Stack direction="row" spacing={3}>
                <FormControlLabel control={<Checkbox/>} name='Metapredict' label="Metapredict" />
                <InputSlider predictorMinScore={predictorSlider.MetaPredict} PredName={'MetaPredict'}/>
                <FormControlLabel control={<Checkbox/>} name='AlphaFold' label="AlphaFold" />
              </Stack>
            </Stack>
          </FormGroup>
        </div>
        <ThemeProvider theme={theme}>
          <Button type="submit" variant="contained" color="neutral">Submit</Button>
        </ThemeProvider>
      </div>
    </Box>
  );
}
