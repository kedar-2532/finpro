import { useEffect, useState } from 'react'

import DashboardLayout from "../../layouts/DashboardLayout"
import MonthlyChart from './MonthlyChart'

function Analytics(){
    const[risk,setRisk] = useState(null)

    const[insights,setInsights] = useState([])

    const[monthlyData,setMonthlyData] = useState([])

    useEffect(()=>{

    async function fetchAnalytics(){

        try{

            const token=

            localStorage.getItem(
                "access"
            )

            const riskResponse=

            await fetch(

                "http://127.0.0.1:8000/api/finance/risk-score/",

                {

                    headers:{

                        Authorization:
                        `Bearer ${token}`

                    }

                }

            )

            const riskData=

            await riskResponse.json()

            setRisk(
                riskData
            )

            const insightsResponse =await fetch(
                "http://127.0.0.1:8000/api/finance/ai-insights/",
                {
                    headers:{
                        Authorization:`Bearer ${token}`
                    }
                }
            )
            const insightsData = await insightsResponse.json()
            setInsights(insightsData)
            
            const monthlyReponse = await fetch(
                'http://127.0.0.1:8000/api/finance/monthly-summary/',
                {
                    headers:{
                        Authorization:`Bearer ${token}`
                    }
                }
            )
            const monthly = await monthlyReponse.json()
            console.log("Mobthly:",monthly)
            setMonthlyData(monthly)
            
        }
        catch(error){

            console.log(error)

        }

    }

    fetchAnalytics()

},[])
return(
    <DashboardLayout>

        <h1 className='text-4xl font-bold mb-6'>Analytics</h1>

        {
            risk && (
                <div className='gird grid-cols-4 gap-4 mn-6'>

                    <div className='bg-white shadow rounded-xl p-5'>
                        <h3>Risk Level</h3>
                        <p className='text-2xl font-bold'>
                            {
                                risk.risk_level
                            }
                        </p>
                    </div>

                    <div className='bg-white shadow rounded-xl p-5'>
                        <h3>Savings Rate</h3>
                        <p className='text-2xl font-bold'>
                            {
                                risk.saving_rate
                            }%
                        </p>
                    </div>

                    <div className='bg-white shadow rounded-xl p-5'>
                        <h3>Income</h3>
                        <p className='text-2xl font-bold'>
                            ₹{
                                risk.income
                            }
                        </p>
                    </div>

                    <div className='bg-white shadow rounded-xl p-5'>
                        <h3>Expense</h3>
                        <p>
                            ₹{
                                risk.expense
                            }
                        </p>
                    </div>

                </div>
            )
        }
        <div className='bg-white rounded-xl shadow p-5'>
            <h2 className='text-2xl font-bold mb-4'>AI Insights</h2>
            {
                insights.map(
                    (item,index)=>(
                        <div key={index} className='border-b my-2'>
                            {item}
                        </div>
                    )
                )
            }
        </div>

        <MonthlyChart data={monthlyData} />
        
    </DashboardLayout>
)
}
export default Analytics