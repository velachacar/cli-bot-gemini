import axios from 'axios';

const apiUrl = import.meta.env.VITE_SERVER_URL;

console.log(apiUrl);

export const fetchData = async(url, method, data=null, token=null) =>{

    let headers = {}
    
    if(token){
        headers={Authorization: `Bearer ${token}`}
    }

    const config = {
        url: apiUrl + url,
        method, 
        data,
        headers: headers
    }

    const res = await axios(config);
    return res;

}