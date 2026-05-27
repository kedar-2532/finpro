import { useEffect, useState } from 'react'

import DashboardLayout from '../../layouts/DashboardLayout'

function Alerts(){
    const[alerts,setAlerts] = useState([])

    useEffect(()=>{
        async function fetchAlerts(){
            try{
                const token = localStorage.getItem('access')

                const response = await fetch(
                    'http://127.0.0.1:8000/api/finance/alerts/',
                    {
                        headers:{
                            Authorization:`Bearer ${token}`
                        }
                    }
                )
                const data = await response.json()

                setAlerts(data)
            }
            catch(error){
                console.log(error)
            }
        }
        fetchAlerts()
    },[])
    return(
        <DashboardLayout>

            <h1 className='text-4xl font-bold mb-6'>Alerts</h1>

            <div className='bg-white p-5 rounded-xl shadow'>
                {
                    alerts.length===0?
                    (
                        <p>No alerts 🎉</p>
                    )
                    :
                    (
                        alerts.map((item,index)=>(
                            <div key={index} className='border=b py-3 text-red-600 font-medium'>
                                ⚠️ {item}
                            </div>
                        )
                        )
                    )
                }
            </div>
        </DashboardLayout>
    )
}

export default Alerts