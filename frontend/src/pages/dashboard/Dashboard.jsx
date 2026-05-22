import { useEffect, useState } from 'react';
import DashboardLayout from "../../layouts/DashboardLayout";
import { getDashboardData } from '../../services/dashboardService';
import RecentTransactions from '../../components/RecentTransactions';
import FinanceChart from '../../components/FinanceChart';

function Dashboard() {

  const [data,setData]=useState(null)

  useEffect(()=>{
    
    async function fetchData(){

      try{

        const result=await getDashboardData()

        console.log(result)

        setData(result)

      }catch(error){
        
        console.log(error)

      }

    }

    fetchData()

  },[])

  if(!data){

    return(
      <DashboardLayout>

        <h1>Loading...</h1>

      </DashboardLayout>
    )
  }
  return (
    <DashboardLayout>

      <h1 className="text-4xl font-bold mb-6">
        Dashboard
      </h1>

      <div className='grid grid-cols-3 gap-5'>

        <div className='bg-white p-5 rounded-xl shadnow'>

          <h2>Total Balance</h2>

          <p className='test-2xl font-bold'>
            ₹ {data.total_balance}
          </p>

        </div>

        <div className='bg-white p-5 rounded-xl shadow'>

          <h2>Total Income</h2>

          <p className='text-2xl font-bold test-green-600'>
            ₹ {data.total_income}
          </p>

        </div>

        <div className='bg-white p-5 rounded-xl shadow'>

          <h2>Total Expense</h2>

          <p className='text-2xl font-bold text-red-600'>
            ₹ {data.total_expense}
          </p>

        </div>
      
      </div>

      <RecentTransactions
        transactions={
          data.recent_transactions
        }
      />

      <div className='mt-6'>
        <FinanceChart

          income={data.total_income}

          expense={data.total_expense}
          
        />
      </div>

    </DashboardLayout>
  );

}

export default Dashboard;