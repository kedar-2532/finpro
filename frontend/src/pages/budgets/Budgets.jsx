import { useEffect, useState } from 'react'
import DashboardLayout from '../../layouts/DashboardLayout'

function Budgets() {

    const[budgets, setBudgets]= useState([])
    useEffect(()=>{

    async function fetchBudgets(){

        try{
            const token=
            localStorage.getItem("access")
            const response=
            await fetch(
                "http://127.0.0.1:8000/api/finance/budget-summary/",
                {
                    headers:{
                        Authorization:`Bearer ${token}`
                    }
                }
            )

            const data = await response.json()
            console.log("BUDGET DATA:", data)
            setBudgets(data)
        }
        catch(error){
            console.log(error)
        }
    }
    fetchBudgets()
},[])

  return (
    <DashboardLayout>

        <h1 className='text-4xl font-bold mb-6'>Budget</h1>

        <div className='grid grid-4'>
            {
            (budgets.results || budgets).map(
                (item)=>(
                    <div key={item.category} className='bg-white p-5 rounded-xl shadow'>
                        <h2 className='font-bold text-xl'>
                            {
                                item.category
                            }
                        </h2>
                        <p>
                            Limit: ₹ { item.monthly_limit }
                        </p>

                        <p>
                            Spent: ₹ {item.spent } 
                        </p>

                        <p>
                            Remaining: ₹ {item.remaining}
                        </p>

                        <div className='w-full bg-gray-200 h-4 mt-3'>
                            <div className='bg-blue-500 n-4 rounded-full' style={{ 
                                width:`${
                                    Math.min(item.spent/item.monthly_limit*100,100)
                                        }%`
                                    }}>

                                </div>
                        </div>
                        
                    </div>
                )
            )
            }
        </div>

    </DashboardLayout>
  )
}

export default Budgets
