import { useEffect, useState } from 'react'
import toast from 'react-hot-toast';

import DashboardLayout from '../../layouts/DashboardLayout'
import { getTransactions, deleteTransaction, addTransaction } from '../../services/transactionService'
import AddTransactionForm from '../../components/AddTransactionForm'


function Transactions(){

const[transactions,setTransactions]=useState([])

useEffect(()=>{
    async function FetchTransactions(){
        try{
            const data = await getTransactions()
            console.log('DATA:',data)
            setTransactions(data.results || data)
        }
        catch(error){
            console.log(error)
        }
    }
    FetchTransactions()
},[])

async function handleDelete(id){
try{
    await deleteTransaction(id)
    
    const data = await getTransactions()
    console.log('DATA:',data)
    setTransactions(data.results || data)
    toast.success('Transaction Deleted');
}
catch(error){
    toast.error("Operation Failed")
    console.log(error)
}

}

async function handleAdd(form) {
    try{
        await addTransaction(form)
        const data = await getTransactions()

        setTransactions(data.results || data)
        toast.success('Transaction Added');
    }
    catch(error){
        toast.error("Operation Failed")
        console.log(error)
    }
    

}

return(
    <DashboardLayout>
        <h1 className='text-4xl font-bold mb-6'>Transactions</h1>

        <AddTransactionForm onAdd={handleAdd} />

        <div className='bg-white p-5 rounded-xl shodow'>
            <table className='w-full'>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Type</th>
                        <th>Amount</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        transactions.map((item)=>(
                            <tr key={item.id} className='border-b'>
                                <td>{item.id}</td>
                                <td>{item.transaction_type}</td>
                                <td>₹ {item.amount}</td>
                                <td>
                                    <button onClick={()=> handleDelete(item.id)} className='bg-red-500 text-white px-3 py-1 rounded'>Delete</button>
                                </td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        </div>
    </DashboardLayout>
)
}
export default Transactions